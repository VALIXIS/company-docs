with open('current_showcase_index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("current_showcase_index.html lines:", len(text.splitlines()))
for l in text.splitlines()[:25]:
    print(l)
