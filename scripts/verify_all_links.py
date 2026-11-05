import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

html_files = []
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.normpath(os.path.join(root, f)))

print(f"Total HTML files to inspect: {len(html_files)}")
broken_links = 0

for file_path in html_files:
    dir_name = os.path.dirname(file_path)
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    links = re.findall(r'href=[\"\']([^\"\']+)[\"\']', content)
    for link in links:
        if link.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#', 'data:')):
            continue
        # Strip anchor
        clean_link = link.split('#')[0].split('?')[0]
        if not clean_link:
            continue
        
        target_path = os.path.normpath(os.path.join(dir_name, clean_link))
        # If directory, look for index.html
        if os.path.isdir(target_path):
            target_path = os.path.join(target_path, 'index.html')
            
        if not os.path.exists(target_path):
            print(f"[BROKEN] In {file_path}: href='{link}' -> {target_path} NOT FOUND")
            broken_links += 1

if broken_links == 0:
    print("[SUCCESS] All relative internal links across all HTML files are valid!")
else:
    print(f"[FAIL] Found {broken_links} broken relative links.")
