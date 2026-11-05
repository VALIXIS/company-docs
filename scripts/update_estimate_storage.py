import os

def update_estimate_integration(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update button 4 link
    content = content.replace(
        '<a href="../contact/" class="btn-act btn-consult">',
        '<a href="../contact/?from=estimate#inquiry-form" id="consultLink" class="btn-act btn-consult">'
    )

    # In calculateScope, store in sessionStorage
    target_str = "document.getElementById('emailLink').href = mailtoUrl;"
    replacement_str = """document.getElementById('emailLink').href = mailtoUrl;

      // Phase 6 Integration: Cache scope brief for seamless Contact Form pre-fill
      try {
        sessionStorage.setItem('valixis_estimated_scope', briefText);
        sessionStorage.setItem('valixis_estimated_type', selectedType);
        sessionStorage.setItem('valixis_estimated_timeline', selectedTimeline);
      } catch (e) {
        console.warn('SessionStorage unavailable:', e);
      }"""

    if target_str in content and "valixis_estimated_scope" not in content:
        content = content.replace(target_str, replacement_str)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

for p in ['estimate/index.html', 'VALIXIS WEBSITE/estimate/index.html']:
    if os.path.exists(p):
        update_estimate_integration(p)
