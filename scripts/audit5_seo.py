import os
import re
import json
import xml.etree.ElementTree as ET
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 80)
print("AUDIT SCRIPT 5: TECHNICAL SEO, SCHEMAS & ENTITY RECOGNITION")
print("=" * 80)

canonical_pages = [
    'index.html',
    'about/index.html',
    'services/index.html',
    'services/ai-automation/index.html',
    'services/software-mobile/index.html',
    'services/web-platforms/index.html',
    'services/3d-gaming-interactive/index.html',
    'work/index.html',
    'work/rose-cafe/index.html',
    'work/novel-hotel/index.html',
    'work/hiyya-dino-mandi/index.html',
    'estimate/index.html',
    'ecosystem/index.html',
    'projects/index.html',
    'leadership/index.html',
    'leadership/subhash-annam/index.html',
    'leadership/jyothsna-sri/index.html',
    'contact/index.html',
    'client-sites/index.html'
]

jsonld_errors = 0
canonical_mismatches = 0
meta_issues = 0

for cp in canonical_pages:
    with open(cp, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Canonical check
    canon_match = re.search(r'<link\s+rel=[\"\']canonical[\"\']\s+href=[\"\']([^\"\']+)[\"\']', html)
    if not canon_match:
        canon_match = re.search(r'<link\s+href=[\"\']([^\"\']+)[\"\']\s+rel=[\"\']canonical[\"\']', html)
    
    expected_slug = "" if cp == "index.html" else cp.replace('index.html', '')
    expected_canon = f"https://valixis.tech/{expected_slug}"
    
    if not canon_match or canon_match.group(1) != expected_canon:
        print(f"  [CANONICAL ISSUE] {cp}: found '{canon_match.group(1) if canon_match else None}' vs expected '{expected_canon}'")
        canonical_mismatches += 1

    # 2. Meta description
    desc_match = re.search(r'<meta\s+name=[\"\']description[\"\']\s+content=[\"\']([^\"\']+)[\"\']', html, re.IGNORECASE)
    if not desc_match:
        desc_match = re.search(r'<meta\s+content=[\"\']([^\"\']+)[\"\']\s+name=[\"\']description[\"\']', html, re.IGNORECASE)
    if not desc_match or len(desc_match.group(1)) < 30:
        print(f"  [META DESC ISSUE] {cp}: length {len(desc_match.group(1)) if desc_match else 0}")
        meta_issues += 1

    # 3. JSON-LD validity
    json_blocks = re.findall(r'<script\s+type=[\"\']application/ld\+json[\"\']>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
    if not json_blocks:
        print(f"  [JSON-LD MISSING] {cp}")
        jsonld_errors += 1
    else:
        for b in json_blocks:
            try:
                parsed = json.loads(b.strip())
            except Exception as e:
                print(f"  [JSON-LD SYNTAX ERROR] in {cp}: {e}")
                jsonld_errors += 1

print(f"Canonical URL mismatches: {canonical_mismatches}")
print(f"Meta description issues: {meta_issues}")
print(f"JSON-LD syntax / missing errors: {jsonld_errors}")

# Sitemap XML Check
print("\n--- Sitemap.xml Verification ---")
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap_xml = f.read()

root = ET.fromstring(sitemap_xml)
sitemap_urls = [elem.text for elem in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
print(f"Total sitemap URLs: {len(sitemap_urls)}")

# Verify every canonical page is in sitemap
missing_from_sitemap = 0
for cp in canonical_pages:
    expected_slug = "" if cp == "index.html" else cp.replace('index.html', '')
    expected_canon = f"https://valixis.tech/{expected_slug}"
    if expected_canon not in sitemap_urls:
        print(f"  [MISSING FROM SITEMAP] {expected_canon}")
        missing_from_sitemap += 1
print(f"Missing from sitemap: {missing_from_sitemap}")

# Robots.txt Check
print("\n--- Robots.txt Verification ---")
with open('robots.txt', 'r', encoding='utf-8') as f:
    robots_txt = f.read()

print("User-agent in robots.txt:", "User-agent:" in robots_txt)
print("Sitemap directive in robots.txt:", "Sitemap: https://valixis.tech/sitemap.xml" in robots_txt)
print("ASCII check:", all(ord(c) < 128 for c in robots_txt))
