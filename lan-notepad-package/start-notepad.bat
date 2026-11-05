@echo off
title LAN Notepad & Command Hub (Server)
cd /d "%~dp0\lan-notepad"
echo ========================================================
echo  Starting LAN Notepad & Command Hub Server...
echo ========================================================
node -v >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Node.js is not installed or not in PATH!
    echo Please install Node.js from https://nodejs.org or run:
    echo   winget install OpenJS.NodeJS.LTS
    echo.
    pause
    exit /b 1
)
node server.js
pause
