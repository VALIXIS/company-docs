/**
 * ==========================================================================
 * VALIXIS SHARED CORE ENGINE (WEBSITE 2.1)
 * Lenis Smooth Scroll + Dual Cyber Cursor + Spotlight Physics + Nav Drawer
 * ==========================================================================
 */

(function initValixisCore() {
  'use strict';

  // State guards
  const isFinePointer = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let isPageActive = !document.hidden;

  function trackLeadEvent(name, params = {}) {
    if (typeof window.gtag !== 'function') return;
    window.gtag('event', name, {
      event_category: 'lead',
      page_path: window.location.pathname,
      ...params
    });
  }
  window.VALIXIS_TRACK_EVENT = trackLeadEvent;

  document.addEventListener('visibilitychange', () => {
    isPageActive = !document.hidden;
  });

  // 1. INJECT & INITIALIZE DUAL CYBER CURSOR
  if (isFinePointer && !prefersReducedMotion && document.body.dataset.customCursor === 'true') {
    let cursorDot = document.getElementById('cursorDot');
    let cursorRing = document.getElementById('cursorRing');

    if (!cursorDot) {
      cursorDot = document.createElement('div');
      cursorDot.id = 'cursorDot';
      cursorDot.className = 'custom-cursor-dot';
      cursorDot.setAttribute('aria-hidden', 'true');
      document.body.appendChild(cursorDot);
    }

    if (!cursorRing) {
      cursorRing = document.createElement('div');
      cursorRing.id = 'cursorRing';
      cursorRing.className = 'custom-cursor-ring';
      cursorRing.setAttribute('aria-hidden', 'true');
      document.body.appendChild(cursorRing);
    }

    let mouseX = -100;
    let mouseY = -100;
    let ringX = -100;
    let ringY = -100;
    let isCursorActive = false;

    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      if (!isCursorActive) {
        isCursorActive = true;
        ringX = mouseX;
        ringY = mouseY;
        document.body.classList.add('cursor-active');
      }
      cursorDot.style.left = `${mouseX}px`;
      cursorDot.style.top = `${mouseY}px`;
    }, { passive: true });

    document.addEventListener('mouseleave', () => {
      document.body.classList.remove('cursor-active');
    });

    document.addEventListener('mouseenter', () => {
      document.body.classList.add('cursor-active');
    });

    window.addEventListener('mousedown', () => {
      document.body.classList.add('cursor-click');
    });

    window.addEventListener('mouseup', () => {
      document.body.classList.remove('cursor-click');
    });

    function renderCursor() {
      if (!isPageActive) {
        requestAnimationFrame(renderCursor);
        return;
      }
      if (isCursorActive) {
        ringX += (mouseX - ringX) * 0.18;
        ringY += (mouseY - ringY) * 0.18;
        cursorRing.style.left = `${ringX}px`;
        cursorRing.style.top = `${ringY}px`;
      }
      requestAnimationFrame(renderCursor);
    }
    requestAnimationFrame(renderCursor);

    // Hover detection for interactive targets
    const interactiveSelector = 'a, button, input, textarea, select, .spotlight-card, .btn-primary-gradient, .btn-outline-glass, .nav-cta-btn, .opt-card, [role="button"]';
    document.addEventListener('mouseover', (e) => {
      if (e.target && e.target.closest && e.target.closest(interactiveSelector)) {
        document.body.classList.add('cursor-hover');
      }
    });
    document.addEventListener('mouseout', (e) => {
      if (e.target && e.target.closest && e.target.closest(interactiveSelector)) {
        document.body.classList.remove('cursor-hover');
      }
    });
  }

  // 2. LENIS SMOOTH SCROLLING
  if (typeof window.Lenis !== 'undefined' && !prefersReducedMotion) {
    const lenis = new window.Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      direction: 'vertical',
      smooth: true,
      mouseMultiplier: 1.0,
      smoothTouch: false, // native momentum on touch screens
      touchMultiplier: 2.0,
      infinite: false
    });

    function lenisRaf(time) {
      if (isPageActive) {
        lenis.raf(time);
      }
      requestAnimationFrame(lenisRaf);
    }
    requestAnimationFrame(lenisRaf);

    // Anchor smooth jump
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href');
        if (targetId && targetId !== '#') {
          try {
            const targetEl = document.querySelector(targetId);
            if (targetEl) {
              e.preventDefault();
              lenis.scrollTo(targetEl, { offset: -80 });
            }
          } catch (_) {}
        }
      });
    });
  }

  // 3. SPOTLIGHT CARDS MOUSE TRACKING & 3D BENTO TILT
  function initSpotlights() {
    const cards = document.querySelectorAll('.spotlight-card, .opt-card, .mv-card, .leader-card, .val-card, .exec-card, .bp-card, .service-card, .product-card');
    cards.forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);

        if (isFinePointer && !prefersReducedMotion) {
          const centerX = rect.width / 2;
          const centerY = rect.height / 2;
          const rotateX = ((y - centerY) / centerY) * -5.0;
          const rotateY = ((x - centerX) / centerX) * 5.0;
          card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) scale3d(1.015, 1.015, 1.015)`;
        }
      });

      card.addEventListener('mouseleave', () => {
        if (isFinePointer && !prefersReducedMotion) {
          card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
        }
      });
    });
  }

  // 4. MOBILE NAVIGATION DRAWER
  function initMobileNav() {
    const toggle = document.getElementById('mobileMenuToggle') || document.querySelector('.mobile-menu-toggle, .mobile-nav-toggle');
    const drawer = document.getElementById('mobileNavDrawer') || document.querySelector('.mobile-nav-drawer');
    const legacyLinks = document.querySelector('.nav-links');

    if (!toggle) return;

    function toggleMenu(e) {
      if (e) e.stopPropagation();
      if (drawer) {
        const isOpen = drawer.classList.toggle('open');
        toggle.classList.toggle('active', isOpen);
        toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        drawer.setAttribute('aria-hidden', isOpen ? 'false' : 'true');
      } else if (legacyLinks) {
        const isOpen = legacyLinks.classList.toggle('active');
        toggle.classList.toggle('active', isOpen);
        toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      }
    }

    toggle.addEventListener('click', toggleMenu);

    if (drawer) {
      drawer.querySelectorAll('.mobile-nav-link, .mobile-drawer-btn, a').forEach(link => {
        link.addEventListener('click', () => {
          drawer.classList.remove('open');
          toggle.classList.remove('active');
          toggle.setAttribute('aria-expanded', 'false');
          drawer.setAttribute('aria-hidden', 'true');
        });
      });

      document.addEventListener('click', (e) => {
        if (!drawer.contains(e.target) && !toggle.contains(e.target) && drawer.classList.contains('open')) {
          drawer.classList.remove('open');
          toggle.classList.remove('active');
          toggle.setAttribute('aria-expanded', 'false');
          drawer.setAttribute('aria-hidden', 'true');
        }
      });
    } else if (legacyLinks) {
      legacyLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
          legacyLinks.classList.remove('active');
          toggle.classList.remove('active');
          toggle.setAttribute('aria-expanded', 'false');
        });
      });

      document.addEventListener('click', (e) => {
        if (!toggle.contains(e.target) && !legacyLinks.contains(e.target) && legacyLinks.classList.contains('active')) {
          legacyLinks.classList.remove('active');
          toggle.classList.remove('active');
          toggle.setAttribute('aria-expanded', 'false');
        }
      });
    }
  }

  // 5. SCROLL DEPTH & REVEAL ANIMATIONS (LIGHT & HARDWARE-ACCELERATED)
  function initScrollReveals() {
    document.querySelectorAll('#divisions .section-header, #products .section-header, #mission .section-header, #leadership .section-header').forEach(el => el.classList.add('reveal-on-scroll'));
    const revealEls = document.querySelectorAll('.reveal-on-scroll');
    if (!revealEls.length) return;

    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
      revealEls.forEach(el => el.classList.add('is-revealed'));
      return;
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px'
    });

    revealEls.forEach(el => observer.observe(el));
  }

  function initContactDock() {
    if (document.querySelector('.contact-dock')) return;
    const dock = document.createElement('nav');
    dock.className = 'contact-dock';
    dock.setAttribute('aria-label', 'Contact VALIXIS');
    dock.innerHTML = '<a href="/contact/" data-contact-action="contact" data-contact-location="dock" aria-label="Contact VALIXIS"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>Contact</a><a href="/estimate/" data-contact-action="estimate" data-contact-location="dock" aria-label="Estimate Project Scope"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>Estimate</a>';
    document.body.appendChild(dock);
    document.addEventListener('click', (event) => {
      const link = event.target.closest('[data-contact-action]');
      if (!link || typeof window.gtag !== 'function') return;
      trackLeadEvent(link.dataset.contactAction, {
        event_label: link.dataset.contactLocation || window.location.pathname
      });
    });
  }

  function initLeadTelemetry() {
    document.addEventListener('click', (event) => {
      const leadAction = event.target.closest && event.target.closest('[data-lead-action]');
      if (leadAction) {
        trackLeadEvent(leadAction.dataset.leadAction, { event_label: leadAction.getAttribute('href') || window.location.pathname });
        return;
      }
      const link = event.target.closest && event.target.closest('a[href]');
      if (!link) return;
      const href = link.getAttribute('href') || '';
      if (href.includes('estimate')) trackLeadEvent('estimator_open', { event_label: href });
      else if (href.includes('contact') || href.includes('#booking') || href.includes('#inquiry-form')) trackLeadEvent('contact_path_open', { event_label: href });
    }, { passive: true });

    const form = document.querySelector('#projectInquiryForm');
    if (form) {
      let started = false;
      form.addEventListener('focusin', () => {
        if (started) return;
        started = true;
        trackLeadEvent('contact_form_start');
      });
    }
  }

  function initServiceWorld() {
    if (!document.querySelector('.service-hero, .services-grid')) return;
    if (document.querySelector('.services-grid')) document.body.classList.add('services-overview');
    const coreScript = document.querySelector('script[src*="valixis-core.js"]');
    if (!coreScript) return;
    const sceneUrl = new URL('valixis-scenes.js', coreScript.src).href;
    const loadScene = () => {
      const script = document.createElement('script');
      script.src = sceneUrl;
      script.defer = true;
      document.body.appendChild(script);
    };
    if (window.THREE) { loadScene(); return; }
    const three = document.createElement('script');
    three.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
    three.onload = loadScene;
    document.head.appendChild(three);
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      initSpotlights();
      initMobileNav();
      initScrollReveals();
      initContactDock();
      initLeadTelemetry();
      initServiceWorld();
    });
  } else {
    initSpotlights();
    initMobileNav();
    initScrollReveals();
    initContactDock();
    initLeadTelemetry();
    initServiceWorld();
  }
})();
