/**
 * VALIXIS Product Portfolio - Client Experience & Interactive Demos
 * Simple, human, frictionless, and touch-responsive
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
        navLinks.style.background = 'rgba(14, 18, 29, 0.98)';
        navLinks.style.padding = '1.5rem';
        navLinks.style.borderRadius = '0 0 16px 16px';
        navLinks.style.border = '1px solid rgba(255,255,255,0.1)';
      }
    });
  }

  // 2. Interactive Showcase Switcher
  const showcaseTabs = document.querySelectorAll('.showcase-tab');
  const previewViews = document.querySelectorAll('.preview-view');

  showcaseTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      showcaseTabs.forEach(t => t.classList.remove('active'));
      previewViews.forEach(v => v.classList.remove('active'));

      tab.classList.add('active');
      const targetId = tab.getAttribute('data-view');
      const targetView = document.getElementById(targetId);
      if (targetView) targetView.classList.add('active');
    });
  });

  // 2b. Interactive Phone Mockup Demo (Direct Ordering Simulation)
  let orderTotal = 0;
  const orderTotalDisplay = document.getElementById('orderTotalDisplay');
  const phoneOrderSuccess = document.getElementById('phoneOrderSuccess');
  const btnSimulateUpi = document.getElementById('btnSimulateUpi');

  document.querySelectorAll('.btn-add-item').forEach(btn => {
    btn.addEventListener('click', () => {
      const price = parseInt(btn.getAttribute('data-price') || '220', 10);
      orderTotal += price;
      if (orderTotalDisplay) {
        orderTotalDisplay.innerText = `₹${orderTotal}`;
      }
      btn.innerText = '✓ Added';
      btn.style.background = '#38bdf8';
      setTimeout(() => {
        btn.innerText = '+ Add';
        btn.style.background = 'var(--accent-emerald)';
      }, 1000);
    });
  });

  if (btnSimulateUpi && phoneOrderSuccess) {
    btnSimulateUpi.addEventListener('click', () => {
      if (orderTotal === 0) orderTotal = 390;
      btnSimulateUpi.innerHTML = '⚡ Processing UPI Payment...';
      btnSimulateUpi.disabled = true;

      setTimeout(() => {
        phoneOrderSuccess.style.display = 'block';
        btnSimulateUpi.innerHTML = '✓ Payment Received (100% Direct)';
        phoneOrderSuccess.innerHTML = `
          <div style="font-size:0.8rem; color:#34d399; font-weight:700; margin-bottom:0.25rem;">
            ✓ UPI Payment of ₹${orderTotal} settled directly into your bank!
          </div>
          <div style="font-size:0.75rem; color:#cbd5e1; line-height:1.4;">
            📲 Automated WhatsApp alert sent to customer: <em>"Hi! Your order has been received and will be ready in 15 minutes."</em>
          </div>
          <div style="font-size:0.7rem; color:#94a3b8; margin-top:0.35rem;">
            Commission paid to aggregators: <strong>₹0 (You saved ₹${Math.round(orderTotal * 0.25)})</strong>
          </div>
        `;
      }, 700);
    });
  }

  // 3. Project Category Filter
  const catBtns = document.querySelectorAll('.cat-btn');
  const projectCards = document.querySelectorAll('.project-card');

  catBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      catBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      projectCards.forEach(card => {
        const cat = card.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // 4. Project Details Modal (Simple, Human, Informative)
  const projectsData = {
    'valixis-os': {
      title: '🏢 VALIXIS Business OS',
      tag: 'Business Dashboard & CRM',
      problem: 'Small companies waste hours every day copy-pasting client info between Excel, WhatsApp, and 4 different monthly software tools that cost $1,500/year.',
      solution: 'A simple, custom dashboard where you manage all client leads, see active projects on a visual board, and send professional invoices with one click.',
      benefit: 'Saves 10 to 15 hours of repetitive admin work every week, replaces expensive subscriptions, and keeps your entire business organized.',
      tech: 'Web Dashboard, Supabase Database, Instant PDF Invoices'
    },
    'valixis-desk': {
      title: '🎧 VALIXIS Desk (Smart Customer Support)',
      tag: 'Customer Service & Chat',
      problem: 'Customers ask questions at night or on weekends, but your staff is off-duty—causing lost sales and frustrated clients.',
      solution: 'A shared support inbox that connects your website chat, email, and WhatsApp. Our smart AI helper answers common questions in under 1 second.',
      benefit: 'Your customers get instant answers 24/7 without needing to hire a night shift support team.',
      tech: 'WhatsApp Integration, Realtime Chat, AI Smart Answers'
    },
    'direct-order': {
      title: '☕ Direct QR Ordering & Booking Portal',
      tag: 'For Cafes, Bakeries & Clinics',
      problem: 'Food delivery apps take 20% to 25% of your bill in commissions, and busy clinics lose patients when front-desk phone lines are engaged.',
      solution: 'A clean mobile website where customers scan a QR code or click a link to view your menu or doctors, pick a time, and pay instantly via UPI.',
      benefit: 'Money goes directly to your bank account with zero aggregator commissions, and bookings happen automatically 24/7.',
      tech: 'UPI Instant Pay, WhatsApp Booking Alerts, Mobile-Optimized'
    },
    'fitora': {
      title: '🏋️ Fitora & FitSync (Fitness Mobile App)',
      tag: 'Health & Wellness Mobile App',
      problem: 'Generic workout apps don\'t adapt to daily energy levels and fail to keep users motivated past the first week.',
      solution: 'A personalized mobile fitness app that creates customized daily workout routines, syncs automatically with Apple Health and smartwatches, and provides audio voice guidance during workouts.',
      benefit: 'High user retention, 4.8-star user ratings, and smooth performance on both iPhone and Android.',
      tech: 'Flutter iOS & Android, Apple Health, Health Connect'
    },
    'med-reminder': {
      title: '💊 MedReminder (Smart Health Assistant)',
      tag: 'Healthcare Mobile App',
      problem: 'Patients miss daily medications because phone battery savers kill background alarm apps, leading to health risks.',
      solution: 'A reliable medication reminder app with loud, device-waking alarms that never fail, adherence progress tracking for family members, and an emergency medical card on the lock screen.',
      benefit: '99.8% alarm reliability across all Android phones (Samsung, Xiaomi, OnePlus) with zero subscription fees.',
      tech: 'Flutter, High-Priority Alarms, Offline Storage'
    },
    'events-app': {
      title: '🏛️ Campus & Venue Booking Portal',
      tag: 'Facilities & Hall Reservations',
      problem: 'Universities, colleges, and event halls struggle with double-booked auditoriums, lost paper requests, and confused coordinators.',
      solution: 'An interactive visual calendar where organizers can see which halls are free, view audio/visual facilities, and submit requests for admin approval in 30 seconds.',
      benefit: 'Zero double-booking mistakes and reduces approval time from 3 days to minutes.',
      tech: 'Interactive Calendar, Admin Approvals, Supabase'
    },
    'ai-pdf': {
      title: '📄 AI PDF Maker & Document Suite',
      tag: 'Mobile Productivity Tool',
      problem: 'Professionals and students spend hours converting rough notes into clean, presentable PDF reports.',
      solution: 'A fast mobile utility that organizes unformatted text into styled PDF documents with headers, tables, and bullet points—plus on-device PDF compression and merging.',
      benefit: 'Creates publication-ready documents in seconds with 100% on-device privacy (no files sent to the cloud).',
      tech: 'Flutter, Offline PDF Engine, Hive Storage'
    },
    'resume-brain': {
      title: '💼 Resume Brain (AI Career Assistant)',
      tag: 'Career & Document AI',
      problem: 'Job seekers send generic resumes that get rejected by automated applicant tracking systems (ATS).',
      solution: 'An intelligent builder that analyzes job descriptions and tailors resume bullet points to highlight matching experience and generate clean PDF resumes.',
      benefit: 'Improves interview callback rates by tailoring qualifications directly to job criteria.',
      tech: 'Flutter, AI Text Enhancement, Vector PDF'
    },
    'smart-crop': {
      title: '🌾 Smart Crop Advisory System',
      tag: 'Agriculture & AI Helper',
      problem: 'Farmers and rural growers lack immediate access to agricultural experts to identify plant diseases and evaluate soil fertilizers.',
      solution: 'A decision support tool where users photograph damaged plant leaves for instant disease diagnosis, plus soil NPK analysis for balanced fertilizer advice.',
      benefit: 'Provides instant diagnosis in 3 seconds in regional languages, protecting harvest yields.',
      tech: 'Python FastAPI, React, Vision AI, Multilingual'
    },
    'pocket-ledger': {
      title: '💰 PocketLedger & Balance Reader',
      tag: 'Personal Finance Utility',
      problem: 'People lose track of daily expenses and upcoming subscriptions, while online finance apps compromise personal privacy.',
      solution: 'A privacy-first cash ledger with visual spending charts, upcoming subscription reminders, and an Android widget that parses bank SMS alerts locally without cloud uploads.',
      benefit: 'Gives users complete clarity over their money with zero cloud privacy risks.',
      tech: 'Flutter, Jetpack Compose, Local Encryption'
    },
    'subbu-cloud': {
      title: '☁️ Subbu Cloud (Private Media Hub)',
      tag: 'Private Cloud Storage',
      problem: 'Big cloud storage services charge expensive monthly fees and throttle 4K video playback.',
      solution: 'A self-hosted private media server with instant 4K video streaming, photo albums, and document backups accessible anywhere via secure tunnel.',
      benefit: 'Unlimited private storage with zero monthly subscriptions and complete ownership.',
      tech: 'FastAPI, Cloudflare Tunnel, Secure Streaming'
    },
    'planly': {
      title: '📝 Planly (Mindful Task Planner)',
      tag: 'Daily Productivity',
      problem: 'Cluttered productivity apps overwhelm users with complicated setups and endless notifications.',
      solution: 'A clean, distraction-free daily planner with a single-task Focus Mode, visual calendar deadlines, and evening reflection notes.',
      benefit: 'Helps individuals get their most important work done without digital anxiety.',
      tech: 'Flutter, Local Hive Cache, Smart Notifications'
    }
  };

  const modalOverlay = document.getElementById('projectModal');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const modalContent = document.getElementById('modalContent');

  document.querySelectorAll('.open-project-modal').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const id = btn.getAttribute('data-id');
      const item = projectsData[id];
      if (!item || !modalOverlay || !modalContent) return;

      modalContent.innerHTML = `
        <span style="font-size:0.8rem; font-weight:700; color:var(--accent-cyan); text-transform:uppercase; letter-spacing:0.05em;">${item.tag}</span>
        <h2 style="font-size:1.6rem; font-weight:800; color:#fff; margin:0.5rem 0 1.25rem;">${item.title}</h2>
        
        <div style="background:rgba(239, 68, 68, 0.08); border-left:3px solid #ef4444; padding:1rem; border-radius:0 8px 8px 0; margin-bottom:1.25rem;">
          <strong style="color:#f87171; font-size:0.85rem; text-transform:uppercase; display:block; margin-bottom:0.25rem;">The Real Problem</strong>
          <p style="font-size:0.925rem; color:#cbd5e1; line-height:1.5;">${item.problem}</p>
        </div>

        <div style="background:rgba(6, 182, 212, 0.08); border-left:3px solid var(--accent-cyan); padding:1rem; border-radius:0 8px 8px 0; margin-bottom:1.25rem;">
          <strong style="color:var(--accent-cyan-light); font-size:0.85rem; text-transform:uppercase; display:block; margin-bottom:0.25rem;">What We Built</strong>
          <p style="font-size:0.925rem; color:#cbd5e1; line-height:1.5;">${item.solution}</p>
        </div>

        <div style="background:rgba(16, 185, 129, 0.08); border-left:3px solid #10b981; padding:1rem; border-radius:0 8px 8px 0; margin-bottom:1.75rem;">
          <strong style="color:#34d399; font-size:0.85rem; text-transform:uppercase; display:block; margin-bottom:0.25rem;">How It Helps Your Business</strong>
          <p style="font-size:0.925rem; color:#e2e8f0; font-weight:500; line-height:1.5;">${item.benefit}</p>
        </div>

        <div style="display:flex; gap:1rem; flex-wrap:wrap; align-items:center;">
          <a href="https://wa.me/919603416707?text=Hi%20VALIXIS,%20I%20am%20interested%20in%20building%20something%20like%20${encodeURIComponent(item.title)}%20for%20my%20business." target="_blank" class="btn btn-whatsapp">
            💬 Discuss This on WhatsApp (+91 9603416707)
          </a>
          <button class="btn btn-secondary" onclick="document.getElementById('projectModal').classList.remove('active')">
            Close
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
