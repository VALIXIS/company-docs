import os
import re
import json

base_dirs = [
    r"c:\Users\nagas\Documents\antigravity\resilient-heisenberg\VALIXIS WEBSITE",
    r"c:\Users\nagas\Documents\antigravity\resilient-heisenberg"
]

def replace_json_ld(html, new_json_data):
    pattern = r'<script\s+type=["\']application/ld\+json["\']\s*>[\s\S]*?</script>'
    replacement = f'<script type="application/ld+json">\n{json.dumps(new_json_data, indent=2, ensure_ascii=False)}\n  </script>'
    return re.sub(pattern, lambda m: replacement, html, count=1)

print("Applying Phase 2 Technical Foundation & SEO Upgrades...")

for base in base_dirs:
    print(f"\n==========================================")
    print(f"PROCESSING DIRECTORY: {base}")
    print(f"==========================================")
    
    # ----------------------------------------------------
    # 1. robots.txt
    # ----------------------------------------------------
    rob_path = os.path.join(base, "robots.txt")
    rob_content = """# robots.txt for https://valixis.tech
# Independent Technology Venture - Founded 2026

User-agent: *
Allow: /

# Canonical XML Sitemap
Sitemap: https://valixis.tech/sitemap.xml
"""
    with open(rob_path, "w", encoding="utf-8") as f:
        f.write(rob_content)
    print("  [OK] Updated robots.txt (clean ASCII comments)")

    # ----------------------------------------------------
    # 2. sitemap.xml
    # ----------------------------------------------------
    sm_path = os.path.join(base, "sitemap.xml")
    sm_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">

  <!-- Homepage / Core Digital Identity -->
  <url>
    <loc>https://valixis.tech/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>

  <!-- About / Venture Profile -->
  <url>
    <loc>https://valixis.tech/about/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- Executive Leadership Overview -->
  <url>
    <loc>https://valixis.tech/leadership/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- Founder & CEO Profile: Subhash Annam -->
  <url>
    <loc>https://valixis.tech/leadership/subhash-annam/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- Co-Founder & CCO Profile: Jyothsna Sri -->
  <url>
    <loc>https://valixis.tech/leadership/jyothsna-sri/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- Client Showcases Portal -->
  <url>
    <loc>https://valixis.tech/client-sites/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- Software Ecosystem -->
  <url>
    <loc>https://valixis.tech/ecosystem/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>

  <!-- Projects & Lifecycle Tracker -->
  <url>
    <loc>https://valixis.tech/projects/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>

  <!-- Contact & Global Inquiries -->
  <url>
    <loc>https://valixis.tech/contact/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>

</urlset>
"""
    with open(sm_path, "w", encoding="utf-8") as f:
        f.write(sm_content)
    print("  [OK] Updated sitemap.xml with 9 canonical URLs (including /client-sites/) and 2026-11-03 lastmod")

    # ----------------------------------------------------
    # 3. Homepage (index.html)
    # ----------------------------------------------------
    hp_path = os.path.join(base, "index.html")
    if os.path.exists(hp_path):
        with open(hp_path, "r", encoding="utf-8") as f:
            hp = f.read()

        # Update clean title
        hp = re.sub(
            r'<title>.*?</title>',
            '<title>VALIXIS &mdash; Building Intelligent Solutions for a Better Tomorrow | AI &amp; Next-Gen Gaming</title>',
            hp
        )

        # Update meta description to crisp snippet length
        hp = re.sub(
            r'<meta\s+name=["\']description["\']\s+content=["\'][^"\']+["\']',
            '<meta name="description" content="VALIXIS is an independent technology venture founded in 2026 by Subhash Annam and Jyothsna Sri, pioneering Artificial Intelligence, Software Engineering &amp; Next-Gen Gaming."',
            hp
        )

        # Update Open Graph tags for high-res logo dimensions
        if '<meta property="og:image:width"' not in hp:
            hp = hp.replace(
                '<meta property="og:image" content="https://valixis.tech/assets/valixis-logo-full.jpg">',
                '<meta property="og:image" content="https://valixis.tech/assets/valixis-logo-full.jpg">\n  <meta property="og:image:width" content="1024">\n  <meta property="og:image:height" content="1024">\n  <meta property="og:image:alt" content="VALIXIS Official Emblem">'
            )
        if '<meta property="og:locale"' not in hp:
            hp = hp.replace(
                '<meta property="og:site_name" content="VALIXIS">',
                '<meta property="og:site_name" content="VALIXIS">\n  <meta property="og:locale" content="en_US">'
            )

        # Update Desktop Navigation to include Showcase
        if 'href="client-sites/"' not in hp:
            hp = re.sub(
                r'(<nav class="nav-links">[\s\S]*?<a href="projects/">Projects</a>)',
                r'\1\n      <a href="client-sites/">Showcase</a>',
                hp
            )

        # Update Mobile Drawer to include Showcase
        if 'href="client-sites/"' not in hp or 'class="mobile-drawer-link">Showcase</a>' not in hp:
            hp = re.sub(
                r'(<div class="mobile-drawer-links">[\s\S]*?<a href="projects/" class="mobile-drawer-link">Projects</a>)',
                r'\1\n        <a href="client-sites/" class="mobile-drawer-link">Showcase</a>',
                hp
            )

        # Update Footer subpage navigation to include Showcase
        if '<a href="client-sites/">Showcase</a>' not in hp:
            hp = re.sub(
                r'(<div class="footer-subpages-nav"[\s\S]*?<a href="projects/">Projects</a>)',
                r'\1 <span class="sep">&middot;</span> <a href="client-sites/">Showcase</a>',
                hp
            )

        # Update JSON-LD schema with complete Organization properties
        org_schema_replacement = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "Organization",
                    "@id": "https://valixis.tech/#organization",
                    "name": "VALIXIS",
                    "alternateName": [
                        "VALIXIS Technologies"
                    ],
                    "url": "https://valixis.tech",
                    "logo": {
                        "@type": "ImageObject",
                        "url": "https://valixis.tech/assets/valixis-logo-full.jpg",
                        "width": 1024,
                        "height": 1024,
                        "caption": "VALIXIS Official Brand Emblem"
                    },
                    "image": "https://valixis.tech/assets/valixis-logo-full.jpg",
                    "description": "VALIXIS is an independent technology venture founded in 2026 by Subhash Annam and Jyothsna Sri, pioneering at the convergence of Artificial Intelligence, Software Engineering, Application Development, Digital Products, and Next-Gen Gaming.",
                    "foundingDate": "2026",
                    "legalName": "VALIXIS (Independent Technology Venture)",
                    "founder": [
                        {
                            "@type": "Person",
                            "@id": "https://valixis.tech/leadership/subhash-annam/#person",
                            "name": "Subhash Annam",
                            "jobTitle": "Founder & Chief Executive Officer (CEO)",
                            "url": "https://valixis.tech/leadership/subhash-annam/",
                            "image": "https://valixis.tech/assets/subhash-annam.jpg"
                        },
                        {
                            "@type": "Person",
                            "@id": "https://valixis.tech/leadership/jyothsna-sri/#person",
                            "name": "Jyothsna Sri",
                            "jobTitle": "Co-Founder & Chief Commercial Officer (CCO)",
                            "url": "https://valixis.tech/leadership/jyothsna-sri/",
                            "image": "https://valixis.tech/assets/jyothsna-sri.jpg"
                        }
                    ],
                    "knowsAbout": [
                        "Artificial Intelligence",
                        "Software Engineering",
                        "Application Development",
                        "Web Development",
                        "Digital Products",
                        "Gaming and Interactive Experiences",
                        "Distributed Systems",
                        "Cloud Architecture"
                    ],
                    "contactPoint": {
                        "@type": "ContactPoint",
                        "email": "official.valixis@gmail.com",
                        "telephone": "+91-9603416707",
                        "contactType": "General & Commercial Inquiries",
                        "availableLanguage": [
                            "English",
                            "Telugu",
                            "Hindi"
                        ]
                    }
                },
                {
                    "@type": "WebSite",
                    "@id": "https://valixis.tech/#website",
                    "url": "https://valixis.tech",
                    "name": "VALIXIS",
                    "description": "Building Intelligent Solutions for a Better Tomorrow",
                    "publisher": {
                        "@id": "https://valixis.tech/#organization"
                    }
                },
                {
                    "@type": "FAQPage",
                    "@id": "https://valixis.tech/#faq",
                    "mainEntity": [
                        {
                            "@type": "Question",
                            "name": "What is VALIXIS?",
                            "acceptedAnswer": {
                                "@type": "Answer",
                                "text": "VALIXIS is an independent technology venture founded in 2026, pioneering at the convergence of Artificial Intelligence, Software Engineering, Application Development, Digital Products, and Next-Gen Gaming."
                            }
                        },
                        {
                            "@type": "Question",
                            "name": "When was VALIXIS founded?",
                            "acceptedAnswer": {
                                "@type": "Answer",
                                "text": "VALIXIS was founded in 2026."
                            }
                        },
                        {
                            "@type": "Question",
                            "name": "Who founded VALIXIS?",
                            "acceptedAnswer": {
                                "@type": "Answer",
                                "text": "VALIXIS was founded by Subhash Annam, who serves as Founder & Chief Executive Officer (CEO)."
                            }
                        },
                        {
                            "@type": "Question",
                            "name": "Who is the co-founder of VALIXIS?",
                            "acceptedAnswer": {
                                "@type": "Answer",
                                "text": "The co-founder of VALIXIS is Jyothsna Sri, who serves as Co-Founder & Chief Commercial Officer (CCO)."
                            }
                        },
                        {
                            "@type": "Question",
                            "name": "What does VALIXIS develop?",
                            "acceptedAnswer": {
                                "@type": "Answer",
                                "text": "VALIXIS develops intelligent software systems, autonomous AI agent pipelines, cross-platform applications, cloud infrastructure, and interactive 3D gaming experiences."
                            }
                        },
                        {
                            "@type": "Question",
                            "name": "What is the VALIXIS software ecosystem?",
                            "acceptedAnswer": {
                                "@type": "Answer",
                                "text": "The VALIXIS software ecosystem comprises proprietary platforms including VALIXIS Portal (flagship operations backbone), VALIXIS Flow (workflow automation engine), VALIXIS Cloud (sovereign distributed storage), VALIXIS Desk-AI (desktop cognitive workspace), VALIXIS Pulse (mesh observability), Fitora (consumer AI physical conditioning), and VALIXIS Gaming Studio."
                            }
                        },
                        {
                            "@type": "Question",
                            "name": "What is the official website of VALIXIS?",
                            "acceptedAnswer": {
                                "@type": "Answer",
                                "text": "The official website of VALIXIS is https://valixis.tech."
                            }
                        }
                    ]
                }
            ]
        }

        hp = replace_json_ld(hp, org_schema_replacement)

        with open(hp_path, "w", encoding="utf-8") as f:
            f.write(hp)
        print("  [OK] Updated index.html (Metadata, OpenGraph, Navigation with Showcase, Organization JSON-LD)")

    # ----------------------------------------------------
    # 4. About Page (about/index.html)
    # ----------------------------------------------------
    ab_path = os.path.join(base, "about", "index.html")
    if os.path.exists(ab_path):
        with open(ab_path, "r", encoding="utf-8") as f:
            ab = f.read()

        ab_schema = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "AboutPage",
                    "@id": "https://valixis.tech/about/#webpage",
                    "url": "https://valixis.tech/about/",
                    "name": "About VALIXIS — Independent Technology Venture Founded in 2026",
                    "description": "Discover VALIXIS, an independent technology venture founded in 2026 by Subhash Annam and Jyothsna Sri, engineering at the forefront of AI, software architecture, and interactive computing.",
                    "isPartOf": {
                        "@type": "WebSite",
                        "@id": "https://valixis.tech/#website",
                        "url": "https://valixis.tech",
                        "name": "VALIXIS"
                    },
                    "mainEntity": {
                        "@type": "Organization",
                        "@id": "https://valixis.tech/#organization",
                        "name": "VALIXIS",
                        "url": "https://valixis.tech",
                        "logo": "https://valixis.tech/assets/valixis-logo-full.jpg"
                    },
                    "breadcrumb": {
                        "@id": "https://valixis.tech/about/#breadcrumb"
                    }
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": "https://valixis.tech/about/#breadcrumb",
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
                            "name": "About",
                            "item": "https://valixis.tech/about/"
                        }
                    ]
                }
            ]
        }

        ab = replace_json_ld(ab, ab_schema)

        # Include Showcase in navigation
        if 'href="../client-sites/"' not in ab:
            ab = re.sub(
                r'(<nav class="nav-links">[\s\S]*?<a href="\.\./projects/">Projects</a>)',
                r'\1\n      <a href="../client-sites/">Showcase</a>',
                ab
            )
            ab = re.sub(
                r'(<div class="footer-links">[\s\S]*?<a href="\.\./projects/">Projects</a>)',
                r'\1 <span class="sep">&middot;</span> <a href="../client-sites/">Showcase</a>',
                ab
            )

        with open(ab_path, "w", encoding="utf-8") as f:
            f.write(ab)
        print("  [OK] Updated about/index.html (Schema mainEntity, Navigation with Showcase)")

    # ----------------------------------------------------
    # 5. Leadership Hub (leadership/index.html)
    # ----------------------------------------------------
    lead_path = os.path.join(base, "leadership", "index.html")
    if os.path.exists(lead_path):
        with open(lead_path, "r", encoding="utf-8") as f:
            lead = f.read()

        lead_schema = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "CollectionPage",
                    "@id": "https://valixis.tech/leadership/#webpage",
                    "url": "https://valixis.tech/leadership/",
                    "name": "Executive Leadership — Subhash Annam (CEO) & Jyothsna Sri (CCO) | VALIXIS",
                    "description": "Meet the founders of VALIXIS, an independent technology venture founded in 2026: Subhash Annam (Founder & CEO) and Jyothsna Sri (Co-Founder & CCO).",
                    "isPartOf": {
                        "@type": "WebSite",
                        "@id": "https://valixis.tech/#website",
                        "url": "https://valixis.tech",
                        "name": "VALIXIS"
                    },
                    "publisher": {
                        "@type": "Organization",
                        "@id": "https://valixis.tech/#organization",
                        "name": "VALIXIS"
                    },
                    "breadcrumb": {
                        "@id": "https://valixis.tech/leadership/#breadcrumb"
                    },
                    "mainEntity": [
                        {
                            "@id": "https://valixis.tech/leadership/subhash-annam/#person"
                        },
                        {
                            "@id": "https://valixis.tech/leadership/jyothsna-sri/#person"
                        }
                    ]
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": "https://valixis.tech/leadership/#breadcrumb",
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
                            "name": "Leadership",
                            "item": "https://valixis.tech/leadership/"
                        }
                    ]
                },
                {
                    "@type": "Person",
                    "@id": "https://valixis.tech/leadership/subhash-annam/#person",
                    "name": "Subhash Annam",
                    "jobTitle": "Founder & Chief Executive Officer (CEO)",
                    "worksFor": {
                        "@type": "Organization",
                        "@id": "https://valixis.tech/#organization",
                        "name": "VALIXIS"
                    },
                    "url": "https://valixis.tech/leadership/subhash-annam/",
                    "image": "https://valixis.tech/assets/subhash-annam.jpg"
                },
                {
                    "@type": "Person",
                    "@id": "https://valixis.tech/leadership/jyothsna-sri/#person",
                    "name": "Jyothsna Sri",
                    "jobTitle": "Co-Founder & Chief Commercial Officer (CCO)",
                    "worksFor": {
                        "@type": "Organization",
                        "@id": "https://valixis.tech/#organization",
                        "name": "VALIXIS"
                    },
                    "url": "https://valixis.tech/leadership/jyothsna-sri/",
                    "image": "https://valixis.tech/assets/jyothsna-sri.jpg"
                }
            ]
        }

        lead = replace_json_ld(lead, lead_schema)

        if 'href="../client-sites/"' not in lead:
            lead = re.sub(
                r'(<nav class="nav-links">[\s\S]*?<a href="\.\./projects/">Projects</a>)',
                r'\1\n      <a href="../client-sites/">Showcase</a>',
                lead
            )
            lead = re.sub(
                r'(<div class="footer-links">[\s\S]*?<a href="\.\./projects/">Projects</a>)',
                r'\1 <span class="sep">&middot;</span> <a href="../client-sites/">Showcase</a>',
                lead
            )

        with open(lead_path, "w", encoding="utf-8") as f:
            f.write(lead)
        print("  [OK] Updated leadership/index.html (CollectionPage schema & links)")

    # ----------------------------------------------------
    # 6. Founder Profiles (Subhash Annam & Jyothsna Sri)
    # ----------------------------------------------------
    for p_name, p_slug, p_role in [
        ("Subhash Annam", "subhash-annam", "Founder & Chief Executive Officer (CEO)"),
        ("Jyothsna Sri", "jyothsna-sri", "Co-Founder & Chief Commercial Officer (CCO)")
    ]:
        p_path = os.path.join(base, "leadership", p_slug, "index.html")
        if os.path.exists(p_path):
            with open(p_path, "r", encoding="utf-8") as f:
                prof = f.read()

            prof_schema = {
                "@context": "https://schema.org",
                "@graph": [
                    {
                        "@type": "Person",
                        "@id": f"https://valixis.tech/leadership/{p_slug}/#person",
                        "name": p_name,
                        "jobTitle": p_role,
                        "worksFor": {
                            "@type": "Organization",
                            "@id": "https://valixis.tech/#organization",
                            "name": "VALIXIS",
                            "url": "https://valixis.tech",
                            "logo": "https://valixis.tech/assets/valixis-logo-full.jpg"
                        },
                        "url": f"https://valixis.tech/leadership/{p_slug}/",
                        "image": f"https://valixis.tech/assets/{p_slug}.jpg",
                        "description": f"Official executive profile for {p_name}, {p_role} of VALIXIS, an independent technology venture founded in 2026.",
                        "sameAs": []
                    },
                    {
                        "@type": "ProfilePage",
                        "@id": f"https://valixis.tech/leadership/{p_slug}/#webpage",
                        "url": f"https://valixis.tech/leadership/{p_slug}/",
                        "name": f"{p_name} — {p_role} | VALIXIS",
                        "isPartOf": {
                            "@type": "WebSite",
                            "@id": "https://valixis.tech/#website",
                            "url": "https://valixis.tech",
                            "name": "VALIXIS"
                        },
                        "mainEntity": {
                            "@id": f"https://valixis.tech/leadership/{p_slug}/#person"
                        },
                        "breadcrumb": {
                            "@id": f"https://valixis.tech/leadership/{p_slug}/#breadcrumb"
                        }
                    },
                    {
                        "@type": "BreadcrumbList",
                        "@id": f"https://valixis.tech/leadership/{p_slug}/#breadcrumb",
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
                                "name": "Leadership",
                                "item": "https://valixis.tech/leadership/"
                            },
                            {
                                "@type": "ListItem",
                                "position": 3,
                                "name": p_name,
                                "item": f"https://valixis.tech/leadership/{p_slug}/"
                            }
                        ]
                    }
                ]
            }

            prof = replace_json_ld(prof, prof_schema)

            if 'href="../../client-sites/"' not in prof:
                prof = re.sub(
                    r'(<nav class="nav-links">[\s\S]*?<a href="\.\./\.\./projects/">Projects</a>)',
                    r'\1\n      <a href="../../client-sites/">Showcase</a>',
                    prof
                )
                prof = re.sub(
                    r'(<div class="footer-links">[\s\S]*?<a href="\.\./\.\./projects/">Projects</a>)',
                    r'\1 <span class="sep">&middot;</span> <a href="../../client-sites/">Showcase</a>',
                    prof
                )

            with open(p_path, "w", encoding="utf-8") as f:
                f.write(prof)
            print(f"  [OK] Updated leadership/{p_slug}/index.html (Person + ProfilePage schema & navigation)")

    # ----------------------------------------------------
    # 7. Projects Page (projects/index.html)
    # ----------------------------------------------------
    proj_path = os.path.join(base, "projects", "index.html")
    if os.path.exists(proj_path):
        with open(proj_path, "r", encoding="utf-8") as f:
            proj = f.read()

        proj_schema = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebPage",
                    "@id": "https://valixis.tech/projects/#webpage",
                    "url": "https://valixis.tech/projects/",
                    "name": "Projects & Development Pipeline — Lifecycle Tracker | VALIXIS",
                    "description": "Transparent development status of all VALIXIS projects. Clearly categorizing launched platforms, active pipelines, and exploratory research.",
                    "isPartOf": {
                        "@type": "WebSite",
                        "@id": "https://valixis.tech/#website",
                        "url": "https://valixis.tech",
                        "name": "VALIXIS"
                    },
                    "publisher": {
                        "@type": "Organization",
                        "@id": "https://valixis.tech/#organization",
                        "name": "VALIXIS",
                        "url": "https://valixis.tech",
                        "logo": "https://valixis.tech/assets/valixis-logo-full.jpg"
                    },
                    "breadcrumb": {
                        "@id": "https://valixis.tech/projects/#breadcrumb"
                    }
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": "https://valixis.tech/projects/#breadcrumb",
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
                            "name": "Projects",
                            "item": "https://valixis.tech/projects/"
                        }
                    ]
                }
            ]
        }

        proj = replace_json_ld(proj, proj_schema)

        # Add direct link to client-sites under Bespoke Client Portfolios card
        if 'href="../client-sites/"' not in proj:
            proj = re.sub(
                r'(<h3 class="p-title">Bespoke Client Portfolios &amp; Showcases</h3>[\s\S]*?</div>\s*</div>)',
                r'\1\n          <div style="margin-top:14px;"><a href="../client-sites/" style="display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:600; color:#00D9FF; text-decoration:none; border:1px solid rgba(0,217,255,0.35); padding:6px 14px; border-radius:6px; background:rgba(0,217,255,0.06); transition:all 0.2s ease;"><span>Explore Live Client Showcases</span> &rarr;</a></div>',
                proj
            )

        if '<a href="../client-sites/">Showcase</a>' not in proj:
            proj = re.sub(
                r'(<nav class="nav-links">[\s\S]*?<a href="\.\./projects/" class="active">Projects</a>)',
                r'\1\n      <a href="../client-sites/">Showcase</a>',
                proj
            )
            proj = re.sub(
                r'(<div class="footer-links">[\s\S]*?<a href="\.\./projects/">Projects</a>)',
                r'\1 <span class="sep">&middot;</span> <a href="../client-sites/">Showcase</a>',
                proj
            )

        with open(proj_path, "w", encoding="utf-8") as f:
            f.write(proj)
        print("  [OK] Updated projects/index.html (Linked Client Showcase card & navigation)")

    # ----------------------------------------------------
    # 8. Ecosystem Page (ecosystem/index.html)
    # ----------------------------------------------------
    eco_path = os.path.join(base, "ecosystem", "index.html")
    if os.path.exists(eco_path):
        with open(eco_path, "r", encoding="utf-8") as f:
            eco = f.read()

        eco_schema = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "CollectionPage",
                    "@id": "https://valixis.tech/ecosystem/#webpage",
                    "url": "https://valixis.tech/ecosystem/",
                    "name": "The VALIXIS Software Ecosystem — Proprietary Technology & Platforms",
                    "description": "Explore the proprietary technology ecosystem engineered by VALIXIS: VALIXIS Portal, VALIXIS Flow, VALIXIS Cloud, VALIXIS Desk-AI, VALIXIS Pulse, Fitora, and VALIXIS Gaming Studio.",
                    "isPartOf": {
                        "@type": "WebSite",
                        "@id": "https://valixis.tech/#website",
                        "url": "https://valixis.tech",
                        "name": "VALIXIS"
                    },
                    "publisher": {
                        "@type": "Organization",
                        "@id": "https://valixis.tech/#organization",
                        "name": "VALIXIS",
                        "url": "https://valixis.tech",
                        "logo": "https://valixis.tech/assets/valixis-logo-full.jpg"
                    },
                    "breadcrumb": {
                        "@id": "https://valixis.tech/ecosystem/#breadcrumb"
                    }
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": "https://valixis.tech/ecosystem/#breadcrumb",
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
                            "name": "Ecosystem",
                            "item": "https://valixis.tech/ecosystem/"
                        }
                    ]
                }
            ]
        }

        eco = replace_json_ld(eco, eco_schema)

        if 'href="../client-sites/"' not in eco:
            eco = re.sub(
                r'(<nav class="nav-links">[\s\S]*?<a href="\.\./projects/">Projects</a>)',
                r'\1\n      <a href="../client-sites/">Showcase</a>',
                eco
            )
            eco = re.sub(
                r'(<div class="footer-links">[\s\S]*?<a href="\.\./projects/">Projects</a>)',
                r'\1 <span class="sep">&middot;</span> <a href="../client-sites/">Showcase</a>',
                eco
            )

        with open(eco_path, "w", encoding="utf-8") as f:
            f.write(eco)
        print("  [OK] Updated ecosystem/index.html (Schema & navigation)")

    # ----------------------------------------------------
    # 9. Contact Page (contact/index.html)
    # ----------------------------------------------------
    con_path = os.path.join(base, "contact", "index.html")
    if os.path.exists(con_path):
        with open(con_path, "r", encoding="utf-8") as f:
            con = f.read()

        con_schema = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "ContactPage",
                    "@id": "https://valixis.tech/contact/#webpage",
                    "url": "https://valixis.tech/contact/",
                    "name": "Contact & Global Communications — Inquiries | VALIXIS",
                    "description": "Official communications and inquiries portal for VALIXIS. Connect with the executive team for technology partnerships, enterprise systems, and inquiries.",
                    "isPartOf": {
                        "@type": "WebSite",
                        "@id": "https://valixis.tech/#website",
                        "url": "https://valixis.tech",
                        "name": "VALIXIS"
                    },
                    "mainEntity": {
                        "@type": "Organization",
                        "@id": "https://valixis.tech/#organization",
                        "name": "VALIXIS",
                        "url": "https://valixis.tech",
                        "contactPoint": {
                            "@type": "ContactPoint",
                            "email": "official.valixis@gmail.com",
                            "telephone": "+91-9603416707",
                            "contactType": "General & Commercial Inquiries"
                        }
                    },
                    "breadcrumb": {
                        "@id": "https://valixis.tech/contact/#breadcrumb"
                    }
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": "https://valixis.tech/contact/#breadcrumb",
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
                            "name": "Contact",
                            "item": "https://valixis.tech/contact/"
                        }
                    ]
                }
            ]
        }

        con = replace_json_ld(con, con_schema)

        if 'href="../client-sites/"' not in con:
            con = re.sub(
                r'(<nav class="nav-links">[\s\S]*?<a href="\.\./projects/">Projects</a>)',
                r'\1\n      <a href="../client-sites/">Showcase</a>',
                con
            )
            con = re.sub(
                r'(<div class="footer-links">[\s\S]*?<a href="\.\./projects/">Projects</a>)',
                r'\1 <span class="sep">&middot;</span> <a href="../client-sites/">Showcase</a>',
                con
            )

        with open(con_path, "w", encoding="utf-8") as f:
            f.write(con)
        print("  [OK] Updated contact/index.html (Schema & navigation)")

    # ----------------------------------------------------
    # 10. Client Sites Index (client-sites/index.html)
    # ----------------------------------------------------
    cs_idx = os.path.join(base, "client-sites", "index.html")
    if os.path.exists(cs_idx):
        with open(cs_idx, "r", encoding="utf-8") as f:
            cs = f.read()

        # Add back navigation link to VALIXIS homepage in showcase header
        if 'https://valixis.tech' not in cs and 'href="../"' not in cs:
            cs = re.sub(
                r'(<div class="brand-monogram">V</div>)',
                r'<a href="../" style="text-decoration:none;" title="Return to VALIXIS Homepage">\1</a>',
                cs
            )
            cs = re.sub(
                r'(<div class="brand-text">)',
                r'<a href="../" style="text-decoration:none; color:inherit;" title="Return to VALIXIS Homepage"><div class="brand-text">',
                cs
            )
            cs = cs.replace('High-Converting Digital Experiences</div>', 'High-Converting Digital Experiences</div></a>', 1)

        # Add canonical tag if missing
        if '<link rel="canonical"' not in cs:
            cs = re.sub(
                r'(<title>.*?</title>)',
                r'\1\n  <link rel="canonical" href="https://valixis.tech/client-sites/">',
                cs
            )

        with open(cs_idx, "w", encoding="utf-8") as f:
            f.write(cs)
        print("  [OK] Updated client-sites/index.html (Canonical tag & homepage return link)")

    # ----------------------------------------------------
    # 11. Novel Hotel Footer (client-sites/novel-hotel/index.html)
    # ----------------------------------------------------
    nh_path = os.path.join(base, "client-sites", "novel-hotel", "index.html")
    if os.path.exists(nh_path):
        with open(nh_path, "r", encoding="utf-8") as f:
            nh = f.read()

        if "Engineered by VALIXIS" not in nh:
            nh = nh.replace(
                "<p>© 2026 NOVEL Hotel & Restaurant, Guntur. All rights reserved.</p>",
                '<p>© 2026 NOVEL Hotel & Restaurant, Guntur. All rights reserved. &middot; <span style="color:var(--text-gold);">Engineered by <a href="https://valixis.tech" target="_blank" style="color:var(--text-gold); font-weight:700; text-decoration:none;">VALIXIS</a></span></p>'
            )
            with open(nh_path, "w", encoding="utf-8") as f:
                f.write(nh)
            print("  [OK] Updated client-sites/novel-hotel/index.html (Added VALIXIS attribution)")

print("\nAll Phase 2 upgrades applied successfully across both directories.")
