# Professional Client Website Handover Guide

> **Based on Insights from:** [@sohail_systems](https://www.instagram.com/reel/DfUR9qLzkhf/)  
> **Topic:** *What to do after completing a client project? (Beginner vs. Pro Handover)*  
> **Core Objective:** Safely and completely transfer ownership, infrastructure, and technical assets to the client to ensure self-sufficiency and avoid post-launch legal liabilities.

---

## 1. Executive Summary: The Beginner Trap vs. The Pro Standard

In freelance web development and agency work, getting paid and launching a website is only half the battle. A critical distinction separates novice developers from seasoned professionals:

| Stage | The Beginner Mistake | The Professional Standard |
| :--- | :--- | :--- |
| **Mindset** | "I finished the site, got paid, and I'm done!" | "The project is only complete once the client fully owns and controls every asset." |
| **Account Ownership** | Uses personal accounts/emails to register domains, hosting, and services. | Requires the client's email/account upfront or executes an official transfer. |
| **Ongoing Costs** | Gets hit with surprise hosting/domain renewal invoices on personal credit cards. | Client directly owns all subscription accounts and pays all vendor invoices. |
| **Legal & Liability** | Developer remains legally tied to domain/infrastructure, open to disputes. | Complete separation of liability; ownership transferred with written sign-off. |
| **Documentation** | Leaves client with zero instructions, leading to endless support pings. | Provides a structured Handover Document with credentials, tech stack, and videos. |

---

## 2. Comprehensive 5-Pillar Handover Protocol

### Pillar 1: Domain Name & DNS Transfer
* **The Rule:** You must never retain legal ownership of a client's primary brand asset.
* **Key Actions:**
  1. **Registrar Transfer:** If purchased on Namecheap, GoDaddy, Cloudflare Registrar, Porkbun, or Google/Squarespace, initiate an account-to-account push/transfer.
  2. **Registrant Contact Info:** Verify that the WHOIS/Registrant contact displays the client's legal business name and primary email address.
  3. **Payment Method:** Ensure the client has their own payment card attached for automatic annual renewals.

---

### Pillar 2: Hosting & Compute Infrastructure
* **Platforms Mentioned:** Vercel, Railway, Netlify, DigitalOcean, AWS, VPS.
* **The Rule:** The client must own the hosting workspace and be directly billed for usage.
* **Key Actions:**
  1. **Workspace / Team Transfer:** Transfer the project to the client's personal or team account on Vercel, Railway, etc.
  2. **Billing Setup:** Ensure the client adds their own payment method to cover compute, bandwidth, and add-ons.
  3. **Role Assignment:** Downgrade developer access from Primary Owner to Admin/Collaborator (or remove entirely upon final sign-off).

---

### Pillar 3: Source Code & Repository (Git)
* **Platforms:** GitHub, GitLab, Bitbucket.
* **The Rule:** The client must own the intellectual property (IP) and the canonical codebase repository.
* **Key Actions:**
  1. **Repository Transfer:** In GitHub, navigate to **Settings → General → Danger Zone → Transfer Ownership**, then transfer to the client's GitHub username or Organization.
  2. **Clean Repository:** Remove temporary branches, test keys, and personal commit artifacts.
  3. **Deployment Integration:** Re-link the newly transferred GitHub repository to the client's hosting platform (Vercel/Railway) for automated CI/CD deployments.

---

### Pillar 4: Third-Party Services & Integrations
* **Services Mentioned:** Cloudflare, Google Analytics, Payment Processors, etc.
* **Checklist of External Accounts to Transfer/Assign:**
  * [ ] **Cloudflare / DNS Management:** Invite client as Super Administrator; transfer zone ownership.
  * [ ] **Google Analytics & GTM:** Grant client "Administrator" role on the GA4 property and Tag Manager container.
  * [ ] **Payment Gateways (Stripe, Razorpay, PayPal):** Ensure the account is under the client's corporate identity with their payout bank account attached.
  * [ ] **Transactional Email (Resend, SendGrid, Postmark):** Transfer team ownership or ensure API keys are tied to the client’s domain authentication (DKIM, SPF, DMARC).
  * [ ] **Headless CMS / Database (Supabase, Sanity, Strapi):** Transfer project ownership to client organization.

---

### Pillar 5: The Master Handover Document
A successful handover culminates in a single master document delivered to the client.

#### What Must Be Included:
1. **Asset Directory & Dashboard Links:**
   * Direct login URLs for domain registrar, hosting dashboard, database, and analytics.
2. **Access Credentials & Account Details:**
   * Login usernames, instructions for password resets, and invite acceptance links (delivered securely via Bitwarden/1Password or direct invite).
3. **Environment Variables (`.env`):**
   * Clear list of all required environment variables (`DATABASE_URL`, `PUBLIC_API_KEY`, etc.) with descriptions of what each key does.
4. **Technology Stack Specification:**
   * Frameworks, libraries, node version, database engine, and third-party APIs used.
5. **Operational Guide & Walkthrough Videos:**
   * Step-by-step instructions on:
     * How to edit copy or update content.
     * How to trigger or verify a deployment.
     * How to check analytics and form submissions.
   * Short 3–5 minute Loom or recorded screen walkthroughs demonstrating the dashboard.

---

## 3. Legal Protection & Offboarding Best Practices

* **Avoid Legal Complications:** Keeping a client's site on your personal hosting makes you liable for downtime, copyright infringement, data breaches, or billing lapses.
* **Final Sign-Off Form:** Issue a formal acceptance form where the client acknowledges receipt of all assets, verifies that the site meets contractual requirements, and accepts ownership.
* **Maintenance & Support Boundaries:** Clearly delineate where complimentary launch support ends and where paid retainer/maintenance begins.

---

## 4. Reusable Client Handover Checklist Template

```markdown
# Project Handover Checklist: [Client Name / Project Name]

Date: [YYYY-MM-DD]
Lead Developer: [Your Name]
Client Representative: [Client Name & Email]

### 1. Domain & DNS
- [ ] Domain transferred to client registrar account
- [ ] WHOIS contact details updated to client's legal entity
- [ ] Client credit card added for auto-renewal
- [ ] DNS records (A, CNAME, MX, TXT) verified and active

### 2. Hosting & Compute (e.g., Vercel / Railway)
- [ ] Hosting project transferred to client account/team
- [ ] Client billing information configured
- [ ] Custom domain linked with active SSL certificate
- [ ] Automatic deployments verified upon push to `main`

### 3. Codebase & Git
- [ ] GitHub repository transferred to client organization
- [ ] Master/Main branch protection rules configured
- [ ] Developer access adjusted or offboarded

### 4. Third-Party Integrations
- [ ] Cloudflare / CDN access transferred
- [ ] Google Analytics 4 & Search Console ownership granted
- [ ] Stripe / Payment Gateway in live production mode
- [ ] Email service (Resend / SendGrid) domain verification completed

### 5. Documentation & Deliverables
- [ ] Master Handover Document delivered
- [ ] `.env.example` and production environment secrets documented
- [ ] Screen recording / video walkthrough provided
- [ ] Final sign-off received and contract closed
```
