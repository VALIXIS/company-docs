import os
import json
import re
import xml.etree.ElementTree as ET

PAGES = [
    'index.html',
    'about/index.html',
    'leadership/index.html',
    'leadership/subhash-annam/index.html',
    'leadership/jyothsna-sri/index.html',
    'ecosystem/index.html',
    'projects/index.html',
    'contact/index.html'
]

results = {
    'json_ld_valid': True,
    'canonicals_valid': True,
    'titles_valid': True,
    'meta_desc_valid': True,
    'internal_links_valid': True,
    'sitemap_valid': True,
    'robots_valid': True,
    'details': []
}

print("=== STARTING TECHNICAL VALIDATION ===")

# 1. Validate Robots.txt
if os.path.exists('robots.txt'):
    with open('robots.txt', 'r', encoding='utf-8') as f:
        robots_content = f.read()
    if 'User-agent: *' in robots_content and 'Sitemap: https://valixis.tech/sitemap.xml' in robots_content:
        results['details'].append("[PASS] robots.txt exists and contains valid directives and sitemap URL.")
    else:
        results['robots_valid'] = False
        results['details'].append("[FAIL] robots.txt missing required directives.")
else:
    results['robots_valid'] = False
    results['details'].append("[FAIL] robots.txt not found.")

# 2. Validate Sitemap.xml
if os.path.exists('sitemap.xml'):
    try:
        tree = ET.parse('sitemap.xml')
        root = tree.getroot()
        urls = [elem.text for elem in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
        results['details'].append(f"[PASS] sitemap.xml is valid XML containing {len(urls)} URLs: {urls}")
    except Exception as e:
        results['sitemap_valid'] = False
        results['details'].append(f"[FAIL] sitemap.xml parse error: {e}")
else:
    results['sitemap_valid'] = False
    results['details'].append("[FAIL] sitemap.xml not found.")

# 3. Validate HTML Pages
for page_path in PAGES:
    if not os.path.exists(page_path):
        results['details'].append(f"[FAIL] Page {page_path} does not exist!")
        continue

    with open(page_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Parse JSON-LD
    json_ld_matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    if not json_ld_matches:
        results['details'].append(f"[FAIL] {page_path} has NO JSON-LD structured data!")
        results['json_ld_valid'] = False
    else:
        for idx, match in enumerate(json_ld_matches):
            try:
                parsed = json.loads(match.strip())
                types = []
                if isinstance(parsed, dict):
                    if '@graph' in parsed:
                        types = [item.get('@type') for item in parsed['@graph']]
                    else:
                        types = [parsed.get('@type')]
                results['details'].append(f"[PASS] {page_path} JSON-LD block #{idx+1} parsed successfully! Types: {types}")
            except Exception as e:
                results['json_ld_valid'] = False
                results['details'].append(f"[FAIL] {page_path} JSON-LD block #{idx+1} syntax error: {e}")

    # Check Title & Meta Description
    title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    if title_match and title_match.group(1).strip():
        title = title_match.group(1).strip()
    else:
        title = None
        results['titles_valid'] = False
        results['details'].append(f"[FAIL] {page_path} is missing a <title> tag!")

    meta_match = re.search(r'<meta name="description" content="(.*?)"', html, re.DOTALL)
    if meta_match and meta_match.group(1).strip():
        meta_desc = meta_match.group(1).strip()
    else:
        meta_desc = None
        results['meta_desc_valid'] = False
        results['details'].append(f"[FAIL] {page_path} is missing a meta description!")

    # Check Canonical
    canonical_match = re.search(r'<link rel="canonical" href="(.*?)"', html)
    if canonical_match and canonical_match.group(1).strip():
        canonical = canonical_match.group(1).strip()
    else:
        canonical = None
        results['canonicals_valid'] = False
        results['details'].append(f"[FAIL] {page_path} is missing a canonical link!")

    results['details'].append(f"[PAGE AUDIT] {page_path} | Title: '{title[:45]}...' | Canonical: {canonical}")

print("\n--- SUMMARY OF RESULTS ---")
for line in results['details']:
    print(line)

all_passed = all([
    results['json_ld_valid'],
    results['canonicals_valid'],
    results['titles_valid'],
    results['meta_desc_valid'],
    results['sitemap_valid'],
    results['robots_valid']
])
print(f"\nOVERALL VALIDATION SUCCESS: {all_passed}")
