import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 80)
print("AUDIT SCRIPT 4: BUSINESS FEATURES TESTING")
print("=" * 80)

def test_feature(name, success, details=""):
    status = "[PASS]" if success else "[FAIL]"
    print(f"  {status} {name:<45} {details}")
    return success

# 1. Portfolio & Case Studies
with open('work/index.html', 'r', encoding='utf-8') as f:
    work_html = f.read()

test_feature("Portfolio: Rose Cafe Card", "Rose Cafe" in work_html and "rose-cafe" in work_html)
test_feature("Portfolio: Novel Hotel Card", "Novel Hotel" in work_html and "novel-hotel" in work_html)
test_feature("Portfolio: Hiyya Dino Mandi Card", "Hiyya Dino Mandi" in work_html and "hiyya-dino-mandi" in work_html)
test_feature("Portfolio: Roastery Coffee House Card", "Roastery Coffee House" in work_html)
test_feature("Portfolio: Subko Specialty Coffee Card", "Subko Specialty Coffee" in work_html)
test_feature("Portfolio: Blue Tokai Card", "Blue Tokai Coffee Roasters" in work_html)
test_feature("Portfolio: Sandboxed Modal Preview", 'id="demoModal"' in work_html and 'sandbox=' in work_html)
test_feature("Portfolio: Case Studies Exist", 
    os.path.exists('work/rose-cafe/index.html') and 
    os.path.exists('work/novel-hotel/index.html') and 
    os.path.exists('work/hiyya-dino-mandi/index.html'))

# 2. Client Demos
demos = [
    'client-sites/rose-cafe/index.html',
    'client-sites/novel-hotel/index.html',
    'client-sites/hiyya-dino-mandi/index.html',
    'client-sites/roastery-coffee-house/index.html',
    'client-sites/subko-coffee/index.html',
    'client-sites/blue-tokai/index.html'
]
for d in demos:
    test_feature(f"Client Demo: {os.path.basename(os.path.dirname(d))}", os.path.exists(d), f"Size: {os.path.getsize(d) if os.path.exists(d) else 0} B")

# 3. Services Hub & Sub-services
services = [
    'services/index.html',
    'services/ai-automation/index.html',
    'services/software-mobile/index.html',
    'services/web-platforms/index.html',
    'services/3d-gaming-interactive/index.html'
]
for s in services:
    test_feature(f"Service Route: {s}", os.path.exists(s), f"Size: {os.path.getsize(s) if os.path.exists(s) else 0} B")

# 4. Project Scope Calculator
with open('estimate/index.html', 'r', encoding='utf-8') as f:
    est_html = f.read()

test_feature("Calculator: 3-Step Wizard", 'id="step1"' in est_html and 'id="step2"' in est_html and 'id="step3"' in est_html)
test_feature("Calculator: Result Pane", 'id="step4"' in est_html and 'id="resComplexity"' in est_html)
test_feature("Calculator: WhatsApp & Email URLs", 'id="waLink"' in est_html and 'id="emailLink"' in est_html)
test_feature("Calculator: SessionStorage Handoff", 'valixis_estimated_scope' in est_html)

# 5. Booking (Cal.com)
with open('contact/index.html', 'r', encoding='utf-8') as f:
    contact_html = f.read()

test_feature("Booking: Cal.com Container", 'id="booking"' in contact_html and 'id="calIframe"' in contact_html)
test_feature("Booking: Dark Theme Parameter", 'theme=dark' in contact_html)
test_feature("Booking: Direct Action Fallbacks", 'btn-fallback-wa' in contact_html and 'btn-fallback-email' in contact_html)

# 6. Contact & Scope Form
test_feature("Form: Mandatory Input Fields", 
    'id="clientName"' in contact_html and 
    'id="clientEmail"' in contact_html and 
    'id="projectCategory"' in contact_html and 
    'id="projectDescription"' in contact_html)
test_feature("Form: Anti-Spam Honeypot", 'id="valixis_hp_security"' in contact_html)
test_feature("Form: Velocity Check", 'PAGE_LOAD_TIMESTAMP' in contact_html)
test_feature("Form: Standby Fallback Dispatch", 'showStandbyFallback' in contact_html)

# 7. Product Showcase
with open('ecosystem/index.html', 'r', encoding='utf-8') as f:
    eco_html = f.read()

test_feature("Showcase: 7 Products Defined", 
    all(k in eco_html for k in ['VALIXIS Portal', 'VALIXIS FLOW', 'VALIXIS CLOUD', 'VALIXIS DESK_AI', 'VALIXIS PULSE', 'Fitora', 'VALIXIS Gaming Studio']))
test_feature("Showcase: Status Filtering", 'filterProducts(' in eco_html and 'data-status=' in eco_html)

# 8. Video Playback
test_feature("Video: Player Element", 'id="valixisPlayer"' in eco_html and 'poster=' in eco_html)
test_feature("Video: WebVTT Subtitles", 'kind="captions"' in eco_html and os.path.exists('assets/videos/valixis-demo-captions.vtt'))
test_feature("Video: Interactive Transcript", 'id="transcriptDrawer"' in eco_html and '00:00' in eco_html)
test_feature("Video: MP4 Asset Present", os.path.exists('assets/videos/valixis-product-preview.mp4'))
