@echo off
TITLE STOP ALL VALIXIS BOTS AND ENGINES
COLOR 0C

echo ============================================================
echo   STOPPING ALL RUNNING VALIXIS BOTS, ENGINES AND SERVERS
echo ============================================================
echo.

echo [*] Terminating all Python processes (Mesh, Hunter, Radar, Server)...
taskkill /F /IM python.exe /T 2>nul
taskkill /F /IM pythonw.exe /T 2>nul

echo [*] Terminating all Node.js processes (WhatsApp Bridge)...
taskkill /F /IM node.exe /T 2>nul

echo.
echo ============================================================
echo [SUCCESS] All VALIXIS bots, background daemons, and
echo           servers have been completely stopped.
echo ============================================================
echo.
pause
