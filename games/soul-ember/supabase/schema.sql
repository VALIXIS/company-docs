-- ==============================================================================
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
    business_email TEXT NOT NULL CHECK (business_email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
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
        business_email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' AND
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
