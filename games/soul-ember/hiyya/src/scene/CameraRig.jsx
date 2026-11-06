import { useMemo } from 'react'
import * as THREE from 'three'
import { useFrame, useThree } from '@react-three/fiber'
import { evaluateRig, createAnchors } from '../lib/cameraPath'
import { store, smooth } from '../lib/store'

/** Drives the camera from store.dive. Also ticks the dino animation first so the head
 *  bone matrix is current when the head-attached Bézier points are evaluated. */
export default function CameraRig({ rig }) {
  const { camera, size, pointer } = useThree()
  const fake = useMemo(() => {            // identity "head": used until/unless the GLB loads
    const h = new THREE.Object3D(); h.updateMatrixWorld(true)
    return { head: h, anchors: createAnchors(h) }
  }, [])
  const pos = useMemo(() => new THREE.Vector3(), [])
  const look = useMemo(() => new THREE.Vector3(), [])

  useFrame((state, dt) => {
    const d = Math.min(dt, 0.05)
    // damped scroll: responsive follow-through without lag
    store.dive += (store.target - store.dive) * (1 - Math.exp(-9 * d))
    if (Math.abs(store.target - store.dive) < 0.0004) store.dive = store.target
    const p = store.dive

    rig.current.tick?.(state.clock.elapsedTime, d)
    const head = rig.current.head || fake.head
    const anchors = rig.current.anchors || fake.anchors
    evaluateRig(p, head, anchors, size.width / size.height, pos, look)

    // hero parallax follows the pointer, fades out as the dive starts
    const par = 1 - smooth(0, 0.12, p)
    pos.x += pointer.x * 0.35 * par
    pos.y += pointer.y * 0.18 * par
    // smooth cinematic roar tremor (harmonic resonance, no random jitter)
    const time = state.clock.elapsedTime
    const shake = smooth(0.25, 0.5, p) * (1 - smooth(0.82, 0.98, p)) * 0.035
    pos.x += (Math.sin(time * 24) * 0.65 + Math.cos(time * 38) * 0.35) * shake
    pos.y += (Math.cos(time * 28) * 0.55 + Math.sin(time * 18) * 0.45) * shake
    camera.position.copy(pos)
    camera.lookAt(look)
    // FOV opens up as we plunge for a sense of speed
    const fov = 32 + 22 * smooth(0.5, 0.95, p)
    if (Math.abs(camera.fov - fov) > 0.01) { camera.fov = fov; camera.updateProjectionMatrix() }
  })
  return null
}
