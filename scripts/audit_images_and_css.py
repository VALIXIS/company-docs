import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

files = [
    'index.html',
    'estimate/index.html',
    'work/index.html',
    'work/rose-cafe/index.html',
    'work/novel-hotel/index.html',
    'work/hiyya-dino-mandi/index.html',
    'services/index.html',
    'services/ai-automation/index.html',
    'services/software-mobile/index.html',
    'services/web-platforms/index.html',
    'services/3d-gaming-interactive/index.html',
    'client-sites/index.html',
    'about/index.html',
    'leadership/index.html',
    'leadership/subhash-annam/index.html',
    'leadership/jyothsna-sri/index.html',
    'ecosystem/index.html',
    'projects/index.html',
    'contact/index.html'
]

img_tag_pattern = re.compile(r'<img\s+[^>]*?>', re.IGNORECASE)

for fp in files:
    if not os.path.exists(fp):
        print(f"MISSING: {fp}")
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        html = f.read()

    has_focus = 'focus-visible' in html
    has_motion = 'prefers-reduced-motion' in html

    imgs = img_tag_pattern.findall(html)
    unbounded_imgs = []
    for img in imgs:
        has_w = 'width=' in img
        has_h = 'height=' in img
        if not (has_w and has_h):
            src_m = re.search(r'src=[\'"](.*?)[\'"]', img)
            src = src_m.group(1) if src_m else 'unknown'
            unbounded_imgs.append((img, src))

    print(f"{fp} => focus={has_focus}, motion={has_motion}, unbounded_imgs={len(unbounded_imgs)}")
    if unbounded_imgs:
        for tag, src in unbounded_imgs[:4]:
            print(f"   src: {src}")
