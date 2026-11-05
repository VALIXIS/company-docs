with open('ai_agents/static/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Title:", text[:1000])
import re
print("\nSections / Panels:")
for m in re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', text)[:10]:
    print(" ", re.sub(r'<[^>]+>', '', m).strip())
