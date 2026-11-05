with open('sitemap.xml', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines():
    if '<loc>' in line:
        print(line.strip())
