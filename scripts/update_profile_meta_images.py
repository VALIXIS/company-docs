for path in [
    'leadership/subhash-annam/index.html',
    'VALIXIS WEBSITE/leadership/subhash-annam/index.html',
    'leadership/jyothsna-sri/index.html',
    'VALIXIS WEBSITE/leadership/jyothsna-sri/index.html'
]:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Replace og:image and twitter:image
    text = text.replace('assets/subhash-annam.jpg', 'assets/valixis-logo-full.jpg')
    text = text.replace('assets/jyothsna-sri.jpg', 'assets/valixis-logo-full.jpg')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Updated metadata images in {path}")
