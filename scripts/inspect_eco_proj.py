with open('ecosystem/index.html', 'r', encoding='utf-8') as f:
    eco = f.read()

with open('projects/index.html', 'r', encoding='utf-8') as f:
    proj = f.read()

print(f"ecosystem/index.html length: {len(eco)}, lines: {len(eco.splitlines())}")
print(f"projects/index.html length: {len(proj)}, lines: {len(proj.splitlines())}")

import re
print("\n--- Titles & Headings in ecosystem/index.html ---")
for h in re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', eco, re.IGNORECASE)[:15]:
    print("  ", re.sub(r'<[^>]+>', '', h).strip())

print("\n--- Titles & Headings in projects/index.html ---")
for h in re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', proj, re.IGNORECASE)[:15]:
    print("  ", re.sub(r'<[^>]+>', '', h).strip())
