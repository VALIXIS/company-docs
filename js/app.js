/**
 * VALIXIS Product Portfolio - Client Experience & Interactive Demos
 * Clean, Professional, Zero Emojis, Touch-Responsive
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
        navLinks.style.background = 'rgba(12, 16, 27, 0.98)';
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
        orderTotalDisplay.innerText = `INR ${orderTotal}`;
      }
      btn.innerText = 'Added';
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
      btnSimulateUpi.innerHTML = 'Processing UPI Payment...';
      btnSimulateUpi.disabled = true;

      setTimeout(() => {
        phoneOrderSuccess.style.display = 'block';
        btnSimulateUpi.innerHTML = 'Payment Received (100% Direct)';
        phoneOrderSuccess.innerHTML = `
          <div style="font-size:0.8rem; color:#34d399; font-weight:700; margin-bottom:0.25rem;">
            UPI Payment of INR ${orderTotal} settled directly into your bank account.
          </div>
          <div style="font-size:0.75rem; color:#cbd5e1; line-height:1.4;">
            Automated WhatsApp notification sent to customer: "Your order has been received and will be ready in 15 minutes."
          </div>
          <div style="font-size:0.7rem; color:#94a3b8; margin-top:0.35rem;">
            Commission paid to aggregators: <strong>INR 0 (Saved approx. INR ${Math.round(orderTotal * 0.25)})</strong>
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

  // 4. Project Details Modal (Zero Emojis, Clear Breakdown)
  const projectsData = {
    'valixis-os': {
      title: 'VALIXIS Business OS',
      tag: 'Business Dashboard & CRM',
      problem: 'Companies waste hours every day copy-pasting client details across separate spreadsheets, email threads, and multiple disconnected software subscriptions.',
      solution: 'A unified company dashboard where you manage all client leads, see active deliverables on a visual board, and send professional invoices in seconds.',
      benefit: 'Saves 10 to 15 hours of repetitive administration weekly, eliminates expensive monthly software subscriptions, and keeps your entire business organized.',
      tech: 'Web Dashboard, Supabase Database, Instant PDF Invoices'
    },
    'valixis-desk': {
      title: 'VALIXIS Desk',
      tag: 'Customer Support & Chat',
      problem: 'Customers inquire outside business hours, but your team is offline—resulting in delayed replies, lost sales, and customer frustration.',
      solution: 'A shared support inbox that connects your website chat, email, and WhatsApp. Automated smart assistants resolve common questions in under 1 second.',
      benefit: 'Your customers receive prompt responses 24/7 without needing additional support staff.',
      tech: 'WhatsApp Cloud Integration, Realtime Chat, Smart Assistant'
    },
    'direct-order': {
      title: 'Direct QR Ordering & Booking Portal',
      tag: 'For Cafes, Bakeries & Clinics',
      problem: 'Aggregators take 20% to 25% of your bill in commissions, and busy clinics lose patient appointments when reception phone lines are engaged.',
      solution: 'A mobile web app where customers scan a QR code or tap a link to view your menu or doctors, choose a time slot, and pay directly via UPI.',
      benefit: 'Funds deposit directly into your bank account with zero aggregator commissions, and appointments book automatically around the clock.',
      tech: 'UPI Instant Pay, WhatsApp Booking Alerts, Mobile-First'
    },
    'fitora': {
      title: 'Fitora & FitSync',
      tag: 'Health & Wellness Mobile App',
      problem: 'Generic fitness apps fail to personalize workout intensity and lack integration with modern smartwatches and wearables.',
      solution: 'A personalized mobile application providing customized daily routines, seamless Apple Health and Health Connect synchronization, and hands-free audio voice coaching.',
      benefit: 'Maintains high 90-day retention, 4.8-star user satisfaction, and smooth performance on iOS and Android.',
      tech: 'Flutter iOS & Android, Apple Health, Health Connect'
    },
    'med-reminder': {
      title: 'MedReminder Assistant',
      tag: 'Healthcare Mobile App',
      problem: 'Patients miss essential medication dosages because aggressive Android OEM battery optimizations terminate background alarm apps.',
      solution: 'A reliable mobile adherence assistant featuring high-priority device-waking alarms that never fail, adherence progress reports, and an emergency lock-screen medical ID.',
      benefit: 'Delivers 99.8% alarm firing reliability across all major Android manufacturers with zero monthly fees and complete on-device privacy.',
      tech: 'Flutter, High-Priority Alarms, Local Storage'
    },
    'events-app': {
      title: 'Campus & Venue Booking Portal',
      tag: 'Facilities & Hall Reservations',
      problem: 'Universities and event spaces frequently struggle with double-booked auditoriums, slow manual paper approvals, and scheduling confusion.',
      solution: 'An interactive visual calendar portal where organizers check live hall vacancies, inspect AV equipment specifications, and submit requests for admin approval.',
      benefit: 'Prevents double-booking completely and accelerates approval turnaround from 3 days to instantaneous review.',
      tech: 'Interactive Calendar, Admin Review, Supabase'
    },
    'ai-pdf': {
      title: 'AI PDF Maker & Document Suite',
      tag: 'Mobile Document Utility',
      problem: 'Professionals and students spend excessive time formatting rough meeting notes into presentable, structured PDF summaries.',
      solution: 'A fast mobile utility that organizes unstructured text into styled PDF documents with headers, tables, and bullet points, alongside on-device PDF compression and merging.',
      benefit: 'Generates polished documents in seconds with complete on-device data privacy.',
      tech: 'Flutter, Offline PDF Engine, Hive Storage'
    },
    'resume-brain': {
      title: 'Resume Brain',
      tag: 'Career & Document Optimization',
      problem: 'Job seekers submit generic resumes that are filtered out by automated applicant tracking systems (ATS).',
      solution: 'An intelligent builder that analyzes job postings and tailors resume bullet points to highlight relevant experience, exporting crisp vector PDFs.',
      benefit: 'Substantially improves interview callback rates by aligning candidate qualifications with employer criteria.',
      tech: 'Flutter, Text Optimization, Vector PDF'
    },
    'smart-crop': {
      title: 'Smart Crop Advisory System',
      tag: 'Agritech & Computer Vision',
      problem: 'Farmers and rural cultivators lack immediate access to specialists for identifying plant pathology and evaluating soil fertilizers.',
      solution: 'An agricultural decision support platform that identifies plant diseases from a leaf photograph in 3 seconds, paired with soil NPK chemical evaluations in vernacular languages.',
      benefit: 'Protects harvest yields with rapid diagnosis and localized agricultural advice.',
      tech: 'Python FastAPI, React, Vision Diagnostics, Multilingual'
    },
    'pocket-ledger': {
      title: 'PocketLedger & Balance Reader',
      tag: 'Personal Finance Utility',
      problem: 'Users lose track of cash expenditures and recurring subscriptions, while standard online financial apps risk sensitive personal banking data.',
      solution: 'A privacy-first cash ledger with visual spending analytics, upcoming renewal reminders, and an Android widget that parses bank SMS alerts locally without cloud uploads.',
      benefit: 'Provides instant financial awareness with complete data privacy and zero bank login credentials required.',
      tech: 'Flutter, Jetpack Compose, Local Encryption'
    },
    'subbu-cloud': {
      title: 'Subbu Cloud',
      tag: 'Private Cloud Storage',
      problem: 'Commercial cloud storage providers charge steep recurring subscription fees and restrict high-bitrate 4K streaming.',
      solution: 'A self-hosted private media server supporting 4K video playback, image galleries, and file backups accessible securely from any device.',
      benefit: 'Delivers full data ownership and unlimited private storage without ongoing cloud hosting bills.',
      tech: 'FastAPI, Cloudflare Tunnel, Secure Streaming'
    },
    'planly': {
      title: 'Planly Task Planner',
      tag: 'Daily Productivity',
      problem: 'Complex productivity platforms overwhelm users with excessive configuration and constant notification distractions.',
      solution: 'A focused daily planning app featuring a single-task Focus Mode, clean calendar deadlines, and mindful evening reflection prompts.',
      benefit: 'Helps users maintain momentum on essential daily goals with minimal interface friction.',
      tech: 'Flutter, Local Hive Cache, Smart Reminders'
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
          <strong style="color:#f87171; font-size:0.8rem; text-transform:uppercase; display:block; margin-bottom:0.25rem;">The Challenge</strong>
          <p style="font-size:0.925rem; color:#cbd5e1; line-height:1.5;">${item.problem}</p>
        </div>

        <div style="background:rgba(6, 182, 212, 0.08); border-left:3px solid var(--accent-cyan); padding:1rem; border-radius:0 8px 8px 0; margin-bottom:1.25rem;">
          <strong style="color:var(--accent-cyan-light); font-size:0.8rem; text-transform:uppercase; display:block; margin-bottom:0.25rem;">What We Built</strong>
          <p style="font-size:0.925rem; color:#cbd5e1; line-height:1.5;">${item.solution}</p>
        </div>

        <div style="background:rgba(16, 185, 129, 0.08); border-left:3px solid #10b981; padding:1rem; border-radius:0 8px 8px 0; margin-bottom:1.75rem;">
          <strong style="color:#34d399; font-size:0.8rem; text-transform:uppercase; display:block; margin-bottom:0.25rem;">Business Value</strong>
          <p style="font-size:0.925rem; color:#e2e8f0; font-weight:500; line-height:1.5;">${item.benefit}</p>
        </div>

        <div style="display:flex; gap:1rem; flex-wrap:wrap; align-items:center;">
          <a href="https://wa.me/919603416707?text=Hi%20Subhash,%20I%20am%20interested%20in%20building%20something%20like%20${encodeURIComponent(item.title)}%20for%20my%20business." target="_blank" class="btn btn-whatsapp-pill">
            <svg class="svg-icon" width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86.174.086.275.072.376-.044.101-.116.433-.506.549-.68.116-.173.231-.144.39-.086s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.099.824zm-3.392-10.216c-5.503 0-9.969 4.467-9.969 9.97 0 1.76.459 3.477 1.332 4.992l-1.417 5.178 5.305-1.391c1.465.799 3.12 1.221 4.749 1.221 5.503 0 9.97-4.467 9.97-9.97 0-5.503-4.467-9.97-9.97-9.97zm0 18.127c-1.488 0-2.946-.4-4.22-1.155l-.303-.18-3.136.822.837-3.056-.197-.314c-.829-1.319-1.267-2.852-1.267-4.419 0-4.505 3.666-8.17 8.172-8.17 4.505 0 8.171 3.665 8.171 8.17s-3.666 8.172-8.171 8.172z"/></svg>
            <span>Chat with Subhash on WhatsApp</span>
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
