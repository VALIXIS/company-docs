import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 80)
print("AUDIT SCRIPT 6: ACCESSIBILITY & WCAG 2.1 AA AUDIT")
print("=" * 80)

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

h1_issues = 0
form_label_issues = 0
reduced_motion_count = 0
focus_visible_count = 0

for cp in canonical_pages:
    with open(cp, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Heading check
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
    if len(h1s) != 1:
        print(f"  [H1 ISSUE] {cp}: has {len(h1s)} <h1> elements")
        h1_issues += 1

    # 2. Form input label check
    inputs = re.findall(r'<input\s+[^>]*>', html, re.IGNORECASE)
    for inp in inputs:
        # Ignore honeypot
        if 'hp_security' in inp or 'hp_trap' in inp or 'display:none' in inp:
            continue
        id_m = re.search(r'id=[\"\']([^\"\']+)[\"\']', inp)
        has_aria = 'aria-label' in inp or 'aria-labelledby' in inp
        if id_m:
            inp_id = id_m.group(1)
            has_label = f'for="{inp_id}"' in html or f"for='{inp_id}'" in html
            if not has_label and not has_aria:
                print(f"  [INPUT LABEL ISSUE] in {cp}: input id='{inp_id}' has no matching label or aria-label")
                form_label_issues += 1

    # 3. Reduced motion
    if 'prefers-reduced-motion' in html:
        reduced_motion_count += 1

    # 4. Focus visible
    if ':focus-visible' in html or ':focus' in html:
        focus_visible_count += 1

print(f"H1 count issues: {h1_issues}")
print(f"Form input label issues: {form_label_issues}")
print(f"Pages supporting prefers-reduced-motion: {reduced_motion_count} / {len(canonical_pages)}")
print(f"Pages with explicit focus styles: {focus_visible_count} / {len(canonical_pages)}")
