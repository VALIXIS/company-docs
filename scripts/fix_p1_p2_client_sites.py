import os

JSON_LD_SCHEMA = """  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "CollectionPage",
      "@id": "https://valixis.tech/client-sites/#webpage",
      "url": "https://valixis.tech/client-sites/",
      "name": "VALIXIS Technologies — Client Showcase Directory & Demos",
      "description": "Explore live, interactive client showcase websites engineered by VALIXIS Technologies across hospitality, dining, retail, and commercial sectors.",
      "isPartOf": {
        "@type": "WebSite",
        "@id": "https://valixis.tech/#website",
        "url": "https://valixis.tech",
        "name": "VALIXIS"
      },
      "breadcrumb": {
        "@id": "https://valixis.tech/client-sites/#breadcrumb"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://valixis.tech/client-sites/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://valixis.tech/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Client Demos",
          "item": "https://valixis.tech/client-sites/"
        }
      ]
    }
  ]
}
  </script>
"""

def update_client_sites(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Meta description & Schema
    if '<meta name="description"' not in content:
        head_tag = '<link rel="canonical" href="https://valixis.tech/client-sites/">'
        meta_replacement = """<meta name="description" content="Explore live, interactive client showcase websites engineered by VALIXIS Technologies across hospitality, dining, retail, and commercial sectors.">
  <link rel="canonical" href="https://valixis.tech/client-sites/">
""" + JSON_LD_SCHEMA
        content = content.replace(head_tag, meta_replacement)

    # 2. H1 fix
    old_h2 = '<div class="studio-brand-text">\n        <h2>VALIXIS Technologies</h2>'
    new_h1 = '<div class="studio-brand-text">\n        <h1 style="font-size: 1.15rem; font-weight: 700; color: #FFF; margin: 0; line-height: 1.2;">VALIXIS Technologies</h1>'
    if old_h2 in content:
        content = content.replace(old_h2, new_h1)

    # 3. Iframe sandbox
    old_iframe = '<iframe id="previewIframe" src="hiyya-dino-mandi/index.html"></iframe>'
    new_iframe = '<iframe id="previewIframe" src="hiyya-dino-mandi/index.html" sandbox="allow-scripts allow-same-origin allow-forms allow-popups" title="VALIXIS Client Site Interactive Preview"></iframe>'
    if old_iframe in content:
        content = content.replace(old_iframe, new_iframe)

    # 4. turnoverSlider label
    old_slider = '<input type="range" class="roi-range" id="turnoverSlider"'
    new_slider = '<label for="turnoverSlider" style="position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);border:0;">Monthly Online Takeaway Orders Value</label>\n            <input type="range" class="roi-range" id="turnoverSlider"'
    if old_slider in content and 'for="turnoverSlider"' not in content:
        content = content.replace(old_slider, new_slider)

    # 5. Accessibility CSS (:focus-visible & prefers-reduced-motion)
    if 'prefers-reduced-motion' not in content:
        a11y_css = """
    /* WCAG 2.1 AA Accessibility */
    a:focus-visible, button:focus-visible, input:focus-visible, select:focus-visible {
      outline: 2px solid var(--valixis-accent) !important;
      outline-offset: 2px !important;
    }
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }
  </style>"""
        content = content.replace('</style>', a11y_css, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

for p in ['client-sites/index.html', 'VALIXIS WEBSITE/client-sites/index.html']:
    if os.path.exists(p):
        update_client_sites(p)
