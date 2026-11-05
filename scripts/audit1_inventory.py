import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 80)
print("AUDIT SCRIPT 1: REPOSITORY ARCHITECTURE & INVENTORY")
print("=" * 80)

html_files = []
css_mentions = 0
js_mentions = 0

for root, dirs, files in os.walk('.'):
    if any(k in root for k in ['.git', 'node_modules', 'brain', '__pycache__']):
        continue
    for f in files:
        full = os.path.normpath(os.path.join(root, f))
        if f.endswith('.html'):
            html_files.append((full, os.path.getsize(full)))

print(f"Total HTML files found in repo: {len(html_files)}")
print("\nKey Website Routes (Canonical Pages):")
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

for cp in canonical_pages:
    exists_root = os.path.exists(cp)
    exists_mirror = os.path.exists(os.path.join('VALIXIS WEBSITE', cp))
    size_root = os.path.getsize(cp) if exists_root else 0
    size_mirror = os.path.getsize(os.path.join('VALIXIS WEBSITE', cp)) if exists_mirror else 0
    match_str = "MATCH" if size_root == size_mirror and exists_root else "MISMATCH"
    print(f"  [{match_str}] {cp:<42} Root: {size_root:>7} B | Mirror: {size_mirror:>7} B")
