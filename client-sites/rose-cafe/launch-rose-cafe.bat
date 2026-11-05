@echo off
title "Rose Cafe - 5th Floor Indoor Floral Cafe"
echo =========================================================================
echo       ROSE CAFE - 5TH FLOOR INDOOR FLORAL HAVEN
echo =========================================================================
echo.
echo Opening Rose Cafe website preview in your default browser...
start "" "%~dp0index.html"
echo [OK] Launched!
ping 127.0.0.1 -n 2 >nul
