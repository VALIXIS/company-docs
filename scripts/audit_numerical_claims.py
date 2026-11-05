import glob
import re

html_files = sorted(glob.glob('./**/*.html', recursive=True))

patterns = [
    (re.compile(r'(\d+[\d\.,]*%|\d+[\d\.,]*\s*percent)', re.IGNORECASE), "Percentage"),
    (re.compile(r'\b\d+\s*\+\b|\b\d+[kKmMbB]\+?\b'), "Metric Number+"),
    (re.compile(r'\b(uptime|latency|throughput|sla|requests|clients|projects|active users)\b', re.IGNORECASE), "Metric Keyword"),
]

print("=== AUDITING NUMERICAL & CAPABILITY CLAIMS ===")
findings = []

for f in html_files:
    if any(x in f for x in ['.git', 'node_modules', 'scratch']):
        continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        for idx, line in enumerate(fp, 1):
            # Skip code scripts or SVGs or pure CSS
            if '<script' in line or '<style' in line or 'path d=' in line or 'viewBox' in line:
                continue
            line_clean = re.sub(r'<[^>]+>', ' ', line).strip()
            if not line_clean:
                continue
            for pat, ptype in patterns:
                m = pat.search(line_clean)
                if m:
                    findings.append((f, idx, ptype, m.group(0), line_clean[:140]))
                    break

print(f"Total potential claim instances found: {len(findings)}")
for f, idx, ptype, val, text in findings[:45]:
    print(f"{f}:{idx} [{ptype}: {val}] -> {text}")
