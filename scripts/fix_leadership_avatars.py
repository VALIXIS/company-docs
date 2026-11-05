import re

for path in ['leadership/index.html', 'VALIXIS WEBSITE/leadership/index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Replace Subhash avatar
    text = re.sub(
        r'<div class="avatar-wrapper">\s*<img src="\.\./assets/subhash-annam\.jpg"[^>]*>\s*</div>',
        '<div class="avatar-wrapper"><div class="avatar-initials" aria-label="Subhash Annam Initials">SA</div></div>',
        text
    )
    # Replace Jyothsna avatar
    text = re.sub(
        r'<div class="avatar-wrapper jyothsna">\s*<img src="\.\./assets/jyothsna-sri\.jpg"[^>]*>\s*</div>',
        '<div class="avatar-wrapper jyothsna"><div class="avatar-initials jyothsna" aria-label="Jyothsna Sri Initials">JS</div></div>',
        text
    )
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Regex replaced avatars in {path}")
