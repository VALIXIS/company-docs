@echo off
title Setup Always-On Autostart for LAN Notepad
echo ========================================================
echo  Configuring LAN Notepad to Always Run on Boot...
echo ========================================================

node -v >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Node.js is not found on this laptop!
    echo Node.js is required to run LAN Notepad.
    echo Please download and install Node.js from:
    echo   https://nodejs.org
    echo Or run: winget install OpenJS.NodeJS.LTS
    echo.
    pause
    exit /b 1
)

set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
set "RUNNER_VBS=%STARTUP_FOLDER%\LAN-Notepad-Autostart.vbs"

:: Create the launcher in Windows Startup folder so it runs every time user logs in
(
echo Set WshShell = CreateObject^("WScript.Shell"^)
echo WshShell.Run "cmd /c ""cd /d ""%~dp0lan-notepad"" && node server.js""", 0, False
) > "%RUNNER_VBS%"

echo.
echo [SUCCESS] LAN Notepad has been registered to Windows Startup!
echo Startup script created at:
echo   %RUNNER_VBS%
echo.
echo LAN Notepad will automatically launch silently in the background
echo whenever this laptop boots or logs in.
echo.
echo Starting LAN Notepad right now in the background...
wscript "%RUNNER_VBS%"
echo.
echo ========================================================
echo [DONE] LAN Notepad server is now running!
echo Access it from your network or Tailscale on Port 5000:
echo Example: http://localhost:5000
echo ========================================================
echo You can close this window now.
pause
