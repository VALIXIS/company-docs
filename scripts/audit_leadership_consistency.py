import glob
import re
import json

html_files = sorted(glob.glob('./**/*.html', recursive=True))

print("=== CHECKING LEADERSHIP PROFILES AND SCHEMA ===")
for f in html_files:
    if any(x in f for x in ['.git', 'node_modules', 'scratch']):
        continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    # Check JSON-LD
    scripts = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', content, re.DOTALL)
    for s in scripts:
        try:
            data = json.loads(s.strip())
            graph = data.get('@graph', [data])
            for node in graph:
                if node.get('@type') == 'Person':
                    name = node.get('name')
                    job = node.get('jobTitle')
                    org = node.get('worksFor', {}).get('name') if isinstance(node.get('worksFor'), dict) else node.get('worksFor')
                    print(f"{f}: Person -> {name} | {job} | worksFor: {org}")
        except Exception:
            pass

    # Check leadership cards in HTML
    for m in re.finditer(r'<h[234][^>]*class=["\'][^"\']*leader-name[^"\']*["\'][^>]*>(.*?)</h[234]>\s*<div[^>]*class=["\'][^"\']*leader-role[^"\']*["\'][^>]*>(.*?)</div>', content, re.DOTALL):
        name = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        role = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        print(f"{f}: HTML Card -> {name} | {role}")
