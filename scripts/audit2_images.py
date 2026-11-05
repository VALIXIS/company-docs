import os
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

print("=== Image Attributes & CLS Audit ===")
missing_lazy = 0
missing_dimensions = 0
total_images = 0

for cp in canonical_pages:
    with open(cp, 'r', encoding='utf-8') as f:
        content = f.read()

    imgs = re.findall(r'(<img\s+[^>]*>)', content, re.IGNORECASE)
    for tag in imgs:
        total_images += 1
        src_match = re.search(r'src=[\"\']([^\"\']+)[\"\']', tag)
        src = src_match.group(1) if src_match else "unknown"
        has_lazy = 'loading=' in tag.lower()
        has_w = 'width=' in tag.lower()
        has_h = 'height=' in tag.lower()

        # If it's a hero or brand logo in navbar, lazy loading is not needed, but width/height is needed for CLS
        is_above_fold = 'brand-lockup' in tag or 'valixis-horizontal' in tag
        
        if not has_lazy and not is_above_fold:
            missing_lazy += 1
            # print(f"  [MISSING LAZY] {cp}: {src}")

        if not (has_w and has_h):
            missing_dimensions += 1
            # print(f"  [MISSING DIMENSIONS] {cp}: {src}")

print(f"Total <img> tags evaluated: {total_images}")
print(f"Images without explicit loading='lazy' (below fold): {missing_lazy}")
print(f"Images without explicit width/height attributes (CLS risk): {missing_dimensions}")
