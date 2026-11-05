with open('sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()

import xml.etree.ElementTree as ET
root = ET.fromstring(content)
urls = [elem.text for elem in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
print(f"Total URLs in sitemap: {len(urls)}")
for u in urls:
    if 'contact' in u:
        print("Contact in sitemap:", u)
