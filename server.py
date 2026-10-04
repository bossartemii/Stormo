#!/usr/bin/env python3
"""
Stormo local server — PC (Windows / macOS / Linux) and Android (Termux).
Server locale di Stormo · Локальный сервер Stormo

Serves the app on http://localhost:8080 and adds an optional proxy
(/proxy?url=...) so the browser can reach AI providers that block
direct browser calls (CORS). Python standard library only.

Usage / Uso / Запуск:
    python3 server.py              # http://localhost:8080
    python3 server.py --port 9000
    python3 server.py --lan        # also reachable from other devices on your Wi-Fi
    python3 server.py --no-open    # don't open the browser
"""
import argparse
import http.server
import json
import os
import shutil
import socket
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import webbrowser

ROOT = os.path.dirname(os.path.abspath(__file__))
FORWARD_HEADERS = ("authorization", "x-api-key", "anthropic-version", "content-type", "http-referer", "x-title")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *args):
        # never log proxied URLs: they can contain API keys (e.g. Gemini)
        line = fmt % args
        if "/proxy" not in line:
            sys.stderr.write("  " + line + "\n")

    def _path(self):
        return urllib.parse.urlsplit(self.path).path

    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self._path().endswith("/proxy/ping"):
            return self._json(200, {"ok": True, "app": "stormo"})
        super().do_GET()

    def do_POST(self):
        if not self._path().endswith("/proxy"):
            return self._json(404, {"error": "not found"})
        query = urllib.parse.parse_qs(urllib.parse.urlsplit(self.path).query)
        url = (query.get("url") or [""])[0]
        if not url.startswith(("https://", "http://")):
            return self._json(400, {"error": "proxy: missing or invalid url"})
        length = int(self.headers.get("Content-Length") or 0)
        data = self.rfile.read(length) if length else None
        headers = {k: v for k, v in self.headers.items() if k.lower() in FORWARD_HEADERS}
        headers["User-Agent"] = "Stormo/1.1"
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                code, body, ctype = r.status, r.read(), r.headers.get("Content-Type", "application/json")
        except urllib.error.HTTPError as e:
            code, body, ctype = e.code, e.read(), e.headers.get("Content-Type", "application/json")
        except Exception as e:  # network error, timeout, TLS…
            return self._json(502, {"error": f"proxy: {e}"})
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except OSError:
        return None


def open_browser(url):
    if shutil.which("termux-open-url"):  # Android / Termux
        subprocess.Popen(["termux-open-url", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        try:
            webbrowser.open(url)
        except Exception:
            pass


def main():
    ap = argparse.ArgumentParser(description="Stormo local server")
    ap.add_argument("--port", type=int, default=int(os.environ.get("PORT", 8080)))
    ap.add_argument("--lan", action="store_true", help="listen on all interfaces (other devices on your network)")
    ap.add_argument("--no-open", action="store_true", help="don't open the browser")
    args = ap.parse_args()

    host = "0.0.0.0" if args.lan else "127.0.0.1"
    server = None
    for port in range(args.port, args.port + 20):
        try:
            server = http.server.ThreadingHTTPServer((host, port), Handler)
            break
        except OSError:
            continue
    if not server:
        sys.exit(f"No free port between {args.port} and {args.port + 19}")

    url = f"http://localhost:{port}/"
    print("\n  🐟 Stormo")
    print(f"  ➜  {url}")
    if args.lan:
        ip = lan_ip()
        if ip:
            print(f"  ➜  http://{ip}:{port}/   (Wi-Fi / LAN)")
        print("  ⚠  LAN mode: anyone on your network can use this page and its proxy.")
    print("\n  IT  Apri l'indirizzo nel browser. Ctrl+C per fermare.")
    print("  EN  Open the address in your browser. Ctrl+C to stop.")
    print("  RU  Откройте адрес в браузере. Ctrl+C — остановить.\n")
    if not args.no_open:
        open_browser(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Bye 👋")
        server.server_close()


if __name__ == "__main__":
    main()
