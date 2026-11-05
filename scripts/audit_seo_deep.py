import os, sys, json, re
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 80)
print("DEEP AUDIT: ITEMS 6 - 10 (SCHEMA, ENTITIES, CANONICALS, ROBOTS, NOINDEX)")
print("=" * 80)

# Check Subhash Annam links & schema
with open('leadership/subhash-annam/index.html', 'r', encoding='utf-8') as f:
    subhash_html = f.read()

# Check Jyothsna Sri links & schema
with open('leadership/jyothsna-sri/index.html', 'r', encoding='utf-8') as f:
    jyothsna_html = f.read()

# Check Leadership index
with open('leadership/index.html', 'r', encoding='utf-8') as f:
    lead_html = f.read()

# 6. Backlinks to Organization in leadership profiles
print("\n--- ITEM 6: Backlinks to VALIXIS Organization in Leadership Profiles ---")
subhash_links = re.findall(r'<a\s+[^>]*?href=[\'"](.*?)[\'"][^>]*?>(.*?)</a>', subhash_html, re.I)
subhash_org_links = [l for l in subhash_links if 'about' in l[0] or l[0] in ['../../', '/', 'https://valixis.tech', 'https://valixis.tech/']]
print(f"Subhash Annam profile org backlinks ({len(subhash_org_links)}):")
for url, text in subhash_org_links:
    clean_text = re.sub(r'<[^>]+>', '', text).strip()
    print(f"   href='{url}' -> '{clean_text}'")

jyothsna_links = re.findall(r'<a\s+[^>]*?href=[\'"](.*?)[\'"][^>]*?>(.*?)</a>', jyothsna_html, re.I)
jyothsna_org_links = [l for l in jyothsna_links if 'about' in l[0] or l[0] in ['../../', '/', 'https://valixis.tech', 'https://valixis.tech/']]
print(f"Jyothsna Sri profile org backlinks ({len(jyothsna_org_links)}):")
for url, text in jyothsna_org_links:
    clean_text = re.sub(r'<[^>]+>', '', text).strip()
    print(f"   href='{url}' -> '{clean_text}'")

# 7 & 8. Schema.org JSON-LD Entities and Stable Identifiers
print("\n--- ITEM 7 & 8: Schema.org Entities, Stable @id Identifiers, & Person-Org Relations ---")

def extract_jsonld(html, filename):
    matches = re.findall(r'<script\s+type=[\'"]application/ld\+json[\'"]>([\s\S]*?)</script>', html, re.I)
    schemas = []
    for m in matches:
        try:
            parsed = json.loads(m)
            schemas.append(parsed)
        except Exception as e:
            print(f"JSON-LD parse error in {filename}: {e}")
    return schemas

# Check Homepage schema
with open('index.html', 'r', encoding='utf-8') as f:
    home_schemas = extract_jsonld(f.read(), 'index.html')

print("Homepage Schemas:")
for s in home_schemas:
    graph = s.get('@graph', [s])
    for item in graph:
        print(f"  @type: {item.get('@type')}, @id: {item.get('@id')}")
        if item.get('@type') == 'Organization':
            print(f"    founder @id: {item.get('founder', {}).get('@id') if isinstance(item.get('founder'), dict) else item.get('founder')}")
            print(f"    funder/co-founder: {item.get('funder', {}).get('@id') if isinstance(item.get('funder'), dict) else item.get('funder')}")

# Check Subhash Schema
subhash_schemas = extract_jsonld(subhash_html, 'subhash-annam/index.html')
print("\nSubhash Annam Schemas:")
for s in subhash_schemas:
    graph = s.get('@graph', [s])
    for item in graph:
        print(f"  @type: {item.get('@type')}, @id: {item.get('@id')}")
        if item.get('@type') == 'Person':
            print(f"    name: {item.get('name')}")
            print(f"    jobTitle: {item.get('jobTitle')}")
            print(f"    worksFor: {item.get('worksFor')}")

# Check Jyothsna Schema
jyothsna_schemas = extract_jsonld(jyothsna_html, 'jyothsna-sri/index.html')
print("\nJyothsna Sri Schemas:")
for s in jyothsna_schemas:
    graph = s.get('@graph', [s])
    for item in graph:
        print(f"  @type: {item.get('@type')}, @id: {item.get('@id')}")
        if item.get('@type') == 'Person':
            print(f"    name: {item.get('name')}")
            print(f"    jobTitle: {item.get('jobTitle')}")
            print(f"    worksFor: {item.get('worksFor')}")

# 9. Canonical URLs, Robots Directives, Sitemap Inclusion
print("\n--- ITEM 9: Canonicals, Robots Directives, Sitemap Inclusion ---")
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    tree = ET.parse(f)
    sitemap_locs = [loc.text.strip() for loc in tree.getroot().findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

with open('robots.txt', 'r', encoding='utf-8') as f:
    robots_txt = f.read()

print(f"Total sitemap URLs: {len(sitemap_locs)}")
print(f"Subhash Annam in sitemap: {'https://valixis.tech/leadership/subhash-annam/' in sitemap_locs}")
print(f"Jyothsna Sri in sitemap: {'https://valixis.tech/leadership/jyothsna-sri/' in sitemap_locs}")
print(f"Leadership in sitemap: {'https://valixis.tech/leadership/' in sitemap_locs}")
print(f"Robots.txt has sitemap directive: {'sitemap.xml' in robots_txt.lower()}")

# 10. Ensure no important leadership page is marked noindex or blocked
print("\n--- ITEM 10: Noindex / Robots Block Check ---")
for p, html in [('leadership/index.html', lead_html), ('leadership/subhash-annam/index.html', subhash_html), ('leadership/jyothsna-sri/index.html', jyothsna_html)]:
    has_noindex = 'noindex' in html.lower()
    has_canonical = re.search(r'<link\s+rel=[\'"]canonical[\'"]\s+href=[\'"](.*?)[\'"]', html)
    can_url = has_canonical.group(1) if has_canonical else 'None'
    print(f"{p}:")
    print(f"  noindex present?: {has_noindex}")
    print(f"  canonical URL: {can_url}")
    print(f"  crawlable by robots.txt?: {'Disallow: /leadership' not in robots_txt}")
