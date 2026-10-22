/**
 * VALIXIS 3D Interactive WebGL Scene
 * Built with Three.js for high-performance background visual depth
 */

(function initVALIXIS3D() {
  const container = document.getElementById('canvas3d-container');
  if (!container || typeof THREE === 'undefined') return;

  const canvas = document.getElementById('canvas3d');
  const scene = new THREE.Scene();

  const camera = new THREE.PerspectiveCamera(
    60,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
  );
  camera.position.z = 85;

  const renderer = new THREE.WebGLRenderer({
    canvas: canvas,
    alpha: true,
    antialias: true
  });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // 1. Central 3D Geometric Tech Core (Icosahedron Wireframe)
  const coreGeometry = new THREE.IcosahedronGeometry(22, 1);
  const coreMaterial = new THREE.MeshBasicMaterial({
    color: 0x00f2fe,
    wireframe: true,
    transparent: true,
    opacity: 0.22
  });
  const coreMesh = new THREE.Mesh(coreGeometry, coreMaterial);
  scene.add(coreMesh);

  // 2. Outer Concentric Halo
  const outerGeometry = new THREE.TorusGeometry(32, 0.4, 16, 100);
  const outerMaterial = new THREE.MeshBasicMaterial({
    color: 0x6366f1,
    transparent: true,
    opacity: 0.18
  });
  const outerRing = new THREE.Mesh(outerGeometry, outerMaterial);
  outerRing.rotation.x = Math.PI / 3;
  scene.add(outerRing);

  // 3. Second Slanted Cyan Ring
  const innerRingGeo = new THREE.TorusGeometry(26, 0.3, 16, 100);
  const innerRingMat = new THREE.MeshBasicMaterial({
    color: 0x10b981,
    transparent: true,
    opacity: 0.15
  });
  const innerRing = new THREE.Mesh(innerRingGeo, innerRingMat);
  innerRing.rotation.y = Math.PI / 4;
  scene.add(innerRing);

  // 4. Floating Neural Particles & Constellation
  const particleCount = 130;
  const positions = new Float32Array(particleCount * 3);
  const velocities = [];

  for (let i = 0; i < particleCount; i++) {
    const radius = 35 + Math.random() * 55;
    const theta = Math.random() * Math.PI * 2;
    const phi = Math.acos(Math.random() * 2 - 1);

    positions[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
    positions[i * 3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
    positions[i * 3 + 2] = radius * Math.cos(phi);

    velocities.push({
      x: (Math.random() - 0.5) * 0.05,
      y: (Math.random() - 0.5) * 0.05,
      z: (Math.random() - 0.5) * 0.05
    });
  }

  const particleGeometry = new THREE.BufferGeometry();
  particleGeometry.setAttribute(
    'position',
    new THREE.BufferAttribute(positions, 3)
  );

  // Generate glowing particle sprite
  function createParticleTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 32;
    canvas.height = 32;
    const ctx = canvas.getContext('2d');
    const gradient = ctx.createRadialGradient(16, 16, 0, 16, 16, 16);
    gradient.addColorStop(0, 'rgba(0, 242, 254, 1)');
    gradient.addColorStop(0.3, 'rgba(99, 102, 241, 0.7)');
    gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');
    ctx.fillStyle = gradient;
    ctx.beginPath();
    ctx.arc(16, 16, 16, 0, Math.PI * 2);
    ctx.fill();
    return new THREE.CanvasTexture(canvas);
  }

  const particleMaterial = new THREE.PointsMaterial({
    size: 2.5,
    map: createParticleTexture(),
    transparent: true,
    opacity: 0.75,
    blending: THREE.AdditiveBlending,
    depthWrite: false
  });

  const particleSystem = new THREE.Points(particleGeometry, particleMaterial);
  scene.add(particleSystem);

  // Interactive Mouse Tilt
  let mouseX = 0;
  let mouseY = 0;
  let targetX = 0;
  let targetY = 0;
  const windowHalfX = window.innerWidth / 2;
  const windowHalfY = window.innerHeight / 2;

  document.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX - windowHalfX) * 0.0008;
    mouseY = (e.clientY - windowHalfY) * 0.0008;
  }, { passive: true });

  // Animation Loop
  let clock = new THREE.Clock();

  function animate() {
    requestAnimationFrame(animate);
    const delta = clock.getDelta();

    // Rotate geometric core
    coreMesh.rotation.y += 0.25 * delta;
    coreMesh.rotation.x += 0.15 * delta;

    outerRing.rotation.z += 0.1 * delta;
    outerRing.rotation.y += 0.08 * delta;

    innerRing.rotation.x -= 0.12 * delta;
    innerRing.rotation.z -= 0.09 * delta;

    // Gentle particle drift
    const pos = particleGeometry.attributes.position.array;
    for (let i = 0; i < particleCount; i++) {
      pos[i * 3] += velocities[i].x;
      pos[i * 3 + 1] += velocities[i].y;
      pos[i * 3 + 2] += velocities[i].z;

      // Boundary rebound
      if (Math.abs(pos[i * 3]) > 75) velocities[i].x *= -1;
      if (Math.abs(pos[i * 3 + 1]) > 75) velocities[i].y *= -1;
      if (Math.abs(pos[i * 3 + 2]) > 75) velocities[i].z *= -1;
    }
    particleGeometry.attributes.position.needsUpdate = true;

    // Smooth camera inertia with mouse
    targetX += (mouseX - targetX) * 0.05;
    targetY += (mouseY - targetY) * 0.05;

    camera.position.x = targetX * 30;
    camera.position.y = -targetY * 30;
    camera.lookAt(scene.position);

    renderer.render(scene, camera);
  }

  animate();

  // Resize listener
  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });
})();
