import urllib.request
import urllib.error
import re
import xml.etree.ElementTree as ET

urls = [
    'https://valixis.tech/',
    'https://valixis.tech/about/',
    'https://valixis.tech/leadership/',
    'https://valixis.tech/leadership/subhash-annam/',
    'https://valixis.tech/leadership/jyothsna-sri/',
    'https://valixis.tech/services/',
    'https://valixis.tech/work/',
    'https://valixis.tech/estimate/',
    'https://valixis.tech/ecosystem/',
    'https://valixis.tech/contact/',
    'https://valixis.tech/sitemap.xml',
    'https://valixis.tech/robots.txt'
]

headers = {'User-Agent': 'Mozilla/5.0'}

# 1. Fetch sitemap.xml and parse URLs
req_sm = urllib.request.Request('https://valixis.tech/sitemap.xml', headers=headers)
with urllib.request.urlopen(req_sm) as resp:
    sitemap_xml = resp.read().decode('utf-8')

root = ET.fromstring(sitemap_xml)
sitemap_urls = set()
for url_elem in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    loc = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    if loc is not None and loc.text:
        sitemap_urls.add(loc.text.strip())

# 2. Fetch robots.txt
req_rob = urllib.request.Request('https://valixis.tech/robots.txt', headers=headers)
with urllib.request.urlopen(req_rob) as resp:
    robots_txt = resp.read().decode('utf-8')

print("=" * 90)
print(f"{'URL':<42} | {'STATUS':<6} | {'IN SITEMAP':<10} | {'CANONICAL':<35} | {'ROBOTS META'}")
print("=" * 90)

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req) as resp:
            status = resp.status
            content = resp.read().decode('utf-8', errors='ignore')
            
            in_sitemap = "YES" if u in sitemap_urls or (u.endswith('/') and u in sitemap_urls) else "N/A"
            if u.endswith('sitemap.xml') or u.endswith('robots.txt'):
                in_sitemap = "--"
            
            canonical_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', content, re.IGNORECASE)
            canonical = canonical_match.group(1) if canonical_match else "MISSING"
            if u.endswith('sitemap.xml') or u.endswith('robots.txt'):
                canonical = "--"
                
            robots_match = re.search(r'<meta\s+name=["\']robots["\']\s+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
            robots_meta = robots_match.group(1) if robots_match else "MISSING"
            if u.endswith('sitemap.xml') or u.endswith('robots.txt'):
                robots_meta = "--"
                
            print(f"{u:<42} | {status:<6} | {in_sitemap:<10} | {canonical:<35} | {robots_meta}")
    except Exception as e:
        print(f"{u:<42} | ERROR: {e}")

print("=" * 90)
print("\nROBOTS.TXT CONTENT:")
print(robots_txt.strip())
print(f"\nTOTAL SITEMAP URLS COUNT: {len(sitemap_urls)}")
