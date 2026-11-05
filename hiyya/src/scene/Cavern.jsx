import { useLayoutEffect, useMemo, useRef } from 'react'
import * as THREE from 'three'
import { useFrame } from '@react-three/fiber'
import { fogTexture } from './glow'
import { store } from '../lib/store'

function rand(seed) { let s = seed; return () => (s = (s * 16807) % 2147483647) / 2147483647 }

export function Cavern() {
  const rocks = useRef(), spikes = useRef()
  const nRocks = store.isMobile ? 36 : 70, nSpikes = store.isMobile ? 24 : 46
  useLayoutEffect(() => {
    const r = rand(42), m = new THREE.Matrix4(), q = new THREE.Quaternion(), e = new THREE.Euler(), s = new THREE.Vector3(), p = new THREE.Vector3()
    for (let i = 0; i < nRocks; i++) {                    // boulders ringing the back half of the cave
      const a = Math.PI + (r() - 0.5) * Math.PI * 1.5, rad = 14 + r() * 10, sc = 1.5 + r() * 4.5
      p.set(Math.sin(a) * rad, sc * 0.3, -Math.cos(a) * rad * 0.9 - 2)
      e.set(r() * 3, r() * 3, r() * 3); q.setFromEuler(e); s.set(sc, sc * (0.7 + r()), sc)
      rocks.current.setMatrixAt(i, m.compose(p, q, s))
    }
    for (let i = 0; i < nSpikes; i++) {                   // stalactites
      const a = r() * Math.PI * 2, rad = 3 + r() * 18, h = 2 + r() * 5
      p.set(Math.sin(a) * rad, 14 - h / 2 + r(), Math.cos(a) * rad - 2)
      q.setFromEuler(e.set(Math.PI, 0, 0)); s.set(0.5 + r() * 0.9, h, 0.5 + r() * 0.9)
      spikes.current.setMatrixAt(i, m.compose(p, q, s))
    }
    rocks.current.instanceMatrix.needsUpdate = spikes.current.instanceMatrix.needsUpdate = true
  }, [nRocks, nSpikes])
  return (
    <group>
      <mesh rotation-x={-Math.PI / 2} position-y={-0.02}>
        <planeGeometry args={[80, 80]} />
        <meshStandardMaterial color="#120d08" roughness={0.92} metalness={0.05} />
      </mesh>
      <instancedMesh ref={rocks} args={[null, null, nRocks]}>
        <dodecahedronGeometry args={[1, 0]} />
        <meshStandardMaterial color="#1a130d" roughness={1} flatShading />
      </instancedMesh>
      <instancedMesh ref={spikes} args={[null, null, nSpikes]}>
        <coneGeometry args={[1, 1, 6]} />
        <meshStandardMaterial color="#17110c" roughness={1} flatShading />
      </instancedMesh>
    </group>
  )
}

export function FogCards({ n = store.isMobile ? 5 : 9 }) {
  const grp = useRef()
  const tex = useMemo(() => fogTexture(), [])
  const items = useMemo(() => { const r = rand(7); return Array.from({ length: n }, () => ({ x: (r() - 0.5) * 22, y: 0.6 + r() * 2.2, z: -4 + r() * 14, s: 7 + r() * 7, sp: 0.05 + r() * 0.1 })) }, [n])
  useFrame((st) => grp.current.children.forEach((c, i) => { c.position.x = items[i].x + Math.sin(st.clock.elapsedTime * items[i].sp + i) * 1.8 }))
  return (
    <group ref={grp}>
      {items.map((it, i) => (
        <sprite key={i} position={[it.x, it.y, it.z]} scale={[it.s, it.s * 0.45, 1]}>
          <spriteMaterial map={tex} transparent opacity={0.55} depthWrite={false} fog={false} />
        </sprite>
      ))}
    </group>
  )
}

export function Lights() {
  return (
    <>
      <hemisphereLight args={['#243228', '#050705', 0.8]} />
      {/* Dramatic amber rim light defining the spine and crown */}
      <spotLight position={[0, 9, -5]} color="#ff7a00" intensity={45} angle={0.7} penumbra={0.6} decay={2} />
      {/* High-quality warm key light carving out the snout and teeth */}
      <spotLight position={[2.5, 6.5, 9.5]} color="#fff3db" intensity={50} angle={0.5} penumbra={0.5} decay={2} />
      {/* Soft emerald bioluminescent cheek fill */}
      <pointLight position={[-5, 3.5, 3]} color="#10b981" intensity={12} distance={18} decay={2} />
    </>
  )
}

export function Placeholder() {
  // Shown while t-rex.glb streams in, or permanently if it fails to load.
  const g = useRef()
  const tex = useMemo(() => fogTexture(), [])
  useFrame((s) => { if (g.current) g.current.children.forEach((c) => c.scale.setScalar(0.45 + Math.sin(s.clock.elapsedTime * 2) * 0.08)) })
  return (
    <group>
      <mesh position={[0, 3.2, 3]}><sphereGeometry args={[2.2, 24, 16]} /><meshStandardMaterial color="#0c0907" roughness={1} /></mesh>
      <mesh position={[0, 4.9, 4.4]} scale={[1.2, 1, 1.9]}><sphereGeometry args={[1, 24, 16]} /><meshStandardMaterial color="#0c0907" roughness={1} /></mesh>
      <group ref={g}>
        {[-0.3, 0.3].map((x) => (
          <sprite key={x} position={[x, 5.2, 5.2]}>
            <spriteMaterial map={tex} color="#ff9a1a" blending={THREE.AdditiveBlending} transparent depthWrite={false} fog={false} />
          </sprite>
        ))}
      </group>
    </group>
  )
}
