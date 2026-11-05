with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

for i, line in enumerate(content.splitlines(), 1):
    if 'href="contact/' in line or 'href="../contact/' in line or 'id="contact"' in line or 'href="#contact"' in line:
        print(f"L{i}: {line.strip()[:100]}")
