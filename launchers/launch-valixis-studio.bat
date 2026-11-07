@echo off
title VALIXIS TECHNOLOGIES - Multi-Client Studio Showcase
echo ==========================================================
echo   VALIXIS TECHNOLOGIES - CLIENT DEMO PORTFOLIO STUDIO
echo ==========================================================
echo.
echo Launching Master Client Studio in default browser...
start "" "%~dp0..\client-sites\index.html"
echo.
echo Demo switcher launched successfully!
echo Featuring:
echo   [1] HIYYA DINO MANDI (Jurassic Prehistoric + Mandi Platter Sizer + 3D WebGL)
echo   [2] NOVEL Hotel & Rooftop Restaurant (Guntur's #1 Luxury Hotel & Biryani)
echo   [3] Roastery Coffee House (Hyderabad)
echo   [4] Subko Specialty Coffee & Bakehouse (Mumbai)
echo   [5] Blue Tokai Coffee Roasters (Mumbai)
echo.
echo Starting local mobile preview server on port 8080...
python -m http.server 8080 --directory "%~dp0..\client-sites"
pause
