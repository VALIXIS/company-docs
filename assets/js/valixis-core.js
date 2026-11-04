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
  if (isFinePointer && !prefersReducedMotion) {
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
    const cards = document.querySelectorAll('.spotlight-card, .opt-card');
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
          const rotateX = ((y - centerY) / centerY) * -4.5;
          const rotateY = ((x - centerX) / centerX) * 4.5;
          card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateY(-3px)`;
        }
      });

      card.addEventListener('mouseleave', () => {
        if (isFinePointer && !prefersReducedMotion) {
          card.style.transform = '';
        }
      });
    });
  }

  // 4. MOBILE NAVIGATION DRAWER
  function initMobileNav() {
    const toggle = document.querySelector('.mobile-nav-toggle');
    const links = document.querySelector('.nav-links');
    if (toggle && links) {
      toggle.addEventListener('click', () => {
        const isOpen = links.classList.toggle('active');
        toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });

      // Close on clicking outside or on link
      document.addEventListener('click', (e) => {
        if (!toggle.contains(e.target) && !links.contains(e.target) && links.classList.contains('active')) {
          links.classList.remove('active');
          toggle.setAttribute('aria-expanded', 'false');
        }
      });
    }
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      initSpotlights();
      initMobileNav();
    });
  } else {
    initSpotlights();
    initMobileNav();
  }
})();
