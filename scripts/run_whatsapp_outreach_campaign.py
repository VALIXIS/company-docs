import os
import sys
import time
import random
import sqlite3
import logging
import requests
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ai_agents"))
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("whatsapp_outreach.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("WhatsAppOutreach")

ENV_PATH = os.path.join(os.path.dirname(__file__), "ai_agents", ".env")
load_dotenv(ENV_PATH)

BRIDGE_URL = os.getenv("WHATSAPP_LOCAL_SERVICE_URL", "http://100.127.80.62:3001").rstrip('/')
DB_PATH = os.path.join(os.path.dirname(__file__), "ai_agents", "data", "leads.db")
PORTFOLIO_URL = "https://valixis.github.io/company-docs/"

def check_bridge_status():
    try:
        r = requests.get(f"{BRIDGE_URL}/status", timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data.get("ready", False)
    except Exception:
        pass
    return False

def send_wa(recipient_raw, text):
    digits = "".join(filter(str.isdigit, recipient_raw))
    if len(digits) == 10:
        digits = "91" + digits
    jid = f"{digits}@c.us"
    payload = {
        "recipient": jid,
        "message": text,
        "phone": jid
    }
    try:
        res = requests.post(f"{BRIDGE_URL}/send-task-alert", json=payload, timeout=25)
        return res.status_code == 200
    except Exception as e:
        logger.error(f"Error sending to {recipient_raw}: {e}")
        return False

def generate_custom_pitch(company, niche, existing_copy):
    if existing_copy and len(existing_copy.strip()) > 35:
        clean = existing_copy.strip()
        if "valixis.github.io/company-docs" not in clean:
            clean += f"\n\nOur live client builds & documentation: {PORTFOLIO_URL}"
        return clean

    niche_lower = (niche or "").lower()
    if any(k in niche_lower for k in ["cafe", "roaster", "coffee", "patisserie", "dessert", "bakery", "dining"]):
        return (
            f"Hey {company} team! ☕ Loving the aesthetic and energy of your space.\n\n"
            f"I run VALIXIS, an engineering studio based in AP/Telangana. We build sleek, branded direct online ordering & VIP loyalty web apps for specialty cafes that save 20-25% on delivery platform commissions.\n\n"
            f"You can review our live architecture documentation and past builds here: {PORTFOLIO_URL}\n\n"
            f"Would love to share a quick 60-second interactive preview tailored to {company} if you're open to exploring!"
        )
    elif any(k in niche_lower for k in ["clinic", "dental", "skin", "aesthetic", "dermatology", "laser"]):
        return (
            f"Hello {company} team! 👋\n\n"
            f"I run VALIXIS Technologies, a specialized engineering studio. We build custom high-converting patient booking workflows and VIP consultation portals for aesthetic & dental clinics.\n\n"
            f"Our clients typically see a 35% increase in confirmed bookings with automated WhatsApp reminders that cut front desk call loads.\n\n"
            f"Feel free to check our live engineering documentation & architecture here: {PORTFOLIO_URL}\n\n"
            f"Would love to share a quick preview if helpful for your front desk!"
        )
    elif any(k in niche_lower for k in ["agency", "marketing", "creative", "branding"]):
        return (
            f"Hi {company} leadership! 👋\n\n"
            f"I lead VALIXIS Technologies, a dedicated 7-member engineering pod based in AP/Telangana. We act as an external white-label technical arm for growth and creative agencies—handling custom web applications, portals, and Flutter mobile apps behind the scenes.\n\n"
            f"Explore our engineering portfolio & architecture: {PORTFOLIO_URL}\n\n"
            f"Would you be open to a quick 10-minute sync this week to explore partnering on upcoming client tech requests?"
        )
    else:
        return (
            f"Hey {company} team! 👋\n\n"
            f"I run VALIXIS Technologies, a 7-member dedicated engineering pod. We help brands and startups rapidly build high-performance web apps, MVP modules, and automations in dedicated 30-day sprints.\n\n"
            f"Our live engineering architecture & documentation: {PORTFOLIO_URL}\n\n"
            f"Would love to connect for a quick 5-minute chat to see if we can help scale your tech pipeline!"
        )

def run_continuous_outreach():
    logger.info("==================================================")
    logger.info("🚀 VALIXIS 24/7 AUTONOMOUS PAN-INDIA WHATSAPP ENGINE")
    logger.info(f"Target Bridge: {BRIDGE_URL}")
    logger.info("==================================================")
    
    total_lifetime_delivered = 0

    while True:
        try:
            # 1. Verify bridge health
            if not check_bridge_status():
                logger.warning("WhatsApp Bridge offline or busy. Waiting 15s to retry...")
                time.sleep(15)
                continue

            # 2. Query available uncontacted leads
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, company, phone, niche, whatsapp_copy 
                FROM leads 
                WHERE status = 'READY_WHATSAPP'
                ORDER BY id ASC
                LIMIT 30
            """)
            leads = cursor.fetchall()
            conn.close()

            # If no leads left in current queue, replenish from autonomous hunter!
            if not leads:
                logger.info("Replenishing queue with fresh Pan-India targets...")
                try:
                    from autonomous_india_lead_hunter import replenish_leads
                    replenish_leads()
                except Exception as e:
                    logger.error(f"Error replenishing leads: {e}")
                
                time.sleep(10)
                continue

            logger.info(f"📋 Loaded active batch: {len(leads)} verified mobile targets.")

            batch_delivered = 0
            for idx, (lead_id, company, phone, niche, wa_copy) in enumerate(leads, 1):
                custom_pitch = generate_custom_pitch(company, niche, wa_copy)
                logger.info(f"[{idx}/{len(leads)}] Dispatching to {company} ({phone})...")
                
                success = send_wa(phone, custom_pitch)
                
                conn = sqlite3.connect(DB_PATH)
                c = conn.cursor()
                if success:
                    c.execute("UPDATE leads SET status = 'CONTACTED_WA', updated_at = CURRENT_TIMESTAMP WHERE id = ?", (lead_id,))
                    batch_delivered += 1
                    total_lifetime_delivered += 1
                    logger.info(f"  ✅ Delivered [{batch_delivered} in batch | {total_lifetime_delivered} total]: {company}")
                    conn.commit()
                    conn.close()

                    # Human anti-spam interval ONLY on successful delivery
                    delay = random.uniform(15.0, 22.0)
                    logger.info(f"⏳ Human cooldown {delay:.1f}s before next pitch...\n")
                    time.sleep(delay)

                    # Batch break every 12 messages
                    if batch_delivered > 0 and batch_delivered % 12 == 0:
                        logger.info("☕ Batch milestone (12 sends) reached. Taking a 5-minute human rest interval...")
                        time.sleep(300)
                else:
                    c.execute("UPDATE leads SET status = 'NO_WHATSAPP', updated_at = CURRENT_TIMESTAMP WHERE id = ?", (lead_id,))
                    logger.warning(f"  ❌ No WhatsApp for {company}. Skipped instantly in 0.8s.")
                    conn.commit()
                    conn.close()
                    time.sleep(0.8)

            logger.info(f"✨ Batch finished. Batch delivered: {batch_delivered}. Cooldown 30s before next batch...")
            time.sleep(30)

        except Exception as e:
            logger.error(f"Unexpected loop exception: {e}")
            time.sleep(20)

if __name__ == "__main__":
    run_continuous_outreach()
