import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_header_footer(self, total_pages):
        self.saveState()
        self.setFont("Helvetica-Bold", 7.5)
        self.setFillColor(colors.HexColor("#475569"))
        
        # Running Header on pages after page 1
        if self._pageNumber > 1:
            self.drawString(36, 814, "VALIXIS TECHNOLOGIES  *  SERVICES CATALOGUE & COMMERCIAL CHARTER")
            self.drawRightString(559, 814, "REF: VAL-CAT-2026-V1  |  DATE: OCTOBER 30, 2026")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(36, 808, 559, 808)

        # Running Footer on all pages
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 36, 559, 36)
        
        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(36, 25, "Valixis Technologies  *  Official Charter & Services Catalogue  *  https://valixis.tech  *  contact@valixis.tech")
        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.drawRightString(559, 25, page_str)
        self.restoreState()

def build_catalogue_pdf(filename="VALIXIS_Services_Catalogue_and_Charter.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=38,
        bottomMargin=42
    )

    styles = getSampleStyleSheet()
    
    primary = colors.HexColor("#0f172a")     # Slate 900
    accent = colors.HexColor("#0284c7")      # Sky 600
    dark_gray = colors.HexColor("#334155")   # Slate 700
    border_color = colors.HexColor("#cbd5e1")# Slate 300
    green_color = colors.HexColor("#059669") # Emerald 600
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15.5,
        leading=18.5,
        textColor=primary,
        spaceAfter=2
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.2,
        leading=12,
        textColor=colors.HexColor("#475569"),
        spaceAfter=7
    )

    h1_style = ParagraphStyle(
        'Heading1Custom',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=primary,
        spaceBefore=6,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyCustom',
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.8,
        textColor=dark_gray,
        spaceAfter=3
    )

    body_bold = ParagraphStyle(
        'BodyBoldCustom',
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10.8,
        textColor=primary,
        spaceAfter=3
    )

    legal_clause_style = ParagraphStyle(
        'LegalClause',
        fontName='Helvetica',
        fontSize=7.5,
        leading=10.2,
        textColor=dark_gray,
        spaceAfter=3.2,
        alignment=4
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        fontName='Helvetica',
        fontSize=7.3,
        leading=9.8,
        textColor=dark_gray
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        fontName='Helvetica-Bold',
        fontSize=7.3,
        leading=9.8,
        textColor=primary
    )

    table_cell_price = ParagraphStyle(
        'TableCellPrice',
        fontName='Helvetica-Bold',
        fontSize=7.3,
        leading=9.8,
        textColor=green_color
    )

    story = []

    # ================= PAGE 1: COVER & CAPABILITIES OVERVIEW =================
    logo_path = 'valixis_horizontal_lockup.png'
    if os.path.exists(logo_path):
        img = Image(logo_path, width=155, height=21.9)
        company_info = Paragraph(
            "<b>VALIXIS TECHNOLOGIES</b><br/>"
            "<font color='#64748b' size=7>"
            "Elite Digital Engineering, High-Converting Web Platforms & Dedicated Dev Pods<br/>"
            "Official Portal: https://valixis.tech  |  Docs: valixis.github.io/company-docs/<br/>"
            "Email: contact@valixis.tech  |  Phone: +91 91334 32168  |  Date: October 30, 2026"
            "</font>",
            body_style
        )
        header_table = Table([[img, company_info]], colWidths=[165, 358])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (1,0), (1,0), 'RIGHT'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ]))
        story.append(header_table)
    else:
        story.append(Paragraph("<b>VALIXIS TECHNOLOGIES</b>", title_style))
    
    story.append(HRFlowable(width="100%", thickness=1.2, color=primary, spaceBefore=2, spaceAfter=6))

    story.append(Paragraph("OFFICIAL SERVICES CATALOGUE & ENGAGEMENT CHARTER", title_style))
    story.append(Paragraph("Bespoke Web Platforms, Direct-Ordering Engines, 3D Portals & Dedicated Dev Pods", subtitle_style))

    # Executive Overview Box
    intro_data = [
        [
            Paragraph("<b>DOCUMENT CLASSIFICATION:</b>", body_bold),
            Paragraph("Client-Facing Services Catalogue, Commercial Rate Card & Master Engagement Agreement", body_style)
        ],
        [
            Paragraph("<b>SERVICE PROVIDER:</b>", body_bold),
            Paragraph("<b>VALIXIS TECHNOLOGIES</b> &bull; Represented by Subhash, Founder & Lead &bull; Hyderabad, India", body_style)
        ],
        [
            Paragraph("<b>CORE SPECIALIZATION:</b>", body_bold),
            Paragraph("Zero-Commission F&B Direct Ordering (UPI/KDS), Clinic Booking Portals, 3D Web Apps, and 30-Day Dev Sprints", body_style)
        ],
        [
            Paragraph("<b>VERIFICATION & CODE:</b>", body_bold),
            Paragraph("Official Company Documentation & Live Builds: <b>https://valixis.github.io/company-docs/</b>", body_style)
        ],
        [
            Paragraph("<b>EFFECTIVE DATE:</b>", body_bold),
            Paragraph("October 30, 2026 &nbsp;&bull;&nbsp; Applicable for Q4 2026 &ndash; 2027 Client Engagements", body_style)
        ]
    ]
    intro_table = Table(intro_data, colWidths=[140, 383])
    intro_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 0.8, border_color),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(intro_table)
    story.append(Spacer(1, 5))

    story.append(Paragraph("1. EXECUTIVE INTRODUCTION & THE VALIXIS ADVANTAGE", h1_style))
    story.append(Paragraph(
        "<b>VALIXIS Technologies</b> is an elite technology enterprise operating at the intersection of high-converting web engineering, automated operational workflows, and interactive digital experiences. "
        "Unlike traditional agencies that sell bloated WordPress templates that load slowly and fail to convert visitors, Valixis engineers custom, mobile-first web applications built for speed (Google Lighthouse 90+), direct revenue generation, and seamless integration with day-to-day business operations.",
        legal_clause_style
    ))
    story.append(Paragraph(
        "Whether you are a specialty cafe looking to eliminate 25% aggregator cuts, a premier clinic automating 24/7 patient booking, or a high-growth startup shipping software features in 30 days, Valixis provides end-to-end engineering pods with clear, predictable deliverables.",
        legal_clause_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("2. THE SIX CORE SERVICE PILLARS (OVERVIEW)", h1_style))

    pillars_data = [
        [
            Paragraph("<b>Service Pillar</b>", table_header_style),
            Paragraph("<b>Target Audience</b>", table_header_style),
            Paragraph("<b>Core Business Problem Solved</b>", table_header_style),
            Paragraph("<b>Key Technical Solution</b>", table_header_style)
        ],
        [
            Paragraph("<b>1. Direct F&B Ordering & KDS</b>", table_cell_bold),
            Paragraph("Cafes, Bakeries, QSRs, Roasteries", table_cell_style),
            Paragraph("Losing 22%-28% to Swiggy/Zomato; zero customer data ownership.", table_cell_style),
            Paragraph("1-click UPI direct ordering; instant WhatsApp Kitchen Display dispatch.", table_cell_style)
        ],
        [
            Paragraph("<b>2. 24/7 Clinic Booking Portals</b>", table_cell_bold),
            Paragraph("Dental, Skin, Aesthetic, Wellness", table_cell_style),
            Paragraph("Missed after-hours inquiries; high 30%-40% patient no-show rates.", table_cell_style),
            Paragraph("Automated slot booking with instant WhatsApp reminders & confirmations.", table_cell_style)
        ],
        [
            Paragraph("<b>3. 3D Hospitality & Dining</b>", table_cell_bold),
            Paragraph("Luxury Dining, Mandi, Resorts", table_cell_style),
            Paragraph("Empty banquet spaces; high OTA commissions (Booking.com/MMT).", table_cell_style),
            Paragraph("Interactive 3D virtual tour, platter customizer & direct banquet booking.", table_cell_style)
        ],
        [
            Paragraph("<b>4. Startup Dedicated Dev Pod</b>", table_cell_bold),
            Paragraph("SaaS, Funded Tech Startups", table_cell_style),
            Paragraph("3-6 months and ₹20L+ wasted hiring full-time in-house devs.", table_cell_style),
            Paragraph("7-member external engineering pod shipping MVPs & features in 30-45 days.", table_cell_style)
        ],
        [
            Paragraph("<b>5. Web Speed & Conversion Revamp</b>", table_cell_bold),
            Paragraph("Outdated Local Businesses", table_cell_style),
            Paragraph("High bounce rates from slow 7-second WordPress/Wix sites.", table_cell_style),
            Paragraph("Clean modern rebuild with 90+ Lighthouse score and 1-second load times.", table_cell_style)
        ],
        [
            Paragraph("<b>6. Managed Cloud Care & SLA</b>", table_cell_bold),
            Paragraph("All Active Business Clients", table_cell_style),
            Paragraph("Unexpected server crashes, domain expirations, out-of-date menus.", table_cell_style),
            Paragraph("Cloudflare CDN hosting, SSL, uptime monitoring, and priority updates.", table_cell_style)
        ]
    ]

    pillars_table = Table(pillars_data, colWidths=[120, 100, 155, 148])
    pillars_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(pillars_table)

    # ================= PAGE 2: SERVICES CATALOGUE & RATE CARD =================
    story.append(PageBreak())

    story.append(Paragraph("OFFICIAL SERVICES CATALOGUE & COMMERCIAL RATE CARD", title_style))
    story.append(Paragraph("Transparent Pricing, Deliverables, Turnaround Times & Pilot Cohort Packages", subtitle_style))

    cat_data = [
        [
            Paragraph("<b>Service Module & Vertical</b>", table_header_style),
            Paragraph("<b>Deliverables & Architecture</b>", table_header_style),
            Paragraph("<b>Turnaround</b>", table_header_style),
            Paragraph("<b>Founder Pilot Rate</b>", table_header_style),
            Paragraph("<b>Standard Agency Rate</b>", table_header_style),
            Paragraph("<b>Recurring / Rev-Share</b>", table_header_style)
        ],
        [
            Paragraph("<b>1. Direct F&B Ordering & KDS Engine</b><br/><font color='#64748b' size=6.5>Specialty Cafes & Bakeries</font>", table_cell_bold),
            Paragraph("Bespoke mobile-first web app, interactive digital menu with modifiers (milk, roast, size), 1-click UPI checkout, and automated WhatsApp Barista KDS dispatch.", table_cell_style),
            Paragraph("5 &ndash; 7 Days", table_cell_style),
            Paragraph("<b>₹18,000 &ndash; ₹20,000</b><br/><font size=6.5 color='#0284c7'>Pilot Cohort</font>", table_cell_price),
            Paragraph("₹50,000 &ndash; ₹75,000", table_cell_style),
            Paragraph("<b>1.5% GMV share</b><br/><font size=6.5 color='#64748b'>or ₹3,500/mo floor</font>", table_cell_bold)
        ],
        [
            Paragraph("<b>2. Clinic 24/7 WhatsApp Booking</b><br/><font color='#64748b' size=6.5>Dental, Skin & Aesthetics</font>", table_cell_bold),
            Paragraph("Instagram bio & Google booking portal, doctor schedule selector, treatment showcase, and automated WhatsApp appointment confirmations & reminders.", table_cell_style),
            Paragraph("4 &ndash; 6 Days", table_cell_style),
            Paragraph("<b>₹20,000 &ndash; ₹25,000</b><br/><font size=6.5 color='#0284c7'>Pilot Cohort</font>", table_cell_price),
            Paragraph("₹55,000 &ndash; ₹80,000", table_cell_style),
            Paragraph("₹3,000 / month<br/><font size=6.5 color='#64748b'>hosting & SMS bot</font>", table_cell_style)
        ],
        [
            Paragraph("<b>3. Luxury 3D Hospitality Portal</b><br/><font color='#64748b' size=6.5>Fine Dining, Mandi & Hotels</font>", table_cell_bold),
            Paragraph("Interactive 3D space/dish virtual showcase, banquet/majlis family feast pre-ordering, party hall reservation modal, and zero-commission direct booking.", table_cell_style),
            Paragraph("7 &ndash; 10 Days", table_cell_style),
            Paragraph("<b>₹25,000 &ndash; ₹30,000</b><br/><font size=6.5 color='#0284c7'>Pilot Cohort</font>", table_cell_price),
            Paragraph("₹80,000 &ndash; ₹1,15,000", table_cell_style),
            Paragraph("₹4,500 / month<br/><font size=6.5 color='#64748b'>or 2% banquet GMV</font>", table_cell_style)
        ],
        [
            Paragraph("<b>4. Startup Dedicated Dev Pod</b><br/><font color='#64748b' size=6.5>SaaS & Tech Startups</font>", table_cell_bold),
            Paragraph("Dedicated 7-member full-stack engineering team shipping Next.js web applications, API integrations, client portals, or Flutter MVPs with clean CI/CD.", table_cell_style),
            Paragraph("30 &ndash; 45 Day Sprint", table_cell_style),
            Paragraph("<b>₹60,000 / mo</b><br/><font size=6.5 color='#0284c7'>India / Seed</font>", table_cell_price),
            Paragraph("₹1,20,000 / mo<br/>($2,500/mo Intl)", table_cell_style),
            Paragraph("Quarterly Pod Contract<br/><font size=6.5 color='#64748b'>dedicated sprint</font>", table_cell_style)
        ],
        [
            Paragraph("<b>5. Web Speed & Conversion Revamp</b><br/><font color='#64748b' size=6.5>Local Business Overhaul</font>", table_cell_bold),
            Paragraph("Complete visual and performance overhaul of slow legacy WordPress/Wix sites into lightning-fast, mobile-first web apps with 90+ Lighthouse score.", table_cell_style),
            Paragraph("3 &ndash; 5 Days", table_cell_style),
            Paragraph("<b>₹15,000 &ndash; ₹18,000</b><br/><font size=6.5 color='#0284c7'>Single Site</font>", table_cell_price),
            Paragraph("₹35,000 &ndash; ₹50,000", table_cell_style),
            Paragraph("₹2,000 / month<br/><font size=6.5 color='#64748b'>hosting & updates</font>", table_cell_style)
        ],
        [
            Paragraph("<b>6. Managed Cloud Care & SLA</b><br/><font color='#64748b' size=6.5>Retainer for All Clients</font>", table_cell_bold),
            Paragraph("High-speed Cloudflare CDN & SSL hosting, up to 2 menu/pricing catalog updates per month, 99.9% uptime monitoring, and priority WhatsApp SLA support.", table_cell_style),
            Paragraph("Continuous Monthly", table_cell_style),
            Paragraph("<b>₹2,500 / mo</b><br/><font size=6.5 color='#0284c7'>Baseline</font>", table_cell_price),
            Paragraph("₹4,500 / mo", table_cell_style),
            Paragraph("Billed quarterly<br/><font size=6.5 color='#64748b'>guaranteed uptime</font>", table_cell_style)
        ]
    ]

    cat_table = Table(cat_data, colWidths=[105, 172, 50, 68, 64, 64])
    cat_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(cat_table)
    story.append(Spacer(1, 4))

    story.append(Paragraph("3. COMMERCIAL NOTES & REVENUE-SHARE EXPLANATION", h1_style))
    story.append(Paragraph(
        "&bull;&nbsp;&nbsp;<b>The Pilot Cohort Incentive:</b> Pilot rates are strictly reserved for early flagship clients who agree to provide a video testimonial, live case study showcase rights, and sign within seven (7) days of proposal presentation.<br/>"
        "&bull;&nbsp;&nbsp;<b>The 1.5% GMV Direct Share:</b> Applicable strictly to online transactions processed directly through the custom web portal. In-store cash or third-party aggregator orders carry zero fee. Collected either via automated gateway split (Razorpay Route) or monthly reconciliation.<br/>"
        "&bull;&nbsp;&nbsp;<b>Statutory Taxes:</b> All figures are quoted in Indian Rupees (INR) or US Dollars (USD) net of applicable statutory GST / taxes.",
        legal_clause_style
    ))

    # ================= PAGE 3: LEGALITIES, TERMS & SIGNATURES =================
    story.append(PageBreak())

    story.append(Paragraph("MASTER ENGAGEMENT TERMS & LEGAL GUARDRAILS", title_style))
    story.append(Paragraph("Standard Legalities, Milestone Framework, Zero-Custody Rule & Execution Block", subtitle_style))

    story.append(Paragraph("4. MASTER TERMS OF ENGAGEMENT", h1_style))
    story.append(Paragraph(
        "<b>4.1 Exhaustive Specifications:</b> The contracted scope of services is limited strictly to the modules selected in Section 3 above. Any additional features, structural pivots, or integrations requested during or post-development constitute out-of-scope work, billed at Valixis's standard rate of <b>₹2,500 / $45 per engineer-hour</b>.<br/>"
        "<b>4.2 Milestone Payment Structure:</b> For standard projects, fees follow the 50-30-20 framework (50% upfront mobilization, 30% on staging demo approval, 20% prior to live DNS cutover). For pilot cohort builds (₹15k-₹25k), fees are structured as 50% mobilization deposit on Day 1 and 50% upon live domain deployment. Work commences solely upon cleared receipt of Milestone 1.<br/>"
        "<b>4.3 Client Asset Delay Clause (7-Day Rule):</b> Client shall deliver all brand assets (logos, photography, menu prices, payment gateway keys, DNS access) within seven (7) business days. Any delay by Client automatically extends the target delivery deadline by the same duration. If delays exceed thirty (30) days, Valixis may invoice for completed milestones and pause work.<br/>"
        "<b>4.4 Revision Policy:</b> Client is entitled to one (1) consolidated written round of feedback during pilot builds (or two rounds for standard builds). Consolidated feedback must be provided by the designated Single Point of Contact (SPOC).<br/>"
        "<b>4.5 Conditional IP Ownership Transfer:</b> Valixis assigns all bespoke design graphics, customized styling, and branding assets to Client strictly upon receipt of <b>100% full and final payment</b>. Valixis retains sole ownership over its pre-existing code libraries, developer tools, algorithms, 3D shaders, and reusable boilerplates, granting Client a perpetual, royalty-free license for live operational use.<br/>"
        "<b>4.6 Zero Custody of Funds:</b> All customer payment gateways (Razorpay, Cashfree, PhonePe, or UPI VPA) must be owned and KYC-verified directly in Client's name. <b>Valixis acts solely as a technical software integrator and at no point holds, custodies, or processes customer funds.</b><br/>"
        "<b>4.7 30-Day Bug-Fix Warranty & Liability Ceiling:</b> Valixis provides a complimentary thirty (30) day warranty starting from live launch to resolve any coding defects inconsistent with agreed specifications. To the maximum extent permitted by law, Valixis's total aggregate liability arising out of this engagement shall not exceed the total fees actually received from Client.<br/>"
        "<b>4.8 Kill Fee & Cancellation:</b> The initial 50% mobilization deposit is non-refundable as liquidated damages for committed engineering capacity. If Client terminates for convenience, Client must settle all unbilled work completed to date.<br/>"
        "<b>4.9 Governing Law & Jurisdiction:</b> This engagement is governed by the laws of India, with exclusive jurisdiction in the courts of <b>Hyderabad, Telangana</b>.",
        legal_clause_style
    ))
    story.append(Spacer(1, 4))

    # Acceptance Signatures
    story.append(Paragraph("5. FORMAL ACCEPTANCE & EXECUTION", h1_style))
    story.append(Paragraph(
        "By signing below, the parties confirm acceptance of the selected service module, commercial rate, and legal terms set forth in this document.",
        legal_clause_style
    ))
    story.append(Spacer(1, 4))

    sig_data = [
        [
            Paragraph("<b>FOR VALIXIS TECHNOLOGIES:</b>", body_bold),
            Paragraph("<b>FOR CLIENT ENTITY:</b>", body_bold)
        ],
        [
            Paragraph("<br/><br/>____________________________________________________<br/>Authorized Signature", body_style),
            Paragraph("<br/><br/>____________________________________________________<br/>Authorized Signature", body_style)
        ],
        [
            Paragraph("<b>Name:</b> Subhash<br/><b>Title:</b> Founder & Lead<br/><b>Date:</b> October 30, 2026<br/><b>Entity:</b> Valixis Technologies &bull; contact@valixis.tech", body_style),
            Paragraph("<b>Name:</b> [___________________________________]<br/><b>Title:</b> [___________________________________]<br/><b>Date:</b> [____ / ____ / 2026]<br/><b>Entity:</b> [___________________________________]", body_style)
        ]
    ]

    sig_table = Table(sig_data, colWidths=[261, 262])
    sig_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.8, border_color),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(sig_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Generated PDF: {filename} ({os.path.getsize(filename)} bytes)")

if __name__ == "__main__":
    build_catalogue_pdf()
