with open('about/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_str = "VALIXIS was founded in <strong>2026</strong> by systems architect <strong>Subhash Annam</strong> and commercial strategist <strong>Jyothsna Sri</strong>. The venture was established on first principles"
new_str = "VALIXIS was founded in <strong>2026</strong> by systems architect <strong>Subhash Annam</strong> and commercial strategist <strong>Jyothsna Sri</strong> as an independent, currently unregistered technology venture. The venture was established on first principles"

if old_str in text:
    text = text.replace(old_str, new_str)
    with open('about/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    with open('VALIXIS WEBSITE/about/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated about/index.html with explicit 'independent, currently unregistered technology venture' phrasing.")
else:
    print("old_str not found!")
