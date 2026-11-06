// ==============================================================================
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

    const emailRegex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
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
