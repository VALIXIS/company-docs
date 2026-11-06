import * as THREE from 'three'
let tex
export function glowTexture() {
  if (tex) return tex
  const c = document.createElement('canvas'); c.width = c.height = 128
  const g = c.getContext('2d'), r = g.createRadialGradient(64, 64, 0, 64, 64, 64)
  r.addColorStop(0, 'rgba(255,200,90,1)'); r.addColorStop(0.25, 'rgba(255,140,20,.55)')
  r.addColorStop(1, 'rgba(255,90,0,0)')
  g.fillStyle = r; g.fillRect(0, 0, 128, 128)
  tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace
  return tex
}
export function fogTexture() {
  const c = document.createElement('canvas'); c.width = c.height = 128
  const g = c.getContext('2d'), r = g.createRadialGradient(64, 64, 0, 64, 64, 64)
  r.addColorStop(0, 'rgba(120,95,70,.35)'); r.addColorStop(1, 'rgba(120,95,70,0)')
  g.fillStyle = r; g.fillRect(0, 0, 128, 128)
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t
}
