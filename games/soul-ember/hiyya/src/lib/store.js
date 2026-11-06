// Plain mutable object: read inside rAF / useFrame loops, never triggers React renders.
export const store = {
  target: 0,   // raw dive progress 0..1 from ScrollTrigger
  dive: 0,     // damped dive progress used by camera, dino and overlays
  after: 0,    // 0..1 how far the user has scrolled past the dive (content reveal)
  sound: true,
  isMobile: typeof window !== 'undefined' && window.matchMedia('(max-width: 820px)').matches,
}
export const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v))
export const smooth = (a, b, v) => { const t = clamp((v - a) / (b - a)); return t * t * (3 - 2 * t) }
export const easeInOutCubic = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2)
