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
            self.drawString(38, 814, "VALIXIS TECHNOLOGIES  *  MASTER SERVICES AGREEMENT & STATEMENT OF WORK")
            self.drawRightString(557, 814, "REF: VAL-MSA-2026-FNB")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(38, 808, 557, 808)

        # Running Footer on all pages
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(38, 38, 557, 38)
        
        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(38, 27, "Valixis Technologies  *  Confidential  *  https://valixis.tech  *  contact@valixis.tech")
        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.drawRightString(557, 27, page_str)
        self.restoreState()

def build_pdf(filename="VALIXIS_Master_Client_Agreement.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=38,
        rightMargin=38,
        topMargin=40,
        bottomMargin=44
    )

    styles = getSampleStyleSheet()
    
    primary_color = colors.HexColor("#0f172a") # Slate 900
    accent_blue = colors.HexColor("#0369a1")   # Sky 700
    dark_gray = colors.HexColor("#334155")     # Slate 700
    border_color = colors.HexColor("#cbd5e1")  # Slate 300
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=19,
        textColor=primary_color,
        spaceAfter=2
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=12.5,
        textColor=colors.HexColor("#475569"),
        spaceAfter=8
    )

    h1_style = ParagraphStyle(
        'Heading1Custom',
        fontName='Helvetica-Bold',
        fontSize=10.2,
        leading=13.5,
        textColor=primary_color,
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyCustom',
        fontName='Helvetica',
        fontSize=8,
        leading=11.2,
        textColor=dark_gray,
        spaceAfter=3
    )

    body_bold = ParagraphStyle(
        'BodyBoldCustom',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11.2,
        textColor=primary_color,
        spaceAfter=3
    )

    legal_clause_style = ParagraphStyle(
        'LegalClause',
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.6,
        textColor=dark_gray,
        spaceAfter=3.5,
        alignment=4 # Justified
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=dark_gray
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=10,
        textColor=primary_color
    )

    story = []

    # ================= PAGE 1 =================
    logo_path = 'valixis_horizontal_lockup.png'
    if os.path.exists(logo_path):
        img = Image(logo_path, width=150, height=21.2)
        company_info = Paragraph(
            "<b>VALIXIS TECHNOLOGIES</b><br/>"
            "<font color='#64748b' size=7>"
            "Elite Digital Engineering, High-Converting Web Platforms & Direct UPI Ordering<br/>"
            "Official Portal: https://valixis.tech  |  Docs: valixis.github.io/company-docs/<br/>"
            "Direct Office: contact@valixis.tech  |  Phone: +91 91334 32168 / Operations Pod"
            "</font>",
            body_style
        )
        header_table = Table([[img, company_info]], colWidths=[160, 359])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (1,0), (1,0), 'RIGHT'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ]))
        story.append(header_table)
    else:
        story.append(Paragraph("<b>VALIXIS TECHNOLOGIES</b>", title_style))
    
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#0f172a"), spaceBefore=1, spaceAfter=6))

    story.append(Paragraph("MASTER SERVICES AGREEMENT & STATEMENT OF WORK", title_style))
    story.append(Paragraph("Bespoke Web Platform, Direct UPI Ordering Engine & KDS Infrastructure", subtitle_style))

    # Parties Metadata Box
    meta_data = [
        [
            Paragraph("<b>SERVICE PROVIDER:</b>", body_bold),
            Paragraph("<b>VALIXIS TECHNOLOGIES</b> (Represented by Subhash, Founder & Lead)<br/>Hyderabad, Telangana, India  |  contact@valixis.tech", body_style)
        ],
        [
            Paragraph("<b>CLIENT ENTITY:</b>", body_bold),
            Paragraph("<b>[__________________________________________________]</b> (Cafe / Hospitality Entity)<br/>Registered Address: [__________________________________________________]<br/>Authorized Signatory: [________________________]  |  Designation: [___________]<br/>GSTIN / Tax ID: [___________________]  |  Contact: [_____________________]", body_style)
        ],
        [
            Paragraph("<b>PROJECT SCOPE:</b>", body_bold),
            Paragraph("Bespoke Web Portal, Interactive Digital Menu, Direct 1-Click UPI Dispatch & Barista KDS", body_style)
        ],
        [
            Paragraph("<b>EFFECTIVE DATE:</b>", body_bold),
            Paragraph("[____ / ____ / 2026] &nbsp;&nbsp;|&nbsp;&nbsp; <b>TARGET STAGING DATE:</b> 14 Calendar Days from Advance Receipt", body_style)
        ],
        [
            Paragraph("<b>TOTAL CONTRACT VALUE:</b>", body_bold),
            Paragraph("<b>₹ [____________________]</b> (INR) / <b>$ [__________]</b> (USD) &nbsp;+ Applicable Statutory Taxes", body_bold)
        ]
    ]

    meta_table = Table(meta_data, colWidths=[135, 384])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 0.8, border_color),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "This Master Services Agreement (\"Agreement\") is entered into by and between <b>VALIXIS TECHNOLOGIES</b> (\"Valixis\", \"Developer\"), and the client entity identified above (\"Client\"). "
        "WHEREAS, Client desires to retain Valixis to architect, design, develop, and deploy an enterprise-grade digital web portal and direct ordering engine; and "
        "WHEREAS, Valixis possesses proprietary expertise and engineering frameworks to deliver said digital solutions; "
        "NOW, THEREFORE, the parties agree to the following legally binding terms and conditions:",
        legal_clause_style
    ))
    story.append(Spacer(1, 4))

    # SECTION 1
    story.append(Paragraph("1. ENGAGEMENT & STATEMENT OF WORK (SOW)", h1_style))
    story.append(Paragraph(
        "1.1 <b>Scope of Engagement:</b> Valixis shall deliver the software engineering, UI/UX architecture, digital menu configuration, direct payment integration, and deployment services explicitly itemized in <b>Schedule A (Statement of Work)</b> of this Agreement.<br/>"
        "1.2 <b>Exhaustive Scope:</b> The deliverables detailed in Schedule A constitute the complete agreed scope. Any work, design modifications, integrations, or operational workflows not explicitly enumerated therein are out-of-scope and subject to Section 4.",
        legal_clause_style
    ))

    # SECTION 2
    story.append(Paragraph("2. COMMERCIAL TERMS & 50-30-20 MILESTONE PAYMENT SCHEDULE", h1_style))
    story.append(Paragraph(
        "2.1 <b>Milestone Structure:</b> All engineering mobilization and delivery adhere strictly to the following three-phase milestone payment framework. Work shall commence only upon receipt of cleared funds for Milestone 1:",
        legal_clause_style
    ))

    milestone_table_data = [
        [
            Paragraph("Milestone Phase", table_header_style),
            Paragraph("Billing %", table_header_style),
            Paragraph("Trigger Event & Criteria", table_header_style),
            Paragraph("Deliverable Released", table_header_style)
        ],
        [
            Paragraph("<b>M1: Mobilization Deposit</b>", table_cell_bold),
            Paragraph("<b>50%</b>", table_cell_bold),
            Paragraph("Signing of Agreement & Onboarding Kickoff", table_cell_style),
            Paragraph("Architecture lock, UI wireframes, staging sandbox setup. Non-refundable.", table_cell_style)
        ],
        [
            Paragraph("<b>M2: Staging Demo Approval</b>", table_cell_bold),
            Paragraph("<b>30%</b>", table_cell_bold),
            Paragraph("Interactive Staging URL deployment with active menu & ordering logic", table_cell_style),
            Paragraph("Review link access (`preview.valixis.com/client`), consolidated feedback cycle.", table_cell_style)
        ],
        [
            Paragraph("<b>M3: Production Cutover</b>", table_cell_bold),
            Paragraph("<b>20%</b>", table_cell_bold),
            Paragraph("Prior to live DNS cutover to Client domain", table_cell_style),
            Paragraph("Production DNS point, live PG key injection, administrative credentials handover.", table_cell_style)
        ]
    ]

    milestone_table = Table(milestone_table_data, colWidths=[120, 52, 182, 165])
    milestone_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0f172a")),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(milestone_table)
    story.append(Spacer(1, 3))
    story.append(Paragraph(
        "2.2 <b>Invoicing & Interest:</b> Invoices are due upon presentation. Overdue balances beyond seven (7) business days accrue interest at 1.5% per month or the statutory ceiling. Valixis reserves the right to suspend development or revoke staging access during delinquency.",
        legal_clause_style
    ))

    # ================= PAGE 2 =================
    story.append(PageBreak())

    # SECTION 3
    story.append(Paragraph("3. CLIENT COOPERATION & ASSET DELAY CLAUSE (7-DAY RULE)", h1_style))
    story.append(Paragraph(
        "3.1 <b>Asset Submission:</b> Client shall furnish all mandatory assets listed in <b>Schedule B</b> (logos, high-res photos, approved menu pricing, DNS credentials, payment gateway keys) within seven (7) business days of executing this Agreement.<br/>"
        "3.2 <b>Timeline Adjustment:</b> In the event Client fails to supply required assets, review sign-offs, or approvals within seven (7) business days, the agreed target completion date shall automatically extend on a day-for-day basis. If client delays exceed thirty (30) calendar days, Valixis may invoice for completed milestones and place the project on standby status subject to a reactivation fee.",
        legal_clause_style
    ))

    # SECTION 4
    story.append(Paragraph("4. REVISION LIMITS & SCOPE MANAGEMENT", h1_style))
    story.append(Paragraph(
        "4.1 <b>Included Revisions:</b> The Project fee includes two (2) consolidated rounds of styling, text, and layout feedback during the Milestone 2 Staging Phase. Feedback must be compiled in writing by the designated SPOC.<br/>"
        "4.2 <b>Out-of-Scope Alterations:</b> Requests involving architectural pivots, additional pages, third-party POS backend API syncs, or custom native application builds not listed in Schedule A shall be deemed a Change Order, billed at Valixis's standard rate of <b>₹2,500 / $45 per engineer-hour</b>, subject to a signed addendum.",
        legal_clause_style
    ))

    # SECTION 5
    story.append(Paragraph("5. INTELLECTUAL PROPERTY RIGHTS & CONDITIONAL TITLE TRANSFER", h1_style))
    story.append(Paragraph(
        "5.1 <b>Conditional Assignment:</b> Conditioned strictly upon receipt of <b>100% full and final payment</b> of all contracted sums, Valixis assigns to Client all right, title, and interest in and to the bespoke UI graphics, customized styling, and specific branded text content developed uniquely for Client.<br/>"
        "5.2 <b>Developer Retained IP:</b> Valixis retains exclusive ownership, copyright, and patent rights over all pre-existing code libraries, developer tools, algorithms, 3D shader routines, headless KDS dispatch wrappers, and reusable software boilerplates (\"Developer IP\"). Valixis grants Client an irrevocable, non-exclusive, perpetual, royalty-free license to use said Developer IP solely in conjunction with the live Project.<br/>"
        "5.3 <b>Promotional Rights:</b> Valixis reserves the right to showcase screenshots, live demonstrations, and performance metrics of the Project in its marketing case studies, awards, and digital portfolio.",
        legal_clause_style
    ))

    # SECTION 6
    story.append(Paragraph("6. PAYMENT GATEWAYS, DIRECT UPI & ZERO-CUSTODY ACKNOWLEDGMENT", h1_style))
    story.append(Paragraph(
        "6.1 <b>Direct Merchant Relationship:</b> Client explicitly agrees that all customer payment processing accounts (Razorpay, Cashfree, PhonePe, or UPI VPA) must be owned and KYC-verified directly in Client's name. <b>Valixis acts solely as a technical software integrator and at no point custodies, processes, handles, or holds customer funds.</b><br/>"
        "6.2 <b>Third-Party Outages:</b> Valixis shall not be held liable for losses or interruptions stemming from payment gateway downtimes, banking network latencies, SMS/WhatsApp delivery delays, or domain registrar suspensions outside Developer's direct control.",
        legal_clause_style
    ))

    # SECTION 7
    story.append(Paragraph("7. LIMITED WARRANTY & LIMITATION OF LIABILITY", h1_style))
    story.append(Paragraph(
        "7.1 <b>30-Day Bug-Fix Warranty:</b> Valixis provides a complimentary thirty (30) calendar day bug-fix warranty commencing on the official live launch date. During this period, Valixis shall promptly correct any software defects or broken links inconsistent with Schedule A specifications. This warranty excludes modifications made by Client or third-party API changes.<br/>"
        "7.2 <b>Liability Ceiling:</b> TO THE MAXIMUM EXTENT PERMITTED BY LAW, IN NO EVENT SHALL VALIXIS'S AGGREGATE FINANCIAL LIABILITY ARISING OUT OF THIS AGREEMENT EXCEED THE TOTAL PROJECT FEES ACTUALLY RECEIVED BY VALIXIS HEREUNDER. NEITHER PARTY SHALL BE LIABLE FOR INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES (INCLUDING LOST REVENUES OR REPUTATIONAL LOSS).",
        legal_clause_style
    ))

    # SECTION 8
    story.append(Paragraph("8. TERMINATION & KILL FEE", h1_style))
    story.append(Paragraph(
        "8.1 <b>Termination for Cause:</b> Either party may terminate upon written notice if the other party breaches a material obligation and fails to cure within fourteen (14) calendar days.<br/>"
        "8.2 <b>Convenience Termination / Kill Fee:</b> Should Client terminate for convenience prior to completion, the initial 50% mobilization deposit is strictly non-refundable as liquidated damages for allocated engineering availability, and Client shall immediately settle all unbilled milestone work completed up to the date of notice.",
        legal_clause_style
    ))

    # SECTION 9 & 10
    story.append(Paragraph("9. CONFIDENTIALITY & NON-DISCLOSURE", h1_style))
    story.append(Paragraph(
        "Both parties agree that all commercial pricing, customer metrics, technical system keys, and proprietary data shared during this engagement shall remain strictly confidential and shall not be divulged to any third party without express written permission.",
        legal_clause_style
    ))

    story.append(Paragraph("10. GOVERNING LAW & DISPUTE RESOLUTION", h1_style))
    story.append(Paragraph(
        "This Agreement shall be governed by and construed in accordance with the laws of India. Any controversy or dispute arising out of or relating to this Agreement that cannot be amicably resolved shall be submitted to the exclusive jurisdiction of the competent courts in <b>Hyderabad, Telangana</b>.",
        legal_clause_style
    ))

    # ================= PAGE 3 =================
    story.append(PageBreak())

    story.append(Paragraph("SCHEDULE A: STATEMENT OF WORK (SOW) SPECIFICATION", h1_style))
    story.append(Paragraph(
        "The following deliverables represent the complete, exhaustive project scope agreed for deployment:",
        legal_clause_style
    ))

    sow_data = [
        [
            Paragraph("Deliverable Module", table_header_style),
            Paragraph("Technical Specifications & Architecture", table_header_style),
            Paragraph("Verification Criteria", table_header_style)
        ],
        [
            Paragraph("<b>1. High-Performance Web Portal</b>", table_cell_bold),
            Paragraph("Responsive, mobile-first web app with custom brand gradients, hero section, brand story, visual gallery, and location maps.", table_cell_style),
            Paragraph("Lighthouse performance score 90+ on mobile & desktop audits.", table_cell_style)
        ],
        [
            Paragraph("<b>2. Interactive Digital Menu & Modifiers</b>", table_cell_bold),
            Paragraph("Complete digital menu categories, real-time item variants (e.g. Oat/Almond milk, roast origin, sweetness), and dietary indicators.", table_cell_style),
            Paragraph("All menu items rendered accurately with instant cart addition and price updates.", table_cell_style)
        ],
        [
            Paragraph("<b>3. Zero-Commission 1-Click UPI Engine</b>", table_cell_bold),
            Paragraph("Direct UPI deep-link / dynamic QR generation routing 100% of transaction amounts directly into Client's merchant account.", table_cell_style),
            Paragraph("Zero per-transaction commission cut deducted by developer or intermediary.", table_cell_style)
        ],
        [
            Paragraph("<b>4. Kitchen Display (KDS) Alert Dispatch</b>", table_cell_bold),
            Paragraph("Automated order notification modal that generates formatted order tickets for barista/counter staff via WhatsApp Business / SMS.", table_cell_style),
            Paragraph("Immediate ticket receipt containing items, table/takeaway number, and total.", table_cell_style)
        ],
        [
            Paragraph("<b>5. Technical SEO & OpenGraph Suite</b>", table_cell_bold),
            Paragraph("Production metadata, OpenGraph preview cards for WhatsApp/Instagram sharing, and favicon suite (16x16 up to 512x512).", table_cell_style),
            Paragraph("Social media link previews generate correct image, title, and description tags.", table_cell_style)
        ],
        [
            Paragraph("<b>6. 30-Day Stabilization Warranty</b>", table_cell_bold),
            Paragraph("Dedicated 30-day post-launch support addressing coding defects, layout adjustments, and broken hyperlinks.", table_cell_style),
            Paragraph("Fast-track resolution for any unexpected runtime bugs within 24 business hours.", table_cell_style)
        ]
    ]

    sow_table = Table(sow_data, colWidths=[125, 254, 140])
    sow_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0f172a")),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(sow_table)

    story.append(Spacer(1, 6))
    story.append(Paragraph("SCHEDULE B: MANDATORY CLIENT ONBOARDING CHECKLIST", h1_style))
    story.append(Paragraph(
        "Client shall deliver the following items to Valixis within seven (7) business days of execution to initiate development:",
        legal_clause_style
    ))

    checklist_items = [
        "1. High-resolution vector logo (.SVG or transparent .PNG format, lockup and standalone emblem).",
        "2. Final approved menu spreadsheet with retail pricing, item descriptions, dietary tags, and variant add-ons.",
        "3. High-resolution food, beverage, and cafe interior photography (minimum 2400x1600px resolution).",
        "4. DNS registrar credentials or Cloudflare delegated access for live domain cutover (e.g. `order.cafename.com`).",
        "5. Direct merchant UPI VPA handle (`brandname@bank`) or Payment Gateway API credentials (Key ID & Secret).",
        "6. Designate official Single Point of Contact (SPOC) with WhatsApp number for staging approval communication."
    ]
    for item in checklist_items:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{item}", legal_clause_style))

    story.append(Spacer(1, 8))

    # EXECUTION & SIGNATURE BLOCK
    story.append(Paragraph("EXECUTION & ACCEPTANCE SIGNATURES", h1_style))
    story.append(Paragraph(
        "IN WITNESS WHEREOF, the parties hereto have executed and accepted this Master Services Agreement & Statement of Work as of the Effective Date written above. Each signatory warrants they are authorized to legally bind their organization.",
        legal_clause_style
    ))
    story.append(Spacer(1, 6))

    sig_data = [
        [
            Paragraph("<b>FOR VALIXIS TECHNOLOGIES:</b>", body_bold),
            Paragraph("<b>FOR CLIENT:</b>", body_bold)
        ],
        [
            Paragraph("<br/><br/>____________________________________________________<br/>Authorized Signature", body_style),
            Paragraph("<br/><br/>____________________________________________________<br/>Authorized Signature", body_style)
        ],
        [
            Paragraph("<b>Name:</b> Subhash<br/><b>Title:</b> Founder & Lead<br/><b>Date:</b> [____ / ____ / 2026]<br/><b>Entity:</b> Valixis Technologies", body_style),
            Paragraph("<b>Name:</b> [___________________________________]<br/><b>Title:</b> [___________________________________]<br/><b>Date:</b> [____ / ____ / 2026]<br/><b>Entity:</b> [___________________________________]", body_style)
        ]
    ]

    sig_table = Table(sig_data, colWidths=[259, 260])
    sig_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.8, border_color),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(sig_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF Successfully Generated: {filename} ({os.path.getsize(filename)} bytes)")

if __name__ == "__main__":
    build_pdf()
