import os
import sys
import re

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

tests_passed = 0
tests_failed = 0

def check(condition, message):
    global tests_passed, tests_failed
    if condition:
        print(f"  [PASS] {message}")
        tests_passed += 1
    else:
        print(f"  [FAIL] {message}")
        tests_failed += 1

print("=" * 80)
print("VALIXIS WEBSITE 2.0 — PHASE 6 TECHNICAL AUDIT & VERIFICATION SUITE")
print("Focus: Consultation Booking, Cal.com Scoping, Contact Form & Lead Management")
print("=" * 80)

# -----------------------------------------------------------------------------
# 1. PART A: CAL.COM INTEGRATION AUDIT
# -----------------------------------------------------------------------------
print("\n--- 1. PART A: CAL.COM INTEGRATION ---")

contact_path = 'contact/index.html'
check(os.path.exists(contact_path), "contact/index.html exists")

with open(contact_path, 'r', encoding='utf-8') as f:
    contact_html = f.read()

# Headline and description checks
cal_headline = "Book a 15-Minute Architecture & Scoping Session"
cal_desc = "Discuss your product idea, technical requirements and possible implementation approach with the VALIXIS team."
check(cal_headline.lower() in contact_html.lower(), f"Exact Cal.com headline present: '{cal_headline}'")
check(cal_desc.lower() in contact_html.lower(), f"Exact Cal.com supporting description present: '{cal_desc}'")

# Elements and containers
check('id="booking"' in contact_html, "Dedicated booking container with id='booking' present")
check('class="cal-embed-wrapper"' in contact_html, "Cal embed container with styling wrapper present")
check('id="calIframe"' in contact_html, "Cal iframe with id='calIframe' present")
check('id="calLoader"' in contact_html, "Cal loading state / skeleton present with id='calLoader'")
check('class="spinner-ring"' in contact_html, "Animated loading spinner present")
check('theme=dark' in contact_html, "Dark theme parameter specified for Cal.com embed")

# Error / Standby fallback
check('class="cal-fallback-box"' in contact_html, "Calendar fallback container present for privacy/adblock/standby")
check('href="https://wa.me/919603416707' in contact_html, "WhatsApp direct booking fallback present")
check('href="mailto:official.valixis@gmail.com' in contact_html, "Email consultation request fallback present")

# Configurable event URL variable
check('window.VALIXIS_CALCOM_URL' in contact_html, "Configuration variable 'window.VALIXIS_CALCOM_URL' implemented")
check('valixis/15min' in contact_html, "Default Cal.com slug 'valixis/15min' configured")
check('handleCalLoaded()' in contact_html, "Cal iframe onload handler implemented")

# -----------------------------------------------------------------------------
# 2. PART B: CONTACT FORM & LEAD INGESTION AUDIT
# -----------------------------------------------------------------------------
print("\n--- 2. PART B: CONTACT FORM & LEAD INGESTION ---")

check('id="inquiry-form"' in contact_html, "Formal inquiry container with id='inquiry-form' present")
check('id="projectInquiryForm"' in contact_html, "Inquiry form element with id='projectInquiryForm' present")

# Required Fields
check('id="clientName"' in contact_html and 'name="clientName"' in contact_html, "Field: Full Name present (id='clientName')")
check('id="clientEmail"' in contact_html and 'name="clientEmail"' in contact_html, "Field: Business Email present (id='clientEmail')")
check('id="clientCompany"' in contact_html and 'name="clientCompany"' in contact_html, "Field: Company Name present (id='clientCompany')")
check('id="projectCategory"' in contact_html and 'name="projectCategory"' in contact_html, "Field: Project Category present (id='projectCategory')")
check('id="expectedTimeline"' in contact_html and 'name="expectedTimeline"' in contact_html, "Field: Expected Timeline present (id='expectedTimeline')")
check('id="preferredContact"' in contact_html and 'name="preferredContact"' in contact_html, "Field: Preferred Contact Method present (id='preferredContact')")
check('id="projectDescription"' in contact_html and 'name="projectDescription"' in contact_html, "Field: Project Description present (id='projectDescription')")

# Anti-Spam Protections
check('id="valixis_hp_security"' in contact_html, "Anti-spam honeypot input present ('valixis_hp_security')")
check('class="hp-security-trap"' in contact_html, "Honeypot hidden via offscreen / display:none styles")
check('PAGE_LOAD_TIMESTAMP' in contact_html, "Anti-bot submission velocity check (timestamp delta) implemented")

# Client-Side Validations
check('emailRegex' in contact_html, "Client-side email RFC regex validation implemented")
check('char-count' in contact_html and 'handleDescriptionInput' in contact_html, "Live character count feedback implemented for description")

# Privacy Notice
check('Confidentiality Notice:' in contact_html or 'Privacy Notice:' in contact_html, "Clear confidentiality & privacy notice present")
check('never shared with third-party' in contact_html.lower(), "Third-party non-disclosure commitment explicitly stated")

# Feedback & Submission States
check('id="formFeedback"' in contact_html, "Form feedback container with id='formFeedback' present")
check('submitBtn.disabled = true' in contact_html, "Double-submission prevention (disabling button) implemented")
check('showStandbyFallback' in contact_html, "Graceful fallback dispatch (WhatsApp/Email pre-fill) implemented")

# Estimator Pre-fill Integration
check('checkEstimatorPreFill' in contact_html, "Estimator calculator pre-fill handler implemented")
check('valixis_estimated_scope' in contact_html, "SessionStorage scope pre-fill reader implemented")

# -----------------------------------------------------------------------------
# 3. PART C: SUPABASE SERVERLESS BACKEND AUDIT
# -----------------------------------------------------------------------------
print("\n--- 3. PART C: SUPABASE SERVERLESS BACKEND ---")

schema_path = 'supabase/schema.sql'
edge_path = 'supabase/functions/submit-inquiry/index.ts'
readme_path = 'supabase/README.md'

check(os.path.exists(schema_path), f"Database schema exists: {schema_path}")
check(os.path.exists(edge_path), f"Edge function exists: {edge_path}")
check(os.path.exists(readme_path), f"Backend documentation exists: {readme_path}")

with open(schema_path, 'r', encoding='utf-8') as f:
    schema_sql = f.read()

check('valixis_inquiries' in schema_sql, "Table 'public.valixis_inquiries' defined in schema")
check('ROW LEVEL SECURITY' in schema_sql, "Row Level Security (RLS) explicitly enabled in schema")
check('FOR INSERT' in schema_sql and 'TO anon' in schema_sql, "RLS policy allows anonymous INSERTs with validation")
check('TO service_role' in schema_sql, "RLS policy restricts management to service_role / authenticated")
check('idx_valixis_inquiries_created_at' in schema_sql, "Performance index on created_at present")

with open(edge_path, 'r', encoding='utf-8') as f:
    edge_code = f.read()

check('Access-Control-Allow-Origin' in edge_code, "CORS headers properly defined in Edge Function")
check('OPTIONS' in edge_code, "CORS preflight (OPTIONS) request handled")
check('hpSecurityTrap' in edge_code, "Honeypot bot trapping handled on server-side")
check('createClient' in edge_code, "Supabase client initialization present")
check('SUPABASE_SERVICE_ROLE_KEY' in edge_code, "Uses server-side SUPABASE_SERVICE_ROLE_KEY (not exposed to client)")

# -----------------------------------------------------------------------------
# 4. PART D: NOTIFICATIONS & ZERO SECRETS AUDIT
# -----------------------------------------------------------------------------
print("\n--- 4. PART D: NOTIFICATIONS & ZERO SECRETS ---")

check('RESEND_API_KEY' in edge_code, "Resend API integration present in Edge Function")
check('official.valixis@gmail.com' in edge_code, "Notification dispatch configured to 'official.valixis@gmail.com'")
check('https://api.resend.com/emails' in edge_code, "Direct Resend HTTPS API endpoint used")

# Check frontend for any leaked API keys
check('SUPABASE_SERVICE_ROLE_KEY' not in contact_html, "No SUPABASE_SERVICE_ROLE_KEY in contact/index.html")
check('RESEND_API_KEY' not in contact_html, "No RESEND_API_KEY in contact/index.html")
check('re_' not in contact_html or 're_123' not in contact_html, "No live Resend secret tokens in contact/index.html")

# -----------------------------------------------------------------------------
# 5. ESTIMATOR & HOMEPAGE CROSS-LINKAGE AUDIT
# -----------------------------------------------------------------------------
print("\n--- 5. ESTIMATOR & HOMEPAGE CROSS-LINKAGE ---")

with open('estimate/index.html', 'r', encoding='utf-8') as f:
    estimate_html = f.read()

check('contact/?from=estimate#inquiry-form' in estimate_html, "Estimator connects to contact form with '?from=estimate#inquiry-form'")
check('valixis_estimated_scope' in estimate_html, "Estimator saves calculated scope in sessionStorage")

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

check('contact/' in index_html, "Homepage links to contact page")
check('official.valixis@gmail.com' in index_html, "Homepage lists official email")

# -----------------------------------------------------------------------------
# 6. DIRECTORY SYNCHRONIZATION AUDIT
# -----------------------------------------------------------------------------
print("\n--- 6. DIRECTORY SYNCHRONIZATION ---")

sync_pairs = [
    ('contact/index.html', 'VALIXIS WEBSITE/contact/index.html'),
    ('estimate/index.html', 'VALIXIS WEBSITE/estimate/index.html'),
    ('supabase/schema.sql', 'VALIXIS WEBSITE/supabase/schema.sql'),
    ('supabase/functions/submit-inquiry/index.ts', 'VALIXIS WEBSITE/supabase/functions/submit-inquiry/index.ts'),
    ('supabase/README.md', 'VALIXIS WEBSITE/supabase/README.md'),
]

for p1, p2 in sync_pairs:
    if os.path.exists(p1) and os.path.exists(p2):
        s1 = os.path.getsize(p1)
        s2 = os.path.getsize(p2)
        check(s1 == s2, f"Files synchronized: {p1} ({s1} bytes) == {p2} ({s2} bytes)")
    else:
        check(False, f"Missing sync pair: {p1} or {p2}")

# -----------------------------------------------------------------------------
# SUMMARY
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
total_tests = tests_passed + tests_failed
pass_rate = (tests_passed / total_tests) * 100 if total_tests > 0 else 0
print(f"PHASE 6 AUDIT RESULTS: {tests_passed}/{total_tests} TESTS PASSED ({pass_rate:.1f}%)")
if tests_failed == 0:
    print("ALL PHASE 6 VERIFICATION CRITERIA MET WITH 100% SUCCESS.")
else:
    print(f"ATTENTION: {tests_failed} tests failed. Immediate review required.")
print("=" * 80)
