@echo off
REM Stormo - avvio rapido / quick start / быстрый запуск (Windows)
cd /d "%~dp0"
where py >nul 2>nul && (py -3 server.py %* & goto :eof)
where python >nul 2>nul && (python server.py %* & goto :eof)
echo Serve Python 3 / Python 3 required: https://www.python.org/downloads/
pause
