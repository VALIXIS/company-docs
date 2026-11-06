@echo off
setlocal enabledelayedexpansion
title HIYYA DINO MANDI 3D - Prehistoric Dining Experience
cls
echo =========================================================================
echo       HIYYA DINO MANDI - 3D T-REX DIVE ^& ARABIAN FEAST EXPERIENCE
echo =========================================================================
echo.

:: Detect project directory whether launched from client-sites, root, or hiyya
set "HIYYA_DIR="
if exist "%~dp0..\..\hiyya\package.json" (
    set "HIYYA_DIR=%~dp0..\..\hiyya"
) else if exist "%~dp0..\hiyya\package.json" (
    set "HIYYA_DIR=%~dp0..\hiyya"
) else if exist "%~dp0package.json" (
    set "HIYYA_DIR=%~dp0"
)

if "%HIYYA_DIR%"=="" (
    echo [ERROR] Could not locate the 'hiyya' 3D project folder.
    echo Please make sure the 'hiyya' folder exists in your project.
    echo.
    pause
    exit /b 1
)

cd /d "%HIYYA_DIR%"
echo [OK] Located 3D project at: %CD%
echo.

:: Launch browser in background after 2 seconds to allow server to bind first
start /b "" cmd /c "ping 127.0.0.1 -n 3 >nul & start http://localhost:5173/"

:: Use optimized production preview if dist exists (instant load), else dev mode
if exist "dist\index.html" (
    echo [INFO] Starting high-speed server from optimized build...
    echo [INFO] Opening http://localhost:5173 in your default browser...
    echo.
    echo Press Ctrl+C at any time to stop the server.
    echo =========================================================================
    npx vite preview --port 5173 --host
) else (
    echo [INFO] Starting Vite development server...
    echo [INFO] Opening http://localhost:5173 in your default browser...
    echo.
    echo Press Ctrl+C at any time to stop the server.
    echo =========================================================================
    npm run dev
)
