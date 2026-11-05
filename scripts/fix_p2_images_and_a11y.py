import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

A11Y_CSS = """
    /* WCAG 2.1 AA Accessibility & Keyboard Navigation */
    a:focus-visible, button:focus-visible, input:focus-visible, select:focus-visible, textarea:focus-visible {
      outline: 2px solid #00D9FF !important;
      outline-offset: 3px !important;
    }
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }
"""

TARGET_DIRS = ['.', 'VALIXIS WEBSITE']
CANONICAL_PAGES = [
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

def fix_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Focus-visible and prefers-reduced-motion
    if 'focus-visible' not in content:
        if '</style>' in content:
            # Insert right before the first closing style tag or last closing style tag
            # Let's insert before '</style>'
            content = content.replace('</style>', A11Y_CSS + '  </style>', 1)
            modified = True
            print(f"[{filepath}] Injected a11y & focus-visible CSS")

    # 2. Add intrinsic dimensions to images missing them
    # Pattern for valixis-horizontal-lockup
    def add_lockup_dims(match):
        tag = match.group(0)
        if 'width=' not in tag and 'height=' not in tag:
            # insert before the closing >
            return tag[:-1] + ' width="836" height="120">'
        return tag

    new_content = re.sub(r'<img\s+[^>]*?valixis-horizontal-lockup[^>]*?>', add_lockup_dims, content)
    if new_content != content:
        content = new_content
        modified = True
        print(f"[{filepath}] Added dimensions to lockup img")

    # Pattern for subhash-annam.jpg
    def add_subhash_dims(match):
        tag = match.group(0)
        if 'width=' not in tag and 'height=' not in tag:
            return tag[:-1] + ' width="600" height="600">'
        return tag

    new_content = re.sub(r'<img\s+[^>]*?subhash-annam\.jpg[^>]*?>', add_subhash_dims, content)
    if new_content != content:
        content = new_content
        modified = True
        print(f"[{filepath}] Added dimensions to subhash-annam img")

    # Pattern for jyothsna-sri.jpg
    def add_jyothsna_dims(match):
        tag = match.group(0)
        if 'width=' not in tag and 'height=' not in tag:
            return tag[:-1] + ' width="600" height="600">'
        return tag

    new_content = re.sub(r'<img\s+[^>]*?jyothsna-sri\.jpg[^>]*?>', add_jyothsna_dims, content)
    if new_content != content:
        content = new_content
        modified = True
        print(f"[{filepath}] Added dimensions to jyothsna-sri img")

    # Pattern for aesthetic_restaurant.jpg
    def add_aesthetic_dims(match):
        tag = match.group(0)
        if 'width=' not in tag and 'height=' not in tag:
            return tag[:-1] + ' width="1200" height="800">'
        return tag

    new_content = re.sub(r'<img\s+[^>]*?aesthetic_restaurant\.jpg[^>]*?>', add_aesthetic_dims, content)
    if new_content != content:
        content = new_content
        modified = True
        print(f"[{filepath}] Added dimensions to aesthetic_restaurant img")

    # Pattern for chic_interior.jpg
    def add_chic_dims(match):
        tag = match.group(0)
        if 'width=' not in tag and 'height=' not in tag:
            return tag[:-1] + ' width="1200" height="800">'
        return tag

    new_content = re.sub(r'<img\s+[^>]*?chic_interior\.jpg[^>]*?>', add_chic_dims, content)
    if new_content != content:
        content = new_content
        modified = True
        print(f"[{filepath}] Added dimensions to chic_interior img")

    # Pattern for unsplash hotel
    def add_unsplash_dims(match):
        tag = match.group(0)
        if 'width=' not in tag and 'height=' not in tag:
            return tag[:-1] + ' width="700" height="467">'
        return tag

    new_content = re.sub(r'<img\s+[^>]*?unsplash\.com/photo-1590490360182-c33d57733427[^>]*?>', add_unsplash_dims, content)
    if new_content != content:
        content = new_content
        modified = True
        print(f"[{filepath}] Added dimensions to unsplash img")

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully wrote updates to {filepath}")

for root_dir in TARGET_DIRS:
    for page in CANONICAL_PAGES:
        fp = os.path.normpath(os.path.join(root_dir, page)) if root_dir != '.' else page
        fix_file(fp)
