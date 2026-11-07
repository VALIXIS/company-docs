@echo off
title HIYYA DINO MANDI - Valixis Live Demo Launcher
echo ===================================================
echo   HIYYA DINO MANDI - GUNTUR | VALIXIS DEMO SUITE
echo ===================================================
echo.
echo Launching 3D Dinosaur Mandi demo in default browser...
start "" "%~dp0..\client-sites\hiyya-dino-mandi\index.html"
echo.
echo Standalone 3D demo opened!
echo.
echo If you want to view on your mobile phone over Wi-Fi:
echo Starting local web server on port 8080...
echo.
python -m http.server 8080 --directory "%~dp0..\client-sites"
pause
