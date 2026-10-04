#!/usr/bin/env sh
# Stormo — avvio rapido / quick start / быстрый запуск
# PC (macOS, Linux) e Android (Termux):   sh start.sh
cd "$(dirname "$0")" || exit 1

if command -v python3 >/dev/null 2>&1; then
  PY=python3
elif command -v python >/dev/null 2>&1; then
  PY=python
elif command -v pkg >/dev/null 2>&1; then
  echo "Termux: installo Python / installing Python / устанавливаю Python…"
  pkg install -y python && PY=python
else
  echo "Serve Python 3 / Python 3 required / Нужен Python 3: https://www.python.org/downloads/"
  exit 1
fi

exec "$PY" server.py "$@"
