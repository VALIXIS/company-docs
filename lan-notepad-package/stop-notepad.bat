@echo off
title Stop LAN Notepad
echo ========================================================
echo Stopping LAN Notepad Server (Port 5000)...
echo ========================================================
set FOUND=0
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :5000 ^| findstr LISTENING') do (
    taskkill /F /PID %%a >nul 2>&1
    echo Terminated process PID %%a running on port 5000.
    set FOUND=1
)
if "%FOUND%"=="0" (
    echo No process was found actively listening on port 5000.
)
echo.
echo Server stopped.
pause
