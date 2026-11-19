/* One branded WebGL scene per service page. The page remains usable without WebGL. */
(function () {
  'use strict';
  const hero = document.querySelector('.service-hero, body.services-overview .page-hero');
  if (!hero || !window.THREE) return;

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const mobile = window.matchMedia('(max-width: 760px)').matches;
  const canvas = document.createElement('canvas');
  canvas.className = 'service-scene-canvas';
  canvas.setAttribute('aria-hidden', 'true');
  hero.prepend(canvas);

  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: !mobile, powerPreference: mobile ? 'low-power' : 'high-performance' });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, mobile ? 1.25 : 1.75));
    hero.classList.add('has-service-webgl');
  } catch (_) {
    canvas.remove();
    return;
  }

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(42, 1, .1, 100);
  camera.position.set(0, 0, 10);
  scene.add(new THREE.AmbientLight(0xF5F7FA, .6));
  const light = new THREE.PointLight(0x00E5FF, 2.3, 30);
  light.position.set(4, 5, 7);
  scene.add(light);
  const group = new THREE.Group();
  scene.add(group);

  const cyan = new THREE.MeshPhongMaterial({ color: 0x00E5FF, emissive: 0x005b69, shininess: 95, transparent: true, opacity: .87, side: THREE.DoubleSide });
  const blue = new THREE.MeshPhongMaterial({ color: 0x2563FF, emissive: 0x101b53, shininess: 110, transparent: true, opacity: .88, side: THREE.DoubleSide });
  const purple = new THREE.MeshPhongMaterial({ color: 0x7C3AED, emissive: 0x2b0b67, shininess: 105, transparent: true, opacity: .83, side: THREE.DoubleSide });
  const magenta = new THREE.MeshPhongMaterial({ color: 0xD946EF, emissive: 0x4f125a, shininess: 95, transparent: true, opacity: .83, side: THREE.DoubleSide });
  const wire = new THREE.MeshBasicMaterial({ color: 0x00E5FF, wireframe: true, transparent: true, opacity: .32 });
  const path = location.pathname;

  function panel(w, h, x, y, z, material) {
    const mesh = new THREE.Mesh(new THREE.BoxGeometry(w, h, .12), material);
    mesh.position.set(x, y, z);
    group.add(mesh);
    const edge = new THREE.LineSegments(new THREE.EdgesGeometry(mesh.geometry), new THREE.LineBasicMaterial({ color: 0xF5F7FA, transparent: true, opacity: .38 }));
    mesh.add(edge);
    return mesh;
  }

  if (path.includes('web-platforms')) {
    panel(4.2, 2.75, 0, 0, 0, blue);
    panel(3.2, 1.8, .55, -.22, .3, purple);
    panel(1.4, 1.12, -1.35, .35, .55, cyan);
    const bar = panel(4.2, .17, 0, 1.45, .1, magenta);
    bar.rotation.z = 0;
  } else if (path.includes('ai-automation')) {
    const core = new THREE.Mesh(new THREE.IcosahedronGeometry(1.55, 1), wire);
    group.add(core);
    for (let i = 0; i < 8; i++) {
      const angle = i * Math.PI / 4;
      const node = new THREE.Mesh(new THREE.SphereGeometry(.16, 12, 12), i % 2 ? magenta : cyan);
      node.position.set(Math.cos(angle) * 2.7, Math.sin(angle) * 1.85, Math.sin(angle * 2) * .7);
      group.add(node);
      const points = [new THREE.Vector3(0, 0, 0), node.position];
      group.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(points), new THREE.LineBasicMaterial({ color: 0x2563FF, transparent: true, opacity: .55 })));
    }
  } else if (path.includes('software-mobile')) {
    panel(2.5, 3.9, -1.05, 0, -.6, blue);
    panel(2.25, 3.55, -.9, 0, -.25, purple);
    panel(2.4, 3.65, .95, -.1, .35, cyan);
    panel(1.55, .14, 1, 1.3, .5, magenta);
    panel(1.65, .85, 1, .3, .52, blue);
  } else if (path.includes('3d-gaming-interactive')) {
    group.add(new THREE.Mesh(new THREE.TorusKnotGeometry(1.4, .31, 100, 12, 2, 3), cyan));
    const shell = new THREE.Mesh(new THREE.IcosahedronGeometry(2.8, 1), wire);
    group.add(shell);
  } else {
    group.add(new THREE.Mesh(new THREE.IcosahedronGeometry(1.65, 1), wire));
    for (let i = 0; i < 3; i++) {
      const orbit = new THREE.Mesh(new THREE.TorusGeometry(2.5 + i * .33, .025, 8, 90), [cyan, purple, magenta][i]);
      orbit.rotation.set(.5 + i * .3, i * .7, i * .5);
      group.add(orbit);
    }
  }

  const count = mobile ? 70 : 220;
  const positions = new Float32Array(count * 3);
  for (let i = 0; i < positions.length; i += 3) {
    positions[i] = (Math.random() - .5) * 15;
    positions[i + 1] = (Math.random() - .5) * 9;
    positions[i + 2] = (Math.random() - .5) * 6 - 2;
  }
  const dustGeometry = new THREE.BufferGeometry();
  dustGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  const dust = new THREE.Points(dustGeometry, new THREE.PointsMaterial({ color: 0x00E5FF, size: .026, transparent: true, opacity: .64 }));
  scene.add(dust);

  function resize() {
    const w = Math.max(canvas.clientWidth, 1), h = Math.max(canvas.clientHeight, 1);
    camera.aspect = w / h;
    camera.position.z = mobile ? 11.5 : 10;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h, false);
    renderer.render(scene, camera);
  }
  resize();
  window.addEventListener('resize', resize, { passive: true });

  let visible = true, pointerX = 0, pointerY = 0, frame = 0;
  const observer = new IntersectionObserver(entries => { visible = entries[0].isIntersecting; if (visible && !reduced && !frame) frame = requestAnimationFrame(draw); }, { threshold: .01 });
  observer.observe(hero);
  hero.addEventListener('pointermove', event => {
    if (mobile || reduced) return;
    const rect = hero.getBoundingClientRect();
    pointerX = ((event.clientX - rect.left) / rect.width - .5) * .4;
    pointerY = ((event.clientY - rect.top) / rect.height - .5) * .25;
  }, { passive: true });

  function draw(time) {
    frame = 0;
    if (!visible || document.hidden || reduced) return;
    const t = time * .001;
    group.rotation.y = t * .18 + pointerX;
    group.rotation.x = Math.sin(t * .36) * .14 + pointerY;
    group.position.y = Math.sin(t * .8) * .12;
    dust.rotation.y = t * .012;
    renderer.render(scene, camera);
    frame = requestAnimationFrame(draw);
  }
  if (!reduced) frame = requestAnimationFrame(draw);
  document.addEventListener('visibilitychange', () => { if (!document.hidden && visible && !reduced && !frame) frame = requestAnimationFrame(draw); });

  const sections = document.querySelectorAll('.content-section, .framework-section');
  if (!reduced && 'IntersectionObserver' in window) {
    const reveal = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('motion-visible'); reveal.unobserve(entry.target); }
    }), { threshold: .08 });
    sections.forEach(section => { section.classList.add('motion-section'); reveal.observe(section); });
  }
})();
