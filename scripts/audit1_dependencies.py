import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

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

scripts_seen = {}
links_seen = {}

for cp in canonical_pages:
    with open(cp, 'r', encoding='utf-8') as f:
        content = f.read()

    scripts = re.findall(r'<script\s+[^>]*src=[\"\']([^\"\']+)[\"\'][^>]*>', content, re.IGNORECASE)
    for s in scripts:
        scripts_seen.setdefault(s, []).append(cp)

    links = re.findall(r'<link\s+[^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>', content, re.IGNORECASE)
    for l in links:
        if 'stylesheet' in l or 'font' in l:
            links_seen.setdefault(l, []).append(cp)

print("=== External & Local Scripts Imported ===")
for s, pages in scripts_seen.items():
    print(f"  {s} -> Used in {len(pages)} pages")

print("\n=== Stylesheets & Font Links ===")
for l, pages in links_seen.items():
    print(f"  {l} -> Used in {len(pages)} pages")
