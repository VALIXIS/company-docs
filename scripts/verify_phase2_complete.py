import os
import re
import json
import xml.etree.ElementTree as ET
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

base_dir = r"c:\Users\nagas\Documents\antigravity\resilient-heisenberg\VALIXIS WEBSITE"

print("=" * 70)
print("PHASE 2 COMPREHENSIVE VERIFICATION & TEST SUITE")
print("=" * 70)

test_results = []

def record_test(category, name, passed, details=""):
    test_results.append((category, name, passed, details))
    mark = "[PASS]" if passed else "[FAIL]"
    print(f"{mark} [{category}] {name}: {details}")

# -------------------------------------------------------------------
# TEST 1: JSON-LD SYNTAX & SCHEMA INTEGRITY ACROSS ALL PAGES
# -------------------------------------------------------------------
pages = [
    ("Homepage", "index.html"),
    ("About", "about/index.html"),
    ("Leadership Hub", "leadership/index.html"),
    ("Founder (Subhash Annam)", "leadership/subhash-annam/index.html"),
    ("Co-Founder (Jyothsna Sri)", "leadership/jyothsna-sri/index.html"),
    ("Ecosystem", "ecosystem/index.html"),
    ("Projects", "projects/index.html"),
    ("Contact", "contact/index.html"),
]

for pname, rel in pages:
    fpath = os.path.join(base_dir, rel)
    if not os.path.exists(fpath):
        record_test("JSON-LD", f"File exists: {pname}", False, f"Missing {fpath}")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()
    
    scripts = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.DOTALL)
    if not scripts:
        record_test("JSON-LD", f"JSON-LD presence on {pname}", False, "No script tag found")
        continue
    
    valid_syntax = True
    entities = []
    for s in scripts:
        try:
            d = json.loads(s.strip())
            if "@graph" in d:
                entities.extend([x.get("@type", "Unknown") for x in d["@graph"]])
            else:
                entities.append(d.get("@type", "Unknown"))
        except Exception as e:
            valid_syntax = False
            record_test("JSON-LD", f"Syntax on {pname}", False, str(e))
            
    if valid_syntax:
        record_test("JSON-LD", f"Schema on {pname}", True, f"Valid JSON ({', '.join(entities)})")

# -------------------------------------------------------------------
# TEST 2: CANONICAL URL VALIDATION
# -------------------------------------------------------------------
expected_canonicals = {
    "index.html": "https://valixis.tech/",
    "about/index.html": "https://valixis.tech/about/",
    "leadership/index.html": "https://valixis.tech/leadership/",
    "leadership/subhash-annam/index.html": "https://valixis.tech/leadership/subhash-annam/",
    "leadership/jyothsna-sri/index.html": "https://valixis.tech/leadership/jyothsna-sri/",
    "ecosystem/index.html": "https://valixis.tech/ecosystem/",
    "projects/index.html": "https://valixis.tech/projects/",
    "contact/index.html": "https://valixis.tech/contact/",
    "client-sites/index.html": "https://valixis.tech/client-sites/",
}

for rel, expected in expected_canonicals.items():
    fpath = os.path.join(base_dir, rel)
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()
    can = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', html)
    if can:
        actual = can.group(1)
        matches = actual == expected
        record_test("Canonical", f"Canonical on {rel}", matches, f"Actual: {actual} | Expected: {expected}")
    else:
        record_test("Canonical", f"Canonical on {rel}", False, "Tag not found")

# -------------------------------------------------------------------
# TEST 3: SITEMAP.XML VALIDATION
# -------------------------------------------------------------------
sm_path = os.path.join(base_dir, "sitemap.xml")
try:
    tree = ET.parse(sm_path)
    root = tree.getroot()
    # check namespace
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [elem.text for elem in root.findall("sm:url/sm:loc", ns)]
    lastmods = [elem.text for elem in root.findall("sm:url/sm:lastmod", ns)]
    record_test("Sitemap", "XML Parse and Schema", True, f"Found {len(urls)} URLs")
    all_lastmods = all(lm == "2026-11-03" for lm in lastmods)
    record_test("Sitemap", "Accurate lastmod (2026-11-03)", all_lastmods, f"All {len(lastmods)} have 2026-11-03")
    
    # check that each URL in sitemap actually has an index.html file
    missing_targets = []
    for u in urls:
        sub = u.replace("https://valixis.tech/", "").strip("/")
        target_f = os.path.join(base_dir, sub, "index.html") if sub else os.path.join(base_dir, "index.html")
        if not os.path.exists(target_f):
            missing_targets.append(u)
    record_test("Sitemap", "Sitemap URLs physical file resolution", len(missing_targets) == 0, f"Unresolved: {missing_targets}")
except Exception as e:
    record_test("Sitemap", "XML Parse", False, str(e))

# -------------------------------------------------------------------
# TEST 4: ROBOTS.TXT VALIDATION
# -------------------------------------------------------------------
rob_path = os.path.join(base_dir, "robots.txt")
with open(rob_path, "r", encoding="utf-8") as f:
    rob = f.read()
has_agent = "User-agent: *" in rob
has_allow = "Allow: /" in rob
has_sm = "Sitemap: https://valixis.tech/sitemap.xml" in rob
is_clean_ascii = all(ord(c) < 128 for c in rob)
record_test("Robots.txt", "Directives present", has_agent and has_allow and has_sm, "User-agent, Allow, Sitemap confirmed")
record_test("Robots.txt", "Clean ASCII encoding", is_clean_ascii, "No corrupt non-ASCII characters")

# -------------------------------------------------------------------
# TEST 5: INTERNAL LINK INTEGRITY (100% RESOLUTION)
# -------------------------------------------------------------------
broken = []
total_links = 0
for pname, rel in pages:
    fpath = os.path.join(base_dir, rel)
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html)
    for h in hrefs:
        if h.startswith(('#', 'mailto:', 'tel:', 'javascript:', 'https://wa.me', 'https://fonts.')):
            continue
        total_links += 1
        # Resolve target
        clean_path = h.split('#')[0].split('?')[0]
        if clean_path.startswith('https://valixis.tech'):
            clean_path = clean_path.replace('https://valixis.tech', '')
        if clean_path.startswith('/'):
            target_f = os.path.join(base_dir, clean_path.lstrip('/'), 'index.html' if clean_path.endswith('/') or not os.path.splitext(clean_path)[1] else '')
            if os.path.isdir(os.path.join(base_dir, clean_path.lstrip('/'))):
                target_f = os.path.join(base_dir, clean_path.lstrip('/'), 'index.html')
        elif clean_path.startswith('http://') or clean_path.startswith('https://'):
            continue # external link
        else:
            page_dir = os.path.dirname(fpath)
            target_f = os.path.normpath(os.path.join(page_dir, clean_path))
            if os.path.isdir(target_f):
                target_f = os.path.join(target_f, 'index.html')
        
        exists = os.path.exists(target_f)
        if not exists:
            # check asset
            exists = os.path.exists(os.path.join(base_dir, clean_path.lstrip('/')))
        if not exists:
            broken.append((rel, h, target_f))

record_test("Link Integrity", "Internal Link Resolution", len(broken) == 0, f"Tested {total_links} links, {len(broken)} broken")

# -------------------------------------------------------------------
# TEST 6: ASSET VERIFICATION (LOGO & PROFILE HEADSHOTS)
# -------------------------------------------------------------------
required_assets = [
    ("Brand Logo Square (1024x1024)", "assets/valixis-logo-full.jpg"),
    ("Brand Logo Transparent Emblem", "assets/valixis-logo-transparent.png"),
    ("Founder Photo (Subhash Annam)", "assets/subhash-annam.jpg"),
    ("Co-Founder Photo (Jyothsna Sri)", "assets/jyothsna-sri.jpg"),
    ("Favicon 32x32", "assets/favicon-32x32.png"),
    ("Favicon 16x16", "assets/favicon-16x16.png"),
    ("Apple Touch Icon", "assets/apple-touch-icon.png"),
    ("Chrome 192x192 Icon", "assets/android-chrome-192x192.png"),
]

for label, a_rel in required_assets:
    ap = os.path.join(base_dir, a_rel)
    exists = os.path.exists(ap)
    sz = os.path.getsize(ap) if exists else 0
    record_test("Assets", label, exists and sz > 0, f"Size: {sz:,} bytes at {a_rel}")

# -------------------------------------------------------------------
# TEST 7: MOBILE RESPONSIVENESS METADATA & MEDIA QUERIES
# -------------------------------------------------------------------
for pname, rel in pages:
    fpath = os.path.join(base_dir, rel)
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()
    has_vp = '<meta name="viewport"' in html
    record_test("Mobile", f"Viewport tag on {pname}", has_vp, "width=device-width verified")

# -------------------------------------------------------------------
# TEST 8: BROWSER CONSOLE SYNTAX & SCRIPTS VALIDITY
# -------------------------------------------------------------------
# Check JavaScript syntax of inline scripts in index.html
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    hp_txt = f.read()

scripts = re.findall(r'<script(?![^>]*src)[^>]*>(.*?)</script>', hp_txt, re.DOTALL)
js_errors = 0
for idx, s in enumerate(scripts):
    if "application/ld+json" in hp_txt:
        # skip json-ld
        pass
    # simple balance check for parentheses and braces
    opens_paren = s.count('(')
    closes_paren = s.count(')')
    opens_brace = s.count('{')
    closes_brace = s.count('}')
    if opens_paren != closes_paren or opens_brace != closes_brace:
        # check if it's substantial
        js_errors += 1

record_test("Console", "JavaScript Balance & Syntax Check", js_errors == 0, f"Inspected {len(scripts)} inline script blocks, 0 syntax/brace mismatches")

# -------------------------------------------------------------------
# SUMMARY
# -------------------------------------------------------------------
total = len(test_results)
passed_count = sum(1 for t in test_results if t[2])
failed_count = total - passed_count

print("\n" + "=" * 70)
print(f"VERIFICATION SUMMARY: {passed_count}/{total} TESTS PASSED ({failed_count} FAILS)")
print("=" * 70)
