with open('scripts/update_contact_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("File size:", len(text))
occurrences = [i for i in range(len(text)) if text.startswith("<!DOCTYPE html>", i)]
print("Occurrences of <!DOCTYPE html>:", len(occurrences), occurrences)
