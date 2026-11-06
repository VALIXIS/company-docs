# VALIXIS Technologies — Serverless Backend Integration Guide
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
