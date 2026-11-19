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
          const targetEl = document.querySelector(targetId);
          if (targetEl) {
            e.preventDefault();
            lenis.scrollTo(targetEl, { offset: -80 });
          }
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
    dock.innerHTML = '<a href="tel:+919603416707" data-contact-action="call" data-contact-location="dock" aria-label="Call VALIXIS at +91 96034 16707"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7l.5 2.8a2 2 0 0 1-.6 2l-1.3 1.3a16 16 0 0 0 6.5 6.5l1.3-1.3a2 2 0 0 1 2-.6l2.8.5a2 2 0 0 1 1.7 2Z"/></svg>Call us</a><a href="https://wa.me/919603416707?text=Hello%20VALIXIS%2C%20I%27d%20like%20to%20discuss%20a%20digital%20project." target="_blank" rel="noopener noreferrer" data-contact-action="whatsapp" data-contact-location="dock" aria-label="Message VALIXIS on WhatsApp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 11.5a8.5 8.5 0 0 1-12.7 7.4L3 20l1.1-5.3A8.5 8.5 0 1 1 21 11.5Z"/><path d="M9 9c.3 2.7 2.1 4.5 5 5"/></svg>WhatsApp</a>';
    document.body.appendChild(dock);
    document.addEventListener('click', (event) => {
      const link = event.target.closest('[data-contact-action]');
      if (!link || typeof window.gtag !== 'function') return;
      window.gtag('event', link.dataset.contactAction === 'call' ? 'click_to_call' : 'whatsapp_start', {
        event_category: 'lead',
        event_label: link.dataset.contactLocation || window.location.pathname
      });
    });
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
      initServiceWorld();
    });
  } else {
    initSpotlights();
    initMobileNav();
    initScrollReveals();
    initContactDock();
    initServiceWorld();
  }
})();
