# 💻 VALIXIS Channel 2 Lead Radar — Old Laptop Quick Setup Guide

This guide explains how to run the **Channel 2 Lead Radar Bot** 24/7 on your secondary/old laptop so it quietly monitors remote client hiring channels and pings your phone whenever a high-budget client ($500–$2,500) posts looking to hire a developer.

---

## 🚀 3-Minute Quick Setup

### Step 1: Ensure Python is Installed
Open Command Prompt (`cmd`) on your old laptop and check:
```cmd
python --version
```
- If Python 3.10+ is installed, you are ready.
- If not installed, download the official installer from [python.org](https://www.python.org/downloads/) (Make sure to check the box: **"Add Python to PATH"** during installation).

### Step 2: Ensure the Workspace Files & `.env` are Present
The bot only requires these core files on the laptop:
- `START_CHANNEL2_BOT.bat`
- `ai_agents/channel2_lead_radar_bot.py`
- `ai_agents/.env` (Contains your `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`, and optional `GEMINI_API_KEY`)
- `ai_agents/data/` (Where `leads.db` stores all captured opportunities)

### Step 3: Run the Bot
Simply double-click:
```
START_CHANNEL2_BOT.bat
```
That's it! A clean black-and-cyan console window will open, showing:
- Active scan cycles every 5 minutes (300s).
- Live heartbeat timestamps.
- Zero paid API keys used.
- Lightweight memory footprint (<50 MB RAM).

---

## ⚡ Recommended Windows Power Setting (For Running with Lid Closed)
To let your old laptop run 24/7 with the screen closed:
1. Press `Win + R`, type `control`, and press Enter.
2. Go to **Hardware and Sound** → **Power Options**.
3. In the left sidebar, click **"Choose what closing the lid does"**.
4. Set **"When I close the lid"** to **"Do nothing"** (for Plugged in).
5. Click **Save changes**.

Now you can plug in the charger, close the laptop lid, tuck it away in a corner, and let it quietly scout clients while sending alerts straight to your phone.

---

## 📱 What You Receive on Telegram
Whenever a paying client posts:
```
🎯 NEW CLIENT HIRING OPPORTUNITY
━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 Community: r/forhire
👤 Client: u/startup_founder
⭐ Score: 85/100 (Verified [Hiring] Tag, Budget Detected)

📌 Title: [HIRING] Need Next.js + Supabase dev for MVP ($1,500 budget)

🔗 Open Reddit Post Directly

💬 Pre-Drafted 1-Click Proposal:
"Hey! Just saw your post regarding the Next.js MVP. I run VALIXIS (https://valixis.tech), 
an independent engineering studio shipping clean builds in 2-week sprints.
Our live blueprints: https://valixis.tech/work/ — let me know if you'd like to chat!"
```
You can simply tap the link, paste the proposal in their DMs, and start the conversation before anyone else.

---

## 🛠️ Testing Commands
To verify the bot at any time:
- **Send a mock test alert to Telegram:**
  ```cmd
  python ai_agents\channel2_lead_radar_bot.py --test-alert
  ```
- **Run a single test scan pass:**
  ```cmd
  python ai_agents\channel2_lead_radar_bot.py --test
  ```
