import os, sys, json, re
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# 1. Homepage
with open('index.html', 'r', encoding='utf-8') as f:
    home_html = f.read()

print('=== 1. HOMEPAGE ===')
print('Has independent technology venture?:', 'independent technology venture' in home_html.lower())
for line in home_html.splitlines():
    if 'independent technology venture' in line.lower() or 'independent tech' in line.lower():
        print('  Matching line:', line.strip())

# 2. About page
with open('about/index.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

print('\n=== 2. ABOUT PAGE ===')
print('Has 2026?:', '2026' in about_html)
print('Has Unregistered / Independent?:', 'unregistered' in about_html.lower() or 'independent' in about_html.lower())
for line in about_html.splitlines():
    if 'unregistered' in line.lower() or 'independent technology venture' in line.lower():
        print('  Line:', line.strip())

# 3. Leadership page
with open('leadership/index.html', 'r', encoding='utf-8') as f:
    lead_html = f.read()

print('\n=== 3. LEADERSHIP PAGE ===')
print('Links to subhash-annam?:', 'subhash-annam' in lead_html)
print('Links to jyothsna-sri?:', 'jyothsna-sri' in lead_html)

# 4. Subhash Annam profile
with open('leadership/subhash-annam/index.html', 'r', encoding='utf-8') as f:
    subhash_html = f.read()

print('\n=== 4. SUBHASH ANNAM PROFILE ===')
print('Identifies as Founder & CEO?:', 'Founder & CEO' in subhash_html or 'Founder & Chief Executive Officer' in subhash_html)
print('Links back to organization / about?:', 'href="../../about/"' in subhash_html or 'href="../../"' in subhash_html or 'about' in subhash_html)

# 5. Jyothsna Sri profile
with open('leadership/jyothsna-sri/index.html', 'r', encoding='utf-8') as f:
    jyothsna_html = f.read()

print('\n=== 5. JYOTHSNA SRI PROFILE ===')
print('Identifies as Co-Founder & CCO?:', 'Co-Founder' in jyothsna_html and ('CCO' in jyothsna_html or 'Chief Commercial Officer' in jyothsna_html))
print('Links back to organization / about?:', 'href="../../about/"' in jyothsna_html or 'href="../../"' in jyothsna_html or 'about' in jyothsna_html)
