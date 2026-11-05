import re

with open('client-sites/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<p[^>]*class=["\'][^"\']*disclaimer[^"\']*["\'][^>]*>(.*?)</p>', text, re.DOTALL)
print("Disclaimers in client-sites/index.html:")
for m in matches:
    print(" -", re.sub(r'\s+', ' ', m).strip()[:200])

with open('work/index.html', 'r', encoding='utf-8') as f:
    text2 = f.read()

matches2 = re.findall(r'<p[^>]*class=["\'][^"\']*disclaimer[^"\']*["\'][^>]*>(.*?)</p>', text2, re.DOTALL)
print("\nDisclaimers in work/index.html:")
for m in matches2:
    print(" -", re.sub(r'\s+', ' ', m).strip()[:200])
