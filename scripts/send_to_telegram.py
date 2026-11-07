"""
VALIXIS Telegram Portfolio Dispatcher
Sends the cafe portfolio HTML files and portfolio link to Telegram.
"""
import os
import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
HTML_DIR = BASE_DIR / "cafe_portfolio_html"
PORTFOLIO_LINK = "https://valixis.github.io/company-docs/"

def send_telegram_message(bot_token: str, chat_id: str, text: str):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = json.dumps({
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def send_telegram_document(bot_token: str, chat_id: str, file_path: Path, caption: str = ""):
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    boundary = "----WebKitFormBoundaryValixisTelegram7MA4YWxkTrZu0gW"
    
    body = bytearray()
    
    # chat_id field
    body.extend(f"--{boundary}\r\n".encode("utf-8"))
    body.extend(f'Content-Disposition: form-data; name="chat_id"\r\n\r\n{chat_id}\r\n'.encode("utf-8"))
    
    # caption field
    if caption:
        body.extend(f"--{boundary}\r\n".encode("utf-8"))
        body.extend(f'Content-Disposition: form-data; name="caption"\r\n\r\n{caption}\r\n'.encode("utf-8"))
        
    # document field
    filename = file_path.name
    with open(file_path, "rb") as f:
        file_bytes = f.read()
        
    mime_type = "application/octet-stream"
    if filename.endswith(".png"):
        mime_type = "image/png"
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        mime_type = "image/jpeg"
    elif filename.endswith(".mp4"):
        mime_type = "video/mp4"
    elif filename.endswith(".html"):
        mime_type = "text/html"
        
    body.extend(f"--{boundary}\r\n".encode("utf-8"))
    body.extend(f'Content-Disposition: form-data; name="document"; filename="{filename}"\r\n'.encode("utf-8"))
    body.extend(f"Content-Type: {mime_type}\r\n\r\n".encode("utf-8"))
    body.extend(file_bytes)
    body.extend(b"\r\n")
    
    body.extend(f"--{boundary}--\r\n".encode("utf-8"))
    
    req = urllib.request.Request(url, data=body, headers={
        "Content-Type": f"multipart/form-data; boundary={boundary}"
    })
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def wait_for_start(bot_token: str, timeout_seconds: int = 120):
    """Waits for any user to tap /start on the bot and returns (chat_id, username)."""
    import time
    start_time = time.time()
    print("[*] Waiting for you to tap /start on the bot in Telegram (t.me/valixis_metspy_bot)...")
    while time.time() - start_time < timeout_seconds:
        url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                if data.get("ok") and data.get("result"):
                    for update in reversed(data["result"]):
                        if "message" in update and "chat" in update["message"]:
                            chat_id = update["message"]["chat"]["id"]
                            username = update["message"]["chat"].get("username", "")
                            first_name = update["message"]["chat"].get("first_name", "")
                            print(f"[+] Message detected from: {first_name} (@{username}) [Chat ID: {chat_id}]")
                            return str(chat_id), username
        except Exception as e:
            pass
        time.sleep(2)
    return None, None

def dispatch_all(bot_token: str, chat_id: str):
    print(f"[*] Sending greeting and portfolio link to chat_id: {chat_id}...")
    intro = (
        f"<b>🚀 VALIXIS Studio — Portfolio Websites & Documentation</b>\n\n"
        f"Here are the standalone <code>index.html</code> files for the high-end cafe & roastery websites we built:\n\n"
        f"🌐 <b>Live Portfolio Link:</b>\n{PORTFOLIO_LINK}\n\n"
        f"Delivering individual HTML website files below 👇"
    )
    send_telegram_message(bot_token, chat_id, intro)
    
    html_files = [
        ("Blue_Tokai_Coffee_Roasters_index.html", "☕ <b>Blue Tokai Coffee Roasters</b> — Specialty Roastery & Cafe Landing Page"),
        ("Roastery_Coffee_House_index.html", "☕ <b>Roastery Coffee House</b> — Heritage Roastery, Menu & Experience"),
        ("Subko_Specialty_Coffee_index.html", "☕ <b>Subko Specialty Coffee & Bakehouse</b> — Craft Coffee & Artisanal Bakes"),
        ("Novel_Hotel_Dining_index.html", "🏨 <b>Novel Hotel & Dining Cafe</b> — Boutique Luxury Hospitality & Cafe"),
        ("Valixis_Cafe_Showcase_Directory_index.html", "📁 <b>Valixis Complete Cafe Showcase</b> — Master Portfolio Showcase")
    ]
    
    for filename, caption in html_files:
        fpath = HTML_DIR / filename
        if fpath.exists():
            print(f"[*] Uploading {filename}...")
            send_telegram_document(bot_token, chat_id, fpath, caption)
            print(f"[+] Sent {filename} successfully.")

    zip_file = HTML_DIR / "valixis_cafe_portfolio_websites.zip"
    if zip_file.exists():
        print(f"[*] Uploading all-in-one zip package...")
        send_telegram_document(bot_token, chat_id, zip_file, "📦 <b>All-in-One Cafe Portfolio Zip Archive</b>")
        print(f"[+] Sent zip package successfully.")

    print("\n[SUCCESS] All files and portfolio links delivered to Telegram!")

if __name__ == "__main__":
    token = sys.argv[1] if len(sys.argv) > 1 else os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("[!] Usage: python send_to_telegram.py <BOT_TOKEN> [CHAT_ID]")
        sys.exit(1)
        
    chat = sys.argv[2] if len(sys.argv) > 2 else None
    if not chat:
        chat, username = wait_for_start(token, timeout_seconds=180)
        if not chat:
            print("[!] Timeout waiting for /start. Please open https://t.me/valixis_metspy_bot and send /start!")
            sys.exit(1)
        print(f"[*] Found user: @{username} (Chat ID: {chat})")
        
    dispatch_all(token, str(chat))
