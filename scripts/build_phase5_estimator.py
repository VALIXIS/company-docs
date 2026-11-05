import os
import re
import json

base_dirs = [
    r"c:\Users\nagas\Documents\antigravity\resilient-heisenberg\VALIXIS WEBSITE",
    r"c:\Users\nagas\Documents\antigravity\resilient-heisenberg"
]

print("Building Phase 5: VALIXIS Interactive Project Scope Estimator...")

def get_estimator_page_html():
    canonical_url = "https://valixis.tech/estimate/"

    schema_json = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebApplication",
                "@id": f"{canonical_url}#app",
                "name": "VALIXIS Interactive Project Scope Estimator",
                "applicationCategory": "BusinessApplication",
                "operatingSystem": "All modern web browsers",
                "description": "Interactive project scope and complexity calculator for estimating custom software, AI automation pipelines, mobile apps, web platforms, and 3D systems.",
                "url": canonical_url,
                "provider": {
                    "@type": "Organization",
                    "@id": "https://valixis.tech/#organization",
                    "name": "VALIXIS",
                    "url": "https://valixis.tech"
                }
            },
            {
                "@type": "WebPage",
                "@id": f"{canonical_url}#webpage",
                "url": canonical_url,
                "name": "Interactive Project Scope Estimator | VALIXIS",
                "description": "Estimate architectural complexity, deliverables, and development timelines for your technology project.",
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
                        "name": "Project Scope Estimator",
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
  <title>Interactive Project Scope Estimator | VALIXIS</title>
  <meta name="description" content="Calculate project scope, architectural complexity, indicative turnaround, and development approaches for AI automation, mobile apps, web platforms, and custom software.">
  <link rel="canonical" href="{canonical_url}">
  <meta name="robots" content="index, follow">
  
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="VALIXIS">
  <meta property="og:locale" content="en_US">
  <meta property="og:title" content="Interactive Project Scope Estimator | VALIXIS">
  <meta property="og:description" content="Calculate project scope, architectural complexity, indicative turnaround, and development approaches for your technology project.">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="https://valixis.tech/assets/valixis-logo-full.jpg">
  <meta property="og:image:width" content="1024">
  <meta property="og:image:height" content="1024">
  <meta property="og:image:alt" content="VALIXIS Official Emblem">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Interactive Project Scope Estimator | VALIXIS">
  <meta name="twitter:description" content="Calculate project scope, architectural complexity, indicative turnaround, and development approaches for your technology project.">
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
      --valixis-cyan-glow: rgba(0, 217, 255, 0.4);
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
      background: radial-gradient(circle at 50% 12%, rgba(0, 217, 255, 0.12) 0%, transparent 60%),
                  radial-gradient(circle at 85% 80%, rgba(124, 58, 237, 0.10) 0%, transparent 50%),
                  #06090E;
      z-index: -1; pointer-events: none;
    }}

    .container {{ width: 100%; max-width: 960px; margin: 0 auto; padding: 0 24px; }}

    .navbar {{
      position: sticky; top: 0; z-index: 100;
      background: rgba(6, 9, 14, 0.82); backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-color); padding: 16px 0;
    }}
    .nav-wrapper {{ display: flex; align-items: center; justify-content: space-between; }}
    .brand-header {{ display: flex; align-items: center; text-decoration: none; }}
    .brand-lockup-img {{ height: 32px; width: auto; display: block; }}
    .nav-links {{ display: flex; gap: 22px; list-style: none; align-items: center; }}
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

    /* Estimator Header */
    .est-hero {{ padding: 40px 0 32px; text-align: center; }}
    .est-badge {{
      display: inline-flex; align-items: center; gap: 8px;
      padding: 5px 14px; border-radius: 999px;
      background: rgba(0, 217, 255, 0.08); border: 1px solid rgba(0, 217, 255, 0.4);
      color: var(--valixis-cyan); font-family: var(--font-mono); font-size: 0.78rem;
      font-weight: 600; text-transform: uppercase; margin-bottom: 16px;
    }}
    .est-heading {{
      font-family: var(--font-display); font-size: 2.4rem; font-weight: 800;
      color: #FFF; margin-bottom: 14px; letter-spacing: -0.02em; line-height: 1.2;
    }}
    .est-lead {{ font-size: 1.05rem; color: var(--text-muted); max-width: 680px; margin: 0 auto; line-height: 1.6; }}

    /* Stepper Progress Bar */
    .stepper-nav {{
      display: flex; justify-content: space-between; position: relative;
      margin: 32px 0 40px; padding: 0 10px;
    }}
    .stepper-track {{
      position: absolute; top: 18px; left: 10%; right: 10%; height: 2px;
      background: rgba(255, 255, 255, 0.1); z-index: 1;
    }}
    .stepper-track-fill {{
      position: absolute; top: 18px; left: 10%; height: 2px;
      background: linear-gradient(90deg, #00D9FF, #3B82F6); z-index: 2; width: 0%;
      transition: width 0.4s ease;
    }}
    .step-node {{
      position: relative; z-index: 3; display: flex; flex-direction: column;
      align-items: center; gap: 8px; cursor: pointer; background: transparent; border: none;
    }}
    .node-circle {{
      width: 38px; height: 38px; border-radius: 50%;
      background: #0D1117; border: 2px solid rgba(255, 255, 255, 0.2);
      display: flex; align-items: center; justify-content: center;
      font-family: var(--font-mono); font-size: 0.85rem; font-weight: 700; color: var(--text-muted);
      transition: all 0.3s ease;
    }}
    .step-node.active .node-circle {{
      border-color: #00D9FF; color: #00D9FF; box-shadow: 0 0 16px rgba(0, 217, 255, 0.45);
    }}
    .step-node.completed .node-circle {{
      background: #00D9FF; border-color: #00D9FF; color: #000;
    }}
    .node-label {{ font-family: var(--font-mono); font-size: 0.74rem; color: var(--text-muted); text-transform: uppercase; }}
    .step-node.active .node-label {{ color: #FFF; font-weight: 600; }}

    /* Wizard Card Box */
    .wizard-box {{
      background: var(--bg-card); border: 1px solid var(--border-color);
      border-radius: 16px; padding: 36px 32px; box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
      position: relative; min-height: 480px; display: flex; flex-direction: column;
      backdrop-filter: blur(16px); margin-bottom: 60px;
    }}

    .step-pane {{ display: none; flex-direction: column; flex-grow: 1; }}
    .step-pane.active {{ display: flex; animation: fadeInSlide 0.3s ease; }}

    @keyframes fadeInSlide {{
      from {{ opacity: 0; transform: translateY(8px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .step-title-wrap {{ margin-bottom: 24px; }}
    .step-num-eyebrow {{ font-family: var(--font-mono); font-size: 0.75rem; text-transform: uppercase; color: var(--valixis-cyan); display: block; margin-bottom: 6px; }}
    .step-h2 {{ font-family: var(--font-display); font-size: 1.45rem; color: #FFF; margin-bottom: 6px; }}
    .step-subtext {{ font-size: 0.90rem; color: var(--text-muted); }}

    /* Option Grid */
    .opt-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; margin-bottom: 30px; }}

    .opt-card {{
      background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-color);
      border-radius: 10px; padding: 18px 16px; cursor: pointer; text-align: left;
      transition: var(--transition-smooth); user-select: none; position: relative;
    }}
    .opt-card:hover {{ background: rgba(255, 255, 255, 0.06); border-color: rgba(255, 255, 255, 0.25); transform: translateY(-2px); }}
    
    /* Selected State */
    .opt-card.selected {{
      background: rgba(0, 217, 255, 0.08); border-color: var(--valixis-cyan);
      box-shadow: 0 4px 18px rgba(0, 217, 255, 0.25);
    }}
    .opt-card.selected::after {{
      content: '✓'; position: absolute; top: 12px; right: 14px;
      color: var(--valixis-cyan); font-family: var(--font-mono); font-weight: bold; font-size: 0.9rem;
    }}

    .opt-card-title {{ font-family: var(--font-display); font-size: 0.98rem; color: #FFF; margin-bottom: 4px; }}
    .opt-card-desc {{ font-size: 0.82rem; color: var(--text-muted); line-height: 1.4; }}

    /* Wizard Nav Actions */
    .wizard-controls {{
      display: flex; justify-content: space-between; align-items: center;
      margin-top: auto; padding-top: 24px; border-top: 1px solid var(--border-color);
    }}
    .btn-step-prev {{
      background: transparent; border: 1px solid var(--border-color); color: var(--text-muted);
      padding: 10px 20px; border-radius: 8px; font-size: 0.85rem; font-weight: 600; cursor: pointer;
      transition: all 0.2s;
    }}
    .btn-step-prev:hover {{ color: #FFF; border-color: rgba(255,255,255,0.3); }}

    .btn-step-next {{
      background: linear-gradient(135deg, #00D9FF 0%, #3B82F6 100%);
      border: none; color: #000; font-weight: 700; padding: 11px 26px; border-radius: 8px;
      font-size: 0.88rem; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 14px rgba(0, 217, 255, 0.3);
    }}
    .btn-step-next:hover {{ filter: brightness(1.15); transform: translateY(-1px); }}
    .btn-step-next:disabled {{ opacity: 0.4; cursor: not-allowed; filter: grayscale(1); transform: none; }}

    /* Results Screen */
    .result-pane {{ display: none; flex-direction: column; flex-grow: 1; }}
    .result-pane.active {{ display: flex; animation: fadeInSlide 0.3s ease; }}

    .result-summary-card {{
      background: rgba(0, 0, 0, 0.35); border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px; padding: 24px; margin-bottom: 24px;
    }}
    .result-row {{ display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }}
    .result-row:last-child {{ border-bottom: none; }}
    .res-label {{ font-family: var(--font-mono); font-size: 0.78rem; text-transform: uppercase; color: var(--text-muted); }}
    .res-val {{ font-family: var(--font-display); font-size: 1rem; color: #FFF; }}
    
    .badges-flex {{ display: flex; flex-wrap: wrap; gap: 6px; justify-content: flex-end; max-width: 60%; }}
    .res-badge {{ background: rgba(0, 217, 255, 0.08); border: 1px solid rgba(0, 217, 255, 0.25); color: #00D9FF; font-family: var(--font-mono); font-size: 0.72rem; padding: 3px 8px; border-radius: 4px; }}

    .approach-box {{
      background: rgba(124, 58, 237, 0.06); border: 1px solid rgba(124, 58, 237, 0.25);
      border-radius: 10px; padding: 18px 20px; margin-bottom: 24px;
    }}
    .approach-title {{ font-family: var(--font-mono); font-size: 0.76rem; text-transform: uppercase; color: #A78BFA; margin-bottom: 4px; }}
    .approach-desc {{ font-size: 0.92rem; color: #E2E8F0; line-height: 1.5; }}

    /* Pricing Charter Note */
    .pricing-note {{
      font-size: 0.82rem; color: var(--text-muted); background: rgba(255, 255, 255, 0.02);
      border-left: 3px solid #00D9FF; padding: 12px 16px; margin-bottom: 28px; line-height: 1.5;
    }}

    /* Action Buttons Row */
    .actions-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 16px; }}
    
    .btn-act {{
      display: inline-flex; align-items: center; justify-content: center; gap: 8px;
      padding: 12px 16px; border-radius: 8px; font-size: 0.84rem; font-weight: 700;
      border: 1px solid; cursor: pointer; text-decoration: none; transition: var(--transition-smooth);
      text-align: center;
    }}
    .btn-wa {{ background: #25D366; color: #000; border-color: #25D366; }}
    .btn-wa:hover {{ filter: brightness(1.15); transform: translateY(-2px); }}
    
    .btn-copy {{ background: rgba(255, 255, 255, 0.06); color: #FFF; border-color: var(--border-color); }}
    .btn-copy:hover {{ background: rgba(255, 255, 255, 0.1); border-color: rgba(255,255,255,0.3); }}

    .btn-email {{ background: rgba(59, 130, 246, 0.12); color: #60A5FA; border-color: rgba(59, 130, 246, 0.35); }}
    .btn-email:hover {{ background: rgba(59, 130, 246, 0.22); }}

    .btn-consult {{ background: rgba(0, 217, 255, 0.12); color: #00D9FF; border-color: rgba(0, 217, 255, 0.35); }}
    .btn-consult:hover {{ background: rgba(0, 217, 255, 0.22); }}

    .copy-toast {{
      display: none; text-align: center; font-family: var(--font-mono);
      font-size: 0.78rem; color: #10B981; margin-top: 8px;
    }}

    /* Footer */
    .footer {{ padding: 32px 0; border-top: 1px solid var(--border-color); text-align: center; font-size: 0.84rem; color: var(--text-muted); }}
    .footer a {{ color: var(--text-muted); text-decoration: none; }}
    .footer a:hover {{ color: var(--valixis-cyan); }}

    @media (max-width: 768px) {{
      .nav-links {{ display: none; }}
      .est-heading {{ font-size: 1.8rem; }}
      .wizard-box {{ padding: 24px 18px; }}
      .actions-grid {{ grid-template-columns: 1fr; }}
      .badges-flex {{ max-width: 100%; justify-content: flex-start; margin-top: 6px; }}
      .result-row {{ flex-direction: column; align-items: flex-start; gap: 4px; }}
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
          <li><a href="../work/" class="nav-link">Work</a></li>
          <li><a href="../estimate/" class="nav-link active">Estimate</a></li>
          <li><a href="../client-sites/" class="nav-link">Showcase</a></li>
          <li><a href="../ecosystem/" class="nav-link">Ecosystem</a></li>
          <li><a href="../projects/" class="nav-link">Projects</a></li>
          <li><a href="../contact/" class="nav-link">Contact</a></li>
        </ul>
      </nav>

      <a href="../contact/" class="btn-cta">
        <span>Book Consultation</span>
      </a>
    </div>
  </header>

  <main>
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="../">Home</a> <span>/</span> <span style="color:#FFF;">Project Scope Estimator</span>
      </nav>

      <section class="est-hero">
        <div class="est-badge">Interactive Architecture Calculator</div>
        <h1 class="est-heading">Interactive Project Scope Estimator</h1>
        <p class="est-lead">
          Configure your technical requirements to generate an indicative complexity profile, development timeline, and structured inquiry brief in under 60 seconds.
        </p>
      </section>

      <!-- Step Progress Bar -->
      <div class="stepper-nav">
        <div class="stepper-track"></div>
        <div class="stepper-track-fill" id="stepperFill"></div>
        
        <button class="step-node active" id="node1" onclick="jumpToStep(1)">
          <div class="node-circle">1</div>
          <span class="node-label">Project Type</span>
        </button>

        <button class="step-node" id="node2" onclick="jumpToStep(2)">
          <div class="node-circle">2</div>
          <span class="node-label">Requirements</span>
        </button>

        <button class="step-node" id="node3" onclick="jumpToStep(3)">
          <div class="node-circle">3</div>
          <span class="node-label">Timeline</span>
        </button>

        <button class="step-node" id="node4" onclick="jumpToStep(4)">
          <div class="node-circle">4</div>
          <span class="node-label">Scope Brief</span>
        </button>
      </div>

      <!-- Wizard Box -->
      <div class="wizard-box">
        
        <!-- STEP 1: PROJECT TYPE -->
        <div class="step-pane active" id="step1">
          <div class="step-title-wrap">
            <span class="step-num-eyebrow">Step 1 of 3</span>
            <h2 class="step-h2">What type of project are you building?</h2>
            <p class="step-subtext">Select the primary system category that best matches your target application.</p>
          </div>

          <div class="opt-grid" id="typeGrid">
            <div class="opt-card" tabindex="0" onclick="selectType(this, 'AI Agent / Automation', 3)">
              <div class="opt-card-title">AI Agent / Automation</div>
              <p class="opt-card-desc">Autonomous multi-agent pipelines, cognitive document intelligence, or RAG search.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="selectType(this, 'Mobile Application', 3)">
              <div class="opt-card-title">Mobile Application</div>
              <p class="opt-card-desc">Cross-platform iOS and Android mobile app built with Flutter or native protocols.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="selectType(this, 'Web Application', 2)">
              <div class="opt-card-title">Web Application</div>
              <p class="opt-card-desc">Interactive SaaS platform, customer portal, or dynamic full-stack dashboard.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="selectType(this, 'Business Website', 1)">
              <div class="opt-card-title">Business Website</div>
              <p class="opt-card-desc">High-converting commercial storefront, restaurant direct ordering, or clinic booking.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="selectType(this, 'Enterprise Platform', 4)">
              <div class="opt-card-title">Enterprise Platform</div>
              <p class="opt-card-desc">Multi-tenant backend, complex role-based access control, and telemetry pipelines.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="selectType(this, '3D Interactive Experience', 3)">
              <div class="opt-card-title">3D Interactive Experience</div>
              <p class="opt-card-desc">Hardware-accelerated browser 3D, spatial product configurator, or virtual tour.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="selectType(this, 'Gaming Project', 4)">
              <div class="opt-card-title">Gaming Project</div>
              <p class="opt-card-desc">Custom interactive game prototype, WebGL canvas mechanics, or physics engine.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="selectType(this, 'Custom Project', 2)">
              <div class="opt-card-title">Custom Project</div>
              <p class="opt-card-desc">Bespoke system architecture or hybrid multi-platform engineering challenge.</p>
            </div>
          </div>

          <div class="wizard-controls">
            <div></div>
            <button class="btn-step-next" id="btnNext1" disabled onclick="nextStep(2)">Continue to Requirements &rarr;</button>
          </div>
        </div>

        <!-- STEP 2: REQUIREMENTS -->
        <div class="step-pane" id="step2">
          <div class="step-title-wrap">
            <span class="step-num-eyebrow">Step 2 of 3</span>
            <h2 class="step-h2">Select key architectural requirements</h2>
            <p class="step-subtext">Choose all technical modules and integrations your system will need. Multiple selections allowed.</p>
          </div>

          <div class="opt-grid" id="reqGrid">
            <div class="opt-card" tabindex="0" onclick="toggleReq(this, 'Authentication & Access Control')">
              <div class="opt-card-title">Authentication</div>
              <p class="opt-card-desc">Secure JWT, OAuth, social login, or multi-tenant user access roles.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="toggleReq(this, 'Admin Dashboard')">
              <div class="opt-card-title">Admin Dashboard</div>
              <p class="opt-card-desc">Centralized control center for managing orders, users, metrics, and content.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="toggleReq(this, 'Payment Gateway & Checkout')">
              <div class="opt-card-title">Payment Gateway</div>
              <p class="opt-card-desc">Direct checkout flow supporting UPI, credit cards, or international Stripe.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="toggleReq(this, 'AI Integration & LLMs')">
              <div class="opt-card-title">AI Integration</div>
              <p class="opt-card-desc">LLM agents, vector embeddings, local model inference, or vision analysis.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="toggleReq(this, 'Third-Party APIs & Webhooks')">
              <div class="opt-card-title">Third-Party APIs</div>
              <p class="opt-card-desc">Integration with external CRMs, ERPs, shipping, or custom data feeds.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="toggleReq(this, 'Real-Time Data & WebSockets')">
              <div class="opt-card-title">Real-Time Data</div>
              <p class="opt-card-desc">Live status updates, telemetry feeds, instant messaging, or WebSockets.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="toggleReq(this, 'Database Architecture (PostgreSQL/RLS)')">
              <div class="opt-card-title">Database Architecture</div>
              <p class="opt-card-desc">Relational PostgreSQL schema with Row Level Security and indexing.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="toggleReq(this, 'Cloud Infrastructure & CDN')">
              <div class="opt-card-title">Cloud Infrastructure</div>
              <p class="opt-card-desc">High-speed global edge caching, SSL, Docker containers, and CI/CD pipelines.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="toggleReq(this, 'Automated Notifications')">
              <div class="opt-card-title">Notifications</div>
              <p class="opt-card-desc">Automated alerts via WhatsApp Business, Telegram, SMS, or transactional email.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="toggleReq(this, 'Custom CMS & Content Editor')">
              <div class="opt-card-title">Custom CMS</div>
              <p class="opt-card-desc">Intuitive portal for non-technical team members to edit menus, blogs, or items.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="toggleReq(this, 'Telemetry & Analytics')">
              <div class="opt-card-title">Analytics</div>
              <p class="opt-card-desc">Privacy-first conversion tracking, error telemetry, and performance monitors.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="toggleReq(this, 'Security & Encryption')">
              <div class="opt-card-title">Security &amp; Hardening</div>
              <p class="opt-card-desc">OWASP compliance, input sanitization, CSRF mitigation, and secret auditing.</p>
            </div>
          </div>

          <div class="wizard-controls">
            <button class="btn-step-prev" onclick="jumpToStep(1)">&larr; Back</button>
            <button class="btn-step-next" id="btnNext2" onclick="nextStep(3)">Continue to Timeline &rarr;</button>
          </div>
        </div>

        <!-- STEP 3: TIMELINE -->
        <div class="step-pane" id="step3">
          <div class="step-title-wrap">
            <span class="step-num-eyebrow">Step 3 of 3</span>
            <h2 class="step-h2">What is your targeted delivery timeline?</h2>
            <p class="step-subtext">Select the timeframe that best aligns with your business launch milestones.</p>
          </div>

          <div class="opt-grid" id="timeGrid">
            <div class="opt-card" tabindex="0" onclick="selectTimeline(this, 'Urgent / 2 Weeks', 'Fast-Track Rapid Sprint')">
              <div class="opt-card-title">Urgent / 2 Weeks</div>
              <p class="opt-card-desc">Fast-track rapid sprint delivering a core functional module or pilot MVP.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="selectTimeline(this, 'Approximately 1 Month', 'Standard Milestone Sprint')">
              <div class="opt-card-title">Approximately 1 Month</div>
              <p class="opt-card-desc">Balanced cadence for a complete responsive web application or portal.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="selectTimeline(this, '2–3 Months', 'Multi-Phase Architectural Build')">
              <div class="opt-card-title">2–3 Months</div>
              <p class="opt-card-desc">Comprehensive mobile app or multi-system enterprise integration.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="selectTimeline(this, 'Long-Term Development', 'Phased Product Roadmap')">
              <div class="opt-card-title">Long-Term Development</div>
              <p class="opt-card-desc">Multi-quarter technical roadmap with iterative production releases.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="selectTimeline(this, 'Ongoing Engineering Partnership', 'Dedicated Dev Pod Retainer')">
              <div class="opt-card-title">Ongoing Partnership</div>
              <p class="opt-card-desc">Retained full-stack engineering pod managing continuous deployments.</p>
            </div>
            <div class="opt-card" tabindex="0" onclick="selectTimeline(this, 'Not Sure Yet', 'Exploratory Technical Discovery')">
              <div class="opt-card-title">Not Sure Yet</div>
              <p class="opt-card-desc">Require initial architectural consultation to define scope and milestones.</p>
            </div>
          </div>

          <div class="wizard-controls">
            <button class="btn-step-prev" onclick="jumpToStep(2)">&larr; Back</button>
            <button class="btn-step-next" id="btnNext3" disabled onclick="calculateScope()">Generate Scope Brief &rarr;</button>
          </div>
        </div>

        <!-- STEP 4: RESULT SCREEN -->
        <div class="result-pane" id="step4">
          <div class="step-title-wrap">
            <span class="step-num-eyebrow">Calculated Scope &bull; Summary Brief</span>
            <h2 class="step-h2">Architectural Assessment Summary</h2>
            <p class="step-subtext">Review your generated project scope profile below. You can copy the brief or send it directly for a rapid quotation.</p>
          </div>

          <div class="result-summary-card">
            <div class="result-row">
              <span class="res-label">Selected Project Type:</span>
              <span class="res-val" id="resType">AI Agent / Automation</span>
            </div>
            <div class="result-row">
              <span class="res-label">Architectural Modules:</span>
              <div class="badges-flex" id="resReqList">
                <span class="res-badge">None Selected</span>
              </div>
            </div>
            <div class="result-row">
              <span class="res-label">Indicative Complexity:</span>
              <span class="res-val" id="resComplexity" style="color:#00D9FF;">Moderate Complexity</span>
            </div>
            <div class="result-row">
              <span class="res-label">Target Delivery Timeline:</span>
              <span class="res-val" id="resTimeline">Approximately 1 Month</span>
            </div>
          </div>

          <div class="approach-box">
            <div class="approach-title">Recommended Engineering Approach</div>
            <p class="approach-desc" id="resApproach">
              Rapid 3 to 10-day foundational sprint pilot focusing on deterministic core modules, followed by incremental integration milestones.
            </p>
          </div>

          <div class="pricing-note">
            <strong>Transparent Commercial Notice:</strong> Indicative estimates align with VALIXIS Services Charter tiers (Founder Pilots from ₹18,000; Monthly Engineering Pods from ₹60,000/mo). Exact pricing and milestones are confirmed upon technical requirements review. No guaranteed pricing without finalized specification.
          </div>

          <div class="actions-grid">
            <button class="btn-act btn-copy" onclick="copyScopeBrief()">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
              <span>1. Copy Scope</span>
            </button>

            <a href="#" id="waLink" target="_blank" rel="noopener noreferrer" class="btn-act btn-wa">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
              <span>2. Send WhatsApp</span>
            </a>

            <a href="#" id="emailLink" class="btn-act btn-email">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              <span>3. Send Email</span>
            </a>

            <a href="../contact/" class="btn-act btn-consult">
              <span>4. Book Strategy Call</span>
            </a>
          </div>

          <div class="copy-toast" id="copyToast">&#10003; Project Scope copied to clipboard! Ready to paste.</div>

          <div style="text-align: center; margin-top: 24px;">
            <button onclick="resetCalculator()" style="background: none; border: none; color: var(--text-muted); font-family: var(--font-mono); font-size: 0.82rem; cursor: pointer; text-decoration: underline;">
              &circlearrowleft; Start Over / Recalculate
            </button>
          </div>
        </div>

      </div>
    </div>
  </main>

  <footer class="footer">
    <div class="container">
      <p>&copy; 2026 VALIXIS. All rights reserved. &bull; <a href="../">valixis.tech</a> &bull; Independent Technology Venture</p>
    </div>
  </footer>

  <script>
    // State
    let selectedType = "";
    let typeWeight = 2;
    let selectedReqs = new Set();
    let selectedTimeline = "";
    let timelineApproach = "";
    let currentStep = 1;

    function selectType(el, name, weight) {{
      document.querySelectorAll('#typeGrid .opt-card').forEach(c => c.classList.remove('selected'));
      el.classList.add('selected');
      selectedType = name;
      typeWeight = weight;
      document.getElementById('btnNext1').disabled = false;

      // Smart recommend based on type
      if (name.includes('AI') && selectedReqs.size === 0) {{
        highlightDefaultReqs(['AI Integration & LLMs', 'Third-Party APIs & Webhooks', 'Real-Time Data & WebSockets']);
      }} else if (name.includes('Mobile') && selectedReqs.size === 0) {{
        highlightDefaultReqs(['Authentication & Access Control', 'Automated Notifications', 'Database Architecture (PostgreSQL/RLS)']);
      }} else if (name.includes('Business Website') && selectedReqs.size === 0) {{
        highlightDefaultReqs(['Payment Gateway & Checkout', 'Automated Notifications', 'Cloud Infrastructure & CDN']);
      }}
    }}

    function highlightDefaultReqs(keys) {{
      document.querySelectorAll('#reqGrid .opt-card').forEach(card => {{
        const title = card.querySelector('.opt-card-title').textContent.trim();
        for (const k of keys) {{
          if (k.toLowerCase().includes(title.toLowerCase())) {{
            card.classList.add('selected');
            selectedReqs.add(k);
          }}
        }}
      }});
    }}

    function toggleReq(el, name) {{
      if (selectedReqs.has(name)) {{
        selectedReqs.delete(name);
        el.classList.remove('selected');
      }} else {{
        selectedReqs.add(name);
        el.classList.add('selected');
      }}
    }}

    function selectTimeline(el, timeName, approach) {{
      document.querySelectorAll('#timeGrid .opt-card').forEach(c => c.classList.remove('selected'));
      el.classList.add('selected');
      selectedTimeline = timeName;
      timelineApproach = approach;
      document.getElementById('btnNext3').disabled = false;
    }}

    function nextStep(step) {{
      jumpToStep(step);
    }}

    function jumpToStep(step) {{
      if (step === 2 && !selectedType) return;
      if (step === 3 && !selectedType) return;
      if (step === 4 && (!selectedType || !selectedTimeline)) return;

      currentStep = step;

      // Update panes
      document.querySelectorAll('.step-pane, .result-pane').forEach(p => p.classList.remove('active'));
      if (step <= 3) {{
        document.getElementById('step' + step).classList.add('active');
      }} else {{
        document.getElementById('step4').classList.add('active');
      }}

      // Update stepper track & circles
      const fill = document.getElementById('stepperFill');
      const pct = ((step - 1) / 3) * 80;
      fill.style.width = pct + '%';

      for (let i = 1; i <= 4; i++) {{
        const node = document.getElementById('node' + i);
        node.classList.remove('active', 'completed');
        if (i < step) {{
          node.classList.add('completed');
        }} else if (i === step) {{
          node.classList.add('active');
        }}
      }}
    }}

    function calculateScope() {{
      const totalPoints = typeWeight + selectedReqs.size;
      let complexity = "Foundational Complexity";
      let approach = "Fixed-scope 3 to 10-day foundational sprint pilot focusing on deterministic core modules, followed by optional milestone sprints.";

      if (totalPoints >= 11) {{
        complexity = "Enterprise-Scale Architecture";
        approach = "Phased multi-milestone enterprise engineering program or dedicated monthly engineering pod with continuous CI/CD releases.";
      }} else if (totalPoints >= 7) {{
        complexity = "Advanced System Architecture";
        approach = "Multi-phase full-stack build across 4 to 8 weeks with rigorous API contract design, automated test suites, and staging verification.";
      }} else if (totalPoints >= 4) {{
        complexity = "Moderate Complexity";
        approach = "Standard 2 to 4-week structured milestone sprint delivering end-to-end user workflows, payment integration, and cloud CDN hosting.";
      }}

      // Populate Result Screen
      document.getElementById('resType').textContent = selectedType || "Custom Project";
      document.getElementById('resComplexity').textContent = complexity;
      document.getElementById('resTimeline').textContent = selectedTimeline || "Flexible Discovery";
      document.getElementById('resApproach').textContent = approach;

      // Badges
      const reqContainer = document.getElementById('resReqList');
      reqContainer.innerHTML = '';
      if (selectedReqs.size === 0) {{
        reqContainer.innerHTML = '<span class="res-badge">Core Architecture Only</span>';
      }} else {{
        selectedReqs.forEach(r => {{
          const b = document.createElement('span');
          b.className = 'res-badge';
          b.textContent = r;
          reqContainer.appendChild(b);
        }});
      }}

      // Build safe formatted text message
      const reqListStr = selectedReqs.size > 0 ? Array.from(selectedReqs).join(', ') : 'Core Architecture';
      const briefText = `Hello VALIXIS Team,\n\nI have generated a preliminary project scope on valixis.tech:\n\n• Project Type: ${{selectedType}}\n• Key Requirements: ${{reqListStr}}\n• Target Timeline: ${{selectedTimeline}}\n• Estimated Complexity: ${{complexity}}\n\nI would like to discuss technical feasibility, deliverables, and a formal proposal.\n\nBest regards.`;

      // Safe URL encoded links
      const waUrl = `https://wa.me/919603416707?text=${{encodeURIComponent(briefText)}}`;
      document.getElementById('waLink').href = waUrl;

      const mailtoUrl = `mailto:official.valixis@gmail.com?subject=${{encodeURIComponent('Project Scope Inquiry: ' + selectedType)}}&body=${{encodeURIComponent(briefText)}}`;
      document.getElementById('emailLink').href = mailtoUrl;

      // Transition to Step 4
      jumpToStep(4);
    }}

    function copyScopeBrief() {{
      const reqListStr = selectedReqs.size > 0 ? Array.from(selectedReqs).join(', ') : 'Core Architecture';
      const briefText = `VALIXIS PROJECT SCOPE BRIEF\n============================\nProject Type: ${{selectedType}}\nArchitectural Requirements: ${{reqListStr}}\nTarget Timeline: ${{selectedTimeline}}\nIndicative Complexity: ${{document.getElementById('resComplexity').textContent}}\nRecommended Approach: ${{document.getElementById('resApproach').textContent}}\nGenerated via: https://valixis.tech/estimate/`;

      navigator.clipboard.writeText(briefText).then(() => {{
        const toast = document.getElementById('copyToast');
        toast.style.display = 'block';
        setTimeout(() => {{ toast.style.display = 'none'; }}, 3500);
      }}).catch(() => {{
        alert('Scope copied to clipboard.');
      }});
    }}

    function resetCalculator() {{
      selectedType = "";
      typeWeight = 2;
      selectedReqs.clear();
      selectedTimeline = "";
      timelineApproach = "";

      document.querySelectorAll('.opt-card').forEach(c => c.classList.remove('selected'));
      document.getElementById('btnNext1').disabled = true;
      document.getElementById('btnNext3').disabled = true;
      jumpToStep(1);
    }}

    // Accessible keyboard interactions
    document.addEventListener('keydown', (e) => {{
      if ((e.key === 'Enter' || e.key === ' ') && e.target.classList.contains('opt-card')) {{
        e.preventDefault();
        e.target.click();
      }}
    }});
  </script>

</body>
</html>
"""

print("Estimator template ready.")


# ===================================================================
# EXECUTION ENGINE FOR PHASE 5
# ===================================================================
for base in base_dirs:
    print(f"\n==========================================")
    print(f"DEPLOYING PROJECT SCOPE ESTIMATOR IN: {base}")
    print(f"==========================================")

    # 1. Create estimate directory
    est_dir = os.path.join(base, "estimate")
    os.makedirs(est_dir, exist_ok=True)

    # 2. Write estimate/index.html
    est_path = os.path.join(est_dir, "index.html")
    with open(est_path, "w", encoding="utf-8") as f:
        f.write(get_estimator_page_html())
    print("  [OK] Created estimate/index.html (Interactive Project Scope Estimator)")

    # 3. Inject Scope Estimator Banner on Homepage (index.html)
    hp_path = os.path.join(base, "index.html")
    if os.path.exists(hp_path):
        with open(hp_path, "r", encoding="utf-8") as f:
            hp = f.read()

        # Update Navigation to include Estimate
        if 'href="estimate/"' not in hp:
            hp = re.sub(
                r'(<nav class="nav-links">[\s\S]*?<a href="work/">Work</a>)',
                r'\1\n      <a href="estimate/">Estimate</a>',
                hp
            )

        if 'class="mobile-drawer-link">Estimate</a>' not in hp:
            hp = re.sub(
                r'(<div class="mobile-drawer-links">[\s\S]*?<a href="work/" class="mobile-drawer-link">Work</a>)',
                r'\1\n        <a href="estimate/" class="mobile-drawer-link">Estimate</a>',
                hp
            )

        if '<a href="estimate/">Estimate</a>' not in hp:
            hp = re.sub(
                r'(<div class="footer-subpages-nav"[\s\S]*?<a href="work/">Work</a>)',
                r'\1 <span class="sep">&middot;</span> <a href="estimate/">Estimate</a>',
                hp
            )

        # Estimator Spotlight Section Markup
        estimator_banner_markup = """
    <!-- INTERACTIVE ESTIMATOR SPOTLIGHT SECTION (PHASE 5) -->
    <section id="estimate-spotlight" class="section estimator-cta-section" style="padding: 70px 0; border-top: 1px solid rgba(255,255,255,0.08); background: radial-gradient(circle at 50% 50%, rgba(0, 217, 255, 0.08) 0%, transparent 70%);">
      <div class="container">
        <div class="spotlight-card" style="padding: 48px 36px; text-align: center; max-width: 880px; margin: 0 auto; border: 1px solid rgba(0, 217, 255, 0.35); box-shadow: 0 16px 40px rgba(0, 217, 255, 0.15);">
          <span style="font-family: var(--font-mono); font-size: 0.78rem; text-transform: uppercase; color: #00D9FF; letter-spacing: 0.1em; display: inline-block; margin-bottom: 12px; background: rgba(0,217,255,0.08); border: 1px solid rgba(0,217,255,0.3); padding: 4px 12px; border-radius: 999px;">
            Interactive Architecture Estimator
          </span>
          <h2 style="font-family: var(--font-display); font-size: 2.1rem; color: #FFF; font-weight: 800; margin-bottom: 14px; letter-spacing: -0.02em;">
            Calculate Your Project Scope &amp; Complexity
          </h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.6; max-width: 680px; margin: 0 auto 28px;">
            Select your project type, choose architectural modules (Authentication, Payments, AI, Databases), and get an instant complexity profile, recommended methodology, and formatted WhatsApp/Email scope brief.
          </p>
          <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
            <a href="estimate/" style="display: inline-flex; align-items: center; gap: 8px; padding: 12px 28px; border-radius: 8px; font-size: 0.95rem; font-weight: 700; color: #000; background: linear-gradient(135deg, #00D9FF 0%, #3B82F6 100%); border: none; text-decoration: none; box-shadow: 0 4px 16px rgba(0,217,255,0.4); transition: all 0.2s;">
              <span>Launch 60-Second Estimator</span> &rarr;
            </a>
            <a href="services/" style="display: inline-flex; align-items: center; gap: 8px; padding: 12px 24px; border-radius: 8px; font-size: 0.95rem; font-weight: 600; color: #FFF; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.18); text-decoration: none; transition: all 0.2s;">
              <span>Explore Service Pillars</span>
            </a>
          </div>
        </div>
      </div>
    </section>
"""

        if 'id="estimate-spotlight"' not in hp:
            hp = re.sub(
                r'(</section>\s*<!-- ECOSYSTEM SECTION -->)',
                r'\n' + estimator_banner_markup + r'\n\1',
                hp
            )

        with open(hp_path, "w", encoding="utf-8") as f:
            f.write(hp)
        print("  [OK] Injected Project Scope Estimator Spotlight Section into index.html")

    # 4. Update Navigation across all Subpages to include Estimate
    all_subpage_targets = [
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
        ("work/index.html", "../"),
        ("work/rose-cafe/index.html", "../../"),
        ("work/novel-hotel/index.html", "../../"),
        ("work/hiyya-dino-mandi/index.html", "../../"),
    ]

    for sub_rel, prefix in all_subpage_targets:
        sub_p = os.path.join(base, sub_rel)
        if os.path.exists(sub_p):
            with open(sub_p, "r", encoding="utf-8") as f:
                content = f.read()

            est_link = f'{prefix}estimate/'
            if f'href="{est_link}"' not in content:
                # Add after work link
                content = re.sub(
                    rf'(<a href="{prefix}work/"[^>]*>Work</a>\s*</li>)',
                    rf'\1\n          <li><a href="{est_link}" class="nav-link">Estimate</a></li>',
                    content
                )
                content = re.sub(
                    rf'(<nav class="nav-links">[\s\S]*?<a href="{prefix}work/"[^>]*>Work</a>)',
                    rf'\1\n      <a href="{est_link}">Estimate</a>',
                    content
                )
                content = re.sub(
                    rf'(<div class="footer-links">[\s\S]*?<a href="{prefix}work/">Work</a>)',
                    rf'\1 <span class="sep">&middot;</span> <a href="{est_link}">Estimate</a>',
                    content
                )
                with open(sub_p, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"  [OK] Added Estimate link to {sub_rel}")

    # 5. Update sitemap.xml with /estimate/
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

  <!-- Interactive Project Scope Estimator -->
  <url>
    <loc>https://valixis.tech/estimate/</loc>
    <lastmod>2026-11-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
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
        print("  [OK] Updated sitemap.xml with 19 canonical URLs (including /estimate/)")

print("\nPhase 5 Project Scope Estimator deployed successfully across both directories.")
