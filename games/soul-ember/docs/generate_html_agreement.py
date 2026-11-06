import os
import base64

with open('valixis_horizontal_lockup.png', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VALIXIS &mdash; Master Services Agreement & Statement of Work</title>
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
      line-height: 1.55;
      font-size: 13.5px;
      padding: 24px 16px;
    }}

    /* Top Control Bar (Hidden in Print) */
    .action-bar {{
      max-width: 900px;
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
      font-size: 15px;
      font-weight: 700;
      letter-spacing: -0.2px;
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
      gap: 12px;
    }}

    .btn {{
      padding: 8px 18px;
      font-size: 13px;
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

    .btn-secondary {{
      background: rgba(255, 255, 255, 0.12);
      color: white;
    }}

    .btn-secondary:hover {{
      background: rgba(255, 255, 255, 0.2);
    }}

    /* Document Container */
    .document-wrapper {{
      max-width: 900px;
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

    /* Header Lockup */
    .doc-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 18px;
      border-bottom: 2px solid var(--primary);
      margin-bottom: 24px;
    }}

    .logo-img {{
      height: 38px;
      width: auto;
      object-fit: contain;
    }}

    .company-details {{
      text-align: right;
      font-size: 11px;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    .company-details strong {{
      font-size: 13px;
      color: var(--primary);
      display: block;
      margin-bottom: 2px;
    }}

    /* Title Block */
    .doc-title-block {{
      margin-bottom: 20px;
    }}

    .doc-title {{
      font-size: 21px;
      font-weight: 800;
      color: var(--primary);
      letter-spacing: -0.4px;
      margin-bottom: 4px;
      text-transform: uppercase;
    }}

    .doc-subtitle {{
      font-size: 13px;
      color: var(--accent-dark);
      font-weight: 600;
    }}

    /* Metadata Box */
    .meta-card {{
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px 20px;
      margin-bottom: 22px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px 24px;
    }}

    .meta-item {{
      display: flex;
      flex-direction: column;
    }}

    .meta-label {{
      font-size: 10.5px;
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.5px;
      color: var(--text-muted);
      margin-bottom: 3px;
    }}

    .meta-val {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text-dark);
    }}

    .meta-input {{
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 5px 8px;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-dark);
      background: #ffffff;
      outline: none;
      font-family: inherit;
      width: 100%;
    }}

    .meta-input:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 0 2px rgba(2, 132, 199, 0.15);
    }}

    /* Section Headings */
    h3.section-heading {{
      font-size: 14.5px;
      font-weight: 800;
      color: var(--primary);
      margin-top: 22px;
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: -0.2px;
      border-left: 3.5px solid var(--accent);
      padding-left: 10px;
    }}

    p.legal-p {{
      font-size: 12.5px;
      color: var(--text);
      line-height: 1.6;
      margin-bottom: 10px;
      text-align: justify;
    }}

    p.legal-p strong {{
      color: var(--text-dark);
    }}

    /* Tables */
    .legal-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0 16px 0;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--border);
      font-size: 12px;
    }}

    .legal-table th {{
      background: var(--primary);
      color: white;
      text-align: left;
      padding: 9px 12px;
      font-weight: 700;
      font-size: 11.5px;
      letter-spacing: 0.3px;
    }}

    .legal-table td {{
      padding: 9px 12px;
      border-bottom: 1px solid var(--border-light);
      vertical-align: top;
      color: var(--text);
    }}

    .legal-table tr:nth-child(even) {{
      background: var(--bg);
    }}

    .legal-table tr:last-child td {{
      border-bottom: none;
    }}

    .amount-badge {{
      background: #ecfdf5;
      color: var(--success);
      border: 1px solid #a7f3d0;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
    }}

    /* Checklists */
    .checklist-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 8px;
      margin: 12px 0 18px 0;
    }}

    .check-card {{
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 9px 14px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 12px;
    }}

    .check-icon {{
      color: var(--accent);
      font-weight: 800;
      font-size: 14px;
      line-height: 1;
    }}

    /* Signature Section */
    .signatures-block {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-top: 24px;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
    }}

    .sig-col {{
      display: flex;
      flex-direction: column;
    }}

    .sig-header {{
      font-size: 12px;
      font-weight: 800;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 30px;
      border-bottom: 1.5px solid var(--border);
      padding-bottom: 6px;
    }}

    .sig-line {{
      border-bottom: 1px solid var(--text-dark);
      margin-bottom: 8px;
    }}

    .sig-meta {{
      font-size: 11.5px;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    .sig-meta strong {{
      color: var(--text-dark);
    }}

    /* Footer */
    .page-footer {{
      margin-top: 30px;
      padding-top: 12px;
      border-top: 1px solid var(--border-light);
      display: flex;
      justify-content: space-between;
      font-size: 10px;
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

      .document-wrapper {{
        box-shadow: none !important;
        border: none !important;
        border-radius: 0 !important;
        max-width: 100% !important;
      }}

      .doc-page {{
        padding: 28px 34px !important;
        page-break-after: always;
        break-after: page;
      }}

      .doc-page:last-child {{
        page-break-after: avoid;
        break-after: avoid;
      }}

      .meta-input {{
        border: none !important;
        background: transparent !important;
        padding: 0 !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Action Bar -->
  <div class="action-bar">
    <h2>
      <span>VALIXIS Client Service Agreement</span>
      <span class="badge">LEGAL TEMPLATE v2026</span>
    </h2>
    <div class="btn-group">
      <button class="btn btn-secondary" onclick="calculateMilestones()">
        <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"></path></svg>
        Recalculate
      </button>
      <button class="btn btn-primary" onclick="window.print()">
        <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2M6 14h12v8H6z"></path></svg>
        Print / Save as PDF
      </button>
    </div>
  </div>

  <!-- Document Container -->
  <div class="document-wrapper">

    <!-- PAGE 1: Parties, Commercial Milestones & Recitals -->
    <div class="doc-page">
      <div class="doc-header">
        <img src="data:image/png;base64,{logo_b64}" alt="Valixis Technologies" class="logo-img">
        <div class="company-details">
          <strong>VALIXIS TECHNOLOGIES</strong>
          Digital Engineering &amp; Direct Ordering Platforms<br>
          Official Portal: https://valixis.tech &bull; Docs: valixis.github.io/company-docs/<br>
          contact@valixis.tech &bull; Hyderabad, Telangana, India
        </div>
      </div>

      <div class="doc-title-block">
        <div class="doc-title">Master Services Agreement &amp; Statement of Work</div>
        <div class="doc-subtitle">Bespoke Web Platform, 1-Click Direct UPI Ordering &amp; Barista KDS Infrastructure</div>
      </div>

      <!-- Live Fillable Metadata -->
      <div class="meta-card">
        <div class="meta-item">
          <span class="meta-label">Client Legal Entity Name</span>
          <input type="text" class="meta-input" id="clientNameInput" value="Roastery Coffee House / Subko Specialty Coffee" placeholder="Enter Client Name">
        </div>
        <div class="meta-item">
          <span class="meta-label">Authorized Signatory &amp; Designation</span>
          <input type="text" class="meta-input" id="clientSignatoryInput" value="Managing Director / Owner" placeholder="Signatory & Title">
        </div>
        <div class="meta-item">
          <span class="meta-label">Total Contract Value (INR / USD)</span>
          <input type="text" class="meta-input" id="totalFeeInput" value="₹ 75,000" onkeyup="calculateMilestones()" placeholder="e.g. ₹ 75,000">
        </div>
        <div class="meta-item">
          <span class="meta-label">Effective Date &amp; Target Launch</span>
          <input type="text" class="meta-input" value="October 30, 2026 &mdash; Target: 14 Business Days">
        </div>
      </div>

      <p class="legal-p">
        This Master Services Agreement ("Agreement") is executed on the Effective Date by and between <strong>VALIXIS TECHNOLOGIES</strong> ("Valixis", "Developer"), represented by Subhash, Founder &amp; Lead, and the Client entity named above ("Client"). 
        WHEREAS, Client desires to retain Valixis to architect, design, program, and launch a bespoke, high-converting digital web portal and commission-free direct ordering system; and WHEREAS, Valixis holds specialized engineering capabilities, proprietary frameworks, and tools to construct said software; 
        NOW, THEREFORE, the parties agree as follows:
      </p>

      <h3 class="section-heading">1. Purpose &amp; Scope of Engagement</h3>
      <p class="legal-p">
        1.1 <strong>Scope of Services:</strong> Valixis shall deliver the software design, UI/UX architecture, digital menu cataloging, 1-click UPI ordering flow, and automated Kitchen Display System (KDS) dispatch strictly as itemized in <strong>Schedule A (Statement of Work)</strong>.<br>
        1.2 <strong>Exhaustive Agreement:</strong> The deliverables specified in Schedule A constitute the entire contracted scope. Any subsequent additions or structural alterations are treated as out-of-scope under Section 4.
      </p>

      <h3 class="section-heading">2. Commercial Terms &amp; 50-30-20 Milestone Schedule</h3>
      <p class="legal-p">
        2.1 <strong>Staged Payment Milestones:</strong> Engineering deployment adheres strictly to the following 50-30-20 schedule. Development commences <em>solely</em> upon cleared receipt of Milestone 1 funds:
      </p>

      <table class="legal-table">
        <thead>
          <tr>
            <th>Milestone Phase</th>
            <th>Billing %</th>
            <th>Calculated Sum</th>
            <th>Trigger Event &amp; Deliverables Released</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>M1: Mobilization Deposit</strong></td>
            <td><strong>50%</strong></td>
            <td><span class="amount-badge" id="m1Amount">₹ 37,500</span></td>
            <td>Due upon Agreement execution. Architecture wireframing, environment setup. Strictly non-refundable.</td>
          </tr>
          <tr>
            <td><strong>M2: Staging Demo Review</strong></td>
            <td><strong>30%</strong></td>
            <td><span class="amount-badge" id="m2Amount">₹ 22,500</span></td>
            <td>Due upon delivery of private Staging URL (<code>preview.valixis.com/client</code>) with interactive menu &amp; cart checkout.</td>
          </tr>
          <tr>
            <td><strong>M3: Production Cutover</strong></td>
            <td><strong>20%</strong></td>
            <td><span class="amount-badge" id="m3Amount">₹ 15,000</span></td>
            <td>Due prior to live domain DNS switch and handover of production administrator credentials.</td>
          </tr>
        </tbody>
      </table>

      <p class="legal-p">
        2.2 <strong>Overdue Invoices:</strong> Invoices unpaid past seven (7) business days accrue interest at 1.5% per month. Valixis reserves the right to halt development or pause staging access during delinquency.
      </p>

      <div class="page-footer">
        <span>VALIXIS TECHNOLOGIES &bull; MASTER SERVICES AGREEMENT</span>
        <span>PAGE 1 OF 3 &bull; REF: VAL-MSA-2026-FNB</span>
      </div>
    </div>

    <!-- PAGE 2: Legal Articles 3 to 10 -->
    <div class="doc-page">
      <h3 class="section-heading">3. Client Cooperation &amp; Asset Delay Clause (7-Day Rule)</h3>
      <p class="legal-p">
        3.1 <strong>Asset Delivery:</strong> Client shall furnish all mandatory assets listed in <strong>Schedule B</strong> (logos, photography, menu spreadsheet, DNS credentials, payment keys) within seven (7) business days of signing.<br>
        3.2 <strong>Timeline Adjustment:</strong> If Client delays asset submission or sign-offs beyond seven (7) business days, the agreed target completion date shall automatically extend on a day-for-day basis. If delays exceed thirty (30) days, Valixis may invoice for completed milestones and place the project on standby.
      </p>

      <h3 class="section-heading">4. Revision Limits &amp; Change Orders</h3>
      <p class="legal-p">
        4.1 <strong>Included Revisions:</strong> The Project fee covers two (2) consolidated rounds of feedback during the Milestone 2 Staging Phase, submitted in writing by the designated SPOC.<br>
        4.2 <strong>Out-of-Scope Alterations:</strong> Requests involving architectural changes, additional page templates, third-party POS API integrations, or native app stores not listed in Schedule A are billed at Valixis's standard rate of <strong>₹2,500 / $45 per engineer-hour</strong> under a written Change Order.
      </p>

      <h3 class="section-heading">5. Intellectual Property Rights &amp; Code Ownership</h3>
      <p class="legal-p">
        5.1 <strong>Conditional Title Transfer:</strong> Conditioned strictly upon receipt of <strong>100% full and final payment</strong>, Valixis assigns to Client all exclusive rights and title in and to the bespoke UI graphics, customized styling, and specific branded text content developed uniquely for Client.<br>
        5.2 <strong>Developer Retained IP:</strong> Valixis retains exclusive ownership, copyright, and patent rights over all pre-existing code libraries, developer tools, algorithms, 3D shader routines, headless KDS dispatch wrappers, and reusable software boilerplates ("Developer IP"). Valixis grants Client an irrevocable, non-exclusive, perpetual, royalty-free license to use said Developer IP solely in conjunction with the live Project.<br>
        5.3 <strong>Portfolio Rights:</strong> Valixis reserves the right to showcase screenshots, live demonstrations, and performance metrics in its digital portfolio and case studies.
      </p>

      <h3 class="section-heading">6. Payment Gateways, Direct UPI &amp; Zero-Custody Acknowledgment</h3>
      <p class="legal-p">
        6.1 <strong>Direct Merchant KYC:</strong> Client explicitly agrees that all customer payment processing accounts (Razorpay, Cashfree, PhonePe, or UPI VPA) must be owned and KYC-verified directly in Client's name. <strong>Valixis acts solely as a technical software integrator and at no point custodies, processes, handles, or holds customer funds.</strong><br>
        6.2 <strong>Third-Party Outages:</strong> Valixis shall not be held liable for losses or interruptions stemming from payment gateway downtimes, banking network latencies, SMS/WhatsApp delivery delays, or domain registrar suspensions outside Developer's direct control.
      </p>

      <h3 class="section-heading">7. Limited Warranty &amp; Limitation of Liability</h3>
      <p class="legal-p">
        7.1 <strong>30-Day Bug-Fix Warranty:</strong> Valixis provides a complimentary thirty (30) calendar day bug-fix warranty commencing on the official live launch date. During this period, Valixis shall promptly correct any software defects or broken links inconsistent with Schedule A specifications. This warranty excludes modifications made by Client or third-party API changes.<br>
        7.2 <strong>Liability Ceiling:</strong> TO THE MAXIMUM EXTENT PERMITTED BY LAW, IN NO EVENT SHALL VALIXIS'S AGGREGATE FINANCIAL LIABILITY ARISING OUT OF THIS AGREEMENT EXCEED THE TOTAL PROJECT FEES ACTUALLY RECEIVED BY VALIXIS HEREUNDER. NEITHER PARTY SHALL BE LIABLE FOR INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES.
      </p>

      <h3 class="section-heading">8. Termination &amp; Kill Fee</h3>
      <p class="legal-p">
        8.1 <strong>Termination for Cause:</strong> Either party may terminate upon written notice if the other party breaches a material obligation and fails to cure within fourteen (14) calendar days.<br>
        8.2 <strong>Convenience Termination:</strong> Should Client terminate for convenience prior to completion, the initial 50% mobilization deposit is strictly non-refundable as liquidated damages for allocated engineering availability, and Client shall immediately settle all unbilled milestone work completed up to the date of notice.
      </p>

      <h3 class="section-heading">9. Confidentiality &amp; Governing Law</h3>
      <p class="legal-p">
        9.1 <strong>Confidentiality:</strong> Both parties agree to maintain strict confidentiality of all commercial, operational, and financial data disclosed during this project.<br>
        9.2 <strong>Governing Law:</strong> This Agreement is governed by the laws of India. Any unresolved dispute shall be subject to the exclusive jurisdiction of the competent courts in <strong>Hyderabad, Telangana</strong>.
      </p>

      <div class="page-footer">
        <span>VALIXIS TECHNOLOGIES &bull; MASTER SERVICES AGREEMENT</span>
        <span>PAGE 2 OF 3 &bull; REF: VAL-MSA-2026-FNB</span>
      </div>
    </div>

    <!-- PAGE 3: Schedules & Signature Blocks -->
    <div class="doc-page">
      <h3 class="section-heading">Schedule A: Statement of Work (SOW) Deliverables</h3>
      <p class="legal-p">The following deliverables represent the complete, exhaustive project scope agreed for deployment:</p>

      <table class="legal-table">
        <thead>
          <tr>
            <th>Deliverable Module</th>
            <th>Technical Specifications &amp; Architecture</th>
            <th>Verification Criteria</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1. High-Performance Web Portal</strong></td>
            <td>Responsive, mobile-first web app with custom brand gradients, hero section, brand story, visual gallery, and location maps.</td>
            <td>Lighthouse performance score 90+ on mobile &amp; desktop viewport audits.</td>
          </tr>
          <tr>
            <td><strong>2. Interactive Digital Menu &amp; Modifiers</strong></td>
            <td>Complete digital menu categories, real-time item variants (e.g. Oat/Almond milk, roast origin, sweetness), and dietary indicators.</td>
            <td>All menu items rendered accurately with instant cart addition and price updates.</td>
          </tr>
          <tr>
            <td><strong>3. Zero-Commission 1-Click UPI Engine</strong></td>
            <td>Direct UPI deep-link / dynamic QR generation routing 100% of transaction amounts directly into Client's merchant account.</td>
            <td>Zero per-transaction commission cut deducted by developer or intermediary.</td>
          </tr>
          <tr>
            <td><strong>4. Kitchen Display (KDS) Alert Dispatch</strong></td>
            <td>Automated order notification modal that generates formatted order tickets for barista/counter staff via WhatsApp Business / SMS.</td>
            <td>Immediate ticket receipt containing items, table/takeaway number, and total.</td>
          </tr>
          <tr>
            <td><strong>5. Technical SEO &amp; OpenGraph Suite</strong></td>
            <td>Production metadata, OpenGraph preview cards for WhatsApp/Instagram sharing, and favicon suite (16x16 up to 512x512).</td>
            <td>Social media link previews generate correct image, title, and description tags.</td>
          </tr>
          <tr>
            <td><strong>6. 30-Day Stabilization Warranty</strong></td>
            <td>Dedicated 30-day post-launch support addressing coding defects, layout adjustments, and broken hyperlinks.</td>
            <td>Fast-track resolution for any unexpected runtime bugs within 24 business hours.</td>
          </tr>
        </tbody>
      </table>

      <h3 class="section-heading">Schedule B: Mandatory Client Onboarding Checklist</h3>
      <div class="checklist-grid">
        <div class="check-card">
          <span class="check-icon">&#10003;</span>
          <span>1. High-resolution vector logo (.SVG or transparent .PNG format, lockup and standalone emblem).</span>
        </div>
        <div class="check-card">
          <span class="check-icon">&#10003;</span>
          <span>2. Final approved menu spreadsheet with retail pricing, item descriptions, dietary tags, and variant add-ons.</span>
        </div>
        <div class="check-card">
          <span class="check-icon">&#10003;</span>
          <span>3. High-resolution food, beverage, and cafe interior photography (minimum 2400x1600px resolution).</span>
        </div>
        <div class="check-card">
          <span class="check-icon">&#10003;</span>
          <span>4. DNS registrar credentials or Cloudflare delegated access for live domain cutover (e.g. <code>order.cafename.com</code>).</span>
        </div>
        <div class="check-card">
          <span class="check-icon">&#10003;</span>
          <span>5. Direct merchant UPI VPA handle (<code>brandname@bank</code>) or Payment Gateway API credentials (Key ID &amp; Secret).</span>
        </div>
        <div class="check-card">
          <span class="check-icon">&#10003;</span>
          <span>6. Designate official Single Point of Contact (SPOC) with WhatsApp number for staging approval communication.</span>
        </div>
      </div>

      <h3 class="section-heading">Execution &amp; Acceptance Signatures</h3>
      <p class="legal-p">
        IN WITNESS WHEREOF, the parties hereto have executed and accepted this Master Services Agreement &amp; Statement of Work as of the Effective Date. Each signatory warrants they are authorized to legally bind their organization.
      </p>

      <div class="signatures-block">
        <div class="sig-col">
          <div class="sig-header">For Valixis Technologies:</div>
          <div class="sig-line" style="margin-top: 36px;"></div>
          <div class="sig-meta">
            <strong>Subhash</strong><br>
            Founder &amp; Lead, Valixis Technologies<br>
            Date: [ ____ / ____ / 2026 ]<br>
            contact@valixis.tech
          </div>
        </div>
        <div class="sig-col">
          <div class="sig-header">For Client:</div>
          <div class="sig-line" style="margin-top: 36px;"></div>
          <div class="sig-meta">
            <strong>Authorized Signatory</strong><br>
            Title: [ __________________________________ ]<br>
            Date: [ ____ / ____ / 2026 ]<br>
            Entity: [ _________________________________ ]
          </div>
        </div>
      </div>

      <div class="page-footer">
        <span>VALIXIS TECHNOLOGIES &bull; MASTER SERVICES AGREEMENT</span>
        <span>PAGE 3 OF 3 &bull; REF: VAL-MSA-2026-FNB</span>
      </div>
    </div>

  </div>

  <script>
    function calculateMilestones() {{
      const valStr = document.getElementById('totalFeeInput').value;
      const num = parseFloat(valStr.replace(/[^0-9.]/g, '')) || 0;
      const isRupee = valStr.includes('₹') || !valStr.includes('$');
      const symbol = isRupee ? '₹ ' : '$ ';
      
      const m1 = Math.round(num * 0.50);
      const m2 = Math.round(num * 0.30);
      const m3 = Math.round(num * 0.20);
      
      document.getElementById('m1Amount').innerText = symbol + m1.toLocaleString('en-IN');
      document.getElementById('m2Amount').innerText = symbol + m2.toLocaleString('en-IN');
      document.getElementById('m3Amount').innerText = symbol + m3.toLocaleString('en-IN');
    }}
  </script>
</body>
</html>
"""

with open('VALIXIS_Client_Service_Agreement.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated HTML Agreement: VALIXIS_Client_Service_Agreement.html ({os.path.getsize('VALIXIS_Client_Service_Agreement.html')} bytes)")
