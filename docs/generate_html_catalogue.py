import os
import base64

with open('valixis_horizontal_lockup.png', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VALIXIS &mdash; Official Services Catalogue, Rate Card &amp; Legal Charter</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #0f172a;
      --primary-light: #1e293b;
      --accent: #0284c7;
      --accent-dark: #0369a1;
      --text: #334155;
      --text-dark: #0f172a;
      --text-muted: #64748b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #cbd5e1;
      --border-light: #e2e8f0;
      --success: #059669;
      --success-bg: #ecfdf5;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: #e2e8f0;
      color: var(--text);
      line-height: 1.5;
      font-size: 13px;
      padding: 24px 16px;
    }}

    /* Top Control Bar (Hidden on Print) */
    .action-bar {{
      max-width: 920px;
      margin: 0 auto 20px auto;
      background: var(--primary);
      color: #fff;
      padding: 14px 24px;
      border-radius: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.25);
    }}

    .action-bar h2 {{
      font-size: 14.5px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .action-bar .badge {{
      background: rgba(2, 132, 199, 0.25);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.4);
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 11px;
      font-family: 'JetBrains Mono', monospace;
    }}

    .action-bar .btn-group {{
      display: flex;
      gap: 10px;
    }}

    .btn {{
      padding: 8px 18px;
      font-size: 12.5px;
      font-weight: 600;
      border-radius: 8px;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
      text-decoration: none;
    }}

    .btn-primary {{
      background: var(--accent);
      color: white;
    }}

    .btn-primary:hover {{
      background: var(--accent-dark);
      transform: translateY(-1px);
    }}

    /* Document Wrapper */
    .doc-container {{
      max-width: 920px;
      margin: 0 auto;
      background: var(--card-bg);
      border-radius: 16px;
      box-shadow: 0 15px 35px -5px rgba(0, 0, 0, 0.1);
      overflow: hidden;
      border: 1px solid var(--border);
    }}

    .doc-page {{
      padding: 44px 50px;
      position: relative;
      background: white;
    }}

    .doc-page:not(:last-child) {{
      border-bottom: 2px dashed var(--border);
    }}

    /* Running Header in Print */
    .running-header {{
      display: flex;
      justify-content: space-between;
      font-size: 9px;
      font-weight: 700;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border-light);
      padding-bottom: 6px;
      margin-bottom: 18px;
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Header Lockup */
    .header-lockup {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 16px;
      border-bottom: 2px solid var(--primary);
      margin-bottom: 20px;
    }}

    .logo-img {{
      height: 38px;
      width: auto;
      object-fit: contain;
    }}

    .corp-details {{
      text-align: right;
      font-size: 11px;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    .corp-details strong {{
      font-size: 12.5px;
      color: var(--primary);
      display: block;
      margin-bottom: 2px;
    }}

    /* Titles */
    .title-block {{
      margin-bottom: 16px;
    }}

    .main-title {{
      font-size: 19px;
      font-weight: 800;
      color: var(--primary);
      letter-spacing: -0.4px;
      text-transform: uppercase;
      margin-bottom: 3px;
    }}

    .sub-title {{
      font-size: 12.5px;
      color: var(--accent-dark);
      font-weight: 600;
    }}

    /* Overview Box */
    .overview-box {{
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 14px 18px;
      margin-bottom: 18px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px 20px;
      font-size: 12px;
    }}

    .ov-item {{
      display: flex;
      flex-direction: column;
    }}

    .ov-label {{
      font-size: 10px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text-muted);
      letter-spacing: 0.5px;
      margin-bottom: 2px;
    }}

    .ov-val {{
      font-size: 12px;
      font-weight: 600;
      color: var(--text-dark);
    }}

    /* Headings */
    h3.sec-head {{
      font-size: 13.5px;
      font-weight: 800;
      color: var(--primary);
      margin-top: 18px;
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: -0.2px;
      border-left: 3.5px solid var(--accent);
      padding-left: 8px;
    }}

    p.legal-p {{
      font-size: 12px;
      color: var(--text);
      line-height: 1.55;
      margin-bottom: 8px;
      text-align: justify;
    }}

    p.legal-p strong {{
      color: var(--text-dark);
    }}

    /* Tables */
    .custom-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0 14px 0;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--border);
      font-size: 11.5px;
    }}

    .custom-table th {{
      background: var(--primary);
      color: white;
      text-align: left;
      padding: 8px 10px;
      font-weight: 700;
      font-size: 11px;
      letter-spacing: 0.2px;
    }}

    .custom-table td {{
      padding: 8px 10px;
      border-bottom: 1px solid var(--border-light);
      vertical-align: middle;
      color: var(--text);
    }}

    .custom-table tr:nth-child(even) {{
      background: var(--bg);
    }}

    .custom-table tr:last-child td {{
      border-bottom: none;
    }}

    .badge-pilot {{
      background: var(--success-bg);
      color: var(--success);
      border: 1px solid #a7f3d0;
      padding: 3px 6px;
      border-radius: 5px;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      font-size: 11px;
      display: inline-block;
    }}

    .badge-tag {{
      font-size: 10px;
      color: var(--accent-dark);
      font-weight: 600;
      display: block;
      margin-top: 2px;
    }}

    /* Signatures */
    .sig-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-top: 18px;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px;
    }}

    .sig-box {{
      display: flex;
      flex-direction: column;
    }}

    .sig-title {{
      font-size: 11.5px;
      font-weight: 800;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 26px;
      border-bottom: 1.5px solid var(--border);
      padding-bottom: 5px;
    }}

    .sig-rule {{
      border-bottom: 1px solid var(--text-dark);
      margin-bottom: 6px;
    }}

    .sig-info {{
      font-size: 11px;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    .sig-info strong {{
      color: var(--text-dark);
    }}

    /* Footer */
    .doc-footer {{
      margin-top: 24px;
      padding-top: 10px;
      border-top: 1px solid var(--border-light);
      display: flex;
      justify-content: space-between;
      font-size: 9.5px;
      color: var(--text-muted);
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Print Styles */
    @media print {{
      body {{
        background: white !important;
        padding: 0 !important;
      }}

      .action-bar {{
        display: none !important;
      }}

      .doc-container {{
        box-shadow: none !important;
        border: none !important;
        border-radius: 0 !important;
        max-width: 100% !important;
      }}

      .doc-page {{
        padding: 30px 36px !important;
        page-break-after: always;
        break-after: page;
      }}

      .doc-page:last-child {{
        page-break-after: avoid;
        break-after: avoid;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Action Bar -->
  <div class="action-bar">
    <h2>
      <span>VALIXIS Services Catalogue &amp; Charter</span>
      <span class="badge">REF: VAL-CAT-2026-V1 &bull; OCT 30, 2026</span>
    </h2>
    <div class="btn-group">
      <button class="btn btn-primary" onclick="window.print()">
        <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2M6 14h12v8H6z"></path></svg>
        Print / Save as PDF
      </button>
    </div>
  </div>

  <div class="doc-container">

    <!-- ================= PAGE 1: COVER & CAPABILITIES OVERVIEW ================= -->
    <div class="doc-page">
      <div class="header-lockup">
        <img src="data:image/png;base64,{logo_b64}" alt="Valixis Technologies" class="logo-img">
        <div class="corp-details">
          <strong>VALIXIS TECHNOLOGIES</strong>
          Digital Engineering, Web Platforms &amp; Dev Pods<br>
          Official Portal: https://valixis.tech &bull; Docs: valixis.github.io/company-docs/<br>
          contact@valixis.tech &bull; Date: October 30, 2026
        </div>
      </div>

      <div class="title-block">
        <div class="main-title">Official Services Catalogue &amp; Engagement Charter</div>
        <div class="sub-title">Bespoke Web Platforms, Direct-Ordering Engines, 3D Portals &amp; Dedicated Dev Pods</div>
      </div>

      <div class="overview-box">
        <div class="ov-item">
          <span class="ov-label">Document Purpose</span>
          <span class="ov-val">Comprehensive Services Catalogue, Commercial Rate Card &amp; Master Terms</span>
        </div>
        <div class="ov-item">
          <span class="ov-label">Service Provider</span>
          <span class="ov-val">VALIXIS TECHNOLOGIES (Subhash, Founder &amp; Lead) &bull; Hyderabad, India</span>
        </div>
        <div class="ov-item">
          <span class="ov-label">Core Competencies</span>
          <span class="ov-val">Zero-Commission UPI Ordering, Clinic WhatsApp Booking, 3D Showcases, Dev Pods</span>
        </div>
        <div class="ov-item">
          <span class="ov-label">Document Date &amp; Validity</span>
          <span class="ov-val">October 30, 2026 &bull; Applicable for Q4 2026 &ndash; 2027 Client Deployments</span>
        </div>
      </div>

      <h3 class="sec-head">1. Executive Introduction &amp; The Valixis Advantage</h3>
      <p class="legal-p">
        <strong>VALIXIS Technologies</strong> is an elite software engineering studio operating at the convergence of high-converting web applications, automated operational workflows, and interactive digital interfaces. 
        Traditional digital agencies sell outdated, bloated WordPress templates that load in 6 to 8 seconds, fail to convert mobile visitors, and disconnect from daily billing operations. 
        In contrast, Valixis engineers custom, mobile-first web platforms optimized for 90+ Google Lighthouse performance scores, instant 1-click customer transactions, and automated operational dispatching.
      </p>
      <p class="legal-p">
        Whether you are a specialty cafe looking to recover 25% commissions lost to food aggregators, a premier medical/dental clinic automating after-hours appointments, or a high-growth tech startup needing software shipped in 30 days, Valixis deploys battle-tested modules with rapid turnaround and transparent milestones.
      </p>

      <h3 class="sec-head">2. The Six Core Service Pillars (Overview)</h3>
      <table class="custom-table">
        <thead>
          <tr>
            <th style="width: 25%;">Service Pillar</th>
            <th style="width: 22%;">Target Audience</th>
            <th style="width: 28%;">Core Business Problem Solved</th>
            <th style="width: 25%;">Key Technical Solution</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1. Direct F&amp;B Ordering &amp; KDS</strong></td>
            <td>Specialty Cafes, Bakeries, QSRs</td>
            <td>Losing 22%-28% to Swiggy/Zomato; zero customer phone ownership.</td>
            <td>1-click UPI direct checkout; automated WhatsApp Barista KDS dispatch.</td>
          </tr>
          <tr>
            <td><strong>2. 24/7 Clinic Booking Portals</strong></td>
            <td>Dental, Skin &amp; Aesthetic Clinics</td>
            <td>Missed calls after-hours; high 30%-40% patient no-show rates.</td>
            <td>Instagram &amp; web booking with automated WhatsApp confirmations.</td>
          </tr>
          <tr>
            <td><strong>3. 3D Hospitality &amp; Dining</strong></td>
            <td>Fine Dining, Mandi, Resorts</td>
            <td>Underbooked banquet halls; heavy OTA commissions (MMT/Booking.com).</td>
            <td>Interactive 3D virtual tour, family feast pre-ordering &amp; event booking.</td>
          </tr>
          <tr>
            <td><strong>4. Startup Dedicated Dev Pod</strong></td>
            <td>SaaS &amp; Funded Startups</td>
            <td>3-6 months and ₹20L+ wasted hiring full-time in-house devs.</td>
            <td>7-member external engineering pod shipping MVPs &amp; features in 30 days.</td>
          </tr>
          <tr>
            <td><strong>5. Web Speed &amp; Conversion Revamp</strong></td>
            <td>Outdated Local Businesses</td>
            <td>60% mobile bounce rate due to slow 7-second legacy websites.</td>
            <td>Modern rebuild with 90+ Lighthouse score and 1-second load times.</td>
          </tr>
          <tr>
            <td><strong>6. Managed Cloud Care &amp; SLA</strong></td>
            <td>All Active Clients</td>
            <td>Unexpected downtime, expired SSL certificates, and out-of-date menus.</td>
            <td>Cloudflare CDN, uptime monitoring, and priority WhatsApp SLA support.</td>
          </tr>
        </tbody>
      </table>

      <div class="doc-footer">
        <span>VALIXIS TECHNOLOGIES &bull; SERVICES CATALOGUE</span>
        <span>PAGE 1 OF 3 &bull; DATE: OCTOBER 30, 2026</span>
      </div>
    </div>

    <!-- ================= PAGE 2: SERVICES CATALOGUE & RATE CARD ================= -->
    <div class="doc-page">
      <div class="running-header">
        <span>VALIXIS TECHNOLOGIES &bull; COMMERCIAL RATE CARD</span>
        <span>REF: VAL-CAT-2026-V1 &bull; PAGE 2 OF 3</span>
      </div>

      <div class="title-block">
        <div class="main-title">Official Services Catalogue &amp; Commercial Rate Card</div>
        <div class="sub-title">Detailed Deliverables, Turnaround Times, Founder Pilot Cohort Pricing &amp; Rev-Share</div>
      </div>

      <table class="custom-table">
        <thead>
          <tr>
            <th style="width: 22%;">Service Module &amp; Vertical</th>
            <th style="width: 32%;">Deliverables &amp; Architecture</th>
            <th style="width: 10%;">Turnaround</th>
            <th style="width: 13%;">Founder Pilot Rate</th>
            <th style="width: 11%;">Standard Rate</th>
            <th style="width: 12%;">Recurring / Retainer</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <strong>1. Direct F&amp;B Ordering &amp; KDS</strong><br>
              <span class="badge-tag">Cafes, Bakeries &amp; QSRs</span>
            </td>
            <td>Mobile-first web app, categorized digital menu with modifiers (milk, roast, size), 1-click UPI checkout, and automated WhatsApp Barista KDS dispatch.</td>
            <td>5 &ndash; 7 Days</td>
            <td><span class="badge-pilot">₹18,000 &ndash; ₹20,000</span></td>
            <td>₹50,000 &ndash; ₹75,000</td>
            <td><strong>1.5% GMV share</strong><br><span style="font-size:10px;color:var(--text-muted);">(or ₹3,500/mo floor)</span></td>
          </tr>
          <tr>
            <td>
              <strong>2. Clinic 24/7 WhatsApp Booking</strong><br>
              <span class="badge-tag">Dental, Skin &amp; Wellness</span>
            </td>
            <td>Instagram bio &amp; Google booking portal, doctor schedule selector, treatment showcase, and automated WhatsApp appointment confirmations &amp; reminders.</td>
            <td>4 &ndash; 6 Days</td>
            <td><span class="badge-pilot">₹20,000 &ndash; ₹25,000</span></td>
            <td>₹55,000 &ndash; ₹80,000</td>
            <td>₹3,000 / month<br><span style="font-size:10px;color:var(--text-muted);">(hosting &amp; SMS bot)</span></td>
          </tr>
          <tr>
            <td>
              <strong>3. Luxury 3D Hospitality Portal</strong><br>
              <span class="badge-tag">Fine Dining, Mandi &amp; Hotels</span>
            </td>
            <td>Interactive 3D virtual space/dish showcase, banquet &amp; majlis family feast pre-ordering, party hall reservation modal, and zero-commission booking.</td>
            <td>7 &ndash; 10 Days</td>
            <td><span class="badge-pilot">₹25,000 &ndash; ₹30,000</span></td>
            <td>₹80,000 &ndash; ₹1,15,000</td>
            <td>₹4,500 / month<br><span style="font-size:10px;color:var(--text-muted);">(or 2% banquet GMV)</span></td>
          </tr>
          <tr>
            <td>
              <strong>4. Startup Dedicated Dev Pod</strong><br>
              <span class="badge-tag">SaaS &amp; Tech Startups</span>
            </td>
            <td>7-member full-stack engineering team shipping Next.js web apps, API integrations, client portals, or Flutter MVPs with clean Git CI/CD pipelines.</td>
            <td>30 &ndash; 45 Days</td>
            <td><span class="badge-pilot">₹60,000 / mo</span><br><span style="font-size:10px;color:var(--accent);">(India / Seed)</span></td>
            <td>₹1,20,000 / mo<br><span style="font-size:10px;color:var(--text-muted);">($2,500/mo Intl)</span></td>
            <td>Quarterly Pod<br><span style="font-size:10px;color:var(--text-muted);">(sprint contract)</span></td>
          </tr>
          <tr>
            <td>
              <strong>5. Web Speed &amp; Conversion Revamp</strong><br>
              <span class="badge-tag">Local Business Overhaul</span>
            </td>
            <td>Complete visual and performance overhaul of slow legacy WordPress/Wix sites into lightning-fast, mobile-first web apps with 90+ Lighthouse score.</td>
            <td>3 &ndash; 5 Days</td>
            <td><span class="badge-pilot">₹15,000 &ndash; ₹18,000</span></td>
            <td>₹35,000 &ndash; ₹50,000</td>
            <td>₹2,000 / month<br><span style="font-size:10px;color:var(--text-muted);">(hosting &amp; updates)</span></td>
          </tr>
          <tr>
            <td>
              <strong>6. Managed Cloud Care &amp; SLA</strong><br>
              <span class="badge-tag">Retainer for All Clients</span>
            </td>
            <td>High-speed Cloudflare CDN &amp; SSL hosting, up to 2 menu/pricing catalog updates per month, 99.9% uptime monitoring, and priority WhatsApp SLA support.</td>
            <td>Monthly</td>
            <td><span class="badge-pilot">₹2,500 / mo</span></td>
            <td>₹4,500 / mo</td>
            <td>Billed quarterly<br><span style="font-size:10px;color:var(--text-muted);">(guaranteed SLA)</span></td>
          </tr>
        </tbody>
      </table>

      <h3 class="sec-head">3. Commercial Notes &amp; Revenue-Share Framework</h3>
      <p class="legal-p">
        &bull;&nbsp;<strong>The Pilot Cohort Incentive:</strong> Pilot rates are reserved for early flagship clients who agree to provide a video testimonial, grant case study portfolio rights, and execute within seven (7) business days of presentation.<br>
        &bull;&nbsp;<strong>The 1.5% GMV Direct Share:</strong> Applies strictly to orders processed directly through the custom web portal. In-store dining and third-party aggregator orders carry zero platform fee. Collected via automated gateway split (Razorpay Route) or monthly reconciliation.<br>
        &bull;&nbsp;<strong>Statutory Taxes:</strong> All rates are quoted in INR or USD net of applicable statutory GST / taxes.
      </p>

      <div class="doc-footer">
        <span>VALIXIS TECHNOLOGIES &bull; RATE CARD</span>
        <span>PAGE 2 OF 3 &bull; DATE: OCTOBER 30, 2026</span>
      </div>
    </div>

    <!-- ================= PAGE 3: LEGALITIES, TERMS & SIGNATURES ================= -->
    <div class="doc-page">
      <div class="running-header">
        <span>VALIXIS TECHNOLOGIES &bull; LEGAL ENGAGEMENT CHARTER</span>
        <span>REF: VAL-CAT-2026-V1 &bull; PAGE 3 OF 3</span>
      </div>

      <div class="title-block">
        <div class="main-title">Master Engagement Terms &amp; Legal Guardrails</div>
        <div class="sub-title">Standard Legalities, Milestone Framework, Zero-Custody Rule &amp; Execution Block</div>
      </div>

      <h3 class="sec-head">4. Master Terms of Engagement</h3>
      <p class="legal-p">
        <strong>4.1 Exhaustive Specifications:</strong> The contracted scope is strictly limited to the service modules chosen from the rate card above. Any structural pivots, extra page templates, or custom backend integrations requested during or post-development constitute out-of-scope work, billed at Valixis's standard rate of <strong>₹2,500 / $45 per engineer-hour</strong> under a written Change Order.<br>
        <strong>4.2 Milestone Payment Structure:</strong> For standard builds, fees follow the 50-30-20 framework (50% upfront mobilization, 30% on staging demo approval, 20% prior to live DNS cutover). For pilot cohort builds (₹15k-₹25k), payments are structured as 50% mobilization deposit on Day 1 and 50% upon live domain deployment. Work commences solely upon cleared receipt of Milestone 1.<br>
        <strong>4.3 Client Asset Delay Clause (7-Day Rule):</strong> Client shall deliver all brand assets (logos, photography, menu prices, payment keys, DNS access) within seven (7) business days. Any delay by Client automatically extends the target delivery deadline by the same duration. If delays exceed thirty (30) days, Valixis may invoice for completed milestones and place the project on standby.<br>
        <strong>4.4 Revision Policy:</strong> Client is entitled to one (1) consolidated written round of feedback during pilot builds (or two rounds for standard builds), compiled by the designated Single Point of Contact (SPOC).<br>
        <strong>4.5 Conditional IP Ownership Transfer:</strong> Valixis assigns all bespoke design graphics, customized styling, and branding assets to Client strictly upon receipt of <strong>100% full and final payment</strong>. Valixis retains sole ownership over its pre-existing code libraries, developer tools, algorithms, 3D shaders, and reusable boilerplates, granting Client a perpetual, royalty-free license for live operational use.<br>
        <strong>4.6 Zero Custody of Funds:</strong> All customer payment gateways (Razorpay, Cashfree, PhonePe, or UPI VPA) must be owned and KYC-verified directly in Client's name. <strong>Valixis acts solely as a technical software integrator and at no point holds, custodies, or processes customer funds.</strong><br>
        <strong>4.7 30-Day Bug-Fix Warranty &amp; Liability Ceiling:</strong> Valixis provides a complimentary thirty (30) day warranty starting from live launch to resolve any coding defects inconsistent with agreed specifications. To the maximum extent permitted by law, Valixis's total aggregate liability arising out of this engagement shall not exceed the total fees actually received from Client.<br>
        <strong>4.8 Kill Fee &amp; Cancellation:</strong> The initial 50% mobilization deposit is non-refundable as liquidated damages for committed engineering capacity. If Client terminates for convenience, Client must settle all unbilled work completed to date.<br>
        <strong>4.9 Governing Law &amp; Jurisdiction:</strong> This engagement is governed by the laws of India, with exclusive jurisdiction in the courts of <strong>Hyderabad, Telangana</strong>.
      </p>

      <h3 class="sec-head">5. Formal Acceptance &amp; Execution</h3>
      <p class="legal-p">
        By signing below, the parties confirm acceptance of the selected service module, commercial rate, and legal terms set forth in this document.
      </p>

      <div class="sig-grid">
        <div class="sig-box">
          <div class="sig-title">For Valixis Technologies:</div>
          <div class="sig-rule" style="margin-top: 32px;"></div>
          <div class="sig-info">
            <strong>Subhash</strong><br>
            Founder &amp; Lead, Valixis Technologies<br>
            Date: October 30, 2026<br>
            contact@valixis.tech &bull; https://valixis.tech
          </div>
        </div>
        <div class="sig-box">
          <div class="sig-title">For Client Entity:</div>
          <div class="sig-rule" style="margin-top: 32px;"></div>
          <div class="sig-info">
            <strong>Authorized Signatory</strong><br>
            Title: [ __________________________________ ]<br>
            Date: [ ____ / ____ / 2026 ]<br>
            Entity: [ _________________________________ ]
          </div>
        </div>
      </div>

      <div class="doc-footer">
        <span>VALIXIS TECHNOLOGIES &bull; LEGAL CHARTER</span>
        <span>PAGE 3 OF 3 &bull; DATE: OCTOBER 30, 2026</span>
      </div>
    </div>

  </div>

</body>
</html>
"""

with open('VALIXIS_Services_Catalogue_and_Charter.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated HTML Catalogue: VALIXIS_Services_Catalogue_and_Charter.html ({os.path.getsize('VALIXIS_Services_Catalogue_and_Charter.html')} bytes)")
