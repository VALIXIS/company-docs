========================================================================
 LAN NOTEPAD & COMMAND HUB - ALWAYS-ON SERVER SETUP (OLDER LAPTOP)
========================================================================

Follow these 3 quick steps on this laptop:

STEP 1: NODE.JS PREREQUISITE
----------------------------
Make sure Node.js is installed on this laptop.
To check, open Command Prompt and type: node -v
If not installed, download the LTS version from:
   https://nodejs.org
or run in PowerShell:
   winget install OpenJS.NodeJS.LTS


STEP 2: RUN OPTIONS
----------------------------
Option A (RECOMMENDED - Always Run on Boot):
   Double-click:  setup-autostart.bat
   - This registers LAN Notepad in your Windows Startup folder.
   - It starts immediately in the background (no visible terminal window).
   - Every time this laptop turns on, it will automatically start!

Option B (Run with Visible Terminal Window):
   Double-click:  start-notepad.bat
   - Shows live server logs and network addresses.

Option C (Silent Background Run One-Time):
   Double-click:  start-hidden.vbs
   - Runs silently in the background without autostarting on boot.


HOW TO STOP THE SERVER:
----------------------------
Double-click:  stop-notepad.bat


HOW TO ACCESS LAN NOTEPAD FROM YOUR OTHER DEVICES:
----------------------------
From your current laptop, phone, or tablet on the same Wi-Fi:
Open your browser and navigate to:
   http://192.168.31.74:5000
Or if using Tailscale:
   http://subhash-pc:5000
   http://100.127.80.62:5000
========================================================================
