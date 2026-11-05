import os

def clean_encoding_and_link(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace potential artifact chars with clean entities/ASCII
    text = text.replace('', '—')
    
    # Save back with explicit UTF-8
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Cleaned {file_path}")

for path in [
    'contact/index.html',
    'VALIXIS WEBSITE/contact/index.html',
    'estimate/index.html',
    'VALIXIS WEBSITE/estimate/index.html'
]:
    if os.path.exists(path):
        clean_encoding_and_link(path)
