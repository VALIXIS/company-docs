import os
import re
from urllib.parse import urlparse

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

print("=== STARTING INTERNAL LINK INTEGRITY AUDIT ===")

broken_links = []
checked_links = 0

for page in PAGES:
    with open(page, 'r', encoding='utf-8') as f:
        html = f.read()

    page_dir = os.path.dirname(page)

    # Find all href and src
    matches = re.findall(r'(?:href|src)=["\'](.*?)["\']', html)
    for target in matches:
        # Ignore external links, mailto, tel, anchors
        if target.startswith(('http://', 'https://', 'mailto:', 'tel:', '#', 'javascript:', 'data:')):
            continue

        checked_links += 1
        clean_target = target.split('?')[0].split('#')[0]
        if not clean_target:
            continue

        resolved_path = os.path.normpath(os.path.join(page_dir, clean_target))

        # If it's a directory, check for index.html
        if os.path.isdir(resolved_path):
            resolved_file = os.path.join(resolved_path, 'index.html')
        else:
            resolved_file = resolved_path

        if not os.path.exists(resolved_file):
            broken_links.append((page, target, resolved_file))

print(f"Total internal links/assets checked: {checked_links}")
if broken_links:
    print(f"BROKEN LINKS DETECTED ({len(broken_links)}):")
    for src, link, res in broken_links:
        print(f"  In {src}: '{link}' -> Resolved to missing: '{res}'")
else:
    print("ALL INTERNAL LINKS AND ASSETS RESOLVED PERFECTLY (0 BROKEN LINKS)!")
