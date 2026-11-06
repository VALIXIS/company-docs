@echo off
title LAN Notepad & Command Hub
cd /d "%~dp0..\lan-notepad"
echo Starting LAN Notepad & Command Hub...
node server.js
pause
