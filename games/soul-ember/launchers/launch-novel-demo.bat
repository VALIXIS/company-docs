@echo off
title NOVEL Hotel & Rooftop - Valixis Live Demo Launcher
echo ===================================================
echo   NOVEL HOTEL - GUNTUR | VALIXIS DEMO SUITE
echo ===================================================
echo.
echo Launching demo in default browser...
start "" "%~dp0..\client-sites\novel-hotel\index.html"
echo.
echo Standalone file opened!
echo.
echo If you want to view on your mobile phone over Wi-Fi:
echo Starting local web server on port 8080...
echo.
python -m http.server 8080 --directory "%~dp0..\client-sites"
pause
