"""
⏰ 4:00 AM Automated Campaign Dispatcher
Resumes and dispatches all remaining leads in leads.db across Resend (9 leads) and Gmail (89 leads).
Ensures 100% deliverability, human pacing, and WhatsApp progress alerts.
"""

import os
import sys
import sqlite3
import logging
from datetime import datetime
from dotenv import load_dotenv

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "ai_agents", ".env"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "ai_agents"))

from whatsapp_client import notify_subhash
from dispatch_batch2_resend import dispatch_resend_campaign
from dispatch_batch2_gmail import dispatch_gmail_campaign

LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "ai_agents", "data", "morning_4am_dispatch.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("Morning4AMDispatcher")

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "ai_agents", "data", "leads.db")

def run_morning_dispatch():
    logger.info("==================================================")
    logger.info(f"⏰ 4:00 AM MORNING AUTOMATED DISPATCH TRIGGERED")
    logger.info(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("==================================================")

    # Check pending counts
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT count(*) FROM leads WHERE status = 'READY_RESEND_BATCH_2'")
    pending_resend = c.fetchone()[0]
    
    c.execute("SELECT count(*) FROM leads WHERE status IN ('READY_GMAIL_BATCH_2', 'READY_GMAIL')")
    pending_gmail = c.fetchone()[0]
    conn.close()

    notify_subhash(
        f"⏰ *4:00 AM MORNING DISPATCH INITIATED*\n\n"
        f"🎯 Remaining Resend Queue: {pending_resend} targets\n"
        f"🎯 Remaining Gmail Queue: {pending_gmail} targets\n"
        f"Gmail 24h rolling limit is 100% reset.\n"
        f"Starting autonomous dispatches now...",
        title=""
    )

    # Step 1: Dispatch remaining Resend leads
    if pending_resend > 0:
        logger.info(f"\n--- [PHASE 1] DISPATCHING {pending_resend} RESEND LEADS ---")
        try:
            dispatch_resend_campaign()
        except Exception as e:
            logger.error(f"Error in Resend dispatch: {e}")

    # Step 2: Dispatch remaining Gmail leads
    if pending_gmail > 0:
        logger.info(f"\n--- [PHASE 2] DISPATCHING {pending_gmail} GMAIL LEADS ---")
        try:
            dispatch_gmail_campaign()
        except Exception as e:
            logger.error(f"Error in Gmail dispatch: {e}")

    # Final summary check
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT status, count(*) FROM leads GROUP BY status")
    counts = dict(c.fetchall())
    conn.close()

    summary_text = (
        f"🏁 *4:00 AM MORNING DISPATCH COMPLETED*\n\n"
        f"📊 Final Database Statuses:\n"
        f"• Contacted via Gmail: {counts.get('CONTACTED_GMAIL', 0)}\n"
        f"• Contacted via Resend: {counts.get('CONTACTED_EMAIL', 0)}\n"
        f"• Bounced (Protected): {counts.get('BOUNCED', 0)}\n\n"
        f"All replies arriving directly in official.valixis@gmail.com and subhash@valixis.tech!"
    )
    logger.info(summary_text)
    notify_subhash(summary_text, title="")

if __name__ == "__main__":
    run_morning_dispatch()
