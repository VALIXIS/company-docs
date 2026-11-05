import os
import re
import json

base_dirs = [
    r"c:\Users\nagas\Documents\antigravity\resilient-heisenberg\VALIXIS WEBSITE",
    r"c:\Users\nagas\Documents\antigravity\resilient-heisenberg"
]

def get_service_page_html(slug, title, service_name, badge, desc, accent_color, glow_color, problems, use_cases, deliverables, tech_stack, approach_steps, actual_projects):
    breadcrumb_title = service_name
    canonical_url = f"https://valixis.tech/services/{slug}/"
    
    problems_html = "".join([f"""
        <div class="service-box">
          <div class="box-icon" style="color: {accent_color};">&#9888;</div>
          <h4 class="box-title">{p['title']}</h4>
          <p class="box-desc">{p['desc']}</p>
        </div>""" for p in problems])

    use_cases_html = "".join([f"""
        <div class="service-box">
          <div class="box-icon" style="color: {accent_color};">&#9670;</div>
          <h4 class="box-title">{u['title']}</h4>
          <p class="box-desc">{u['desc']}</p>
        </div>""" for u in use_cases])

    deliverables_html = "".join([f"""
        <li class="deliverable-item">
          <span class="deliverable-check" style="color: {accent_color};">&#10003;</span>
          <div>
            <strong>{d['title']}</strong> &mdash; <span>{d['desc']}</span>
          </div>
        </li>""" for d in deliverables])

    tech_badges_html = "".join([f"""<span class="tech-badge" style="border-color: rgba(255,255,255,0.15);">{t}</span>""" for t in tech_stack])

    approach_html = "".join([f"""
        <div class="approach-step">
          <div class="step-num" style="color: {accent_color}; border-color: {accent_color};">{idx+1}</div>
          <div class="step-content">
            <h4 class="step-title">{st['title']}</h4>
            <p class="step-desc">{st['desc']}</p>
          </div>
        </div>""" for idx, st in enumerate(approach_steps)])

    projects_html = "".join([f"""
        <div class="service-box" style="border-top: 2px solid {accent_color};">
          <div class="p-status" style="color: {accent_color}; font-family: var(--font-mono); font-size: 0.75rem; text-transform: uppercase; margin-bottom: 8px;">{pr['status']}</div>
          <h4 class="box-title">{pr['title']}</h4>
          <p class="box-desc">{pr['desc']}</p>
        </div>""" for pr in actual_projects])

    schema_json = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": f"{canonical_url}#service",
                "name": service_name,
                "serviceType": service_name,
                "description": desc,
                "provider": {
                    "@type": "Organization",
                    "@id": "https://valixis.tech/#organization",
                    "name": "VALIXIS",
                    "url": "https://valixis.tech"
                },
                "areaServed": "Worldwide",
                "url": canonical_url
            },
            {
                "@type": "WebPage",
                "@id": f"{canonical_url}#webpage",
                "url": canonical_url,
                "name": f"{service_name} — Commercial Services | VALIXIS",
                "description": desc,
                "isPartOf": {
                    "@type": "WebSite",
                    "@id": "https://valixis.tech/#website",
                    "url": "https://valixis.tech",
                    "name": "VALIXIS"
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
                        "name": "Services",
                        "item": "https://valixis.tech/services/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": breadcrumb_title,
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
  <title>{service_name} &mdash; Commercial Solutions | VALIXIS</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical_url}">
  <meta name="robots" content="index, follow">
  
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="VALIXIS">
  <meta property="og:locale" content="en_US">
  <meta property="og:title" content="{service_name} &mdash; VALIXIS Commercial Solutions">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="https://valixis.tech/assets/valixis-logo-full.jpg">
  <meta property="og:image:width" content="1024">
  <meta property="og:image:height" content="1024">
  <meta property="og:image:alt" content="VALIXIS Official Emblem">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{service_name} &mdash; VALIXIS Commercial Solutions">
  <meta name="twitter:description" content="{desc}">
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
      --valixis-cyan: #00D9FF;
      --valixis-blue: #3B82F6;
      --valixis-purple: #7C3AED;
      --valixis-magenta: #FF2ED6;
      --accent: {accent_color};
      --accent-glow: {glow_color};
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
      background: radial-gradient(circle at 50% 15%, var(--accent-glow) 0%, transparent 60%),
                  radial-gradient(circle at 90% 85%, rgba(124, 58, 237, 0.08) 0%, transparent 50%),
                  #06090E;
      z-index: -1; pointer-events: none;
    }}

    .container {{ width: 100%; max-width: 1120px; margin: 0 auto; padding: 0 24px; }}

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
      color: #FFF; background: linear-gradient(135deg, {accent_color} 0%, #3B82F6 100%);
      border: 1px solid rgba(255, 255, 255, 0.2); text-decoration: none;
      box-shadow: 0 4px 14px var(--accent-glow); transition: var(--transition-smooth);
    }}
    .btn-cta:hover {{ transform: translateY(-2px); filter: brightness(1.15); }}

    .btn-outline {{
      display: inline-flex; align-items: center; gap: 8px;
      padding: 9px 18px; border-radius: 8px; font-size: 0.85rem; font-weight: 600;
      color: var(--text-main); background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color); text-decoration: none;
      transition: var(--transition-smooth);
    }}
    .btn-outline:hover {{ border-color: var(--accent); color: var(--accent); }}

    /* Breadcrumbs */
    .breadcrumbs {{ padding: 20px 0 0 0; font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); }}
    .breadcrumbs a {{ color: var(--text-muted); text-decoration: none; transition: var(--transition-smooth); }}
    .breadcrumbs a:hover {{ color: var(--accent); }}
    .breadcrumbs span {{ margin: 0 6px; }}

    /* Hero */
    .service-hero {{ padding: 48px 0 40px; border-bottom: 1px solid var(--border-color); }}
    .service-badge {{
      display: inline-flex; align-items: center; gap: 8px;
      padding: 5px 14px; border-radius: 999px;
      background: rgba(255, 255, 255, 0.04); border: 1px solid {accent_color};
      color: {accent_color}; font-family: var(--font-mono); font-size: 0.78rem;
      font-weight: 600; text-transform: uppercase; margin-bottom: 20px;
    }}
    .service-title {{
      font-family: var(--font-display); font-size: 2.4rem; font-weight: 800;
      color: #FFF; margin-bottom: 16px; line-height: 1.2; letter-spacing: -0.02em;
    }}
    .service-lead {{ font-size: 1.15rem; color: var(--text-muted); max-width: 820px; line-height: 1.6; margin-bottom: 28px; }}

    /* Section Styles */
    .content-section {{ padding: 48px 0; border-bottom: 1px solid var(--border-color); }}
    .section-title-wrap {{ margin-bottom: 32px; }}
    .section-eyebrow {{ font-family: var(--font-mono); font-size: 0.78rem; text-transform: uppercase; color: {accent_color}; margin-bottom: 8px; display: block; }}
    .section-heading {{ font-family: var(--font-display); font-size: 1.6rem; color: #FFF; }}

    /* Grid */
    .grid-2 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }}

    .service-box {{
      background: var(--bg-card); border: 1px solid var(--border-color);
      border-radius: 12px; padding: 24px; transition: var(--transition-smooth);
    }}
    .service-box:hover {{ background: var(--bg-card-hover); border-color: rgba(255, 255, 255, 0.2); transform: translateY(-2px); }}
    .box-icon {{ font-size: 1.5rem; margin-bottom: 12px; }}
    .box-title {{ font-family: var(--font-display); font-size: 1.08rem; color: #FFF; margin-bottom: 8px; }}
    .box-desc {{ font-size: 0.92rem; color: var(--text-muted); line-height: 1.55; }}

    /* Deliverables List */
    .deliverables-list {{ list-style: none; display: flex; flex-direction: column; gap: 16px; }}
    .deliverable-item {{ display: flex; gap: 14px; align-items: flex-start; background: var(--bg-card); border: 1px solid var(--border-color); padding: 16px 20px; border-radius: 10px; }}
    .deliverable-check {{ font-size: 1.1rem; font-weight: bold; line-height: 1.2; }}

    /* Tech Badges */
    .tech-badges-wrap {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 16px; }}
    .tech-badge {{
      background: rgba(255, 255, 255, 0.04); border: 1px solid var(--border-color);
      padding: 6px 14px; border-radius: 6px; font-family: var(--font-mono);
      font-size: 0.82rem; color: #E2E8F0;
    }}

    /* Approach Steps */
    .approach-timeline {{ display: flex; flex-direction: column; gap: 20px; }}
    .approach-step {{ display: flex; gap: 20px; align-items: flex-start; }}
    .step-num {{
      width: 40px; height: 40px; border-radius: 50%; border: 2px solid;
      display: flex; align-items: center; justify-content: center;
      font-family: var(--font-mono); font-weight: 700; flex-shrink: 0; background: var(--bg-card);
    }}
    .step-content {{ background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 18px 22px; flex: 1; }}
    .step-title {{ font-family: var(--font-display); font-size: 1.05rem; color: #FFF; margin-bottom: 6px; }}
    .step-desc {{ font-size: 0.9rem; color: var(--text-muted); line-height: 1.55; }}

    /* CTA Section */
    .cta-banner {{
      padding: 60px 0; text-align: center;
      background: linear-gradient(180deg, rgba(6, 9, 14, 0) 0%, rgba(13, 17, 23, 0.85) 100%);
    }}
    .cta-card {{
      background: var(--bg-card); border: 1px solid var(--border-color);
      border-radius: 16px; padding: 48px 32px; max-width: 780px; margin: 0 auto;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
    }}
    .cta-title {{ font-family: var(--font-display); font-size: 1.8rem; color: #FFF; margin-bottom: 12px; }}
    .cta-desc {{ color: var(--text-muted); font-size: 1rem; margin-bottom: 28px; line-height: 1.6; }}
    .cta-actions {{ display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }}

    /* Footer */
    .footer {{ padding: 32px 0; border-top: 1px solid var(--border-color); text-align: center; font-size: 0.84rem; color: var(--text-muted); }}
    .footer a {{ color: var(--text-muted); text-decoration: none; transition: var(--transition-smooth); }}
    .footer a:hover {{ color: var(--accent); }}

    @media (max-width: 768px) {{
      .nav-links {{ display: none; }}
      .service-title {{ font-size: 1.8rem; }}
      .service-lead {{ font-size: 1rem; }}
      .cta-card {{ padding: 32px 20px; }}
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
          <li><a href="../../services/" class="nav-link active">Services</a></li>
          <li><a href="../../client-sites/" class="nav-link">Showcase</a></li>
          <li><a href="../../ecosystem/" class="nav-link">Ecosystem</a></li>
          <li><a href="../../projects/" class="nav-link">Projects</a></li>
          <li><a href="../../leadership/" class="nav-link">Leadership</a></li>
          <li><a href="../../contact/" class="nav-link">Contact</a></li>
        </ul>
      </nav>

      <a href="../../contact/" class="btn-cta">
        <span>Request Consultation</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      </a>
    </div>
  </header>

  <main>
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="../../">Home</a> <span>/</span> <a href="../../services/">Services</a> <span>/</span> <span style="color:#FFF;">{service_name}</span>
      </nav>

      <section class="service-hero">
        <div class="service-badge">{badge}</div>
        <h1 class="service-title">{service_name}</h1>
        <p class="service-lead">{desc}</p>
        <div style="display:flex; gap:16px; flex-wrap:wrap;">
          <a href="../../contact/" class="btn-cta">Schedule Technical Scoping</a>
          <a href="#deliverables" class="btn-outline">View Deliverables</a>
        </div>
      </section>

      <!-- Problems Solved -->
      <section class="content-section">
        <div class="section-title-wrap">
          <span class="section-eyebrow">Challenges Addressed</span>
          <h2 class="section-heading">Operational &amp; Technical Problems We Solve</h2>
        </div>
        <div class="grid-2">
          {problems_html}
        </div>
      </section>

      <!-- Business Use Cases -->
      <section class="content-section">
        <div class="section-title-wrap">
          <span class="section-eyebrow">Enterprise Applications</span>
          <h2 class="section-heading">High-Value Business Use Cases</h2>
        </div>
        <div class="grid-2">
          {use_cases_html}
        </div>
      </section>

      <!-- Deliverables -->
      <section class="content-section" id="deliverables">
        <div class="section-title-wrap">
          <span class="section-eyebrow">Scope &amp; Handover</span>
          <h2 class="section-heading">Standard Engineering Deliverables</h2>
        </div>
        <ul class="deliverables-list">
          {deliverables_html}
        </ul>
      </section>

      <!-- Technologies Used -->
      <section class="content-section">
        <div class="section-title-wrap">
          <span class="section-eyebrow">Technical Stack</span>
          <h2 class="section-heading">Frameworks, Protocols &amp; Infrastructure</h2>
        </div>
        <div class="tech-badges-wrap">
          {tech_badges_html}
        </div>
      </section>

      <!-- Development Approach -->
      <section class="content-section">
        <div class="section-title-wrap">
          <span class="section-eyebrow">Methodology</span>
          <h2 class="section-heading">Structured Development &amp; Quality Lifecycle</h2>
        </div>
        <div class="approach-timeline">
          {approach_html}
        </div>
      </section>

      <!-- Relevant Actual Projects -->
      <section class="content-section">
        <div class="section-title-wrap">
          <span class="section-eyebrow">Track Record</span>
          <h2 class="section-heading">Proprietary Platforms &amp; Client Deployments</h2>
        </div>
        <div class="grid-3">
          {projects_html}
        </div>
      </section>

      <!-- Consultation CTA -->
      <section class="cta-banner">
        <div class="cta-card">
          <h2 class="cta-title">Ready to Engineer Your Solution?</h2>
          <p class="cta-desc">
            Connect directly with our engineering leadership to review system requirements, architecture feasibility, and delivery timelines.
          </p>
          <div class="cta-actions">
            <a href="../../contact/" class="btn-cta">
              <span>Initiate Direct Inquiry</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
            <a href="https://wa.me/919603416707" target="_blank" rel="noopener noreferrer" class="btn-outline">
              <span>Message on WhatsApp</span>
            </a>
          </div>
        </div>
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

print("Generator script template ready.")

# Service Definitions Data
services_data = [
    {
        "slug": "ai-automation",
        "service_name": "AI Automation & Intelligent Systems",
        "badge": "Cognitive Engineering",
        "accent_color": "#00D9FF",
        "glow_color": "rgba(0, 217, 255, 0.35)",
        "desc": "Autonomous multi-agent pipelines, cognitive document intelligence, natural language orchestration, and custom inference architectures engineered to eliminate operational bottlenecks.",
        "problems": [
            {
                "title": "Manual Workflow Overhead",
                "desc": "Teams spend hours manually transferring data between systems, generating reports, and reconciling operational documents."
            },
            {
                "title": "Delayed Customer Response",
                "desc": "High lead inquiry drop-off due to slow after-hours response times and lack of intelligent 24/7 automated qualification."
            },
            {
                "title": "Unstructured Data Silos",
                "desc": "Critical enterprise data trapped in PDFs, emails, and legacy spreadsheets without semantic search or real-time queryability."
            },
            {
                "title": "Fragile Script Automations",
                "desc": "Brittle, hardcoded RPA scripts that break when UI changes occur or require constant human maintenance."
            }
        ],
        "use_cases": [
            {
                "title": "Autonomous Inbound Lead Qualification",
                "desc": "Deploy 24/7 WhatsApp and web agents that converse naturally, qualify prospect requirements, and route ready bookings into your CRM."
            },
            {
                "title": "Intelligent Document Parsing & Ingestion",
                "desc": "Extract line-item data from invoices, medical receipts, and technical specs with high-confidence schema validation."
            },
            {
                "title": "Enterprise Knowledge Assistants",
                "desc": "Private, permission-aware RAG search across company handbooks, codebases, and customer service documentation."
            },
            {
                "title": "Engineering Pipeline Automation",
                "desc": "Autonomous agents coordinating code reviews, deployment verification, dependency updates, and pull request synchronization."
            }
        ],
        "deliverables": [
            {
                "title": "Production Agent Pipeline",
                "desc": "Custom Python / TypeScript agent graph with structured input/output validation and deterministic fallback guards."
            },
            {
                "title": "REST & Webhook Integration Layer",
                "desc": "High-throughput FastAPI / Node endpoints connecting your CRM, messaging apps (WhatsApp, Telegram, Slack), and databases."
            },
            {
                "title": "Observability & Telemetry Dashboard",
                "desc": "Execution logs, token consumption analytics, latency monitoring, and automated alerts for edge-case failures."
            },
            {
                "title": "Deployment Runbook & Documentation",
                "desc": "Comprehensive architecture guide, environment configuration, containerization manifests, and handover."
            }
        ],
        "tech_stack": [
            "Python 3.12+", "LangChain", "LlamaIndex", "OpenAI API", "Anthropic Claude API", "Gemini 2.5/3 Flash",
            "Local LLMs (Ollama / Llama 3)", "FastAPI", "PostgreSQL / pgvector", "Redis", "Docker", "Webhooks"
        ],
        "approach_steps": [
            {
                "title": "1. Operational Workflow Audit",
                "desc": "We inspect your existing manual processes, input schemas, and data pipelines to identify high-ROI automation targets."
            },
            {
                "title": "2. Agent Graph & Guardrail Design",
                "desc": "We architect deterministic state machines, prompt engineering boundaries, and tool calling definitions."
            },
            {
                "title": "3. Sandbox Integration & Evaluation",
                "desc": "We run rigorous synthetic test suites evaluating edge cases, token latency, accuracy, and error recovery."
            },
            {
                "title": "4. Production Deployment & SLA Monitoring",
                "desc": "We deploy containerized microservices to cloud or on-premise infrastructure with live telemetry."
            }
        ],
        "actual_projects": [
            {
                "status": "In Development",
                "title": "VALIXIS Flow",
                "desc": "Proprietary autonomous agent engine orchestrating asynchronous multi-step developer and administrative workflows."
            },
            {
                "status": "In Development",
                "title": "VALIXIS Desk-AI",
                "desc": "Desktop cognitive assistant delivering local context processing, document comprehension, and system task automation."
            },
            {
                "status": "Internal Pipeline",
                "title": "Inbound Lead Hunter & Dispatcher",
                "desc": "Autonomous multi-channel qualification system managing verification, CRM routing, and Telegram notifications."
            }
        ]
    },
    {
        "slug": "software-mobile",
        "service_name": "Custom Software & Mobile Applications",
        "badge": "Systems & Mobile",
        "accent_color": "#3B82F6",
        "glow_color": "rgba(59, 130, 246, 0.35)",
        "desc": "High-reliability cross-platform mobile applications (iOS & Android) and robust enterprise software architectures engineered for fault tolerance, offline resilience, and fluid 60-120 FPS performance.",
        "problems": [
            {
                "title": "Fragile Multi-Platform Codebases",
                "desc": "Maintaining separate Swift and Kotlin codebases doubles development costs and causes feature parity delays."
            },
            {
                "title": "Sluggish App Performance",
                "desc": "Heavy web-wrappers and poorly architected state trees causing dropped frames, battery drain, and poor app store ratings."
            },
            {
                "title": "Inflexible Off-the-Shelf SaaS",
                "desc": "Generic software forcing businesses into rigid workflows, high per-seat license fees, and zero proprietary IP ownership."
            },
            {
                "title": "Unscalable Database Architecture",
                "desc": "Lack of row-level security, unindexed queries, and poor concurrency causing slow lookups as transaction volumes scale."
            }
        ],
        "use_cases": [
            {
                "title": "Consumer Mobile Applications",
                "desc": "Bespoke iOS and Android mobile apps with slick animations, offline data caching, biometrics, and push notifications."
            },
            {
                "title": "Internal Enterprise Dashboards",
                "desc": "Centralized portals for inventory tracking, role-based employee administration, task dispatch, and reporting."
            },
            {
                "title": "Customer Self-Service Portals",
                "desc": "Account management, order tracking, real-time subscription controls, and direct customer communication channels."
            },
            {
                "title": "Dedicated Engineering Pods",
                "desc": "Sprint-based full-stack engineering pods delivering continuous feature releases, API updates, and Git CI/CD pipelines."
            }
        ],
        "deliverables": [
            {
                "title": "Production iOS & Android Builds",
                "desc": "Native-compiled binaries with signing configurations, ready for Apple App Store and Google Play Store submission."
            },
            {
                "title": "Full-Stack Source Repository",
                "desc": "Clean, modular Flutter or TypeScript codebase adhering to strict architectural layering (UI, Logic, Data)."
            },
            {
                "title": "Scalable Cloud Backend & Database",
                "desc": "PostgreSQL database with Row Level Security (RLS), automated migrations, and high-concurrency connection pooling."
            },
            {
                "title": "Automated CI/CD Pipeline",
                "desc": "GitHub Actions workflow compiling, testing, and generating artifacts automatically on every pull request."
            }
        ],
        "tech_stack": [
            "Flutter & Dart", "TypeScript", "Node.js", "Go", "PostgreSQL", "Supabase RLS",
            "Redis", "Docker", "REST / GraphQL", "GitHub Actions", "Tailwind CSS", "Linux"
        ],
        "approach_steps": [
            {
                "title": "1. Architecture & Domain Modeling",
                "desc": "We establish strict entity relationships, state management patterns, and API contracts before coding begins."
            },
            {
                "title": "2. Agile Sprint Slicing",
                "desc": "We break engineering into 2-week deliverable increments with test-driven development and code reviews."
            },
            {
                "title": "3. Hardware & Network Stress Testing",
                "desc": "We test performance across low-end mobile devices, slow 3G network conditions, and offline synchronization states."
            },
            {
                "title": "4. Store Submission & Cloud Handoff",
                "desc": "We guide your team through store approvals, credentials handover, and production monitoring setup."
            }
        ],
        "actual_projects": [
            {
                "status": "In Development",
                "title": "Fitora Consumer Mobile Platform",
                "desc": "Cross-platform consumer AI application combining computer vision routines with adaptive physical conditioning."
            },
            {
                "status": "In Development",
                "title": "VALIXIS Pulse",
                "desc": "Lightweight telemetry and distributed node monitoring platform designed for real-time uptime verification."
            },
            {
                "status": "Launched Platform",
                "title": "VALIXIS Portal Backbone",
                "desc": "Internal operations engine managing developer workflows, code deployment synchronizations, and permissions."
            }
        ]
    },
    {
        "slug": "web-platforms",
        "service_name": "Web Platforms & Digital Experiences",
        "badge": "Web Engineering & Commerce",
        "accent_color": "#7C3AED",
        "glow_color": "rgba(124, 58, 237, 0.35)",
        "desc": "Ultra-fast, high-converting digital web applications, direct ordering portals, and bespoke commercial showcases built to turn casual visitors into loyal customers with sub-second page loads.",
        "problems": [
            {
                "title": "Aggregator Commission Drain",
                "desc": "F&B, hospitality, and retail businesses losing 22% to 28% of gross revenue to marketplace aggregators with zero customer ownership."
            },
            {
                "title": "Slow Legacy Website Abandonment",
                "desc": "53% of mobile visits are abandoned if a website takes more than 3 seconds to load, severely undermining marketing spend."
            },
            {
                "title": "Zero Customer Data Control",
                "desc": "Marketplace intermediaries conceal customer phone numbers and purchase histories, preventing direct remarketing."
            },
            {
                "title": "Clunky Mobile Checkouts",
                "desc": "Multi-step registration forms and payment friction causing high cart abandonment rates on mobile screens."
            }
        ],
        "use_cases": [
            {
                "title": "Direct F&B Ordering & Kitchen Display (KDS)",
                "desc": "Specialty cafes, bakeries, and QSRs offering 1-click UPI direct checkout and automated WhatsApp barista dispatch."
            },
            {
                "title": "24/7 Clinic & Salon Booking Portals",
                "desc": "Healthcare and wellness clinics capturing appointment bookings directly from Instagram and Google with automated WhatsApp reminders."
            },
            {
                "title": "High-Converting Brand Showcases",
                "desc": "Luxury hospitality, boutique hotels, and artisanal retailers displaying haute menus, room suites, and banquet inquiries."
            },
            {
                "title": "Web Speed & Conversion Overhauls",
                "desc": "Transforming slow WordPress or Wix sites into ultra-fast, mobile-first web applications achieving 90+ Lighthouse scores."
            }
        ],
        "deliverables": [
            {
                "title": "Custom Responsive Web Application",
                "desc": "Ultra-fast web app with mobile-first UI, fluid layout transitions, and instant page transitions."
            },
            {
                "title": "1-Click Direct Ordering / Booking Flow",
                "desc": "Seamless payment and confirmation workflow integrated with UPI, cards, and direct WhatsApp alerts."
            },
            {
                "title": "Search Engine & Schema Optimization",
                "desc": "Complete Schema.org structured data, semantic HTML5 headings, OpenGraph preview cards, and XML sitemaps."
            },
            {
                "title": "Cloudflare Global Edge CDN Hosting",
                "desc": "Enterprise-grade SSL, 99.9% uptime guarantees, asset caching, and continuous security protection."
            }
        ],
        "tech_stack": [
            "Semantic HTML5", "Modern CSS3 / Flex / Grid", "Vanilla ES6+ JavaScript", "Next.js / React",
            "Cloudflare Edge", "Stripe & UPI Integration", "WhatsApp Business Webhooks", "Lighthouse 90+ Tooling"
        ],
        "approach_steps": [
            {
                "title": "1. Conversion Funnel Analysis",
                "desc": "We analyze your customer journey to remove friction, unnecessary form fields, and redundant clicks."
            },
            {
                "title": "2. Brand System & Interaction Design",
                "desc": "We design high-contrast, responsive interfaces tailored to your visual identity and brand tone."
            },
            {
                "title": "3. Performance & Asset Engineering",
                "desc": "We optimize images (WebP/AVIF), eliminate render-blocking scripts, and engineer instantaneous mobile load."
            },
            {
                "title": "4. Payment & Messaging Integration",
                "desc": "We wire real-time checkout, instant WhatsApp notifications, and verify cross-device checkout flows."
            }
        ],
        "actual_projects": [
            {
                "status": "Live Demo",
                "title": "Rose Cafe Multi-Cuisine Web App",
                "desc": "Indoor floral cafe digital portal featuring categorized menu modifiers, 1-click UPI checkout, and WhatsApp KDS."
            },
            {
                "status": "Live Demo",
                "title": "Novel Hotel Gourmet Dining Portal",
                "desc": "Boutique hotel & rooftop dining experience with suite reservations, haute cuisine showcases, and banquet bookings."
            },
            {
                "status": "Live Showcase",
                "title": "Artisanal Specialty Coffee Portfolios",
                "desc": "Digital experiences engineered for Blue Tokai, Subko Specialty Coffee, and Roastery Coffee House."
            }
        ]
    },
    {
        "slug": "3d-gaming-interactive",
        "service_name": "3D, Gaming & Interactive Technology",
        "badge": "Interactive & Spatial Computing",
        "accent_color": "#FF2ED6",
        "glow_color": "rgba(255, 46, 214, 0.35)",
        "desc": "Immersive browser-based 3D digital environments, interactive spatial configurators, architectural hospitality walkthroughs, and next-generation interactive experiences powered by WebGL and custom game engines.",
        "problems": [
            {
                "title": "Static, Low-Engagement Websites",
                "desc": "Flat 2D pages struggle to capture visitor attention or convey the true premium ambiance of physical spaces and products."
            },
            {
                "title": "High Banquet & Event Vacancy",
                "desc": "Hospitality venues and banquet halls lose lucrative corporate and wedding bookings because event organizers cannot visualize the layout."
            },
            {
                "title": "Complex Spatial Products",
                "desc": "Industrial products, luxury goods, and architectural designs cannot be adequately showcased with simple flat photography."
            },
            {
                "title": "Browser Performance Lag",
                "desc": "Poorly optimized 3D web experiences overheat mobile phones, stutter at 15 FPS, and crash mobile browser tabs."
            }
        ],
        "use_cases": [
            {
                "title": "Interactive 3D Hospitality Portals",
                "desc": "Allow guests and event planners to explore restaurant majlis seating, banquet halls, and rooftop views in interactive 3D."
            },
            {
                "title": "3D Product Visualizers & Configurators",
                "desc": "Interactive 360-degree product models allowing customers to inspect materials, colors, and mechanical assemblies in real-time."
            },
            {
                "title": "Gamified Brand Activations",
                "desc": "Interactive, physics-driven web experiences that captivate users, boost average session duration, and build brand affinity."
            },
            {
                "title": "Cross-Platform Interactive Titles",
                "desc": "Indie game titles and experimental interactive mechanics developed with custom physics and stylized art direction."
            }
        ],
        "deliverables": [
            {
                "title": "Hardware-Accelerated WebGL Scene",
                "desc": "Three.js / WebGL canvas running at smooth 60 FPS, with automatic fallback handling for low-power mobile devices."
            },
            {
                "title": "PBR 3D Models & Baked Texture Assets",
                "desc": "Lightweight, low-poly GLTF / GLB assets with baked lighting and physically based rendering (PBR) materials."
            },
            {
                "title": "Orbital Touch & Mouse Camera Controls",
                "desc": "Fluid, bounded camera interactions with inertia damping, pinch-to-zoom, and touch rotation controls."
            },
            {
                "title": "Interactive Hotspots & Annotations",
                "desc": "Clickable 3D pins triggering product specifications, booking modals, or video overlays seamlessly."
            }
        ],
        "tech_stack": [
            "Three.js r128+", "WebGL 2.0", "GLSL Custom Shaders", "Blender (Retopology & Baking)",
            "GLTF / GLB Compression", "GSAP 3", "HTML5 Canvas", "Unreal Engine / Unity"
        ],
        "approach_steps": [
            {
                "title": "1. Spatial Concept & Asset Acquisition",
                "desc": "We capture venue floorplans, CAD schematics, or photogrammetry reference imagery for 3D model creation."
            },
            {
                "title": "2. Low-Poly Retopology & Light Baking",
                "desc": "We optimize polygons and bake raytraced lighting into lightweight textures for mobile browser efficiency."
            },
            {
                "title": "3. WebGL Scene Composition & Shaders",
                "desc": "We write custom WebGL shaders for glow, depth of field, and orbital camera movements with GSAP integration."
            },
            {
                "title": "4. GPU Profiling & Frame-Rate Budgeting",
                "desc": "We audit draw calls, texture memory, and battery consumption, ensuring a rock-solid 60 FPS experience."
            }
        ],
        "actual_projects": [
            {
                "status": "Live on valixis.tech",
                "title": "VALIXIS 3D Emblem Monolith",
                "desc": "Custom WebGL gyro-orbital monolith featuring dual-layer alpha textures and intelligent IntersectionObserver GPU throttling."
            },
            {
                "status": "Live Demo",
                "title": "HIYYA DINO MANDI Prehistoric Sanctuary",
                "desc": "Interactive dining experience integrating prehistoric 3D visual themes with Arabian family feast reservation flows."
            },
            {
                "status": "In Development",
                "title": "VALIXIS Gaming Studio Titles",
                "desc": "Exploratory interactive mechanics, physics simulations, and indie title concept prototypes."
            }
        ]
    }
]

def get_services_hub_html():
    canonical_url = "https://valixis.tech/services/"
    
    cards_html = ""
    for s in services_data:
        cards_html += f"""
        <article class="service-card" style="border-top: 3px solid {s['accent_color']};">
          <div class="card-badge" style="color: {s['accent_color']}; border-color: {s['accent_color']};">{s['badge']}</div>
          <h2 class="card-title">{s['service_name']}</h2>
          <p class="card-desc">{s['desc']}</p>
          
          <div class="card-highlights">
            <span class="highlight-label">Key Applications:</span>
            <ul class="highlight-list">
              {"".join([f"<li>&bull; {u['title']}</li>" for u in s['use_cases'][:3]])}
            </ul>
          </div>

          <div class="card-footer">
            <a href="{s['slug']}/" class="btn-card" style="background: rgba(255,255,255,0.05); color: {s['accent_color']}; border-color: {s['accent_color']};">
              <span>Explore Technical Architecture</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
          </div>
        </article>"""

    schema_json = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "@id": f"{canonical_url}#webpage",
                "url": canonical_url,
                "name": "Commercial Services & Engineering Solutions | VALIXIS",
                "description": "Explore the four core commercial engineering services offered by VALIXIS: AI Automation, Custom Software & Mobile, Web Platforms, and 3D Interactive Technology.",
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
                        "name": "Services",
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
  <title>Commercial Services &amp; Engineering Solutions | VALIXIS</title>
  <meta name="description" content="Explore the four primary commercial engineering services of VALIXIS: AI Automation, Custom Software &amp; Mobile Apps, Web Platforms, and 3D Interactive Computing.">
  <link rel="canonical" href="{canonical_url}">
  <meta name="robots" content="index, follow">
  
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="VALIXIS">
  <meta property="og:locale" content="en_US">
  <meta property="og:title" content="Commercial Services &amp; Engineering Solutions | VALIXIS">
  <meta property="og:description" content="Enterprise AI automation, cross-platform mobile systems, high-converting web apps, and immersive 3D technology.">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="https://valixis.tech/assets/valixis-logo-full.jpg">
  <meta property="og:image:width" content="1024">
  <meta property="og:image:height" content="1024">
  <meta property="og:image:alt" content="VALIXIS Official Emblem">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Commercial Services &amp; Engineering Solutions | VALIXIS">
  <meta name="twitter:description" content="Enterprise AI automation, cross-platform mobile systems, high-converting web apps, and immersive 3D technology.">
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
      background: radial-gradient(circle at 50% 10%, rgba(0, 217, 255, 0.12) 0%, transparent 50%),
                  radial-gradient(circle at 80% 70%, rgba(124, 58, 237, 0.10) 0%, transparent 50%),
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

    /* Hero */
    .hub-hero {{ padding: 48px 0 40px; text-align: center; border-bottom: 1px solid var(--border-color); }}
    .hub-badge {{
      display: inline-flex; align-items: center; gap: 8px;
      padding: 5px 14px; border-radius: 999px;
      background: rgba(0, 217, 255, 0.08); border: 1px solid rgba(0, 217, 255, 0.4);
      color: var(--valixis-cyan); font-family: var(--font-mono); font-size: 0.78rem;
      font-weight: 600; text-transform: uppercase; margin-bottom: 18px;
    }}
    .hub-title {{
      font-family: var(--font-display); font-size: 2.6rem; font-weight: 800;
      color: #FFF; margin-bottom: 16px; letter-spacing: -0.02em; line-height: 1.2;
    }}
    .hub-desc {{ font-size: 1.12rem; color: var(--text-muted); max-width: 780px; margin: 0 auto; line-height: 1.6; }}

    /* Grid */
    .services-grid {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 28px; padding: 48px 0; border-bottom: 1px solid var(--border-color);
    }}

    .service-card {{
      background: var(--bg-card); border: 1px solid var(--border-color);
      border-radius: 14px; padding: 28px; display: flex; flex-direction: column;
      transition: var(--transition-smooth);
    }}
    .service-card:hover {{ background: var(--bg-card-hover); transform: translateY(-4px); box-shadow: 0 12px 30px rgba(0,0,0,0.5); }}
    .card-badge {{
      display: inline-block; padding: 4px 10px; border-radius: 6px; border: 1px solid;
      font-family: var(--font-mono); font-size: 0.72rem; font-weight: 600; text-transform: uppercase;
      margin-bottom: 14px; width: fit-content;
    }}
    .card-title {{ font-family: var(--font-display); font-size: 1.28rem; color: #FFF; margin-bottom: 12px; }}
    .card-desc {{ font-size: 0.94rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 20px; flex-grow: 1; }}

    .card-highlights {{
      background: rgba(0, 0, 0, 0.25); border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 8px; padding: 14px; margin-bottom: 22px;
    }}
    .highlight-label {{ font-family: var(--font-mono); font-size: 0.74rem; text-transform: uppercase; color: var(--valixis-cyan); display: block; margin-bottom: 6px; }}
    .highlight-list {{ list-style: none; font-size: 0.86rem; color: var(--text-main); display: flex; flex-direction: column; gap: 4px; }}

    .btn-card {{
      display: inline-flex; align-items: center; justify-content: space-between;
      width: 100%; padding: 11px 18px; border-radius: 8px; font-size: 0.85rem; font-weight: 600;
      border: 1px solid; text-decoration: none; transition: var(--transition-smooth);
    }}
    .btn-card:hover {{ filter: brightness(1.2); }}

    /* Engagement Model */
    .framework-section {{ padding: 50px 0; border-bottom: 1px solid var(--border-color); }}
    .fw-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-top: 28px; }}
    .fw-card {{ background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 22px; }}
    .fw-title {{ font-family: var(--font-display); font-size: 1.05rem; color: #FFF; margin-bottom: 8px; }}
    .fw-desc {{ font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; }}

    /* CTA Section */
    .cta-banner {{ padding: 60px 0; text-align: center; }}
    .cta-card {{
      background: var(--bg-card); border: 1px solid var(--border-color);
      border-radius: 16px; padding: 48px 32px; max-width: 780px; margin: 0 auto;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
    }}
    .cta-title {{ font-family: var(--font-display); font-size: 1.8rem; color: #FFF; margin-bottom: 12px; }}
    .cta-desc {{ color: var(--text-muted); font-size: 1rem; margin-bottom: 28px; line-height: 1.6; }}

    /* Footer */
    .footer {{ padding: 32px 0; border-top: 1px solid var(--border-color); text-align: center; font-size: 0.84rem; color: var(--text-muted); }}
    .footer a {{ color: var(--text-muted); text-decoration: none; transition: var(--transition-smooth); }}
    .footer a:hover {{ color: var(--valixis-cyan); }}

    @media (max-width: 768px) {{
      .nav-links {{ display: none; }}
      .hub-title {{ font-size: 2rem; }}
      .services-grid {{ grid-template-columns: 1fr; }}
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
          <li><a href="../services/" class="nav-link active">Services</a></li>
          <li><a href="../client-sites/" class="nav-link">Showcase</a></li>
          <li><a href="../ecosystem/" class="nav-link">Ecosystem</a></li>
          <li><a href="../projects/" class="nav-link">Projects</a></li>
          <li><a href="../leadership/" class="nav-link">Leadership</a></li>
          <li><a href="../contact/" class="nav-link">Contact</a></li>
        </ul>
      </nav>

      <a href="../contact/" class="btn-cta">
        <span>Request Consultation</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      </a>
    </div>
  </header>

  <main>
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="../">Home</a> <span>/</span> <span style="color:#FFF;">Services</span>
      </nav>

      <section class="hub-hero">
        <div class="hub-badge">Commercial Engineering Solutions</div>
        <h1 class="hub-title">Specialized Technology Services for Modern Ventures</h1>
        <p class="hub-desc">
          We engineer high-performance software systems, intelligent automation pipelines, mobile-first applications, and interactive 3D platforms built on first-principles systems design.
        </p>
      </section>

      <!-- Services Grid -->
      <section class="services-grid">
        {cards_html}
      </section>

      <!-- Engagement Frameworks -->
      <section class="framework-section">
        <div style="text-align: center; max-width: 680px; margin: 0 auto 30px;">
          <span style="font-family: var(--font-mono); font-size: 0.78rem; text-transform: uppercase; color: var(--valixis-cyan);">Transparent Commercial Models</span>
          <h3 style="font-family: var(--font-display); font-size: 1.6rem; color: #FFF; margin-top: 6px;">How We Partner With Businesses</h3>
        </div>

        <div class="fw-grid">
          <div class="fw-card">
            <h4 class="fw-title">Rapid Sprint Pilot</h4>
            <p class="fw-desc">Fixed-scope 3 to 10-day sprints delivering a fully functional production module or MVP without long-term commitments.</p>
          </div>
          <div class="fw-card">
            <h4 class="fw-title">Dedicated Dev Pod</h4>
            <p class="fw-desc">Continuous monthly full-stack engineering pods deploying new features, API updates, and Git CI/CD pipelines.</p>
          </div>
          <div class="fw-card">
            <h4 class="fw-title">Commission-Free Systems</h4>
            <p class="fw-desc">Direct ordering and booking platforms eliminating heavy 22%-28% marketplace aggregator commissions.</p>
          </div>
          <div class="fw-card">
            <h4 class="fw-title">Managed Cloud Care &amp; SLA</h4>
            <p class="fw-desc">Cloudflare CDN hosting, SSL maintenance, uptime monitoring, and priority technical WhatsApp SLA support.</p>
          </div>
        </div>
      </section>

      <!-- CTA -->
      <section class="cta-banner">
        <div class="cta-card">
          <h3 class="cta-title">Discuss Your Project Requirements</h3>
          <p class="cta-desc">
            Connect directly with our engineering founders to review technical feasibility, architectural options, and turnaround times.
          </p>
          <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap;">
            <a href="../contact/" class="btn-cta">
              <span>Initiate Direct Inquiry</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
            <a href="../client-sites/" class="btn-card" style="width:auto; border-color:rgba(255,255,255,0.2); color:#FFF; background:rgba(255,255,255,0.05);">
              <span>Explore Live Showcase Demos</span>
            </a>
          </div>
        </div>
      </section>

    </div>
  </main>

  <footer class="footer">
    <div class="container">
      <p>&copy; 2026 VALIXIS. All rights reserved. &bull; <a href="../">valixis.tech</a> &bull; Independent Technology Venture</p>
    </div>
  </footer>

</body>
</html>
"""

print("Services data and hub generator prepared.")


# ===================================================================
# EXECUTION ENGINE FOR ALL BASE DIRECTORIES
# ===================================================================
for base in base_dirs:
    print(f"\n==========================================")
    print(f"BUILDING COMMERCIAL SERVICES IN: {base}")
    print(f"==========================================")

    # 1. Create services root directory
    services_dir = os.path.join(base, "services")
    os.makedirs(services_dir, exist_ok=True)

    # 2. Write Services Hub (services/index.html)
    hub_path = os.path.join(services_dir, "index.html")
    with open(hub_path, "w", encoding="utf-8") as f:
        f.write(get_services_hub_html())
    print("  [OK] Created services/index.html (Commercial Services Hub)")

    # 3. Write each of the 4 deep-dive service pages
    for s in services_data:
        s_dir = os.path.join(services_dir, s["slug"])
        os.makedirs(s_dir, exist_ok=True)
        s_path = os.path.join(s_dir, "index.html")
        page_html = get_service_page_html(
            slug=s["slug"],
            title=s["service_name"],
            service_name=s["service_name"],
            badge=s["badge"],
            desc=s["desc"],
            accent_color=s["accent_color"],
            glow_color=s["glow_color"],
            problems=s["problems"],
            use_cases=s["use_cases"],
            deliverables=s["deliverables"],
            tech_stack=s["tech_stack"],
            approach_steps=s["approach_steps"],
            actual_projects=s["actual_projects"]
        )
        with open(s_path, "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f"  [OK] Created services/{s['slug']}/index.html ({s['service_name']})")

    # 4. Inject Commercial Services Section into Homepage (index.html)
    hp_path = os.path.join(base, "index.html")
    if os.path.exists(hp_path):
        with open(hp_path, "r", encoding="utf-8") as f:
            hp = f.read()

        # Update Navigation to include Services
        if 'href="services/"' not in hp:
            hp = re.sub(
                r'(<nav class="nav-links">[\s\S]*?<a href="about/">About</a>)',
                r'\1\n      <a href="services/">Services</a>',
                hp
            )

        if 'class="mobile-drawer-link">Services</a>' not in hp:
            hp = re.sub(
                r'(<div class="mobile-drawer-links">[\s\S]*?<a href="about/" class="mobile-drawer-link">About</a>)',
                r'\1\n        <a href="services/" class="mobile-drawer-link">Services</a>',
                hp
            )

        if '<a href="services/">Services</a>' not in hp:
            hp = re.sub(
                r'(<div class="footer-subpages-nav"[\s\S]*?<a href="about/">About</a>)',
                r'\1 <span class="sep">&middot;</span> <a href="services/">Services</a>',
                hp
            )

        # Build Homepage Services Section Markup
        services_section_markup = """
    <!-- COMMERCIAL SERVICES SECTION (PHASE 3) -->
    <section id="services" class="section services-hub-section" style="padding: 80px 0; border-top: 1px solid rgba(255,255,255,0.08); background: radial-gradient(circle at 50% 0%, rgba(0, 217, 255, 0.05) 0%, transparent 60%);">
      <div class="container">
        <div style="text-align: center; max-width: 760px; margin: 0 auto 50px;">
          <span style="font-family: var(--font-mono); font-size: 0.8rem; text-transform: uppercase; color: #00D9FF; letter-spacing: 0.1em; display: block; margin-bottom: 10px;">Commercial Solutions &bull; Systems Engineering</span>
          <h2 style="font-family: var(--font-display); font-size: 2.2rem; color: #FFF; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 16px;">Core Commercial Engineering Services</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.6;">
            We engineer high-reliability digital platforms, intelligent agent pipelines, and custom software systems designed to solve operational bottlenecks and drive commercial growth.
          </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
          
          <div class="spotlight-card" style="padding: 30px; display: flex; flex-direction: column; border-top: 3px solid #00D9FF;">
            <div style="font-family: var(--font-mono); font-size: 0.72rem; color: #00D9FF; text-transform: uppercase; font-weight: 600; margin-bottom: 12px;">Cognitive Engineering</div>
            <h3 style="font-family: var(--font-display); font-size: 1.25rem; color: #FFF; margin-bottom: 10px;">AI Automation &amp; Intelligent Systems</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.55; margin-bottom: 20px; flex-grow: 1;">
              Autonomous multi-agent pipelines, intelligent document parsing, 24/7 lead qualification, and local model inference architectures.
            </p>
            <a href="services/ai-automation/" style="display: inline-flex; align-items: center; justify-content: space-between; font-size: 0.85rem; font-weight: 600; color: #00D9FF; text-decoration: none; padding: 10px 16px; border-radius: 8px; border: 1px solid rgba(0,217,255,0.3); background: rgba(0,217,255,0.06); transition: all 0.2s;">
              <span>Explore AI Solutions</span> &rarr;
            </a>
          </div>

          <div class="spotlight-card" style="padding: 30px; display: flex; flex-direction: column; border-top: 3px solid #3B82F6;">
            <div style="font-family: var(--font-mono); font-size: 0.72rem; color: #3B82F6; text-transform: uppercase; font-weight: 600; margin-bottom: 12px;">Systems &amp; Mobile</div>
            <h3 style="font-family: var(--font-display); font-size: 1.25rem; color: #FFF; margin-bottom: 10px;">Custom Software &amp; Mobile Apps</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.55; margin-bottom: 20px; flex-grow: 1;">
              High-performance cross-platform iOS &amp; Android mobile applications, internal telemetry dashboards, and cloud backend microservices.
            </p>
            <a href="services/software-mobile/" style="display: inline-flex; align-items: center; justify-content: space-between; font-size: 0.85rem; font-weight: 600; color: #3B82F6; text-decoration: none; padding: 10px 16px; border-radius: 8px; border: 1px solid rgba(59,130,246,0.3); background: rgba(59,130,246,0.06); transition: all 0.2s;">
              <span>Explore Mobile Systems</span> &rarr;
            </a>
          </div>

          <div class="spotlight-card" style="padding: 30px; display: flex; flex-direction: column; border-top: 3px solid #7C3AED;">
            <div style="font-family: var(--font-mono); font-size: 0.72rem; color: #7C3AED; text-transform: uppercase; font-weight: 600; margin-bottom: 12px;">Web &amp; Commerce</div>
            <h3 style="font-family: var(--font-display); font-size: 1.25rem; color: #FFF; margin-bottom: 10px;">Web Platforms &amp; Digital Experiences</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.55; margin-bottom: 20px; flex-grow: 1;">
              High-converting direct ordering web applications, 24/7 clinic booking portals, and commission-free digital storefronts with 1-click UPI checkout.
            </p>
            <a href="services/web-platforms/" style="display: inline-flex; align-items: center; justify-content: space-between; font-size: 0.85rem; font-weight: 600; color: #7C3AED; text-decoration: none; padding: 10px 16px; border-radius: 8px; border: 1px solid rgba(124,58,237,0.3); background: rgba(124,58,237,0.06); transition: all 0.2s;">
              <span>Explore Web Platforms</span> &rarr;
            </a>
          </div>

          <div class="spotlight-card" style="padding: 30px; display: flex; flex-direction: column; border-top: 3px solid #FF2ED6;">
            <div style="font-family: var(--font-mono); font-size: 0.72rem; color: #FF2ED6; text-transform: uppercase; font-weight: 600; margin-bottom: 12px;">Spatial &amp; Interactive</div>
            <h3 style="font-family: var(--font-display); font-size: 1.25rem; color: #FFF; margin-bottom: 10px;">3D, Gaming &amp; Interactive Tech</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.55; margin-bottom: 20px; flex-grow: 1;">
              Immersive browser-based 3D digital environments, spatial hospitality walkthroughs, interactive product configurators, and studio indie game titles.
            </p>
            <a href="services/3d-gaming-interactive/" style="display: inline-flex; align-items: center; justify-content: space-between; font-size: 0.85rem; font-weight: 600; color: #FF2ED6; text-decoration: none; padding: 10px 16px; border-radius: 8px; border: 1px solid rgba(255,46,214,0.3); background: rgba(255,46,214,0.06); transition: all 0.2s;">
              <span>Explore 3D &amp; Gaming</span> &rarr;
            </a>
          </div>

        </div>

        <div style="text-align: center; margin-top: 40px;">
          <a href="services/" style="display: inline-flex; align-items: center; gap: 8px; color: #FFF; text-decoration: none; font-size: 0.95rem; font-weight: 600; border: 1px solid rgba(255,255,255,0.2); padding: 12px 26px; border-radius: 999px; background: rgba(255,255,255,0.03); transition: all 0.2s;">
            <span>View Full Services Portfolio &amp; Engagement Models</span> &rarr;
          </a>
        </div>
      </div>
    </section>
"""

        # Inject right after four pillars section if not already present
        if 'id="services"' not in hp:
            hp = re.sub(
                r'(</section>\s*<!-- ECOSYSTEM SECTION -->)',
                r'\n' + services_section_markup + r'\n\1',
                hp
            )

        with open(hp_path, "w", encoding="utf-8") as f:
            f.write(hp)
        print("  [OK] Injected Commercial Services Section and Navigation links into index.html")

    # 5. Update Navigation on all Subpages (about, leadership, projects, ecosystem, contact, client-sites)
    subpages = [
        ("about/index.html", "../"),
        ("leadership/index.html", "../"),
        ("leadership/subhash-annam/index.html", "../../"),
        ("leadership/jyothsna-sri/index.html", "../../"),
        ("ecosystem/index.html", "../"),
        ("projects/index.html", "../"),
        ("contact/index.html", "../"),
        ("client-sites/index.html", "../"),
    ]

    for sub_rel, prefix in subpages:
        sub_p = os.path.join(base, sub_rel)
        if os.path.exists(sub_p):
            with open(sub_p, "r", encoding="utf-8") as f:
                content = f.read()

            services_link = f'{prefix}services/'
            if f'href="{services_link}"' not in content:
                # Add to nav-links
                content = re.sub(
                    rf'(<a href="{prefix}about/"[^>]*>About</a>\s*</li>)',
                    rf'\1\n          <li><a href="{services_link}" class="nav-link">Services</a></li>',
                    content
                )
                # For pages using plain <a> tags without <li>
                content = re.sub(
                    rf'(<nav class="nav-links">[\s\S]*?<a href="{prefix}about/"[^>]*>About</a>)',
                    rf'\1\n      <a href="{services_link}">Services</a>',
                    content
                )
                # Footer links
                content = re.sub(
                    rf'(<div class="footer-links">[\s\S]*?<a href="{prefix}about/">About</a>)',
                    rf'\1 <span class="sep">&middot;</span> <a href="{services_link}">Services</a>',
                    content
                )
                with open(sub_p, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"  [OK] Added Services navigation link to {sub_rel}")

    # 6. Update sitemap.xml with the 5 new Commercial Services routes
    sm_path = os.path.join(base, "sitemap.xml")
    if os.path.exists(sm_path):
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
    <priority>0.90</priority>
  </url>

  <!-- Service: Custom Software & Mobile Applications -->
  <url>
    <loc>https://valixis.tech/services/software-mobile/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.90</priority>
  </url>

  <!-- Service: Web Platforms & Digital Experiences -->
  <url>
    <loc>https://valixis.tech/services/web-platforms/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.90</priority>
  </url>

  <!-- Service: 3D, Gaming & Interactive Technology -->
  <url>
    <loc>https://valixis.tech/services/3d-gaming-interactive/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.90</priority>
  </url>

  <!-- Client Showcases Portal -->
  <url>
    <loc>https://valixis.tech/client-sites/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.90</priority>
  </url>

  <!-- About / Venture Profile -->
  <url>
    <loc>https://valixis.tech/about/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>

  <!-- Executive Leadership Overview -->
  <url>
    <loc>https://valixis.tech/leadership/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>

  <!-- Founder & CEO Profile: Subhash Annam -->
  <url>
    <loc>https://valixis.tech/leadership/subhash-annam/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>

  <!-- Co-Founder & CCO Profile: Jyothsna Sri -->
  <url>
    <loc>https://valixis.tech/leadership/jyothsna-sri/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>

  <!-- Software Ecosystem -->
  <url>
    <loc>https://valixis.tech/ecosystem/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.80</priority>
  </url>

  <!-- Projects & Lifecycle Tracker -->
  <url>
    <loc>https://valixis.tech/projects/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.80</priority>
  </url>

  <!-- Contact & Global Inquiries -->
  <url>
    <loc>https://valixis.tech/contact/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.80</priority>
  </url>

</urlset>
"""
        with open(sm_path, "w", encoding="utf-8") as f:
            f.write(sm_content)
        print("  [OK] Updated sitemap.xml with 14 canonical URLs (including 5 Services routes)")

print("\nPhase 3 Commercial Services architecture deployed successfully across both directories.")
