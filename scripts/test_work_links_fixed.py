import os
import re

dir_name = 'work'
with open('work/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

links = re.findall(r'(?:href|src|openDemoModal\()[\"\']([^\"\']+)[\"\']', content)
broken = 0
for link in links:
    if link.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#', 'data:')):
        continue
    clean_link = link.split('#')[0].split('?')[0]
    target_path = os.path.normpath(os.path.join(dir_name, clean_link))
    if not os.path.exists(target_path):
        print(f"[BROKEN] link '{link}' -> {target_path} NOT FOUND")
        broken += 1
    else:
        print(f"[OK] {link} -> {target_path}")

print("Total broken in work/index.html:", broken)
