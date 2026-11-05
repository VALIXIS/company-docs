import os

def update_index_performance(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. P3-1: Cursor initialization guard
    cursor_old = """    function renderCursor() {
      if (isCursorActive) {
        ringX += (mouseX - ringX) * 0.18;
        ringY += (mouseY - ringY) * 0.18;
        cursorRing.style.left = `${ringX}px`;
        cursorRing.style.top = `${ringY}px`;
      }
      requestAnimationFrame(renderCursor);
    }
    requestAnimationFrame(renderCursor);"""

    cursor_new = """    const isFinePointer = window.matchMedia && window.matchMedia('(pointer: fine)').matches;
    let isPageActive = !document.hidden;

    document.addEventListener('visibilitychange', () => {
      isPageActive = !document.hidden;
    });

    function renderCursor() {
      if (!isFinePointer || !isPageActive) return;
      if (isCursorActive) {
        ringX += (mouseX - ringX) * 0.18;
        ringY += (mouseY - ringY) * 0.18;
        cursorRing.style.left = `${ringX}px`;
        cursorRing.style.top = `${ringY}px`;
      }
      requestAnimationFrame(renderCursor);
    }
    if (isFinePointer) {
      requestAnimationFrame(renderCursor);
    } else {
      if (cursorDot) cursorDot.style.display = 'none';
      if (cursorRing) cursorRing.style.display = 'none';
    }"""

    if cursor_old in content:
        content = content.replace(cursor_old, cursor_new)
        print("Updated cursor with fine pointer & visibility check")

    # 2. P1-1: Three.js animate() visibility check & P2-4 reduced motion
    three_old = """      // G. Render Loop
      const clock = new THREE.Clock();
      function animate() {
        requestAnimationFrame(animate);
        if (!isHeroVisible) return;

        const elapsedTime = clock.getElapsedTime();"""

    three_new = """      // G. Render Loop
      const clock = new THREE.Clock();
      const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

      function animate() {
        if (!isPageActive || !isHeroVisible) {
          setTimeout(() => { if (isPageActive && isHeroVisible) requestAnimationFrame(animate); }, 250);
          return;
        }
        requestAnimationFrame(animate);

        const elapsedTime = clock.getElapsedTime();

        if (prefersReducedMotion) {
          vGroup.rotation.y = 0;
          vGroup.rotation.x = 0;
          renderer.render(scene, camera);
          return;
        }"""

    if three_old in content:
        content = content.replace(three_old, three_new)
        print("Updated Three.js animate() with visibility & reduced motion")

    # 3. P1-1: Lenis visibility check
    lenis_old = """      function lenisRaf(time) {
        lenis.raf(time);
        requestAnimationFrame(lenisRaf);
      }
      requestAnimationFrame(lenisRaf);"""

    lenis_new = """      function lenisRaf(time) {
        if (isPageActive) {
          lenis.raf(time);
        }
        requestAnimationFrame(lenisRaf);
      }
      requestAnimationFrame(lenisRaf);"""

    if lenis_old in content:
        content = content.replace(lenis_old, lenis_new)
        print("Updated lenisRaf with visibility check")

    # 4. P2-4: CSS prefers-reduced-motion
    reduced_motion_css = """
    /* WCAG 2.1 AA Reduced Motion Accessibility */
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
      .cursor-dot, .cursor-ring { display: none !important; }
    }
  </style>"""

    if "@media (prefers-reduced-motion: reduce)" not in content and "</style>" in content:
        content = content.replace("</style>", reduced_motion_css, 1)
        print("Added prefers-reduced-motion CSS block")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filepath}")

for p in ['index.html', 'VALIXIS WEBSITE/index.html']:
    if os.path.exists(p):
        update_index_performance(p)
