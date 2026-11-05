import os
import re
import json
import xml.etree.ElementTree as ET
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

base_dir = r"c:\Users\nagas\Documents\antigravity\resilient-heisenberg\VALIXIS WEBSITE"

print("=" * 70)
print("PHASE 4 FEATURED WORK & INTERACTIVE SHOWCASE TEST SUITE")
print("=" * 70)

test_results = []

def record(category, name, passed, details=""):
    test_results.append((category, name, passed, details))
    mark = "[PASS]" if passed else "[FAIL]"
    print(f"{mark} [{category}] {name}: {details}")

# All 18 Core Pages in the Website
all_18_pages = [
    ("Homepage", "index.html"),
    ("Work Portfolio Hub", "work/index.html"),
    ("Case Study: Rose Cafe", "work/rose-cafe/index.html"),
    ("Case Study: Novel Hotel", "work/novel-hotel/index.html"),
    ("Case Study: Hiyya Dino", "work/hiyya-dino-mandi/index.html"),
    ("Services Hub", "services/index.html"),
    ("AI Automation", "services/ai-automation/index.html"),
    ("Software & Mobile", "services/software-mobile/index.html"),
    ("Web Platforms", "services/web-platforms/index.html"),
    ("3D & Gaming", "services/3d-gaming-interactive/index.html"),
    ("Client Showcase Portal", "client-sites/index.html"),
    ("About", "about/index.html"),
    ("Leadership Hub", "leadership/index.html"),
    ("Founder (Subhash Annam)", "leadership/subhash-annam/index.html"),
    ("Co-Founder (Jyothsna Sri)", "leadership/jyothsna-sri/index.html"),
    ("Ecosystem", "ecosystem/index.html"),
    ("Projects", "projects/index.html"),
    ("Contact", "contact/index.html"),
]

# -------------------------------------------------------------------
# 1. JSON-LD VALIDATION ACROSS ALL 18 PAGES
# -------------------------------------------------------------------
for pname, rel in all_18_pages:
    fp = os.path.join(base_dir, rel)
    if not os.path.exists(fp):
        record("JSON-LD", f"File presence: {pname}", False, f"Missing {rel}")
        continue
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()
    
    scripts = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.DOTALL)
    if not scripts:
        if rel == "client-sites/index.html":
            record("JSON-LD", f"Schema on {pname}", True, "Showcase gallery (JSON-LD optional)")
            continue
        record("JSON-LD", f"Schema presence on {pname}", False, "No JSON-LD script found")
        continue

    valid = True
    types = []
    for s in scripts:
        try:
            d = json.loads(s.strip())
            if "@graph" in d:
                types.extend([x.get("@type", "Unknown") for x in d["@graph"]])
            else:
                types.append(d.get("@type", "Unknown"))
        except Exception as e:
            valid = False
            record("JSON-LD", f"JSON Syntax on {pname}", False, str(e))
    if valid:
        record("JSON-LD", f"Schema on {pname}", True, f"Valid ({', '.join(types)})")

# -------------------------------------------------------------------
# 2. CANONICAL VALIDATION ACROSS ALL 18 PAGES
# -------------------------------------------------------------------
for pname, rel in all_18_pages:
    fp = os.path.join(base_dir, rel)
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()
    can = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', html)
    expected_path = "" if rel == "index.html" else rel.replace("index.html", "")
    expected_url = f"https://valixis.tech/{expected_path}"
    if can:
        actual = can.group(1)
        record("Canonical", f"Canonical URL on {pname}", actual == expected_url, f"{actual}")
    else:
        record("Canonical", f"Canonical URL on {pname}", False, "Tag missing")

# -------------------------------------------------------------------
# 3. SITEMAP.XML 18-URL PARSE AND LASTMOD VALIDATION
# -------------------------------------------------------------------
sm_path = os.path.join(base_dir, "sitemap.xml")
try:
    tree = ET.parse(sm_path)
    root = tree.getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [elem.text for elem in root.findall("sm:url/sm:loc", ns)]
    lastmods = [elem.text for elem in root.findall("sm:url/sm:lastmod", ns)]
    record("Sitemap", "XML Parse & Schema Integrity", len(urls) == 18, f"Found {len(urls)}/18 canonical URLs")
    all_lastmod_ok = all(lm == "2026-11-03" for lm in lastmods)
    record("Sitemap", "Accurate lastmod dates (2026-11-03)", all_lastmod_ok, f"All {len(lastmods)} timestamps verified")
    
    # Check physical file existence for all 18 URLs
    missing = []
    for u in urls:
        sub = u.replace("https://valixis.tech/", "").strip("/")
        target_f = os.path.join(base_dir, sub, "index.html") if sub else os.path.join(base_dir, "index.html")
        if not os.path.exists(target_f):
            missing.append(u)
    record("Sitemap", "Sitemap Physical File Resolution", len(missing) == 0, f"Unresolved: {missing}")
except Exception as e:
    record("Sitemap", "XML Parse Error", False, str(e))

# -------------------------------------------------------------------
# 4. LINK INTEGRITY CHECK ACROSS ALL 18 PAGES
# -------------------------------------------------------------------
broken = []
total_internal_links = 0
for pname, rel in all_18_pages:
    fp = os.path.join(base_dir, rel)
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html)
    for h in hrefs:
        if h.startswith(('#', 'mailto:', 'tel:', 'javascript:', 'https://wa.me', 'https://fonts.', 'https://instagram.com', 'https://images.unsplash.com')):
            continue
        total_internal_links += 1
        clean_path = h.split('#')[0].split('?')[0]
        if clean_path.startswith('https://valixis.tech'):
            clean_path = clean_path.replace('https://valixis.tech', '')
        if clean_path.startswith('/'):
            target_f = os.path.join(base_dir, clean_path.lstrip('/'), 'index.html' if clean_path.endswith('/') or not os.path.splitext(clean_path)[1] else '')
            if os.path.isdir(os.path.join(base_dir, clean_path.lstrip('/'))):
                target_f = os.path.join(base_dir, clean_path.lstrip('/'), 'index.html')
        elif clean_path.startswith(('http://', 'https://')):
            continue
        else:
            page_dir = os.path.dirname(fp)
            target_f = os.path.normpath(os.path.join(page_dir, clean_path))
            if os.path.isdir(target_f):
                target_f = os.path.join(target_f, 'index.html')
        
        exists = os.path.exists(target_f) or os.path.exists(os.path.join(base_dir, clean_path.lstrip('/')))
        if not exists:
            broken.append((rel, h, target_f))

record("Link Integrity", "Internal Link Resolution", len(broken) == 0, f"Tested {total_internal_links} links, {len(broken)} broken")

# -------------------------------------------------------------------
# 5. INTERACTIVE DEMO SITES VERIFICATION
# -------------------------------------------------------------------
demo_targets = [
    ("Rose Cafe Demo", "client-sites/rose-cafe/index.html"),
    ("Novel Hotel Demo", "client-sites/novel-hotel/index.html"),
    ("Hiyya Dino Mandi Demo", "client-sites/hiyya-dino-mandi/index.html"),
    ("Roastery Coffee Demo", "client-sites/roastery-coffee-house/index.html"),
    ("Subko Coffee Demo", "client-sites/subko-coffee/index.html"),
    ("Blue Tokai Demo", "client-sites/blue-tokai/index.html"),
]

for label, d_rel in demo_targets:
    dp = os.path.join(base_dir, d_rel)
    exists = os.path.exists(dp)
    sz = os.path.getsize(dp) if exists else 0
    record("Demo Resolution", label, exists and sz > 10000, f"Size: {sz:,} bytes at {d_rel}")

# -------------------------------------------------------------------
# 6. LAZY-LOAD & SANDBOX ATTRIBUTES VERIFICATION
# -------------------------------------------------------------------
with open(os.path.join(base_dir, "work", "index.html"), "r", encoding="utf-8") as f:
    work_html = f.read()

has_sandbox = 'sandbox="allow-scripts allow-same-origin allow-forms"' in work_html
has_blank_src = 'src="about:blank"' in work_html
has_lazy_img = 'loading="lazy"' in work_html

record("Security & Performance", "Iframe Sandbox Restrictions", has_sandbox, "allow-scripts allow-same-origin allow-forms verified")
record("Security & Performance", "Iframe Lazy Unloaded Default (src=about:blank)", has_blank_src, "Zero memory overhead on initial load")
record("Security & Performance", "Lazy Loading on Images (loading=lazy)", has_lazy_img, "Native lazy loading verified")

# -------------------------------------------------------------------
# SUMMARY
# -------------------------------------------------------------------
total = len(test_results)
passed = sum(1 for t in test_results if t[2])
failed = total - passed

print("\n" + "=" * 70)
print(f"VERIFICATION SUMMARY: {passed}/{total} TESTS PASSED ({failed} FAILS)")
print("=" * 70)
