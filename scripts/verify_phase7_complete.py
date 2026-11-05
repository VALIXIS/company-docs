import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

tests_passed = 0
tests_failed = 0

def check(condition, message):
    global tests_passed, tests_failed
    if condition:
        print(f"  [PASS] {message}")
        tests_passed += 1
    else:
        print(f"  [FAIL] {message}")
        tests_failed += 1

print("=" * 80)
print("VALIXIS WEBSITE 2.0 — PHASE 7 TECHNICAL AUDIT & VERIFICATION SUITE")
print("Focus: Product Showcase, Verified Statuses, Video Player & Demonstrations")
print("=" * 80)

# -----------------------------------------------------------------------------
# 1. PRODUCT AUDIT & VERIFIED STATUSES
# -----------------------------------------------------------------------------
print("\n--- 1. VERIFIED PRODUCT PRESENTATIONS & STATUSES ---")

eco_path = 'ecosystem/index.html'
check(os.path.exists(eco_path), "ecosystem/index.html exists")

with open(eco_path, 'r', encoding='utf-8') as f:
    eco_html = f.read()

products = [
    ("VALIXIS Portal", "launched", "Live / Launched"),
    ("VALIXIS FLOW", "active", "Active Development"),
    ("VALIXIS CLOUD", "planned", "Planned"),
    ("VALIXIS DESK_AI", "prototype", "Prototype"),
    ("VALIXIS PULSE", "active", "Active Development"),
    ("Fitora", "prototype", "Prototype"),
    ("VALIXIS Gaming Studio", "planned", "Planned")
]

for name, status_slug, status_label in products:
    check(name.lower() in eco_html.lower(), f"Product present: '{name}'")
    check(f'data-status="{status_slug}"' in eco_html, f"Status attribute matches '{status_slug}' for '{name}'")
    check(status_label.lower() in eco_html.lower(), f"Verified status label displayed: '{status_label}'")

# Check required components in product presentation
required_components = [
    ("Purpose", "prod-purpose"),
    ("Problem Solved", "Problem Solved"),
    ("Main Capabilities", "caps-list"),
    ("Verified Tech Stack", "chips-row"),
    ("Terminal / Console / Preview", "terminal-box"),
    ("Call to Action", "btn-card-act"),
]

for label, needle in required_components:
    check(needle in eco_html, f"Component present across cards: '{label}'")

# -----------------------------------------------------------------------------
# 2. VIDEO DEMONSTRATION EXPERIENCE AUDIT
# -----------------------------------------------------------------------------
print("\n--- 2. VIDEO DEMONSTRATION THEATER ---")

check('id="video-demo"' in eco_html, "Video theater container with id='video-demo' present")
check('<video' in eco_html and 'id="valixisPlayer"' in eco_html, "HTML5 <video> element with id='valixisPlayer' present")
check('poster="../assets/videos/valixis-video-poster.png"' in eco_html, "Poster frame configured on video element")
check('preload="none"' in eco_html, "Lazy loading (preload='none') enforced for bandwidth optimization")
check('valixis-product-preview.mp4' in eco_html, "Source MP4 file specified")
check('kind="captions"' in eco_html and 'valixis-demo-captions.vtt' in eco_html, "WebVTT captions track configured")
check('id="videoOverlay"' in eco_html, "Accessible big play button overlay present")
check('id="playBtn"' in eco_html, "HUD play/pause control button present")
check('id="muteBtn"' in eco_html, "HUD audio mute/unmute control present")
check('toggleFullscreen()' in eco_html, "Fullscreen toggle functionality implemented")
check('id="currentTimeDisplay"' in eco_html and 'id="durationDisplay"' in eco_html, "Real-time playback duration counters present")
check('id="transcriptDrawer"' in eco_html, "Timestamped 60-90 second walkthrough transcript drawer present")
check('00:00' in eco_html and '01:30' in eco_html, "Complete 00:00 to 01:30 timestamped narrative present")

# Check video files on disk
video_file = 'assets/videos/valixis-product-preview.mp4'
poster_file = 'assets/videos/valixis-video-poster.png'
vtt_file = 'assets/videos/valixis-demo-captions.vtt'
video_readme = 'assets/videos/README.md'

check(os.path.exists(video_file) and os.path.getsize(video_file) > 100000, f"Demonstration video file exists ({video_file})")
check(os.path.exists(poster_file) and os.path.getsize(poster_file) > 10000, f"Video poster frame exists ({poster_file})")
check(os.path.exists(vtt_file) and os.path.getsize(vtt_file) > 100, f"WebVTT captions file exists ({vtt_file})")
check(os.path.exists(video_readme) and os.path.getsize(video_readme) > 500, f"Video ingestion specifications exist ({video_readme})")

# -----------------------------------------------------------------------------
# 3. FILTERING ENGINE & INTERACTION
# -----------------------------------------------------------------------------
print("\n--- 3. INTERACTIVE PRODUCT FILTERING ENGINE ---")

check('filterProducts(' in eco_html, "JavaScript filterProducts() engine implemented")
check('filter-btn' in eco_html, "Filter tabs present for All, Launched, Active, Prototype, Planned")
check('role="tablist"' in eco_html, "Accessible ARIA tablist semantics implemented")

# -----------------------------------------------------------------------------
# 4. LIFECYCLE ROADMAP & HOMEPAGE CROSS-LINKAGE
# -----------------------------------------------------------------------------
print("\n--- 4. PROJECTS ROADMAP & HOMEPAGE INTEGRATION ---")

proj_path = 'projects/index.html'
check(os.path.exists(proj_path), "projects/index.html exists")

with open(proj_path, 'r', encoding='utf-8') as f:
    proj_html = f.read()

check('1. Launched &amp; Production Platforms' in proj_html, "Lifecycle Group 1: Launched & Production Platforms present")
check('2. Active Development Pipelines' in proj_html, "Lifecycle Group 2: Active Development Pipelines present")
check('3. Active Prototypes &amp; Staging Builds' in proj_html, "Lifecycle Group 3: Active Prototypes & Staging Builds present")
check('4. Planned &amp; Frontier Research' in proj_html, "Lifecycle Group 4: Planned & Frontier Research present")
check('href="../ecosystem/#portal"' in proj_html, "Project card deep-links to Portal")
check('href="../ecosystem/#flow"' in proj_html, "Project card deep-links to FLOW")
check('href="../ecosystem/#pulse"' in proj_html, "Project card deep-links to PULSE")
check('href="../ecosystem/#fitora"' in proj_html, "Project card deep-links to Fitora")
check('href="../ecosystem/#desk-ai"' in proj_html, "Project card deep-links to DESK_AI")
check('href="../ecosystem/#cloud"' in proj_html, "Project card deep-links to CLOUD")
check('href="../ecosystem/#gaming-studio"' in proj_html, "Project card deep-links to Gaming Studio")

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

check('ecosystem/#video-demo' in index_html, "Homepage spotlights 90s technical walkthrough video")
check('href="ecosystem/"' in index_html, "Homepage links to complete 7-product showcase")

# -----------------------------------------------------------------------------
# 5. DIRECTORY SYNCHRONIZATION AUDIT
# -----------------------------------------------------------------------------
print("\n--- 5. DIRECTORY SYNCHRONIZATION ---")

sync_pairs = [
    ('ecosystem/index.html', 'VALIXIS WEBSITE/ecosystem/index.html'),
    ('projects/index.html', 'VALIXIS WEBSITE/projects/index.html'),
    ('index.html', 'VALIXIS WEBSITE/index.html'),
    ('assets/videos/valixis-product-preview.mp4', 'VALIXIS WEBSITE/assets/videos/valixis-product-preview.mp4'),
    ('assets/videos/valixis-video-poster.png', 'VALIXIS WEBSITE/assets/videos/valixis-video-poster.png'),
    ('assets/videos/valixis-demo-captions.vtt', 'VALIXIS WEBSITE/assets/videos/valixis-demo-captions.vtt'),
    ('assets/videos/README.md', 'VALIXIS WEBSITE/assets/videos/README.md'),
]

for p1, p2 in sync_pairs:
    if os.path.exists(p1) and os.path.exists(p2):
        s1 = os.path.getsize(p1)
        s2 = os.path.getsize(p2)
        check(s1 == s2, f"Synchronized: {p1} ({s1} B) == {p2} ({s2} B)")
    else:
        check(False, f"Missing sync pair: {p1} or {p2}")

# -----------------------------------------------------------------------------
# 6. RELATIVE LINK INTEGRITY AUDIT
# -----------------------------------------------------------------------------
print("\n--- 6. LINK INTEGRITY AUDIT ---")

for check_path in ['ecosystem/index.html', 'projects/index.html']:
    dir_name = os.path.dirname(check_path)
    with open(check_path, 'r', encoding='utf-8') as f:
        content = f.read()
    links = re.findall(r'(?:href|src)=[\"\']([^\"\']+)[\"\']', content)
    broken = 0
    for link in links:
        if link.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#', 'data:')):
            continue
        clean = link.split('#')[0].split('?')[0]
        if not clean:
            continue
        target = os.path.normpath(os.path.join(dir_name, clean))
        if os.path.isdir(target):
            target = os.path.join(target, 'index.html')
        if not os.path.exists(target):
            broken += 1
            print(f"  [BROKEN LINK] in {check_path}: {link} -> {target}")
    check(broken == 0, f"All relative links in {check_path} resolve (0 broken)")

# -----------------------------------------------------------------------------
# SUMMARY
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
total_tests = tests_passed + tests_failed
pass_rate = (tests_passed / total_tests) * 100 if total_tests > 0 else 0
print(f"PHASE 7 AUDIT RESULTS: {tests_passed}/{total_tests} TESTS PASSED ({pass_rate:.1f}%)")
if tests_failed == 0:
    print("ALL PHASE 7 VERIFICATION CRITERIA MET WITH 100% SUCCESS.")
else:
    print(f"ATTENTION: {tests_failed} tests failed. Immediate review required.")
print("=" * 80)
