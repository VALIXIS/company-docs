import os
import shutil

SCHEMA_SQL = """-- ==============================================================================
-- VALIXIS Technologies — Lead Inquiries & Consultation Bookings Schema
-- Version: 2.0 (Phase 6 Architecture)
-- Compatibility: Supabase / PostgreSQL 15+
-- ==============================================================================

-- Create schema extension for UUID generation if not already active
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Table: valixis_inquiries
CREATE TABLE IF NOT EXISTS public.valixis_inquiries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    full_name TEXT NOT NULL CHECK (char_length(trim(full_name)) >= 2 AND char_length(full_name) <= 120),
    business_email TEXT NOT NULL CHECK (business_email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'),
    company_name TEXT CHECK (char_length(company_name) <= 150),
    project_category TEXT NOT NULL CHECK (char_length(project_category) >= 3 AND char_length(project_category) <= 100),
    project_description TEXT NOT NULL CHECK (char_length(trim(project_description)) >= 10 AND char_length(project_description) <= 5000),
    expected_timeline TEXT CHECK (char_length(expected_timeline) <= 100),
    preferred_contact TEXT NOT NULL DEFAULT 'Email' CHECK (preferred_contact IN ('Email', 'WhatsApp', 'Direct Phone Call', 'Flexible')),
    status TEXT NOT NULL DEFAULT 'new' CHECK (status IN ('new', 'under_review', 'consultation_scheduled', 'proposal_sent', 'closed_won', 'archived')),
    ip_address TEXT,
    user_agent TEXT,
    notes TEXT
);

-- Comments for documentation & API generation
COMMENT ON TABLE public.valixis_inquiries IS 'Commercial lead inquiries and architecture scoping submissions for VALIXIS Technologies.';
COMMENT ON COLUMN public.valixis_inquiries.status IS 'Workflow triage status: new, under_review, consultation_scheduled, proposal_sent, closed_won, archived.';

-- Indices for performance
CREATE INDEX IF NOT EXISTS idx_valixis_inquiries_created_at ON public.valixis_inquiries (created_at DESC);
CREATE INDEX IF NOT EXISTS idx_valixis_inquiries_status ON public.valixis_inquiries (status);
CREATE INDEX IF NOT EXISTS idx_valixis_inquiries_email ON public.valixis_inquiries (business_email);

-- Enable Row Level Security (RLS)
ALTER TABLE public.valixis_inquiries ENABLE ROW LEVEL SECURITY;

-- ------------------------------------------------------------------------------
-- POLICIES (Least Privilege Security Model)
-- ------------------------------------------------------------------------------

-- 1. Anonymous Users: Allow insertion of new inquiries only
--    Anonymous visitors cannot read, update, or delete inquiries.
CREATE POLICY "Allow public anon inserts with valid data"
    ON public.valixis_inquiries
    FOR INSERT
    TO anon
    WITH CHECK (
        char_length(trim(full_name)) >= 2 AND
        business_email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$' AND
        char_length(trim(project_description)) >= 10
    );

-- 2. Authenticated Admin / Service Role: Full read and update permissions
CREATE POLICY "Allow service role full management"
    ON public.valixis_inquiries
    FOR ALL
    TO service_role
    USING (true)
    WITH CHECK (true);

-- 3. Authenticated Users (Executive Dashboard): Read and update triage status
CREATE POLICY "Allow authenticated staff to read inquiries"
    ON public.valixis_inquiries
    FOR SELECT
    TO authenticated
    USING (true);

CREATE POLICY "Allow authenticated staff to update inquiry status"
    ON public.valixis_inquiries
    FOR UPDATE
    TO authenticated
    USING (true)
    WITH CHECK (true);
"""

EDGE_FUNCTION_TS = """// ==============================================================================
// VALIXIS Technologies — Edge Function: submit-inquiry
// Runtime: Supabase Edge Runtime / Deno
// Purpose: Validates lead inquiries, stores in DB via service role,
//          and dispatches executive notification via Resend API.
// ==============================================================================

import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.39.0";

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

interface InquiryPayload {
  fullName: string;
  businessEmail: string;
  companyName?: string;
  projectCategory: string;
  projectDescription: string;
  expectedTimeline?: string;
  preferredContact: string;
  hpSecurityTrap?: string; // Honeypot field
  submissionTimeDelta?: number; // Anti-bot timestamp check (ms)
}

serve(async (req: Request) => {
  // Handle CORS preflight
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: CORS_HEADERS });
  }

  if (req.method !== "POST") {
    return new Response(JSON.stringify({ error: "Method not allowed. Use POST." }), {
      status: 405,
      headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
    });
  }

  try {
    const body: InquiryPayload = await req.json();

    // 1. Honeypot check (Silent decoy response for bots)
    if (body.hpSecurityTrap && body.hpSecurityTrap.trim() !== "") {
      console.warn("Bot submission detected via honeypot trap. Simulating success.");
      return new Response(
        JSON.stringify({
          success: true,
          message: "Inquiry received. Feasibility assessment pending.",
        }),
        { headers: { ...CORS_HEADERS, "Content-Type": "application/json" }, status: 200 }
      );
    }

    // 2. Submission speed check (Human users take > 2 seconds to complete form)
    if (typeof body.submissionTimeDelta === "number" && body.submissionTimeDelta < 1500) {
      console.warn("Rapid automated submission detected (<1.5s). Rejecting.");
      return new Response(
        JSON.stringify({ error: "Submission velocity flagged. Please complete the form manually." }),
        { headers: { ...CORS_HEADERS, "Content-Type": "application/json" }, status: 429 }
      );
    }

    // 3. Strict Input Validation
    const fullName = (body.fullName || "").trim();
    const businessEmail = (body.businessEmail || "").trim().toLowerCase();
    const companyName = (body.companyName || "").trim();
    const projectCategory = (body.projectCategory || "").trim();
    const projectDescription = (body.projectDescription || "").trim();
    const expectedTimeline = (body.expectedTimeline || "").trim();
    const preferredContact = (body.preferredContact || "Email").trim();

    if (!fullName || fullName.length < 2) {
      return new Response(JSON.stringify({ error: "Please provide your full name (minimum 2 characters)." }), {
        status: 400,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      });
    }

    const emailRegex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$/;
    if (!emailRegex.test(businessEmail)) {
      return new Response(JSON.stringify({ error: "Please enter a valid business email address." }), {
        status: 400,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      });
    }

    if (!projectCategory) {
      return new Response(JSON.stringify({ error: "Please select a project category." }), {
        status: 400,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      });
    }

    if (!projectDescription || projectDescription.length < 10) {
      return new Response(JSON.stringify({ error: "Please provide a project description (minimum 10 characters)." }), {
        status: 400,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      });
    }

    // 4. Initialize Supabase Admin Client
    const supabaseUrl = Deno.env.get("SUPABASE_URL") ?? "";
    const supabaseServiceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "";

    if (!supabaseUrl || !supabaseServiceKey) {
      console.error("Missing SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY in environment.");
      return new Response(
        JSON.stringify({ error: "Backend serverless configuration incomplete." }),
        { status: 500, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } }
      );
    }

    const supabase = createClient(supabaseUrl, supabaseServiceKey);

    // Extract client metadata for audit trail
    const ipAddress = req.headers.get("x-forwarded-for") || req.headers.get("cf-connecting-ip") || "unknown";
    const userAgent = req.headers.get("user-agent") || "unknown";

    // 5. Insert Record into public.valixis_inquiries
    const { data, error: dbError } = await supabase
      .from("valixis_inquiries")
      .insert({
        full_name: fullName,
        business_email: businessEmail,
        company_name: companyName || null,
        project_category: projectCategory,
        project_description: projectDescription,
        expected_timeline: expectedTimeline || null,
        preferred_contact: preferredContact,
        ip_address: ipAddress,
        user_agent: userAgent,
        status: "new",
      })
      .select("id, created_at")
      .single();

    if (dbError) {
      console.error("Database insertion failure:", dbError);
      return new Response(JSON.stringify({ error: "Failed to store inquiry in database." }), {
        status: 500,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      });
    }

    // 6. Optional Notification Dispatch via Resend API
    const resendApiKey = Deno.env.get("RESEND_API_KEY");
    if (resendApiKey) {
      try {
        const emailHtml = `
          <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; margin: 0 auto; background: #0D1117; color: #F1F5F9; border-radius: 12px; padding: 32px; border: 1px solid rgba(0, 217, 255, 0.3);">
            <div style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 16px; margin-bottom: 24px;">
              <h2 style="color: #00D9FF; margin: 0; font-size: 20px; text-transform: uppercase; letter-spacing: 1px;">VALIXIS Lead Notification</h2>
              <p style="color: #94A3B8; margin: 6px 0 0 0; font-size: 13px;">New Architecture Inquiry Logged &bull; ID: ${data.id}</p>
            </div>
            
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 24px;">
              <tr>
                <td style="padding: 8px 0; color: #94A3B8; font-size: 14px; width: 140px;">Client Name:</td>
                <td style="padding: 8px 0; color: #FFFFFF; font-weight: 600; font-size: 14px;">${fullName}</td>
              </tr>
              <tr>
                <td style="padding: 8px 0; color: #94A3B8; font-size: 14px;">Business Email:</td>
                <td style="padding: 8px 0; color: #00D9FF; font-size: 14px;"><a href="mailto:${businessEmail}" style="color: #00D9FF; text-decoration: none;">${businessEmail}</a></td>
              </tr>
              <tr>
                <td style="padding: 8px 0; color: #94A3B8; font-size: 14px;">Company:</td>
                <td style="padding: 8px 0; color: #FFFFFF; font-size: 14px;">${companyName || "Not provided"}</td>
              </tr>
              <tr>
                <td style="padding: 8px 0; color: #94A3B8; font-size: 14px;">Project Category:</td>
                <td style="padding: 8px 0; color: #FF2ED6; font-weight: 600; font-size: 14px;">${projectCategory}</td>
              </tr>
              <tr>
                <td style="padding: 8px 0; color: #94A3B8; font-size: 14px;">Expected Timeline:</td>
                <td style="padding: 8px 0; color: #FFFFFF; font-size: 14px;">${expectedTimeline || "Flexible / Not specified"}</td>
              </tr>
              <tr>
                <td style="padding: 8px 0; color: #94A3B8; font-size: 14px;">Preferred Contact:</td>
                <td style="padding: 8px 0; color: #3B82F6; font-weight: 600; font-size: 14px;">${preferredContact}</td>
              </tr>
            </table>

            <div style="background: rgba(20, 26, 36, 0.9); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 18px; margin-bottom: 24px;">
              <h4 style="color: #94A3B8; font-size: 12px; text-transform: uppercase; margin: 0 0 10px 0;">Project Scope & Description:</h4>
              <p style="color: #F1F5F9; font-size: 14px; line-height: 1.6; white-space: pre-wrap; margin: 0;">${projectDescription}</p>
            </div>

            <div style="text-align: center; padding-top: 16px; border-top: 1px solid rgba(255, 255, 255, 0.1);">
              <a href="mailto:${businessEmail}?subject=Re:%20VALIXIS%20Consultation%20—%20${encodeURIComponent(projectCategory)}" style="background: linear-gradient(135deg, #00D9FF 0%, #3B82F6 100%); color: #000; font-weight: bold; text-decoration: none; padding: 10px 24px; border-radius: 6px; font-size: 13px; display: inline-block;">Reply to Client</a>
            </div>
          </div>
        `;

        await fetch("https://api.resend.com/emails", {
          method: "POST",
          headers: {
            "Authorization": `Bearer ${resendApiKey}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            from: "VALIXIS System <notifications@resend.dev>", // Or verified domain e.g. inquiries@valixis.tech
            to: ["official.valixis@gmail.com"],
            reply_to: businessEmail,
            subject: `[VALIXIS Lead] ${projectCategory} — ${fullName}`,
            html: emailHtml,
          }),
        });
        console.log("Resend notification dispatched successfully.");
      } catch (emailErr) {
        console.error("Resend dispatch failure (inquiry was still stored):", emailErr);
      }
    } else {
      console.log("RESEND_API_KEY not configured. Skipping automated email alert.");
    }

    return new Response(
      JSON.stringify({
        success: true,
        message: "Your inquiry has been successfully registered. Our technical team will review your specifications.",
        inquiryId: data.id,
      }),
      {
        status: 200,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      }
    );
  } catch (err: any) {
    console.error("Unexpected serverless execution error:", err);
    return new Response(
      JSON.stringify({ error: "Internal processing error: " + (err.message || "Unknown error") }),
      { status: 500, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } }
    );
  }
});
"""

SUPABASE_README = """# VALIXIS Technologies — Serverless Backend Integration Guide
**Phase 6 Architecture: Lead Management, Cal.com Scoping, and Inquiry Ingestion**

This directory contains the production-grade database schema and serverless Edge Function for handling lead inquiries and consultation booking coordination for **valixis.tech**.

---

## 1. Architecture Overview

```
Visitor Browser (valixis.tech/contact/)
   │
   ├─► [Honeypot & Velocity Check] (Client-side anti-spam)
   │
   ├─► POST JSON to Supabase Edge Function: `submit-inquiry`
   │      │
   │      ├─► Server-Side Validation & Sanitization
   │      │
   │      ├─► Insert into PostgreSQL: `public.valixis_inquiries` (RLS Protected)
   │      │
   │      └─► Dispatch Alert via Resend API to `official.valixis@gmail.com`
   │
   └─► Instant Fallback: WhatsApp / Email Direct Dispatch (Zero Lead Loss)
```

---

## 2. Setup Instructions

### Step 1: Execute SQL Schema
1. Log in to your [Supabase Dashboard](https://supabase.com/dashboard).
2. Select your project and navigate to the **SQL Editor**.
3. Open [`schema.sql`](./schema.sql), copy its contents, and run it.
4. This creates the `valixis_inquiries` table with appropriate indexes and strict Row Level Security (RLS) policies:
   - `anon` role can ONLY perform INSERT operations on validated fields.
   - `service_role` and authenticated staff maintain full administrative read/update rights.

### Step 2: Deploy the Supabase Edge Function
1. Install Supabase CLI if you haven't already:
   ```bash
   npm install -g supabase
   ```
2. Link your local directory to your Supabase project:
   ```bash
   supabase link --project-ref <YOUR_PROJECT_ID>
   ```
3. Deploy the `submit-inquiry` function:
   ```bash
   supabase functions deploy submit-inquiry --no-verify-jwt
   ```

### Step 3: Configure Server Secrets (Email Notifications)
Set your Resend API key in Supabase Secrets (never expose this in frontend code):
```bash
supabase secrets set RESEND_API_KEY="re_1234567890abcdef"
```
*(Optional: If you use a custom domain on Resend, update the `from:` address in `index.ts` to `inquiries@valixis.tech`)*

### Step 4: Configure the Frontend Client
In `contact/index.html`, locate the configuration block:
```javascript
window.VALIXIS_SUPABASE_ENDPOINT = "https://<YOUR_PROJECT_ID>.supabase.co/functions/v1/submit-inquiry";
window.VALIXIS_CALCOM_URL = "valixis/15min";
```
Replace `<YOUR_PROJECT_ID>` with your live Supabase project ID.

---

## 3. Security Highlights
- **Zero Exposed Secrets:** Service role keys and email dispatch API keys reside exclusively in Supabase environment secrets.
- **Bot Mitigation:** Uses a dual defense strategy — a hidden CSS honeypot trap (`valixis_hp_security`) plus a minimum submission time velocity threshold (>1.5s).
- **Graceful Client Fallback:** If the visitor is offline or Supabase backend is undergoing maintenance, the form automatically pre-packages the inquiry for 1-click WhatsApp (`+91 9603416707`) and Email (`official.valixis@gmail.com`) dispatch. No customer inquiry is ever dropped.
"""

def main():
    paths = ['supabase', 'VALIXIS WEBSITE/supabase']
    for p in paths:
        os.makedirs(f"{p}/functions/submit-inquiry", exist_ok=True)
        with open(f"{p}/schema.sql", 'w', encoding='utf-8') as f:
            f.write(SCHEMA_SQL)
        with open(f"{p}/functions/submit-inquiry/index.ts", 'w', encoding='utf-8') as f:
            f.write(EDGE_FUNCTION_TS)
        with open(f"{p}/README.md", 'w', encoding='utf-8') as f:
            f.write(SUPABASE_README)
        print(f"Generated backend files in {p}")

if __name__ == '__main__':
    main()
