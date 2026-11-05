import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 80)
print("AUDIT SCRIPT 3: SECURITY, CREDENTIALS & IFRAME SCANNER")
print("=" * 80)

# Secret patterns
secret_patterns = [
    (r're_[a-zA-Z0-9_\-]{20,}', "Resend Live API Key"),
    (r'sk_live_[a-zA-Z0-9]{20,}', "Stripe Live Secret Key"),
    (r'sk_test_[a-zA-Z0-9]{20,}', "Stripe Test Secret Key"),
    (r'ghp_[a-zA-Z0-9]{30,}', "GitHub Personal Access Token"),
    (r'gho_[a-zA-Z0-9]{30,}', "GitHub OAuth Token"),
    (r'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\.[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-]+', "JWT Token / Supabase Key"),
    (r'AIza[0-9A-Za-z-_]{35}', "Google API Key"),
    (r'sq0csp-[0-9A-Za-z\-_]{43}', "Square Secret Key"),
    (r'access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}', "Braintree Access Token"),
]

tracked_dirs = ['.', 'VALIXIS WEBSITE']
findings = []

for base in tracked_dirs:
    for root, dirs, files in os.walk(base):
        if any(k in root for k in ['.git', 'node_modules', 'brain', '__pycache__', 'scripts']):
            continue
        for f in files:
            path = os.path.normpath(os.path.join(root, f))
            if f.endswith(('.html', '.js', '.ts', '.sql', '.json', '.md', '.py')):
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as fl:
                        content = fl.read()
                    for pattern, label in secret_patterns:
                        matches = re.findall(pattern, content)
                        for m in matches:
                            # Redact match
                            redacted = m[:6] + "..." + m[-4:] if len(m) > 10 else "***"
                            findings.append((path, label, redacted))
                except Exception as e:
                    pass

print(f"Total potential secret pattern matches: {len(findings)}")
for p, lbl, red in findings:
    print(f"  [FLAG] {p}: {lbl} ({red})")

print("\n=== Iframe Security Sandbox Audit ===")
for root, dirs, files in os.walk('.'):
    if any(k in root for k in ['.git', 'node_modules', 'brain']):
        continue
    for f in files:
        if f.endswith('.html'):
            path = os.path.normpath(os.path.join(root, f))
            with open(path, 'r', encoding='utf-8', errors='ignore') as fl:
                c = fl.read()
            if '<iframe' in c.lower():
                iframe_tags = re.findall(r'<iframe\s+[^>]*>', c, re.IGNORECASE)
                for tag in iframe_tags:
                    has_sandbox = 'sandbox' in tag.lower()
                    print(f"  In {path}: sandbox={has_sandbox} | tag={tag[:85]}...")
