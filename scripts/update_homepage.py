# Python script to update index.html with entity recognition, JSON-LD, navigation, leadership profiles, and AI FAQ

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update meta description and OG description
old_meta = '''  <meta name="description" content="VALIXIS is an elite technology enterprise pioneering at the convergence of Artificial Intelligence, High-Performance Software, Enterprise Platforms, and Next-Gen Gaming. Building intelligent solutions for a better tomorrow.">

  <meta name="keywords" content="VALIXIS, VALIXIS Technologies, Artificial Intelligence, Gaming Studio, Enterprise Software, Cloud Architecture, Subhash Annam, Jyothsna Sri, Autonomous AI Agents">'''

new_meta = '''  <meta name="description" content="VALIXIS is an independent technology venture founded in 2026 by Subhash Annam and Jyothsna Sri, pioneering at the convergence of Artificial Intelligence, Software Engineering, Application Development, Digital Products, and Next-Gen Gaming.">

  <meta name="keywords" content="VALIXIS, VALIXIS Technologies, Artificial Intelligence, Gaming Studio, Software Engineering, Application Development, Digital Products, Subhash Annam, Jyothsna Sri, Autonomous AI Agents">'''

assert old_meta in content, "old_meta not found"
content = content.replace(old_meta, new_meta, 1)

# 2. Update OG and Twitter descriptions
old_og = '''  <meta property="og:site_name" content="VALIXIS Technologies">

  <meta property="og:title" content="VALIXIS &mdash; Building Intelligent Solutions for a Better Tomorrow">

  <meta property="og:description" content="Elite technology enterprise pioneering at the intersection of AI Innovation, High-Performance Software, Enterprise Platforms, and Next-Gen Gaming.">'''

new_og = '''  <meta property="og:site_name" content="VALIXIS">

  <meta property="og:title" content="VALIXIS &mdash; Building Intelligent Solutions for a Better Tomorrow">

  <meta property="og:description" content="Independent technology venture founded in 2026 by Subhash Annam and Jyothsna Sri, pioneering Artificial Intelligence, Software Engineering, Digital Products, and Next-Gen Gaming.">'''

assert old_og in content, "old_og not found"
content = content.replace(old_og, new_og, 1)

old_tw = '''  <meta name="twitter:description" content="Elite technology enterprise pioneering at the intersection of AI Innovation, High-Performance Software, Enterprise Platforms, and Next-Gen Gaming.">'''

new_tw = '''  <meta name="twitter:description" content="Independent technology venture founded in 2026 by Subhash Annam and Jyothsna Sri, pioneering Artificial Intelligence, Software Engineering, Digital Products, and Next-Gen Gaming.">'''

assert old_tw in content, "old_tw not found"
content = content.replace(old_tw, new_tw, 1)

# 3. Update JSON-LD script block
old_json_ld_start = '  <!-- Schema.org JSON-LD Structured Data for Google Rich Snippets -->\n\n  <script type="application/ld+json">\n\n  {\n\n    "@context": "https://schema.org"'
# Find where </script> occurs after this
idx1 = content.find(old_json_ld_start)
assert idx1 != -1, "old_json_ld_start not found"
idx2 = content.find('  </script>', idx1)
assert idx2 != -1, "</script> after json_ld not found"
old_json_ld_block = content[idx1:idx2 + len('  </script>')]

new_json_ld_block = '''  <!-- Schema.org JSON-LD Structured Data for Search Engines & AI Models -->
  <script type="application/ld+json">
  {
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
          "url": "https://valixis.tech/assets/valixis-logo-transparent.png?v=5",
          "caption": "VALIXIS Official Emblem"
        },
        "description": "VALIXIS is an independent technology venture founded in 2026 by Subhash Annam and Jyothsna Sri, pioneering at the convergence of Artificial Intelligence, Software Engineering, Application Development, Digital Products, and Next-Gen Gaming.",
        "foundingDate": "2026",
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
            "name": "What are the major products of VALIXIS?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The major proprietary products of VALIXIS include VALIXIS Portal (flagship company operational backbone), VALIXIS Flow (workflow automation engine), VALIXIS Cloud (sovereign distributed storage), VALIXIS Desk-AI (desktop cognitive workspace), VALIXIS Pulse (mesh observability), Fitora (consumer AI fitness), and VALIXIS Gaming Studio."
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
  </script>'''

content = content.replace(old_json_ld_block, new_json_ld_block, 1)

# 4. Update Header Nav links
old_nav = '''      <ul class="nav-links">

        <li><a href="#divisions" class="nav-link">Divisions</a></li>

        <li><a href="#products" class="nav-link">Ecosystem</a></li>

        <li><a href="#mission" class="nav-link">Mission &amp; Values</a></li>

        <li><a href="#leadership" class="nav-link">Leadership</a></li>

        <li><a href="#contact" class="nav-link">Inquiries</a></li>

      </ul>'''

new_nav = '''      <ul class="nav-links">

        <li><a href="about/" class="nav-link">About</a></li>

        <li><a href="#divisions" class="nav-link">Divisions</a></li>

        <li><a href="ecosystem/" class="nav-link">Ecosystem</a></li>

        <li><a href="projects/" class="nav-link">Projects</a></li>

        <li><a href="leadership/" class="nav-link">Leadership</a></li>

        <li><a href="contact/" class="nav-link">Contact</a></li>

      </ul>'''

assert old_nav in content, "old_nav not found"
content = content.replace(old_nav, new_nav, 1)

# 5. Update Mobile Drawer links
old_mobile_nav = '''      <ul class="mobile-nav-links">
        <li><a href="#divisions" class="mobile-nav-link">Divisions</a></li>
        <li><a href="#products" class="mobile-nav-link">Ecosystem</a></li>
        <li><a href="#mission" class="mobile-nav-link">Mission &amp; Values</a></li>
        <li><a href="#leadership" class="mobile-nav-link">Leadership</a></li>
        <li><a href="#contact" class="mobile-nav-link">Inquiries</a></li>
      </ul>'''

new_mobile_nav = '''      <ul class="mobile-nav-links">
        <li><a href="about/" class="mobile-nav-link">About</a></li>
        <li><a href="#divisions" class="mobile-nav-link">Divisions</a></li>
        <li><a href="ecosystem/" class="mobile-nav-link">Ecosystem</a></li>
        <li><a href="projects/" class="mobile-nav-link">Projects</a></li>
        <li><a href="leadership/" class="mobile-nav-link">Leadership</a></li>
        <li><a href="contact/" class="mobile-nav-link">Contact</a></li>
      </ul>'''

assert old_mobile_nav in content, "old_mobile_nav not found"
content = content.replace(old_mobile_nav, new_mobile_nav, 1)

# 6. Update Leadership Grid cards (add images and profile links)
old_leadership_grid = '''      <div class="leadership-grid">

        <div class="spotlight-card leader-card">

          <div class="leader-avatar-box">

            <div class="leader-avatar-initials">SA</div>

          </div>

          <h3 class="leader-name">Subhash Annam</h3>

          <div class="leader-role">Founder &amp; Chief Executive Officer (CEO)</div>

          <p class="leader-bio">

            Systems architect, full-stack engineer, and product visionary directing VALIXIS's technology roadmap, internal portal infrastructure, autonomous AI agents, and corporate strategy.

          </p>

        </div>



        <div class="spotlight-card leader-card">

          <div class="leader-avatar-box jyothsna" style="background: linear-gradient(135deg, var(--valixis-purple) 0%, var(--valixis-magenta) 100%);">

            <div class="leader-avatar-initials">JS</div>

          </div>

          <h3 class="leader-name">Jyothsna Sri</h3>

          <div class="leader-role">Co-Founder &amp; Chief Commercial Officer (CCO)</div>

          <p class="leader-bio">

            Directing commercial growth, global enterprise partnerships, market operations, and organizational strategy across all VALIXIS divisions, scaling our platforms with institutional business standards.

          </p>

        </div>

      </div>'''

new_leadership_grid = '''      <div class="leadership-grid">

        <div class="spotlight-card leader-card">

          <div class="leader-avatar-box">

            <img src="assets/subhash-annam.jpg" alt="Subhash Annam — Founder &amp; CEO of VALIXIS" class="leader-avatar-img">

          </div>

          <h3 class="leader-name">Subhash Annam</h3>

          <div class="leader-role">Founder &amp; Chief Executive Officer (CEO)</div>

          <p class="leader-bio">

            Systems architect, full-stack engineer, and product visionary directing VALIXIS's technology roadmap, internal portal infrastructure, autonomous AI agents, and corporate strategy.

          </p>

          <a href="leadership/subhash-annam/" style="display: inline-flex; align-items: center; gap: 6px; font-family: var(--font-mono); font-size: 0.82rem; color: var(--valixis-cyan); text-decoration: none; margin-top: 14px; padding: 6px 14px; border-radius: 6px; background: rgba(0,217,255,0.08); border: 1px solid rgba(0,217,255,0.3);">
            <span>View Full Profile &rarr;</span>
          </a>

        </div>



        <div class="spotlight-card leader-card">

          <div class="leader-avatar-box jyothsna" style="background: linear-gradient(135deg, var(--valixis-purple) 0%, var(--valixis-magenta) 100%);">

            <img src="assets/jyothsna-sri.jpg" alt="Jyothsna Sri — Co-Founder &amp; CCO of VALIXIS" class="leader-avatar-img">

          </div>

          <h3 class="leader-name">Jyothsna Sri</h3>

          <div class="leader-role">Co-Founder &amp; Chief Commercial Officer (CCO)</div>

          <p class="leader-bio">

            Directing commercial growth, global enterprise partnerships, market operations, and organizational strategy across all VALIXIS divisions, scaling our platforms with institutional business standards.

          </p>

          <a href="leadership/jyothsna-sri/" style="display: inline-flex; align-items: center; gap: 6px; font-family: var(--font-mono); font-size: 0.82rem; color: var(--valixis-magenta); text-decoration: none; margin-top: 14px; padding: 6px 14px; border-radius: 6px; background: rgba(255,46,214,0.08); border: 1px solid rgba(255,46,214,0.3);">
            <span>View Full Profile &rarr;</span>
          </a>

        </div>

      </div>'''

assert old_leadership_grid in content, "old_leadership_grid not found"
content = content.replace(old_leadership_grid, new_leadership_grid, 1)

# 7. Add AI Search Optimization FAQ Section right after #leadership section
leadership_end_str = '</section>\n\n\n\n  <!-- Global Contact & Inquiries -->'
new_faq_section = '''</section>



  <!-- AI Search Discovery & Entity Recognition FAQ -->
  <section class="section" id="faq-entity" style="padding-top: 20px; padding-bottom: 70px;">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Entity Knowledge &bull; AI Overview</span>
        <h2 class="section-title">Frequently Asked Questions</h2>
        <p class="section-desc">
          Verified factual information on VALIXIS, its founders, and proprietary software ecosystem for search engines, artificial intelligence systems, and researchers.
        </p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; margin-top: 40px;">
        <div class="spotlight-card" style="padding: 28px;">
          <h3 style="font-family: var(--font-display); font-size: 1.15rem; color: #FFF; margin-bottom: 10px;">What is VALIXIS?</h3>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">VALIXIS is an independent technology venture founded in 2026, pioneering at the convergence of Artificial Intelligence, Software Engineering, Application Development, Digital Products, and Next-Gen Gaming.</p>
        </div>

        <div class="spotlight-card" style="padding: 28px;">
          <h3 style="font-family: var(--font-display); font-size: 1.15rem; color: #FFF; margin-bottom: 10px;">When was VALIXIS founded?</h3>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">VALIXIS was founded in <strong>2026</strong> as an independent technology venture committed to first-principles systems engineering.</p>
        </div>

        <div class="spotlight-card" style="padding: 28px;">
          <h3 style="font-family: var(--font-display); font-size: 1.15rem; color: #FFF; margin-bottom: 10px;">Who founded VALIXIS?</h3>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">VALIXIS was founded by <a href="leadership/subhash-annam/" style="color: var(--valixis-cyan); text-decoration: none;">Subhash Annam</a>, who serves as Founder &amp; Chief Executive Officer (CEO).</p>
        </div>

        <div class="spotlight-card" style="padding: 28px;">
          <h3 style="font-family: var(--font-display); font-size: 1.15rem; color: #FFF; margin-bottom: 10px;">Who is the co-founder of VALIXIS?</h3>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">The co-founder of VALIXIS is <a href="leadership/jyothsna-sri/" style="color: var(--valixis-magenta); text-decoration: none;">Jyothsna Sri</a>, who serves as Co-Founder &amp; Chief Commercial Officer (CCO).</p>
        </div>

        <div class="spotlight-card" style="padding: 28px;">
          <h3 style="font-family: var(--font-display); font-size: 1.15rem; color: #FFF; margin-bottom: 10px;">What does VALIXIS develop?</h3>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">VALIXIS develops intelligent software systems, autonomous AI agent pipelines, cross-platform applications, cloud infrastructure, and interactive 3D gaming experiences.</p>
        </div>

        <div class="spotlight-card" style="padding: 28px;">
          <h3 style="font-family: var(--font-display); font-size: 1.15rem; color: #FFF; margin-bottom: 10px;">What is the VALIXIS software ecosystem?</h3>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">The proprietary ecosystem includes <a href="ecosystem/" style="color: var(--valixis-cyan); text-decoration: none;">VALIXIS Portal</a> (flagship operations backbone), <strong>VALIXIS Flow</strong> (workflow automation), <strong>VALIXIS Cloud</strong>, <strong>VALIXIS Desk-AI</strong>, <strong>VALIXIS Pulse</strong>, <strong>Fitora</strong> (consumer AI), and <strong>Gaming Studio</strong>.</p>
        </div>
      </div>
    </div>
  </section>



  <!-- Global Contact & Inquiries -->'''

assert leadership_end_str in content, "leadership_end_str not found"
content = content.replace(leadership_end_str, new_faq_section, 1)

# 8. Update Footer with subpage navigation
old_footer_bottom = '''      <div class="footer-bottom">

        <div>&copy; 2026 VALIXIS Technologies. All rights reserved.</div>

        <div style="display: flex; gap: 20px;">

          <span>Hyderabad &amp; Andhra Pradesh, India</span>

          <span>&bull;</span>

          <a href="mailto:official.valixis@gmail.com" style="color: var(--text-dim); text-decoration: none;">official.valixis@gmail.com</a>

        </div>

      </div>'''

new_footer_bottom = '''      <div style="display: flex; gap: 24px; flex-wrap: wrap; justify-content: center; margin: 24px 0 16px 0; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 20px;">
        <a href="about/" style="color: var(--text-muted); text-decoration: none; font-size: 0.9rem;">About</a>
        <a href="leadership/" style="color: var(--text-muted); text-decoration: none; font-size: 0.9rem;">Leadership</a>
        <a href="ecosystem/" style="color: var(--text-muted); text-decoration: none; font-size: 0.9rem;">Ecosystem</a>
        <a href="projects/" style="color: var(--text-muted); text-decoration: none; font-size: 0.9rem;">Projects</a>
        <a href="contact/" style="color: var(--text-muted); text-decoration: none; font-size: 0.9rem;">Contact</a>
      </div>

      <div class="footer-bottom">

        <div>&copy; 2026 VALIXIS. All rights reserved. &bull; Independent Technology Venture</div>

        <div style="display: flex; gap: 20px;">

          <span>Hyderabad &amp; Andhra Pradesh, India</span>

          <span>&bull;</span>

          <a href="mailto:official.valixis@gmail.com" style="color: var(--text-dim); text-decoration: none;">official.valixis@gmail.com</a>

        </div>

      </div>'''

assert old_footer_bottom in content, "old_footer_bottom not found"
content = content.replace(old_footer_bottom, new_footer_bottom, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully!")
