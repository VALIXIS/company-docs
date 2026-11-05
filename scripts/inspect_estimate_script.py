with open('estimate/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
match = re.search(r'function calculateResult\(\) \{(.*?)\}', content, re.DOTALL)
if match:
    print("Found calculateResult():")
    print(match.group(1)[:400])
else:
    print("calculateResult() not found directly, checking script tags...")
    scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
    for s in scripts:
        if 'calculateResult' in s:
            print("Found script containing calculateResult:")
            for line in s.splitlines()[:30]:
                print(line)
