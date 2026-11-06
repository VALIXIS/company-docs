import * as THREE from 'three'
import { clamp, smooth, easeInOutCubic } from './store'

/* ──────────────────────────────────────────────────────────────────────────
   COORDINATES (metres). Your GLB: root scale 0.01, T-Rex faces +Z, Y is up.
   Measured from the bind pose:  eyes ≈ (±0.3, 5.2, 4.4)
                                 jaw hinge ≈ (0, 4.9, 3.8)
                                 snout tip ≈ z 5.6
   If the dive misses the mouth, tune ONLY the numbers in REST below.
   ────────────────────────────────────────────────────────────────────────── */
export const REST = {
  // Cubic Bézier control points for the camera position
  P0: new THREE.Vector3(0, 5.2, 11.0),    // hero: eye-to-eye, world space
  P1: new THREE.Vector3(0.0, 5.55, 8.4),  // pulls the arc slightly up before diving, world space
  P2: new THREE.Vector3(0, 4.55, 6.5),    // in front of the open jaws, ATTACHED to head bone
  P3: new THREE.Vector3(0, 4.35, 4.3),    // deep in the throat, ATTACHED to head bone
  // Look-at: eyes -> throat
  L0: new THREE.Vector3(0, 5.15, 4.6),    // between the eyes, world space
  L1: new THREE.Vector3(0, 4.25, 2.9),    // down the gullet, ATTACHED to head bone
}
const LOCAL_FROM_HEAD = ['P2', 'P3', 'L1']

export function createAnchors(head) {
  head.updateWorldMatrix(true, false)
  const inv = new THREE.Matrix4().copy(head.matrixWorld).invert()
  const local = {}
  LOCAL_FROM_HEAD.forEach((k) => (local[k] = REST[k].clone().applyMatrix4(inv)))
  return local
}

const _p = [new THREE.Vector3(), new THREE.Vector3(), new THREE.Vector3(), new THREE.Vector3()]
const _a = new THREE.Vector3()

/** B(u) = (1-u)^3 P0 + 3(1-u)^2 u P1 + 3(1-u)u^2 P2 + u^3 P3 */
export function bezier(p0, p1, p2, p3, u, out) {
  const v = 1 - u
  return out.set(0, 0, 0)
    .addScaledVector(p0, v * v * v)
    .addScaledVector(p1, 3 * v * v * u)
    .addScaledVector(p2, 3 * v * u * u)
    .addScaledVector(p3, u * u * u)
}

/**
 * Evaluates camera position + look-at for dive progress p ∈ [0,1].
 *  p 0.00–0.10  camera holds, creature breathes (tiny dolly)
 *  p 0.10–0.92  camera rides the Bézier  (u = easeInOutCubic)
 *  look-at      L(u') = lerp(L0, L1, smoothstep(0.15, 0.85, u))
 */
export function evaluateRig(p, head, anchors, aspect, outPos, outLook) {
  head.updateWorldMatrix(true, false)
  // portrait screens pull the hero shot back so the head still fits
  const k = clamp(1.05 / aspect, 1, 1.9)
  const z0 = REST.L0.z
  _p[0].copy(REST.P0); _p[0].z = z0 + (REST.P0.z - z0) * k
  _p[1].copy(REST.P1); _p[1].z = z0 + (REST.P1.z - z0) * k
  _p[2].copy(anchors.P2).applyMatrix4(head.matrixWorld)
  _p[3].copy(anchors.P3).applyMatrix4(head.matrixWorld)

  const u = easeInOutCubic(clamp((p - 0.1) / 0.82))
  bezier(_p[0], _p[1], _p[2], _p[3], u, outPos)
  // slow handheld push before the dive begins
  outPos.z -= smooth(0, 0.1, p) * 0.35

  _a.copy(anchors.L1).applyMatrix4(head.matrixWorld)
  outLook.lerpVectors(REST.L0, _a, smooth(0.15, 0.85, u))
}
