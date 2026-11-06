import { Component, Suspense, useRef, useState } from 'react'
import * as THREE from 'three'
import { Canvas } from '@react-three/fiber'
import { PerformanceMonitor, Environment } from '@react-three/drei'
import Dino from './Dino'
import CameraRig from './CameraRig'
import Embers from './Embers'
import { Cavern, Lights, Placeholder } from './Cavern'
import { REST } from '../lib/cameraPath'
import { store } from '../lib/store'

class Boundary extends Component {
  state = { failed: false }
  static getDerivedStateFromError() { return { failed: true } }
  componentDidCatch(e) { console.warn('[DinoScene] model failed, using placeholder:', e) }
  render() { return this.state.failed ? this.props.fallback : this.props.children }
}

export default function DinoScene({ active }) {
  const rig = useRef({ head: null, anchors: null, tick: null })
  const [dpr, setDpr] = useState(store.isMobile ? 1.25 : 1.75)
  const p0 = REST.P0
  return (
    <Canvas
      frameloop={active ? 'always' : 'never'}   // GPU fully idle once you are inside the sanctum
      dpr={dpr}
      camera={{ fov: 32, near: 0.05, far: 80, position: [p0.x, p0.y, p0.z] }}
      gl={{ 
        antialias: true, 
        powerPreference: 'high-performance', 
        alpha: false, 
        stencil: false,
        toneMapping: THREE.ACESFilmicToneMapping,
        toneMappingExposure: 1.2
      }}
      style={{ touchAction: 'none', pointerEvents: 'none' }}
    >
      <PerformanceMonitor onDecline={() => setDpr((d) => Math.max(1, d - 0.25))} />
      <color attach="background" args={['#040605']} />
      <fogExp2 attach="fog" args={['#070a08', 0.035]} />
      <Environment files="/textures/env.hdr" environmentIntensity={0.65} />
      <Lights />
      <Cavern />
      <Embers />
      <CameraRig rig={rig} />
      <Boundary fallback={<Placeholder />}>
        <Suspense fallback={<Placeholder />}>
          <Dino rig={rig} />
        </Suspense>
      </Boundary>
    </Canvas>
  )
}
