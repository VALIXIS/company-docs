import { useEffect, useMemo, useRef } from 'react'
import * as THREE from 'three'
import { useGLTF } from '@react-three/drei'
import { createAnchors } from '../lib/cameraPath'
import { store, smooth } from '../lib/store'
import { glowTexture } from './glow'

export const MODEL_URL = '/models/t-rex.glb'
// Roar clip: closed until 2.5s, fully open at 3.0s (55°), open until ~4.5s, closes by 5.5s
const ROAR_START = 2.1, ROAR_END = 4.3

// glTF loader strips "." from node names, so "bn_Head.10" becomes "bn_Head10".
function findBone(root, key) {
  const re = new RegExp(`^bn_${key}\\d*$`)
  let found = null
  root.traverse((o) => { if (!found && re.test(o.name)) found = o })
  return found
}

export default function Dino({ rig }) {
  const { scene, animations } = useGLTF(MODEL_URL, false) // false = skip Draco, meshopt is on by default
  const glowL = useRef(), glowR = useRef(), lightL = useRef(), lightR = useRef()

  const api = useMemo(() => {
    scene.traverse((o) => {
      if (o.isMesh) { o.frustumCulled = false; o.castShadow = false; o.receiveShadow = false }
    })
    const mixer = new THREE.AnimationMixer(scene)
    const clip = (n) => THREE.AnimationClip.findByName(animations, n)
    const idle = mixer.clipAction(clip('idle')), roar = mixer.clipAction(clip('roar'))
    idle.play(); roar.play(); roar.paused = true; roar.setEffectiveWeight(0)
    const bones = { head: findBone(scene, 'Head'), jaw: findBone(scene, 'Jaw'),
      eyeL: findBone(scene, 'LeftEye'), eyeR: findBone(scene, 'RightEye') }
    scene.updateMatrixWorld(true)
    return { mixer, idle, roar, bones }
  }, [scene, animations])

  const _q = useMemo(() => new THREE.Quaternion(), [])
  const _v = useMemo(() => new THREE.Vector3(), [])

  useEffect(() => {
    // Anchors are captured in bind pose BEFORE the first animation tick.
    rig.current.head = api.bones.head
    rig.current.anchors = createAnchors(api.bones.head)
    rig.current.tick = (time, dt) => {
      const p = store.dive
      const w = smooth(0.02, 0.14, p)                       // idle -> roar crossfade
      api.idle.setEffectiveWeight(1 - w)
      api.roar.setEffectiveWeight(w)
      api.roar.time = ROAR_START + (ROAR_END - ROAR_START) * smooth(0.0, 0.8, p) // scroll scrubs the roar
      api.mixer.update(dt)
      scene.updateMatrixWorld(true)
      // amber predator eyes follow the eye bones
      const pulse = 0.85 + Math.sin(time * 2.2) * 0.15 + (w > 0.3 ? 0.4 : 0)
      ;[['eyeL', glowL, lightL], ['eyeR', glowR, lightR]].forEach(([b, g, l]) => {
        if (!api.bones[b] || !g.current) return
        api.bones[b].getWorldPosition(_v)
        g.current.position.copy(_v); g.current.position.z += 0.08
        g.current.scale.setScalar(0.5 * pulse)
        l.current.position.copy(_v); l.current.position.z += 0.35
        l.current.intensity = 2.2 * pulse
      })
    }
    return () => { rig.current.tick = null; rig.current.head = null; rig.current.anchors = null }
  }, [api, rig, scene, _q, _v])

  return (
    <>
      <primitive object={scene} />
      {[glowL, glowR].map((r, i) => (
        <sprite key={i} ref={r}>
          <spriteMaterial map={glowTexture()} blending={THREE.AdditiveBlending} depthWrite={false} transparent fog={false} />
        </sprite>
      ))}
      <pointLight ref={lightL} color="#ff9a1a" distance={5} decay={2} />
      <pointLight ref={lightR} color="#ff9a1a" distance={5} decay={2} />
    </>
  )
}

useGLTF.preload(MODEL_URL, false)
