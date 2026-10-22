/**
 * VALIXIS Product & Engineering Portfolio - Main Application Logic
 * Interactive SaaS simulator, 3D card tilt physics, ROI estimator, and modal deep-dives
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Toggle
  const mobileToggle = document.getElementById('mobileMenuToggle');
  const navLinks = document.getElementById('navLinks');
  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      const isVisible = navLinks.style.display === 'flex';
      navLinks.style.display = isVisible ? 'none' : 'flex';
      if (!isVisible) {
        navLinks.style.flexDirection = 'column';
        navLinks.style.position = 'absolute';
        navLinks.style.top = '100%';
        navLinks.style.left = '0';
        navLinks.style.width = '100%';
        navLinks.style.background = 'rgba(11, 15, 25, 0.98)';
        navLinks.style.padding = '1.5rem';
        navLinks.style.borderRadius = '0 0 16px 16px';
        navLinks.style.border = '1px solid rgba(255,255,255,0.1)';
      }
    });
  }

  // 2. 3D Tilt Effect on Case Study Cards
  const tiltCards = document.querySelectorAll('.tilt-card');
  tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      
      const rotateX = ((y - centerY) / centerY) * -8;
      const rotateY = ((x - centerX) / centerX) * 8;
      
      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0)';
    });
  });

  // 3. Interactive Case Study Filtering
  const filterBtns = document.querySelectorAll('.filter-btn');
  const caseCards = document.querySelectorAll('.case-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterCategory = btn.getAttribute('data-filter');

      caseCards.forEach(card => {
        const cardCategory = card.getAttribute('data-category');
        if (filterCategory === 'all' || cardCategory === filterCategory) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // 4. Interactive SaaS Simulator Deck Tabs
  const simTabs = document.querySelectorAll('.sim-tab-btn');
  const simViews = document.querySelectorAll('.sim-view');

  simTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      simTabs.forEach(t => t.classList.remove('active'));
      simViews.forEach(v => v.classList.remove('active'));

      tab.classList.add('active');
      const targetView = document.getElementById(tab.getAttribute('data-view'));
      if (targetView) targetView.classList.add('active');
    });
  });

  // 4b. Simulator Action: Run Gemini AI Proposal Copilot
  const btnRunAiProposal = document.getElementById('btnRunAiProposal');
  const aiProposalOutput = document.getElementById('aiProposalOutput');
  if (btnRunAiProposal && aiProposalOutput) {
    btnRunAiProposal.addEventListener('click', () => {
      btnRunAiProposal.innerHTML = '⚡ Generating Grounded Proposal...';
      btnRunAiProposal.disabled = true;

      setTimeout(() => {
        aiProposalOutput.innerHTML = `
          <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 1rem; margin-top: 1rem;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
              <span style="font-size:0.75rem; font-family:var(--font-mono); color:#34d399;">🤖 GEMINI 2.5 FLASH PROPOSAL SYNTHESIZER</span>
              <span style="font-size:0.75rem; color:#94a3b8;">Latency: 42ms | Deal Match: 96%</span>
            </div>
            <strong style="color:#fff; font-size:0.9rem;">"Enterprise Cloud Migration & AI Desk Engine"</strong>
            <p style="font-size:0.825rem; color:#cbd5e1; margin-top:0.35rem; line-height:1.5;">
              Scope: 35-day sprint deploying Supabase RLS multi-tenant clusters, Next.js customer portal, and Gemini automated tier-1 ticket resolution. Estimated ROI: 420 hrs saved annually, eliminating $18,400 in disparate SaaS seat subscriptions.
            </p>
          </div>
        `;
        btnRunAiProposal.innerHTML = '✓ Proposal Generated';
      }, 700);
    });
  }

  // 4c. Desk Chat Simulator
  const ticketItems = document.querySelectorAll('.ticket-item');
  const chatMessagesContainer = document.getElementById('chatMessagesContainer');
  const simChatInput = document.getElementById('simChatInput');
  const btnSimSend = document.getElementById('btnSimSend');

  const ticketResponses = {
    't1': {
      customer: "Hi team, how quickly can we migrate our 4,000 active customer records from Salesforce to VALIXIS Business OS without downtime?",
      ai: "Hi Marcus! With our Supabase RLS automated migration scripts, we run an asynchronous batch ingestion with dual-write replication. Zero downtime required, and historical audit logs will be verified in under 90 minutes."
    },
    't2': {
      customer: "Can our support staff use WhatsApp to answer customer questions directly into VALIXIS Desk?",
      ai: "Yes! VALIXIS Desk includes native WhatsApp Cloud API integration. Incoming WhatsApp messages appear in your agent inbox instantly, and our autonomous Gemini co-pilot drafts suggested answers for one-click approval."
    },
    't3': {
      customer: "Does the executive telemetry dashboard support real-time export to our external finance tools?",
      ai: "Absolutely. VALIXIS Pulse provides automated vector PDF invoice generation, real-time webhooks, and direct CSV/JSON telemetry sync for QuickBooks, Zoho Books, and Stripe."
    }
  };

  ticketItems.forEach(item => {
    item.addEventListener('click', () => {
      ticketItems.forEach(t => t.classList.remove('active'));
      item.classList.add('active');

      const tid = item.getAttribute('data-ticket');
      const data = ticketResponses[tid] || ticketResponses['t1'];

      if (chatMessagesContainer) {
        chatMessagesContainer.innerHTML = `
          <div class="msg-bubble msg-customer">
            <strong style="display:block; font-size:0.75rem; color:#94a3b8; margin-bottom:0.25rem;">Client Inquiry</strong>
            ${data.customer}
          </div>
          <div class="msg-bubble msg-ai">
            <span class="ai-badge">🤖 VALIXIS Autonomous Tier-1 Co-Pilot (sub-100ms)</span>
            ${data.ai}
          </div>
        `;
      }
    });
  });

  if (btnSimSend && simChatInput && chatMessagesContainer) {
    btnSimSend.addEventListener('click', () => {
      const val = simChatInput.value.trim();
      if (!val) return;

      const customerMsg = document.createElement('div');
      customerMsg.className = 'msg-bubble msg-customer';
      customerMsg.innerHTML = `<strong style="display:block; font-size:0.75rem; color:#94a3b8; margin-bottom:0.25rem;">You</strong>${val}`;
      chatMessagesContainer.appendChild(customerMsg);
      simChatInput.value = '';

      // Simulated instant AI answer
      setTimeout(() => {
        const aiMsg = document.createElement('div');
        aiMsg.className = 'msg-bubble msg-ai';
        aiMsg.innerHTML = `
          <span class="ai-badge">🤖 VALIXIS Autonomous Tier-1 Co-Pilot</span>
          Thanks for reaching out! Our 7-member dedicated pod can implement custom business logic, secure PostgreSQL RLS data policies, and deploy this in your upcoming sprint. Let's discuss on WhatsApp or schedule a 15-minute scoping call!
        `;
        chatMessagesContainer.appendChild(aiMsg);
        chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
      }, 500);
    });
  }

  // 5. Interactive ROI & Project Estimator Logic
  const calcOptions = document.querySelectorAll('.calc-option-card');
  const sprintSlider = document.getElementById('sprintDurationSlider');
  const sliderValueDisplay = document.getElementById('sliderValueDisplay');
  
  const resTimeline = document.getElementById('resTimeline');
  const resValixisCost = document.getElementById('resValixisCost');
  const resInHouseCost = document.getElementById('resInHouseCost');
  const resSavings = document.getElementById('resSavings');
  const resPodAllocation = document.getElementById('resPodAllocation');

  let selectedModel = 'mvp'; // 'portal', 'mvp', 'enterprise'

  const modelSpecs = {
    'portal': {
      defaultWeeks: 2,
      minWeeks: 1,
      maxWeeks: 3,
      timelineLabel: '7 - 14 Days',
      valixisWeekly: 1400,
      inHouseWeekly: 3800,
      pod: '3 Specialists (Full-Stack + UI/UX + QA)'
    },
    'mvp': {
      defaultWeeks: 6,
      minWeeks: 4,
      maxWeeks: 10,
      timelineLabel: '30 - 45 Days',
      valixisWeekly: 2200,
      inHouseWeekly: 6500,
      pod: '5 Specialists (Lead Arch + 2x Devs + AI + QA)'
    },
    'enterprise': {
      defaultWeeks: 10,
      minWeeks: 8,
      maxWeeks: 16,
      timelineLabel: '60 - 75 Days',
      valixisWeekly: 3100,
      inHouseWeekly: 9200,
      pod: 'Full 7-Member Pod (Complete Dedicated Studio)'
    }
  };

  function updateEstimator() {
    const spec = modelSpecs[selectedModel];
    const weeks = parseInt(sprintSlider.value, 10);
    if (sliderValueDisplay) sliderValueDisplay.innerText = `${weeks} Weeks Sprint`;

    const valixisTotal = weeks * spec.valixisWeekly;
    const inHouseTotal = weeks * spec.inHouseWeekly;
    const savings = inHouseTotal - valixisTotal;
    const savingsPercent = Math.round((savings / inHouseTotal) * 100);

    if (resTimeline) resTimeline.innerText = `${weeks * 7} Days Production Launch`;
    if (resValixisCost) resValixisCost.innerText = `~$${valixisTotal.toLocaleString()} USD`;
    if (resInHouseCost) resInHouseCost.innerText = `~$${inHouseTotal.toLocaleString()} USD`;
    if (resSavings) resSavings.innerText = `Save ~$${savings.toLocaleString()} (${savingsPercent}% saved)`;
    if (resPodAllocation) resPodAllocation.innerText = spec.pod;
  }

  calcOptions.forEach(card => {
    card.addEventListener('click', () => {
      calcOptions.forEach(c => c.classList.remove('active'));
      card.classList.add('active');
      selectedModel = card.getAttribute('data-model');
      
      const spec = modelSpecs[selectedModel];
      sprintSlider.min = spec.minWeeks;
      sprintSlider.max = spec.maxWeeks;
      sprintSlider.value = spec.defaultWeeks;

      updateEstimator();
    });
  });

  if (sprintSlider) {
    sprintSlider.addEventListener('input', updateEstimator);
  }
  updateEstimator();

  // 6. Case Study Deep-Dive Modal Data
  const caseStudiesData = {
    '1': {
      title: '🏢 VALIXIS Business OS — Unified Enterprise Operating System',
      domain: 'Enterprise SaaS / CRM & Operations',
      stack: 'Flutter Web (Material 3), Supabase PostgreSQL, Deno Edge, Google Gemini 2.5 Flash',
      problem: 'Agencies and SMBs were juggling 4–6 subscription tools (Salesforce, ClickUp, Harvest, PandaDoc), costing $1,500+/month with siloed customer data and lost billable hours.',
      solution: 'We engineered a centralized operational system of record unifying lead management, visual Kanban pipelines, deliverable milestones, vector PDF invoicing, and a grounded Gemini AI business copilot.',
      impact: 'Eliminated $18,000/year in SaaS seat expenses, accelerated proposal turnaround from 4 hours to 90 seconds, and ensured strict tenant data privacy with Postgres Row-Level Security (RLS).'
    },
    '2': {
      title: '🎧 VALIXIS Desk — AI Omnichannel Helpdesk & Support Engine',
      domain: 'Customer Experience / Conversational AI',
      stack: 'Flutter Web, Supabase Realtime, Deno Edge, Google Gemini 2.5, WhatsApp Cloud API',
      problem: 'Support teams struggled with slow ticket replies across email, webchat, and WhatsApp, causing customer churn and duplicated agent work.',
      solution: 'An enterprise customer support engine featuring sub-100ms message sync, agent collision radar, SLA visual timers, persistent offline outbox queue, and Gemini autonomous tier-1 resolution.',
      impact: '70% of common customer questions resolved automatically with zero agent touch; eliminated agent collision completely.'
    },
    '3': {
      title: '📡 VALIXIS Pulse — Predictive Intelligence & Telemetry Tower',
      domain: 'Business Intelligence / Real-Time Telemetry',
      stack: 'Flutter Canvas (60fps), Deno Edge Functions (<50ms), Google Gemini 2.5',
      problem: 'Founders and product executives had delayed financial visibility and suffered from silent customer churn discovered only after cancellation.',
      solution: 'An executive command center with high-throughput serverless telemetry ingestion, ARR trajectory forecasting, churn risk radars, and a deep obsidian 60fps canvas interface.',
      impact: 'Identifies accounts at churn risk 30 days prior to contract expiration; ingests high-frequency telemetry events with sub-50ms latency.'
    },
    '4': {
      title: '🌐 VALIXIS Cloud — Commercial Gateway & Identity Hub',
      domain: 'Cloud Infrastructure / Multi-Tenant IAM',
      stack: 'Next.js 14 (App Router), TypeScript, Tailwind CSS, Stripe Subscriptions, PostgreSQL RLS',
      problem: 'Complex user provisioning and recurring multi-tenant subscription management was delaying product launches by months.',
      solution: 'A commercial gateway providing cross-app Single Sign-On (SSO), 60-second workspace reservation (tenant.domain.com), Stripe subscription webhooks, and Token Bucket edge rate limiting.',
      impact: 'Spins up enterprise customer workspaces in under 60 seconds; protected against DDoS and unauthorized API bursts.'
    },
    '5': {
      title: '🏋️ Fitora — AI Mobile Health & Wellness App',
      domain: 'Consumer Mobile App / Digital Health',
      stack: 'Flutter 3.x, Riverpod, Firebase Cloud Firestore, Apple HealthKit & Health Connect',
      problem: 'Fitness apps often feel generic, disconnected from wearable hardware, and quickly lose user engagement.',
      solution: 'A personalized mobile experience featuring adaptive workout generation, background biometrics sync (heart rate, calories, sleep), audio rep coaching, and milestone streaks.',
      impact: 'Maintained 4.8-star user rating, with 68% weekly active user retention over 90 days.'
    },
    '6': {
      title: '💊 MedReminder — Smart Medication Tracker & Assistant',
      domain: 'Digital Healthcare / Patient Adherence',
      stack: 'Flutter 3.x, Hive NoSQL Storage, Android Persistent Alarms & Intent Engine',
      problem: 'Patients frequently missed critical prescription dosages because Android OEM battery management killed background timer apps.',
      solution: 'Engineered persistent high-priority device-waking alarms, deep-link battery optimization bypass guides, offline-first local Hive storage, and emergency lock-screen medical ID.',
      impact: 'Achieved 99.8% alarm firing reliability across aggressive Android vendors (Xiaomi, Samsung, Oppo) with 100% patient data privacy.'
    },
    '7': {
      title: '🏛️ Campus & Venue Reservation Portal',
      domain: 'Facilities Management / Institutional Booking',
      stack: 'Flutter, Supabase Auth & PostgreSQL, TableCalendar, Role-Based Access Control',
      problem: 'Universities and conference halls suffered from double-booked auditoriums, slow paper approvals, and lack of equipment transparency.',
      solution: 'Interactive calendar portal with live vacancy matrix, AV equipment status indicators, and two-tier administrative review workflows.',
      impact: 'Eliminated booking conflicts 100%; reduced facility reservation lead time from 3 days to instantaneous approval.'
    },
    '8': {
      title: '🌾 Agri-Advisory Decision Support System',
      domain: 'Agritech / AI Diagnostics',
      stack: 'Python (FastAPI), React 18 (Vite), Google Gemini Vision, Scikit-Learn',
      problem: 'Smallholder agricultural producers lacked fast, localized plant disease diagnosis and soil-aligned crop selection.',
      solution: 'AI-assisted platform evaluating soil NPK and pH chemistry, cross-referenced with rainfall forecasts and Gemini Vision leaf disease diagnostics with vernacular voice assistance.',
      impact: 'Reduced crop diagnosis time from days to 3 seconds; assisted thousands of rural farmers with actionable remedy recipes.'
    },
    '9': {
      title: '📄 AI PDF & Document Transformation Suite',
      domain: 'Document Automation / Mobile Utility',
      stack: 'Flutter 3.x, Hugging Face Inference API, Hive NoSQL Storage',
      problem: 'Legal and executive professionals wasted hours formatting handwritten and unstructured notes into executive briefs.',
      solution: 'Mobile document processor formatting unstructured text into styled, executive PDFs, featuring on-device PDF splitting, merging, and compression.',
      impact: '100% local-first privacy with no cloud upload requirement for sensitive internal documents; saved 3+ hours per executive report.'
    }
  };

  const modalOverlay = document.getElementById('caseStudyModal');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const modalContentContainer = document.getElementById('modalContentContainer');

  document.querySelectorAll('.open-case-modal').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const id = btn.getAttribute('data-case-id');
      const item = caseStudiesData[id];
      if (!item || !modalOverlay || !modalContentContainer) return;

      modalContentContainer.innerHTML = `
        <span style="font-family:var(--font-mono); color:var(--accent-cyan); font-size:0.8rem; text-transform:uppercase;">${item.domain}</span>
        <h2 style="font-size:1.6rem; font-weight:800; margin:0.5rem 0 1rem; color:#fff;">${item.title}</h2>
        
        <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:1rem; margin-bottom:1.5rem;">
          <span style="font-size:0.75rem; font-family:var(--font-mono); color:#94a3b8; display:block; margin-bottom:0.25rem;">CORE PRODUCTION STACK</span>
          <code style="font-size:0.875rem; color:#38bdf8;">${item.stack}</code>
        </div>

        <div style="margin-bottom:1.25rem;">
          <h4 style="color:#f87171; font-size:0.95rem; margin-bottom:0.35rem;">⚠️ The Business Challenge</h4>
          <p style="font-size:0.9rem; color:#cbd5e1; line-height:1.6;">${item.problem}</p>
        </div>

        <div style="margin-bottom:1.25rem;">
          <h4 style="color:#60a5fa; font-size:0.95rem; margin-bottom:0.35rem;">🛠️ What VALIXIS Engineered</h4>
          <p style="font-size:0.9rem; color:#cbd5e1; line-height:1.6;">${item.solution}</p>
        </div>

        <div style="background:rgba(16,185,129,0.08); border-left:3px solid #10b981; padding:1rem; border-radius:0 8px 8px 0; margin-bottom:1.5rem;">
          <h4 style="color:#34d399; font-size:0.95rem; margin-bottom:0.25rem;">📈 Measurable Business Impact</h4>
          <p style="font-size:0.9rem; color:#e2e8f0; font-weight:500;">${item.impact}</p>
        </div>

        <div style="display:flex; gap:1rem; flex-wrap:wrap; margin-top:2rem;">
          <a href="https://wa.me/919603416707?text=Hi%20VALIXIS,%20I%20am%20interested%20in%20a%20solution%20similar%20to%20${encodeURIComponent(item.title)}" target="_blank" class="btn btn-whatsapp">
            💬 Discuss Similar Project on WhatsApp
          </a>
          <button class="btn btn-secondary" onclick="document.getElementById('caseStudyModal').classList.remove('active')">
            Close Deep Dive
          </button>
        </div>
      `;

      modalOverlay.classList.add('active');
    });
  });

  if (modalCloseBtn && modalOverlay) {
    modalCloseBtn.addEventListener('click', () => modalOverlay.classList.remove('active'));
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) modalOverlay.classList.remove('active');
    });
  }
});
