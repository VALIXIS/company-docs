import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("=== Three.js & Animation Loop Analysis in index.html ===")

three_script = re.search(r'(// Three\.js.*?</script>)', text, re.DOTALL | re.IGNORECASE)
if not three_script:
    three_script = re.search(r'(<script[^>]*>.*?three\.min\.js.*?</script>)', text, re.DOTALL | re.IGNORECASE)

# Let's search for requestAnimationFrame in index.html
rafs = [m.start() for m in re.finditer(r'requestAnimationFrame', text)]
print(f"Occurrences of requestAnimationFrame: {len(rafs)}")

for idx in rafs:
    snippet = text[max(0, idx - 150): min(len(text), idx + 250)]
    print("\n--- RAF Snippet ---")
    print(snippet)

# Check for visibilitychange or IntersectionObserver
print("\n--- Visibility & Intersection Optimization ---")
print("visibilitychange in index.html:", "visibilitychange" in text)
print("IntersectionObserver in index.html:", "IntersectionObserver" in text)
print("prefers-reduced-motion in index.html:", "prefers-reduced-motion" in text)
