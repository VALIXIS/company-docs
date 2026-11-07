@echo off
TITLE VALIXIS Channel 2 Lead Radar Bot (24/7 Daemon)
COLOR 0B

echo ============================================================
echo   VALIXIS CHANNEL 2 LEAD RADAR BOT (Secondary Laptop)
echo   Monitors r/forhire, r/SaaS, r/hiredev, r/webdev for clients
echo   Direct Real-Time Telegram Alerts to Subhash
echo ============================================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not added to PATH.
    echo Please install Python 3.10 or higher from https://python.org
    pause
    exit /b
)

:: Navigate to script directory
cd /d "%~dp0"

:: Check for .env file
if not exist "ai_agents\.env" (
    echo [WARNING] ai_agents\.env file not found.
    echo Make sure TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are configured.
    echo.
)

echo [*] Starting Lead Radar Daemon...
echo [*] Press Ctrl+C at any time to pause or exit.
echo ============================================================
echo.

:LOOP
python ai_agents\channel2_lead_radar_bot.py --interval 300
if errorlevel 1 (
    echo.
    echo [!] Bot encountered an unexpected termination.
    echo [*] Auto-restarting in 20 seconds...
    timeout /t 20 >nul
    goto LOOP
)

pause
