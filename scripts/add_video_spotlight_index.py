import os

target_desc = """        <p class="section-desc">

          From central company operating systems to distributed intelligence and consumer health platforms.

        </p>"""

replacement_desc = """        <p class="section-desc">

          From central company operating systems to distributed intelligence and consumer health platforms.

        </p>

        <div style="margin-top: 20px; display: flex; gap: 14px; align-items: center; flex-wrap: wrap;">

          <a href="ecosystem/#video-demo" class="btn-primary-gradient" style="padding: 10px 22px; font-size: 0.88rem; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; border-radius: 8px; font-weight: 700; color: #FFF; font-family: var(--font-display); box-shadow: 0 0 20px rgba(0, 217, 255, 0.35);">

            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>

            <span>Watch 90s Technical Walkthrough Video &rarr;</span>

          </a>

          <a href="ecosystem/" style="color: var(--valixis-cyan); font-family: var(--font-mono); font-size: 0.85rem; text-decoration: underline; font-weight: 600;">

            Inspect Complete 7-Product Showcase &rarr;

          </a>

        </div>"""

for p in ['index.html', 'VALIXIS WEBSITE/index.html']:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'ecosystem/#video-demo' not in content and target_desc in content:
            content = content.replace(target_desc, replacement_desc)
            with open(p, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {p} with video demo spotlight")
        else:
            print(f"Already updated or target not found in {p}")
