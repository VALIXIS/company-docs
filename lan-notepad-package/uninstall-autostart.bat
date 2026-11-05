@echo off
title Uninstall LAN Notepad Autostart
set "RUNNER_VBS=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\LAN-Notepad-Autostart.vbs"
if exist "%RUNNER_VBS%" (
    del "%RUNNER_VBS%"
    echo [SUCCESS] LAN Notepad autostart script removed from Windows Startup folder.
) else (
    echo [INFO] Autostart script was not found in Startup folder.
)
pause
