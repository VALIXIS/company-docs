import os
import re
import json

base_dirs = [
    r"c:\Users\nagas\Documents\antigravity\resilient-heisenberg\VALIXIS WEBSITE",
    r"c:\Users\nagas\Documents\antigravity\resilient-heisenberg"
]

print("Building Phase 4: VALIXIS Featured Work & Interactive Client Showcase...")

# Project Catalog Data with Strict Classifications
projects_catalog = [
    {
        "id": "rose-cafe",
        "name": "Rose Cafe",
        "location": "Arundelpet, Guntur, AP",
        "industry": "Specialty Floral Cafe & Dining",
        "category": "Direct F&B Ordering & KDS",
        "classification": "Demonstration Project",
        "class_badge_color": "#10B981", # Green
        "accent_color": "#E03E6C",
        "glow_color": "rgba(224, 62, 108, 0.35)",
        "tagline": "5th Floor Indoor Floral Sanctuary & Multi-Cuisine Dining",
        "desc": "A bespoke mobile-first direct ordering web app engineered to bypass third-party food delivery commissions (22%-28%). Features categorized menu modifiers (milk, roast, size), 1-click UPI direct checkout, and automated WhatsApp Barista KDS dispatch.",
        "technologies": ["Mobile-First HTML5", "Modern CSS3", "Vanilla ES6+", "Web Audio API", "WhatsApp KDS Webhooks", "UPI Direct Pay"],
        "demo_url": "../../client-sites/rose-cafe/index.html",
        "demo_direct": "client-sites/rose-cafe/index.html",
        "case_study_url": "rose-cafe/",
        "has_case_study": True,
        "preview_img": "../../client-sites/rose-cafe/assets/gallery/aesthetic_restaurant.jpg",
        "stats": [
            ("Platform Fee", "0% Marketplace Commission"),
            ("Checkout Speed", "1-Click UPI Direct"),
            ("Barista Dispatch", "Automated WhatsApp KDS"),
            ("Page Load", "Under 1.2 Seconds")
        ]
    },
    {
        "id": "novel-hotel",
        "name": "Novel Hotel & Suites",
        "location": "Chandramouli Nagar, Guntur, AP",
        "industry": "Boutique Hospitality & Dining",
        "category": "Luxury Hospitality & Booking",
        "classification": "Demonstration Project",
        "class_badge_color": "#10B981",
        "accent_color": "#D4AF37",
        "glow_color": "rgba(212, 175, 55, 0.35)",
        "tagline": "Boutique Suites, Haute Cuisine & Starlight Rooftop Veranda",
        "desc": "A luxury digital hospitality experience engineered for boutique hotel accommodations and grand dining. Features 3D card tilt physics, suite reservations, rooftop veranda showcase, legendary culinary menu, and direct banquet inquiry booking for up to 300 guests.",
        "technologies": ["Responsive HTML5", "CSS3 Custom Properties", "Tilt.js Physics", "Direct Booking Modal", "Schema.org Hotel"],
        "demo_url": "../../client-sites/novel-hotel/index.html",
        "demo_direct": "client-sites/novel-hotel/index.html",
        "case_study_url": "novel-hotel/",
        "has_case_study": True,
        "preview_img": "https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=700&q=80",
        "stats": [
            ("Banquet Capacity", "Up to 300 Guests"),
            ("Direct Booking", "Zero OTA Commission"),
            ("Dining Veranda", "Starlight Rooftop Showcase"),
            ("Guest Rating", "4.7 / 5.0 Google Reviews")
        ]
    },
    {
        "id": "hiyya-dino-mandi",
        "name": "Hiyya Dino Mandi",
        "location": "Guntur, AP",
        "industry": "Themed Experiential Dining",
        "category": "Experiential Dining & 3D Spatial",
        "classification": "Interactive Concept & Prototype",
        "class_badge_color": "#F59E0B", # Amber
        "accent_color": "#F59E0B",
        "glow_color": "rgba(245, 158, 11, 0.35)",
        "tagline": "Guntur's Prehistoric Arabian Dining Sanctuary",
        "desc": "An experiential dining web platform combining prehistoric atmospheric themes with traditional Arabian Majlis family feast booking. Features atmospheric dark ambient styling, Royal Feast Guild pre-ordering, and direct zero-commission group dining reservations.",
        "technologies": ["CSS3 Spatial Transforms", "HTML5 Canvas Effects", "Interactive Modal Engine", "WhatsApp Dispatch", "Mobile-Optimized"],
        "demo_url": "../../client-sites/hiyya-dino-mandi/index.html",
        "demo_direct": "client-sites/hiyya-dino-mandi/index.html",
        "case_study_url": "hiyya-dino-mandi/",
        "has_case_study": True,
        "preview_img": "../../client-sites/rose-cafe/assets/gallery/chic_interior.jpg",
        "stats": [
            ("Experience", "Prehistoric Arabian Ambiance"),
            ("Seating Flow", "Family Majlis Reservation"),
            ("Pre-Ordering", "Royal Feast Guild Matrix"),
            ("Direct Channel", "Instant WhatsApp Alert")
        ]
    },
    {
        "id": "roastery-coffee-house",
        "name": "Roastery Coffee House",
        "location": "Banjara Hills, Hyderabad, TS",
        "industry": "Heritage Coffee Roastery & Bistro",
        "category": "Specialty Coffee Commerce",
        "classification": "Concept Showcase (Requires Verification)",
        "class_badge_color": "#64748B", # Slate
        "accent_color": "#C28B47",
        "glow_color": "rgba(194, 139, 71, 0.35)",
        "tagline": "Heritage Coffee Roastery & Artisanal Bistro Showcase",
        "desc": "An exploratory technology showcase engineered for heritage specialty coffee venues. Features custom brew method selectors, single-origin bean showcases, bistro breakfast ordering, and 1-click mobile checkout.",
        "technologies": ["Specialty Roast Selector", "Responsive Grid", "UPI Checkout Flow", "Mobile PWA Ready"],
        "demo_url": "../../client-sites/roastery-coffee-house/index.html",
        "demo_direct": "client-sites/roastery-coffee-house/index.html",
        "case_study_url": "",
        "has_case_study": False,
        "preview_img": "",
        "stats": [
            ("Origin Selector", "Artisanal Roast Profiles"),
            ("Ordering", "Direct Bistro Menu"),
            ("Architecture", "Lightweight Client Web App"),
            ("Authorization", "Demonstration Benchmark")
        ]
    },
    {
        "id": "subko-coffee",
        "name": "Subko Specialty Coffee",
        "location": "Bandra, Mumbai, MH",
        "industry": "Specialty Roastery & Craft Bakehouse",
        "category": "Artisanal Retail & Commerce",
        "classification": "Concept Showcase (Requires Verification)",
        "class_badge_color": "#64748B",
        "accent_color": "#CA8A04",
        "glow_color": "rgba(202, 138, 4, 0.35)",
        "tagline": "Specialty Coffee Roasters, Craft Bakehouse & Cacao Mill",
        "desc": "An architectural benchmark demonstration showcasing origin-traceable coffee bags, pod towers, craft sourdough bakehouse items, and single-estate bean selections with direct courier dispatch.",
        "technologies": ["Multi-Category Filter", "Fluid Motion CSS", "Direct Payment Workflow", "High-DPI Typography"],
        "demo_url": "../../client-sites/subko-coffee/index.html",
        "demo_direct": "client-sites/subko-coffee/index.html",
        "case_study_url": "",
        "has_case_study": False,
        "preview_img": "",
        "stats": [
            ("Product Range", "Coffee, Bakehouse & Cacao"),
            ("Direct Order", "Batch Roast Dispatch"),
            ("Architecture", "Clean Vanilla JS & CSS3"),
            ("Authorization", "Demonstration Benchmark")
        ]
    },
    {
        "id": "blue-tokai",
        "name": "Blue Tokai Coffee Roasters",
        "location": "Pali Naka, Bandra West, Mumbai, MH",
        "industry": "Craft Specialty Roastery",
        "category": "Direct-to-Consumer Roastery",
        "classification": "Concept Showcase (Requires Verification)",
        "class_badge_color": "#64748B",
        "accent_color": "#38BDF8",
        "glow_color": "rgba(56, 189, 248, 0.35)",
        "tagline": "Craft Specialty Roastery & Fresh Grind Selection",
        "desc": "An exploratory mobile-first web app demonstrating grind-size customization (Whole Beans, French Press, Aeropress, Espresso), roast profile cards, and fresh harvest delivery scheduling.",
        "technologies": ["Grind Profile Modifier", "Instant UPI Checkout", "Mobile-First Architecture", "FastAPI Ready"],
        "demo_url": "../../client-sites/blue-tokai/index.html",
        "demo_direct": "client-sites/blue-tokai/index.html",
        "case_study_url": "",
        "has_case_study": False,
        "preview_img": "",
        "stats": [
            ("Grind Selector", "7 Custom Brew Sizes"),
            ("Roast Telemetry", "Estate Harvest Date Badges"),
            ("Speed Score", "95+ Mobile Performance"),
            ("Authorization", "Demonstration Benchmark")
        ]
    }
]

print("Catalog data loaded.")

def get_work_hub_html():
    canonical_url = "https://valixis.tech/work/"

    cards_html = ""
    for p in projects_catalog:
        cs_button = f"""<a href="{p['case_study_url']}" class="btn-subtle"><span>View Case Study</span> &rarr;</a>""" if p["has_case_study"] else ""
        
        tech_tags = "".join([f"""<span class="p-tech-tag">{t}</span>""" for t in p["technologies"][:4]])
        
        img_preview = f"""
          <div class="card-img-wrap">
            <img src="{p['preview_img']}" alt="{p['name']}" loading="lazy" class="card-img" />
            <div class="card-img-overlay"></div>
          </div>""" if p.get("preview_img") else ""

        cards_html += f"""
        <article class="work-card" data-category="{p['classification']}" style="border-top: 3px solid {p['accent_color']};">
          {img_preview}
          <div class="card-body">
            <div class="card-top-meta">
              <span class="classification-badge" style="color: {p['class_badge_color']}; border-color: {p['class_badge_color']}; background: rgba(255,255,255,0.03);">
                {p['classification']}
              </span>
              <span class="industry-tag">{p['industry']}</span>
            </div>

            <h2 class="work-title">{p['name']}</h2>
            <div class="work-location">&bull; {p['location']}</div>
            <p class="work-tagline" style="color: {p['accent_color']};">{p['tagline']}</p>
            <p class="work-desc">{p['desc']}</p>

            <div class="tech-stack-row">
              {tech_tags}
            </div>

            <div class="card-action-hub">
              <button onclick="openDemoModal('{p['demo_url']}', '{p['name']}', '{p['accent_color']}')" class="btn-demo" style="background: {p['accent_color']}; color: #000; box-shadow: 0 4px 14px {p['glow_color']};">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                <span>Launch Interactive Demo</span>
              </button>
              {cs_button}
              <a href="{p['demo_url']}" target="_blank" rel="noopener noreferrer" class="btn-icon" title="Open Fullscreen in New Window">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
              </a>
            </div>
          </div>
        </article>"""

    schema_json = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "@id": f"{canonical_url}#webpage",
                "url": canonical_url,
                "name": "Featured Work & Interactive Client Showcases | VALIXIS",
                "description": "Explore production-grade client web platforms, interactive demonstration applications, and spatial dining experiences engineered by VALIXIS.",
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
                    "url": "https://valixis.tech"
                },
                "breadcrumb": {
                    "@id": f"{canonical_url}#breadcrumb"
                }
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{canonical_url}#breadcrumb",
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
                        "name": "Featured Work",
                        "item": canonical_url
                    }
                ]
            }
        ]
    }

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>Featured Work &amp; Interactive Client Showcases | VALIXIS</title>
  <meta name="description" content="Explore live interactive client web applications, demonstration platforms, and spatial dining systems engineered by VALIXIS.">
  <link rel="canonical" href="{canonical_url}">
  <meta name="robots" content="index, follow">
  
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="VALIXIS">
  <meta property="og:locale" content="en_US">
  <meta property="og:title" content="Featured Work &amp; Interactive Client Showcases | VALIXIS">
  <meta property="og:description" content="Explore live interactive client web applications, demonstration platforms, and spatial dining systems engineered by VALIXIS.">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="https://valixis.tech/assets/valixis-logo-full.jpg">
  <meta property="og:image:width" content="1024">
  <meta property="og:image:height" content="1024">
  <meta property="og:image:alt" content="VALIXIS Official Emblem">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Featured Work &amp; Interactive Client Showcases | VALIXIS">
  <meta name="twitter:description" content="Explore live interactive client web applications, demonstration platforms, and spatial dining systems engineered by VALIXIS.">
  <meta name="twitter:image" content="https://valixis.tech/assets/valixis-logo-full.jpg">

  <link rel="icon" type="image/x-icon" href="../favicon.ico?v=3">
  <link rel="icon" type="image/png" sizes="16x16" href="../assets/favicon-16x16.png?v=3">
  <link rel="icon" type="image/png" sizes="32x32" href="../assets/favicon-32x32.png?v=3">
  <link rel="apple-touch-icon" sizes="180x180" href="../assets/apple-touch-icon.png?v=3">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Orbitron:wght@600;700;800;900&display=swap" rel="stylesheet">

  <script type="application/ld+json">
{json.dumps(schema_json, indent=2, ensure_ascii=False)}
  </script>

  <style>
    :root {{
      --valixis-cyan: #00D9FF;
      --valixis-blue: #3B82F6;
      --valixis-purple: #7C3AED;
      --valixis-magenta: #FF2ED6;
      --bg-dark: #0D1117;
      --bg-darker: #06090E;
      --bg-card: rgba(20, 26, 36, 0.85);
      --bg-card-hover: rgba(28, 36, 50, 0.95);
      --border-color: rgba(255, 255, 255, 0.1);
      --text-main: #F1F5F9;
      --text-muted: #94A3B8;
      --font-display: 'Orbitron', -apple-system, sans-serif;
      --font-body: 'Inter', -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --transition-smooth: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; background: var(--bg-darker); color: var(--text-main); font-family: var(--font-body); }}
    body {{ min-height: 100vh; overflow-x: hidden; position: relative; line-height: 1.6; }}

    .ambient-bg {{
      position: fixed; top: 0; left: 0; width: 100%; height: 100%;
      background: radial-gradient(circle at 50% 12%, rgba(0, 217, 255, 0.10) 0%, transparent 60%),
                  radial-gradient(circle at 85% 75%, rgba(124, 58, 237, 0.08) 0%, transparent 50%),
                  #06090E;
      z-index: -1; pointer-events: none;
    }}

    .container {{ width: 100%; max-width: 1140px; margin: 0 auto; padding: 0 24px; }}

    .navbar {{
      position: sticky; top: 0; z-index: 100;
      background: rgba(6, 9, 14, 0.82); backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-color); padding: 16px 0;
    }}
    .nav-wrapper {{ display: flex; align-items: center; justify-content: space-between; }}
    .brand-header {{ display: flex; align-items: center; text-decoration: none; }}
    .brand-lockup-img {{ height: 32px; width: auto; display: block; }}
    .nav-links {{ display: flex; gap: 24px; list-style: none; align-items: center; }}
    .nav-link {{ color: var(--text-muted); text-decoration: none; font-size: 0.88rem; font-weight: 500; transition: var(--transition-smooth); }}
    .nav-link:hover, .nav-link.active {{ color: var(--valixis-cyan); }}

    .btn-cta {{
      display: inline-flex; align-items: center; gap: 8px;
      padding: 9px 18px; border-radius: 8px; font-size: 0.85rem; font-weight: 600;
      color: #FFF; background: linear-gradient(135deg, #00D9FF 0%, #3B82F6 100%);
      border: 1px solid rgba(255, 255, 255, 0.2); text-decoration: none;
      box-shadow: 0 4px 14px rgba(0, 217, 255, 0.35); transition: var(--transition-smooth);
    }}
    .btn-cta:hover {{ transform: translateY(-2px); filter: brightness(1.15); }}

    /* Breadcrumbs */
    .breadcrumbs {{ padding: 20px 0 0 0; font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); }}
    .breadcrumbs a {{ color: var(--text-muted); text-decoration: none; }}
    .breadcrumbs a:hover {{ color: var(--valixis-cyan); }}
    .breadcrumbs span {{ margin: 0 6px; }}

    /* Header */
    .work-hero {{ padding: 48px 0 36px; text-align: center; border-bottom: 1px solid var(--border-color); }}
    .work-badge {{
      display: inline-flex; align-items: center; gap: 8px;
      padding: 5px 14px; border-radius: 999px;
      background: rgba(0, 217, 255, 0.08); border: 1px solid rgba(0, 217, 255, 0.4);
      color: var(--valixis-cyan); font-family: var(--font-mono); font-size: 0.78rem;
      font-weight: 600; text-transform: uppercase; margin-bottom: 16px;
    }}
    .work-heading {{
      font-family: var(--font-display); font-size: 2.6rem; font-weight: 800;
      color: #FFF; margin-bottom: 16px; letter-spacing: -0.02em; line-height: 1.2;
    }}
    .work-lead {{ font-size: 1.1rem; color: var(--text-muted); max-width: 820px; margin: 0 auto; line-height: 1.6; }}

    /* Transparency Disclaimer Notice */
    .classification-banner {{
      background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px; padding: 14px 20px; margin: 28px 0 10px; font-size: 0.82rem; color: var(--text-muted);
      display: flex; gap: 14px; align-items: center; justify-content: center; flex-wrap: wrap;
    }}
    .class-item {{ display: inline-flex; align-items: center; gap: 6px; }}
    .dot {{ width: 8px; height: 8px; border-radius: 50%; display: inline-block; }}

    /* Work Grid */
    .work-grid {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
      gap: 28px; padding: 40px 0 60px;
    }}

    .work-card {{
      background: var(--bg-card); border: 1px solid var(--border-color);
      border-radius: 14px; overflow: hidden; display: flex; flex-direction: column;
      transition: var(--transition-smooth);
    }}
    .work-card:hover {{ background: var(--bg-card-hover); transform: translateY(-4px); box-shadow: 0 14px 35px rgba(0,0,0,0.5); }}

    .card-img-wrap {{ position: relative; width: 100%; height: 180px; overflow: hidden; background: #0A0E17; }}
    .card-img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }}
    .work-card:hover .card-img {{ transform: scale(1.04); }}
    .card-img-overlay {{ position: absolute; inset: 0; background: linear-gradient(180deg, transparent 40%, rgba(20, 26, 36, 0.95) 100%); }}

    .card-body {{ padding: 24px; display: flex; flex-direction: column; flex-grow: 1; }}

    .card-top-meta {{ display: flex; justify-content: space-between; align-items: center; gap: 10px; margin-bottom: 12px; flex-wrap: wrap; }}
    .classification-badge {{
      display: inline-block; padding: 3px 9px; border-radius: 6px; border: 1px solid;
      font-family: var(--font-mono); font-size: 0.70rem; font-weight: 600; text-transform: uppercase;
    }}
    .industry-tag {{ font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-muted); }}

    .work-title {{ font-family: var(--font-display); font-size: 1.35rem; color: #FFF; margin-bottom: 4px; }}
    .work-location {{ font-family: var(--font-mono); font-size: 0.76rem; color: #64748B; margin-bottom: 8px; }}
    .work-tagline {{ font-size: 0.88rem; font-weight: 600; margin-bottom: 10px; line-height: 1.4; }}
    .work-desc {{ font-size: 0.90rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 18px; flex-grow: 1; }}

    .tech-stack-row {{ display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 22px; }}
    .p-tech-tag {{
      background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 4px 10px; border-radius: 5px; font-family: var(--font-mono); font-size: 0.74rem; color: #CBD5E1;
    }}

    .card-action-hub {{ display: flex; gap: 10px; align-items: center; margin-top: auto; flex-wrap: wrap; }}
    .btn-demo {{
      display: inline-flex; align-items: center; gap: 8px;
      padding: 10px 16px; border-radius: 8px; font-size: 0.84rem; font-weight: 700;
      border: none; cursor: pointer; text-decoration: none; transition: var(--transition-smooth);
    }}
    .btn-demo:hover {{ filter: brightness(1.15); transform: translateY(-1px); }}

    .btn-subtle {{
      display: inline-flex; align-items: center; gap: 6px;
      padding: 9px 14px; border-radius: 8px; font-size: 0.82rem; font-weight: 600;
      color: var(--text-main); background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color); text-decoration: none; transition: var(--transition-smooth);
    }}
    .btn-subtle:hover {{ border-color: var(--valixis-cyan); color: var(--valixis-cyan); }}

    .btn-icon {{
      display: inline-flex; align-items: center; justify-content: center;
      width: 38px; height: 38px; border-radius: 8px;
      color: var(--text-muted); background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color); text-decoration: none; transition: var(--transition-smooth);
    }}
    .btn-icon:hover {{ color: #FFF; border-color: rgba(255,255,255,0.3); }}

    /* Interactive Safe Demo Modal */
    .modal-backdrop {{
      display: none; position: fixed; inset: 0; z-index: 1000;
      background: rgba(6, 9, 14, 0.85); backdrop-filter: blur(12px);
      align-items: center; justify-content: center; padding: 20px;
    }}
    .modal-backdrop.active {{ display: flex; }}

    .modal-window {{
      background: #0D1117; border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 16px; width: 100%; max-width: 1040px; height: 88vh;
      display: flex; flex-direction: column; overflow: hidden;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.8);
    }}

    .modal-header {{
      display: flex; justify-content: space-between; align-items: center;
      padding: 14px 20px; border-bottom: 1px solid var(--border-color); background: rgba(6, 9, 14, 0.95);
    }}
    .modal-title-group {{ display: flex; align-items: center; gap: 12px; }}
    .modal-title {{ font-family: var(--font-display); font-size: 1.05rem; color: #FFF; }}
    
    .modal-controls {{ display: flex; align-items: center; gap: 10px; }}
    .device-btn {{
      padding: 5px 12px; border-radius: 6px; font-family: var(--font-mono); font-size: 0.74rem;
      background: rgba(255,255,255,0.06); border: 1px solid var(--border-color); color: var(--text-muted);
      cursor: pointer; transition: all 0.2s;
    }}
    .device-btn.active, .device-btn:hover {{ color: #FFF; border-color: var(--valixis-cyan); }}

    .modal-frame-container {{ flex: 1; position: relative; background: #000; display: flex; align-items: center; justify-content: center; }}
    .demo-iframe {{ width: 100%; height: 100%; border: none; transition: width 0.3s ease; }}
    .demo-iframe.mobile-view {{ width: 390px; height: 100%; box-shadow: 0 0 40px rgba(0,217,255,0.2); border-left: 1px solid #222; border-right: 1px solid #222; }}

    .close-modal-btn {{
      background: none; border: none; color: var(--text-muted); font-size: 1.4rem;
      cursor: pointer; padding: 4px 8px; line-height: 1; transition: color 0.2s;
    }}
    .close-modal-btn:hover {{ color: #FFF; }}

    /* Footer */
    .footer {{ padding: 32px 0; border-top: 1px solid var(--border-color); text-align: center; font-size: 0.84rem; color: var(--text-muted); }}
    .footer a {{ color: var(--text-muted); text-decoration: none; }}
    .footer a:hover {{ color: var(--valixis-cyan); }}

    @media (max-width: 768px) {{
      .nav-links {{ display: none; }}
      .work-heading {{ font-size: 1.9rem; }}
      .work-grid {{ grid-template-columns: 1fr; }}
      .modal-window {{ height: 95vh; padding: 0; }}
      .device-btn {{ display: none; }}
    }}
  </style>
</head>
<body>

  <div class="ambient-bg"></div>

  <header class="navbar">
    <div class="container nav-wrapper">
      <a href="../" class="brand-header" title="VALIXIS &mdash; Return to Homepage">
        <img src="../assets/valixis-horizontal-lockup.png?v=3" alt="VALIXIS" class="brand-lockup-img">
      </a>

      <nav aria-label="Main Navigation">
        <ul class="nav-links">
          <li><a href="../about/" class="nav-link">About</a></li>
          <li><a href="../services/" class="nav-link">Services</a></li>
          <li><a href="../work/" class="nav-link active">Work</a></li>
          <li><a href="../client-sites/" class="nav-link">Showcase</a></li>
          <li><a href="../ecosystem/" class="nav-link">Ecosystem</a></li>
          <li><a href="../projects/" class="nav-link">Projects</a></li>
          <li><a href="../leadership/" class="nav-link">Leadership</a></li>
          <li><a href="../contact/" class="nav-link">Contact</a></li>
        </ul>
      </nav>

      <a href="../contact/" class="btn-cta">
        <span>Commission a Project</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      </a>
    </div>
  </header>

  <main>
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="../">Home</a> <span>/</span> <span style="color:#FFF;">Featured Work</span>
      </nav>

      <section class="work-hero">
        <div class="work-badge">Production Portfolios &amp; Interactive Demos</div>
        <h1 class="work-heading">Client Showcases &amp; Interactive Systems</h1>
        <p class="work-lead">
          Explore functional client web applications, commercial direct ordering engines, and spatial dining environments engineered by VALIXIS. Every demo is live, interactive, and mobile-ready.
        </p>

        <div class="classification-banner">
          <div class="class-item"><span class="dot" style="background:#10B981;"></span> <strong>Demonstration Project:</strong> Functional client system built for local venue operations.</div>
          <div class="class-item"><span class="dot" style="background:#F59E0B;"></span> <strong>Interactive Concept:</strong> Themed experiential dining and 3D spatial prototype.</div>
          <div class="class-item"><span class="dot" style="background:#64748B;"></span> <strong>Concept Showcase:</strong> Architectural benchmark demonstrating specialty workflows.</div>
        </div>
      </section>

      <!-- Work Matrix -->
      <section class="work-grid">
        {cards_html}
      </section>

    </div>
  </main>

  <!-- Safe Interactive Demo Modal -->
  <div class="modal-backdrop" id="demoModal" onclick="closeOnBackdrop(event)">
    <div class="modal-window">
      <div class="modal-header">
        <div class="modal-title-group">
          <span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:#00D9FF;"></span>
          <span class="modal-title" id="modalProjectName">Interactive Preview</span>
        </div>
        <div class="modal-controls">
          <button class="device-btn active" id="btnDesktop" onclick="setDeviceView('desktop')">Desktop</button>
          <button class="device-btn" id="btnMobile" onclick="setDeviceView('mobile')">Mobile (390px)</button>
          <a href="#" id="modalExternalLink" target="_blank" rel="noopener noreferrer" class="btn-subtle" style="padding:4px 10px; font-size:0.75rem;">
            <span>Fullscreen</span> &nearr;
          </a>
          <button class="close-modal-btn" onclick="closeDemoModal()">&times;</button>
        </div>
      </div>
      <div class="modal-frame-container">
        <!-- Sandboxed Lazy-Loaded Iframe -->
        <iframe id="demoIframe" class="demo-iframe" src="about:blank" sandbox="allow-scripts allow-same-origin allow-forms" title="Interactive Client Project Demo"></iframe>
      </div>
    </div>
  </div>

  <footer class="footer">
    <div class="container">
      <p>&copy; 2026 VALIXIS. All rights reserved. &bull; <a href="../">valixis.tech</a> &bull; Independent Technology Venture</p>
    </div>
  </footer>

  <script>
    function openDemoModal(url, name, accent) {{
      const modal = document.getElementById('demoModal');
      const iframe = document.getElementById('demoIframe');
      const title = document.getElementById('modalProjectName');
      const extLink = document.getElementById('modalExternalLink');

      title.textContent = name + ' — Interactive Demo';
      title.style.color = accent || '#FFF';
      extLink.href = url;
      
      // Lazy load only when opened
      iframe.src = url;
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }}

    function closeDemoModal() {{
      const modal = document.getElementById('demoModal');
      const iframe = document.getElementById('demoIframe');
      modal.classList.remove('active');
      iframe.src = 'about:blank'; // Unload to free memory
      document.body.style.overflow = '';
    }}

    function closeOnBackdrop(e) {{
      if (e.target.id === 'demoModal') {{
        closeDemoModal();
      }}
    }}

    function setDeviceView(mode) {{
      const iframe = document.getElementById('demoIframe');
      const btnDesk = document.getElementById('btnDesktop');
      const btnMob = document.getElementById('btnMobile');

      if (mode === 'mobile') {{
        iframe.classList.add('mobile-view');
        btnMob.classList.add('active');
        btnDesk.classList.remove('active');
      }} else {{
        iframe.classList.remove('mobile-view');
        btnDesk.classList.add('active');
        btnMob.classList.remove('active');
      }}
    }}

    // Close on Escape key
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeDemoModal();
    }});
  </script>

</body>
</html>
"""

print("Work Hub template ready.")

# Case Study Detailed Generator
def get_case_study_html(p):
    canonical_url = f"https://valixis.tech/work/{p['id']}/"

    stats_html = "".join([f"""
        <div class="cs-stat-card">
          <div class="cs-stat-val" style="color: {p['accent_color']};">{val}</div>
          <div class="cs-stat-label">{label}</div>
        </div>""" for label, val in p['stats']])

    tech_badges = "".join([f"""<span class="p-tech-tag">{t}</span>""" for t in p['technologies']])

    schema_json = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "@id": f"{canonical_url}#article",
                "headline": f"{p['name']} Case Study — Digital Engineering & Architecture",
                "description": p['desc'],
                "author": {
                    "@type": "Organization",
                    "@id": "https://valixis.tech/#organization",
                    "name": "VALIXIS"
                },
                "publisher": {
                    "@type": "Organization",
                    "@id": "https://valixis.tech/#organization",
                    "name": "VALIXIS"
                },
                "url": canonical_url
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{canonical_url}#breadcrumb",
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
                        "name": "Work",
                        "item": "https://valixis.tech/work/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": p['name'],
                        "item": canonical_url
                    }
                ]
            }
        ]
    }

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>{p['name']} &mdash; Technical Case Study | VALIXIS</title>
  <meta name="description" content="{p['desc'][:160]}">
  <link rel="canonical" href="{canonical_url}">
  <meta name="robots" content="index, follow">
  
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="VALIXIS">
  <meta property="og:locale" content="en_US">
  <meta property="og:title" content="{p['name']} &mdash; Case Study | VALIXIS">
  <meta property="og:description" content="{p['desc'][:160]}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="https://valixis.tech/assets/valixis-logo-full.jpg">
  <meta property="og:image:width" content="1024">
  <meta property="og:image:height" content="1024">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{p['name']} &mdash; Case Study | VALIXIS">
  <meta name="twitter:description" content="{p['desc'][:160]}">
  <meta name="twitter:image" content="https://valixis.tech/assets/valixis-logo-full.jpg">

  <link rel="icon" type="image/x-icon" href="../../favicon.ico?v=3">
  <link rel="icon" type="image/png" sizes="16x16" href="../../assets/favicon-16x16.png?v=3">
  <link rel="icon" type="image/png" sizes="32x32" href="../../assets/favicon-32x32.png?v=3">
  <link rel="apple-touch-icon" sizes="180x180" href="../../assets/apple-touch-icon.png?v=3">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Orbitron:wght@600;700;800;900&display=swap" rel="stylesheet">

  <script type="application/ld+json">
{json.dumps(schema_json, indent=2, ensure_ascii=False)}
  </script>

  <style>
    :root {{
      --accent: {p['accent_color']};
      --accent-glow: {p['glow_color']};
      --bg-dark: #0D1117;
      --bg-darker: #06090E;
      --bg-card: rgba(20, 26, 36, 0.85);
      --bg-card-hover: rgba(28, 36, 50, 0.95);
      --border-color: rgba(255, 255, 255, 0.1);
      --text-main: #F1F5F9;
      --text-muted: #94A3B8;
      --font-display: 'Orbitron', -apple-system, sans-serif;
      --font-body: 'Inter', -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --transition-smooth: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; background: var(--bg-darker); color: var(--text-main); font-family: var(--font-body); }}
    body {{ min-height: 100vh; overflow-x: hidden; position: relative; line-height: 1.6; }}

    .ambient-bg {{
      position: fixed; top: 0; left: 0; width: 100%; height: 100%;
      background: radial-gradient(circle at 50% 12%, var(--accent-glow) 0%, transparent 60%), #06090E;
      z-index: -1; pointer-events: none;
    }}

    .container {{ width: 100%; max-width: 1040px; margin: 0 auto; padding: 0 24px; }}

    .navbar {{
      position: sticky; top: 0; z-index: 100;
      background: rgba(6, 9, 14, 0.82); backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-color); padding: 16px 0;
    }}
    .nav-wrapper {{ display: flex; align-items: center; justify-content: space-between; }}
    .brand-header {{ display: flex; align-items: center; text-decoration: none; }}
    .brand-lockup-img {{ height: 32px; width: auto; display: block; }}
    .nav-links {{ display: flex; gap: 24px; list-style: none; align-items: center; }}
    .nav-link {{ color: var(--text-muted); text-decoration: none; font-size: 0.88rem; font-weight: 500; transition: var(--transition-smooth); }}
    .nav-link:hover, .nav-link.active {{ color: var(--accent); }}

    .btn-cta {{
      display: inline-flex; align-items: center; gap: 8px;
      padding: 9px 18px; border-radius: 8px; font-size: 0.85rem; font-weight: 600;
      color: #000; background: {p['accent_color']}; border: none; text-decoration: none;
      box-shadow: 0 4px 14px var(--accent-glow); transition: var(--transition-smooth);
    }}
    .btn-cta:hover {{ transform: translateY(-2px); filter: brightness(1.15); }}

    .breadcrumbs {{ padding: 20px 0 0 0; font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); }}
    .breadcrumbs a {{ color: var(--text-muted); text-decoration: none; }}
    .breadcrumbs a:hover {{ color: var(--accent); }}
    .breadcrumbs span {{ margin: 0 6px; }}

    .cs-hero {{ padding: 48px 0 32px; border-bottom: 1px solid var(--border-color); }}
    .cs-badge {{
      display: inline-block; padding: 4px 12px; border-radius: 999px; border: 1px solid {p['accent_color']};
      color: {p['accent_color']}; font-family: var(--font-mono); font-size: 0.74rem; font-weight: 600; text-transform: uppercase;
      margin-bottom: 16px;
    }}
    .cs-title {{ font-family: var(--font-display); font-size: 2.5rem; font-weight: 800; color: #FFF; margin-bottom: 8px; }}
    .cs-meta {{ font-family: var(--font-mono); font-size: 0.86rem; color: var(--text-muted); margin-bottom: 18px; }}
    .cs-tagline {{ font-size: 1.15rem; color: var(--text-main); max-width: 820px; line-height: 1.5; margin-bottom: 24px; }}

    .cs-stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 32px 0 10px; }}
    .cs-stat-card {{ background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 20px; }}
    .cs-stat-val {{ font-family: var(--font-display); font-size: 1.25rem; font-weight: 700; margin-bottom: 4px; }}
    .cs-stat-label {{ font-family: var(--font-mono); font-size: 0.76rem; color: var(--text-muted); text-transform: uppercase; }}

    .cs-section {{ padding: 48px 0; border-bottom: 1px solid var(--border-color); }}
    .cs-section-heading {{ font-family: var(--font-display); font-size: 1.5rem; color: #FFF; margin-bottom: 16px; }}
    .cs-body-p {{ color: var(--text-muted); font-size: 1rem; line-height: 1.7; margin-bottom: 20px; }}

    .demo-embed-box {{
      background: #000; border: 1px solid var(--border-color); border-radius: 14px;
      overflow: hidden; height: 600px; position: relative; margin-top: 24px;
    }}
    .demo-embed-iframe {{ width: 100%; height: 100%; border: none; }}

    .p-tech-tag {{
      display: inline-block; background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 6px 12px; border-radius: 6px; font-family: var(--font-mono); font-size: 0.78rem; color: #CBD5E1; margin: 0 8px 8px 0;
    }}

    .footer {{ padding: 32px 0; border-top: 1px solid var(--border-color); text-align: center; font-size: 0.84rem; color: var(--text-muted); }}
    .footer a {{ color: var(--text-muted); text-decoration: none; }}
    .footer a:hover {{ color: var(--accent); }}

    @media (max-width: 768px) {{
      .nav-links {{ display: none; }}
      .cs-title {{ font-size: 1.9rem; }}
      .demo-embed-box {{ height: 450px; }}
    }}
  </style>
</head>
<body>

  <div class="ambient-bg"></div>

  <header class="navbar">
    <div class="container nav-wrapper">
      <a href="../../" class="brand-header" title="VALIXIS &mdash; Return to Homepage">
        <img src="../../assets/valixis-horizontal-lockup.png?v=3" alt="VALIXIS" class="brand-lockup-img">
      </a>

      <nav aria-label="Main Navigation">
        <ul class="nav-links">
          <li><a href="../../about/" class="nav-link">About</a></li>
          <li><a href="../../services/" class="nav-link">Services</a></li>
          <li><a href="../../work/" class="nav-link active">Work</a></li>
          <li><a href="../../client-sites/" class="nav-link">Showcase</a></li>
          <li><a href="../../ecosystem/" class="nav-link">Ecosystem</a></li>
          <li><a href="../../projects/" class="nav-link">Projects</a></li>
          <li><a href="../../leadership/" class="nav-link">Leadership</a></li>
          <li><a href="../../contact/" class="nav-link">Contact</a></li>
        </ul>
      </nav>

      <a href="../../contact/" class="btn-cta">
        <span>Commission Project</span>
      </a>
    </div>
  </header>

  <main>
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="../../">Home</a> <span>/</span> <a href="../../work/">Work</a> <span>/</span> <span style="color:#FFF;">{p['name']}</span>
      </nav>

      <section class="cs-hero">
        <div class="cs-badge">{p['classification']}</div>
        <h1 class="cs-title">{p['name']}</h1>
        <div class="cs-meta">&bull; Location: {p['location']} &bull; Category: {p['category']}</div>
        <p class="cs-tagline">{p['tagline']}</p>
        
        <div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:20px;">
          <a href="{p['demo_url']}" target="_blank" rel="noopener noreferrer" class="btn-cta">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
            <span>Launch Live Fullscreen Demo &nearr;</span>
          </a>
          <a href="../../contact/" style="display:inline-flex; align-items:center; gap:8px; padding:9px 18px; border-radius:8px; font-size:0.85rem; font-weight:600; color:#FFF; background:rgba(255,255,255,0.05); border:1px solid var(--border-color); text-decoration:none;">
            <span>Request Similar System</span>
          </a>
        </div>

        <div class="cs-stats-grid">
          {stats_html}
        </div>
      </section>

      <!-- Challenge -->
      <section class="cs-section">
        <h2 class="cs-section-heading">The Operational Challenge</h2>
        <p class="cs-body-p">
          Hospitality, F&amp;B, and specialty retail venues often face steep commercial friction: third-party delivery aggregators charge between 22% and 28% commissions on every transaction, conceal customer phone numbers, and prevent venues from establishing durable customer relationships. Furthermore, slow legacy websites frequently lose 50%+ of mobile visitors before checkout can occur.
        </p>
      </section>

      <!-- Solution -->
      <section class="cs-section">
        <h2 class="cs-section-heading">The VALIXIS Engineering Solution</h2>
        <p class="cs-body-p">
          VALIXIS engineered a bespoke, ultra-fast mobile-first platform tailored specifically to {p['name']}. By implementing direct 1-click UPI payments, frictionless modifier selectors, and real-time automated WhatsApp dispatch, the platform removes intermediary take-rates and delivers an instantaneous ordering experience.
        </p>
        <div style="margin-top:20px;">
          <h3 style="font-family:var(--font-mono); font-size:0.82rem; text-transform:uppercase; color:var(--accent); margin-bottom:12px;">Verified Technologies</h3>
          <div>{tech_badges}</div>
        </div>
      </section>

      <!-- Live Embed Demo -->
      <section class="cs-section">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
          <h2 class="cs-section-heading" style="margin-bottom:0;">Interactive Working Project</h2>
          <a href="{p['demo_url']}" target="_blank" rel="noopener noreferrer" style="color:var(--accent); text-decoration:none; font-family:var(--font-mono); font-size:0.82rem;">Open Fullscreen &nearr;</a>
        </div>
        <div class="demo-embed-box">
          <iframe src="{p['demo_url']}" class="demo-embed-iframe" loading="lazy" sandbox="allow-scripts allow-same-origin allow-forms" title="{p['name']} Live Demo"></iframe>
        </div>
      </section>

      <!-- CTA -->
      <section style="padding: 60px 0; text-align:center;">
        <h3 style="font-family:var(--font-display); font-size:1.8rem; color:#FFF; margin-bottom:12px;">Commission a System for Your Venue</h3>
        <p style="color:var(--text-muted); font-size:1rem; max-width:640px; margin:0 auto 24px;">
          VALIXIS delivers custom, commission-free web platforms with turnaround times from 3 to 10 days.
        </p>
        <a href="../../contact/" class="btn-cta">
          <span>Discuss Your Project with Founders &rarr;</span>
        </a>
      </section>

    </div>
  </main>

  <footer class="footer">
    <div class="container">
      <p>&copy; 2026 VALIXIS. All rights reserved. &bull; <a href="../../">valixis.tech</a> &bull; Independent Technology Venture</p>
    </div>
  </footer>

</body>
</html>
"""

print("Case study generator ready.")


# ===================================================================
# EXECUTION ENGINE FOR PHASE 4
# ===================================================================
for base in base_dirs:
    print(f"\n==========================================")
    print(f"DEPLOYING FEATURED WORK & SHOWCASES IN: {base}")
    print(f"==========================================")

    # 1. Create work root directory
    work_dir = os.path.join(base, "work")
    os.makedirs(work_dir, exist_ok=True)

    # 2. Write Work Hub (work/index.html)
    hub_path = os.path.join(work_dir, "index.html")
    with open(hub_path, "w", encoding="utf-8") as f:
        f.write(get_work_hub_html())
    print("  [OK] Created work/index.html (Work Portfolio Hub & Lazy Modal)")

    # 3. Write individual case studies
    for p in projects_catalog:
        if p["has_case_study"]:
            cs_dir = os.path.join(work_dir, p["id"])
            os.makedirs(cs_dir, exist_ok=True)
            cs_path = os.path.join(cs_dir, "index.html")
            with open(cs_path, "w", encoding="utf-8") as f:
                f.write(get_case_study_html(p))
            print(f"  [OK] Created work/{p['id']}/index.html ({p['name']} Case Study)")

    # 4. Inject Featured Work Section into Homepage (index.html)
    hp_path = os.path.join(base, "index.html")
    if os.path.exists(hp_path):
        with open(hp_path, "r", encoding="utf-8") as f:
            hp = f.read()

        # Update Navigation to include Work
        if 'href="work/"' not in hp:
            hp = re.sub(
                r'(<nav class="nav-links">[\s\S]*?<a href="services/">Services</a>)',
                r'\1\n      <a href="work/">Work</a>',
                hp
            )

        if 'class="mobile-drawer-link">Work</a>' not in hp:
            hp = re.sub(
                r'(<div class="mobile-drawer-links">[\s\S]*?<a href="services/" class="mobile-drawer-link">Services</a>)',
                r'\1\n        <a href="work/" class="mobile-drawer-link">Work</a>',
                hp
            )

        if '<a href="work/">Work</a>' not in hp:
            hp = re.sub(
                r'(<div class="footer-subpages-nav"[\s\S]*?<a href="services/">Services</a>)',
                r'\1 <span class="sep">&middot;</span> <a href="work/">Work</a>',
                hp
            )

        # Build Featured Work section markup
        work_section_markup = """
    <!-- FEATURED WORK & CLIENT SHOWCASE SECTION (PHASE 4) -->
    <section id="work" class="section work-showcase-section" style="padding: 80px 0; border-top: 1px solid rgba(255,255,255,0.08); background: radial-gradient(circle at 50% 100%, rgba(124, 58, 237, 0.06) 0%, transparent 60%);">
      <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 20px; margin-bottom: 44px;">
          <div style="max-width: 680px;">
            <span style="font-family: var(--font-mono); font-size: 0.8rem; text-transform: uppercase; color: #00D9FF; letter-spacing: 0.1em; display: block; margin-bottom: 10px;">Featured Work &bull; Interactive Prototypes</span>
            <h2 style="font-family: var(--font-display); font-size: 2.2rem; color: #FFF; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 12px;">Live Client Showcases &amp; Web Systems</h2>
            <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.6;">
              Explore production-grade digital platforms engineered by VALIXIS. Each project is live, interactive, and mobile-ready.
            </p>
          </div>
          <div>
            <a href="work/" style="display: inline-flex; align-items: center; gap: 8px; color: #00D9FF; text-decoration: none; font-size: 0.95rem; font-weight: 600; border: 1px solid rgba(0,217,255,0.35); padding: 10px 20px; border-radius: 8px; background: rgba(0,217,255,0.06); transition: all 0.2s;">
              <span>View All 6 Client Projects</span> &rarr;
            </a>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;">

          <!-- Card 1: Rose Cafe -->
          <div class="spotlight-card" style="padding: 28px; display: flex; flex-direction: column; border-top: 3px solid #E03E6C;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
              <span style="font-family: var(--font-mono); font-size: 0.70rem; color: #10B981; border: 1px solid #10B981; padding: 3px 8px; border-radius: 5px; text-transform: uppercase; font-weight: 600;">Demonstration Project</span>
              <span style="font-family: var(--font-mono); font-size: 0.74rem; color: var(--text-muted);">Guntur, AP</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.3rem; color: #FFF; margin-bottom: 6px;">Rose Cafe</h3>
            <p style="font-size: 0.85rem; color: #E03E6C; font-weight: 600; margin-bottom: 10px;">5th Floor Floral Indoor Cafe &amp; Dining</p>
            <p style="color: var(--text-muted); font-size: 0.90rem; line-height: 1.55; margin-bottom: 18px; flex-grow: 1;">
              Direct F&amp;B mobile web app eliminating 22%-28% aggregator commissions. 1-click UPI checkout, menu modifiers, and automated WhatsApp Barista KDS dispatch.
            </p>
            <div style="display: flex; gap: 10px; margin-top: auto; flex-wrap: wrap;">
              <a href="client-sites/rose-cafe/index.html" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 6px; font-size: 0.82rem; font-weight: 700; color: #000; background: #E03E6C; padding: 8px 14px; border-radius: 6px; text-decoration: none;">
                <span>Launch Demo &nearr;</span>
              </a>
              <a href="work/rose-cafe/" style="display: inline-flex; align-items: center; gap: 6px; font-size: 0.82rem; font-weight: 600; color: #FFF; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); padding: 8px 14px; border-radius: 6px; text-decoration: none;">
                <span>Case Study &rarr;</span>
              </a>
            </div>
          </div>

          <!-- Card 2: Novel Hotel -->
          <div class="spotlight-card" style="padding: 28px; display: flex; flex-direction: column; border-top: 3px solid #D4AF37;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
              <span style="font-family: var(--font-mono); font-size: 0.70rem; color: #10B981; border: 1px solid #10B981; padding: 3px 8px; border-radius: 5px; text-transform: uppercase; font-weight: 600;">Demonstration Project</span>
              <span style="font-family: var(--font-mono); font-size: 0.74rem; color: var(--text-muted);">Guntur, AP</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.3rem; color: #FFF; margin-bottom: 6px;">Novel Hotel &amp; Suites</h3>
            <p style="font-size: 0.85rem; color: #D4AF37; font-weight: 600; margin-bottom: 10px;">Boutique Suites, Rooftop &amp; Banquets</p>
            <p style="color: var(--text-muted); font-size: 0.90rem; line-height: 1.55; margin-bottom: 18px; flex-grow: 1;">
              Luxury digital hospitality portal featuring suite reservations, starlight rooftop veranda showcase, haute cuisine biryani menu, and 300-seat banquet booking.
            </p>
            <div style="display: flex; gap: 10px; margin-top: auto; flex-wrap: wrap;">
              <a href="client-sites/novel-hotel/index.html" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 6px; font-size: 0.82rem; font-weight: 700; color: #000; background: #D4AF37; padding: 8px 14px; border-radius: 6px; text-decoration: none;">
                <span>Launch Demo &nearr;</span>
              </a>
              <a href="work/novel-hotel/" style="display: inline-flex; align-items: center; gap: 6px; font-size: 0.82rem; font-weight: 600; color: #FFF; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); padding: 8px 14px; border-radius: 6px; text-decoration: none;">
                <span>Case Study &rarr;</span>
              </a>
            </div>
          </div>

          <!-- Card 3: Hiyya Dino Mandi -->
          <div class="spotlight-card" style="padding: 28px; display: flex; flex-direction: column; border-top: 3px solid #F59E0B;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
              <span style="font-family: var(--font-mono); font-size: 0.70rem; color: #F59E0B; border: 1px solid #F59E0B; padding: 3px 8px; border-radius: 5px; text-transform: uppercase; font-weight: 600;">Interactive Concept</span>
              <span style="font-family: var(--font-mono); font-size: 0.74rem; color: var(--text-muted);">Guntur, AP</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.3rem; color: #FFF; margin-bottom: 6px;">Hiyya Dino Mandi</h3>
            <p style="font-size: 0.85rem; color: #F59E0B; font-weight: 600; margin-bottom: 10px;">Prehistoric Arabian Dining Sanctuary</p>
            <p style="color: var(--text-muted); font-size: 0.90rem; line-height: 1.55; margin-bottom: 18px; flex-grow: 1;">
              Experiential dining platform combining dark atmospheric prehistoric aesthetics with traditional Arabian Majlis family feast pre-ordering workflows.
            </p>
            <div style="display: flex; gap: 10px; margin-top: auto; flex-wrap: wrap;">
              <a href="client-sites/hiyya-dino-mandi/index.html" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 6px; font-size: 0.82rem; font-weight: 700; color: #000; background: #F59E0B; padding: 8px 14px; border-radius: 6px; text-decoration: none;">
                <span>Launch Demo &nearr;</span>
              </a>
              <a href="work/hiyya-dino-mandi/" style="display: inline-flex; align-items: center; gap: 6px; font-size: 0.82rem; font-weight: 600; color: #FFF; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); padding: 8px 14px; border-radius: 6px; text-decoration: none;">
                <span>Case Study &rarr;</span>
              </a>
            </div>
          </div>

        </div>
      </div>
    </section>
"""

        if 'id="work"' not in hp:
            hp = re.sub(
                r'(</section>\s*<!-- ECOSYSTEM SECTION -->)',
                r'\n' + work_section_markup + r'\n\1',
                hp
            )

        with open(hp_path, "w", encoding="utf-8") as f:
            f.write(hp)
        print("  [OK] Injected Featured Work Section into index.html")

    # 5. Update Navigation across all Subpages to include Work
    all_subpage_refs = [
        ("about/index.html", "../"),
        ("leadership/index.html", "../"),
        ("leadership/subhash-annam/index.html", "../../"),
        ("leadership/jyothsna-sri/index.html", "../../"),
        ("ecosystem/index.html", "../"),
        ("projects/index.html", "../"),
        ("contact/index.html", "../"),
        ("client-sites/index.html", "../"),
        ("services/index.html", "../"),
        ("services/ai-automation/index.html", "../../"),
        ("services/software-mobile/index.html", "../../"),
        ("services/web-platforms/index.html", "../../"),
        ("services/3d-gaming-interactive/index.html", "../../"),
    ]

    for sub_rel, prefix in all_subpage_refs:
        sub_p = os.path.join(base, sub_rel)
        if os.path.exists(sub_p):
            with open(sub_p, "r", encoding="utf-8") as f:
                content = f.read()

            work_link = f'{prefix}work/'
            if f'href="{work_link}"' not in content:
                # Add after services link
                content = re.sub(
                    rf'(<a href="{prefix}services/"[^>]*>Services</a>\s*</li>)',
                    rf'\1\n          <li><a href="{work_link}" class="nav-link">Work</a></li>',
                    content
                )
                content = re.sub(
                    rf'(<nav class="nav-links">[\s\S]*?<a href="{prefix}services/"[^>]*>Services</a>)',
                    rf'\1\n      <a href="{work_link}">Work</a>',
                    content
                )
                content = re.sub(
                    rf'(<div class="footer-links">[\s\S]*?<a href="{prefix}services/">Services</a>)',
                    rf'\1 <span class="sep">&middot;</span> <a href="{work_link}">Work</a>',
                    content
                )
                with open(sub_p, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"  [OK] Added Work link to {sub_rel}")

    # 6. Update sitemap.xml with the 4 new Work routes
    sm_path = os.path.join(base, "sitemap.xml")
    if os.path.exists(sm_path):
        sm_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">

  <!-- Homepage / Core Digital Identity -->
  <url>
    <loc>https://valixis.tech/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>

  <!-- Featured Work Portfolio Hub -->
  <url>
    <loc>https://valixis.tech/work/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
  </url>

  <!-- Case Study: Rose Cafe -->
  <url>
    <loc>https://valixis.tech/work/rose-cafe/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.90</priority>
  </url>

  <!-- Case Study: Novel Hotel -->
  <url>
    <loc>https://valixis.tech/work/novel-hotel/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.90</priority>
  </url>

  <!-- Case Study: Hiyya Dino Mandi -->
  <url>
    <loc>https://valixis.tech/work/hiyya-dino-mandi/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.90</priority>
  </url>

  <!-- Commercial Services Hub -->
  <url>
    <loc>https://valixis.tech/services/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
  </url>

  <!-- Service: AI Automation & Intelligent Systems -->
  <url>
    <loc>https://valixis.tech/services/ai-automation/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>

  <!-- Service: Custom Software & Mobile Applications -->
  <url>
    <loc>https://valixis.tech/services/software-mobile/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>

  <!-- Service: Web Platforms & Digital Experiences -->
  <url>
    <loc>https://valixis.tech/services/web-platforms/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>

  <!-- Service: 3D, Gaming & Interactive Technology -->
  <url>
    <loc>https://valixis.tech/services/3d-gaming-interactive/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>

  <!-- Client Showcases Portal -->
  <url>
    <loc>https://valixis.tech/client-sites/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>

  <!-- About / Venture Profile -->
  <url>
    <loc>https://valixis.tech/about/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.80</priority>
  </url>

  <!-- Executive Leadership Overview -->
  <url>
    <loc>https://valixis.tech/leadership/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.80</priority>
  </url>

  <!-- Founder & CEO Profile: Subhash Annam -->
  <url>
    <loc>https://valixis.tech/leadership/subhash-annam/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.80</priority>
  </url>

  <!-- Co-Founder & CCO Profile: Jyothsna Sri -->
  <url>
    <loc>https://valixis.tech/leadership/jyothsna-sri/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.80</priority>
  </url>

  <!-- Software Ecosystem -->
  <url>
    <loc>https://valixis.tech/ecosystem/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.75</priority>
  </url>

  <!-- Projects & Lifecycle Tracker -->
  <url>
    <loc>https://valixis.tech/projects/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.75</priority>
  </url>

  <!-- Contact & Global Inquiries -->
  <url>
    <loc>https://valixis.tech/contact/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.75</priority>
  </url>

</urlset>
"""
        with open(sm_path, "w", encoding="utf-8") as f:
            f.write(sm_content)
        print("  [OK] Updated sitemap.xml with 18 canonical URLs (including 4 Work & Case Study routes)")

print("\nPhase 4 Work Portfolio & Interactive Showcases deployed successfully across both directories.")
