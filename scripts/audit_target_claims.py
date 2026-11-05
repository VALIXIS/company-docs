import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

pages = [
    'index.html',
    'about/index.html',
    'services/index.html',
    'services/ai-automation/index.html',
    'services/software-mobile/index.html',
    'services/web-platforms/index.html',
    'services/3d-gaming-interactive/index.html',
    'work/index.html',
    'work/hiyya-dino-mandi/index.html',
    'work/novel-hotel/index.html',
    'work/rose-cafe/index.html',
    'client-sites/index.html',
    'estimate/index.html',
    'ecosystem/index.html',
    'leadership/index.html',
    'contact/index.html'
]

claim_patterns = [
    (re.compile(r'\b(99\.\d+%|100%|zero downtime|99\.99%)\b', re.IGNORECASE), "High Uptime / Availability"),
    (re.compile(r'\b(\d+\+?\s*(clients|customers|enterprises|brands|projects|deployments|users))\b', re.IGNORECASE), "Client / Project Count"),
    (re.compile(r'\b(\$?\d+[\d,]*\s*(ARR|revenue|processed|turnover|gmv))\b', re.IGNORECASE), "Financial Claim"),
    (re.compile(r'\b(\d+[\d\.,]*\s*(ms|seconds|req\/s|rps|tps))\b', re.IGNORECASE), "Latency / Throughput Claim"),
    (re.compile(r'\b(guaranteed|unbreakable|military-grade|bank-grade)\b', re.IGNORECASE), "Exaggerated Security Claim"),
]

print("=== TARGETED AUDIT: PUBLIC CANONICAL PAGES CLAIMS ===")
findings = []

for page in pages:
    if not os.path.exists(page):
        continue
    with open(page, 'r', encoding='utf-8', errors='ignore') as fp:
        lines = fp.readlines()
    
    in_style = False
    in_script = False
    for i, line in enumerate(lines, 1):
        if '<style' in line: in_style = True
        if '</style>' in line: in_style = False; continue
        if '<script' in line: in_script = True
        if '</script>' in line: in_script = False; continue
        if in_style or in_script: continue
        
        clean = re.sub(r'<[^>]+>', ' ', line).strip()
        if not clean: continue
        
        for pat, cat in claim_patterns:
            m = pat.search(clean)
            if m:
                findings.append((page, i, cat, m.group(0), clean))
                break

print(f"Total claims identified: {len(findings)}\n")
for page, line_num, cat, matched, text in findings:
    print(f"[{cat}] {page}:{line_num}")
    print(f"   Matched: '{matched}'")
    print(f"   Context: {text[:140]}")
    print()
