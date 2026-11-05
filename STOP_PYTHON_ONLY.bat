@echo off
TITLE STOP PYTHON BOTS (KEEP WHATSAPP BOT RUNNING)
COLOR 0E

echo ============================================================
echo   STOPPING PYTHON BOTS ONLY (KEEPING WHATSAPP ACTIVE)
echo ============================================================
echo.

echo [*] Terminating Python processes (Mesh, Email, Hunter, Server)...
taskkill /F /IM python.exe /T 2>nul
taskkill /F /IM pythonw.exe /T 2>nul

echo.
echo ============================================================
echo [SUCCESS] Python bots and Server on Port 8000 stopped.
echo           Node.js WhatsApp Bot on Port 3001 remains ACTIVE!
echo ============================================================
echo.
pause
