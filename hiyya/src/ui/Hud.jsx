import { useEffect, useRef } from 'react'
import gsap from 'gsap'
import { store, smooth } from '../lib/store'
import { playRoar } from '../lib/roar'

/** Everything that tracks the dive lives here and is written straight to the DOM (no React re-renders). */
export default function Hud({ soundOn, setSoundOn }) {
  const hero = useRef(), vortex = useRef(), spin = useRef(), c1 = useRef(), c2 = useRef(), c3 = useRef(), hint = useRef(), flash = useRef()
  useEffect(() => {
    let fired = false
    const cap = (el, a, b, c, d, p) => {
      const o = smooth(a, b, p) * (1 - smooth(c, d, p))
      el.style.opacity = o; el.style.transform = `translateY(${(1 - o) * 24}px) scale(${0.96 + o * 0.04})`
    }
    const tick = () => {
      const p = store.dive, after = store.after
      const h = 1 - smooth(0, 0.09, p)
      hero.current.style.opacity = h; hero.current.style.visibility = h < 0.01 ? 'hidden' : 'visible'
      hint.current.style.opacity = h
      cap(c1.current, 0.1, 0.18, 0.26, 0.34, p)
      cap(c2.current, 0.3, 0.38, 0.5, 0.58, p)
      cap(c3.current, 0.58, 0.66, 0.76, 0.84, p)
      // molten vortex: ramps in while we are inside the throat, fades as the sanctum scrolls up
      const v = smooth(0.74, 0.95, p) * (1 - smooth(0, 1, after))
      vortex.current.style.opacity = v
      vortex.current.style.visibility = v < 0.005 ? 'hidden' : 'visible'
      vortex.current.style.transform = `scale(${0.6 + 1.6 * smooth(0.7, 1, p) + after * 0.8})`
      flash.current.style.opacity = smooth(0.9, 1, p) * (1 - smooth(0, 0.35, after)) * 0.9
      // roar sound fires as the jaws start to open
      if (p > 0.2 && !fired) { fired = true; if (store.sound) playRoar() }
      if (p < 0.08) fired = false
    }
    gsap.ticker.add(tick)
    return () => gsap.ticker.remove(tick)
  }, [])

  const capCls = 'fixed inset-0 z-[6] flex items-center justify-center pointer-events-none opacity-0 text-center px-6 font-royal text-4xl sm:text-6xl md:text-8xl tracking-wide text-white [text-shadow:0_0_60px_rgba(255,122,0,.65)]'
  return (
    <>
      {/* molten vortex portal */}
      <div ref={vortex} className="fixed inset-0 z-[5] pointer-events-none overflow-hidden invisible" style={{ willChange: 'transform, opacity' }}>
        <div ref={spin} className="absolute left-1/2 top-1/2 w-[160vmax] h-[160vmax] -ml-[80vmax] -mt-[80vmax] animate-[vortexSpin_6s_linear_infinite]"
          style={{ background: 'conic-gradient(from 0deg, #1a0300, #8a1c00, #FF7A00, #3b0700, #F59E0B, #5c0d00, #FF4500, #1a0300)', filter: 'blur(28px)' }} />
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(6,9,7,.92)_0%,rgba(40,6,0,.55)_28%,transparent_70%)]" />
      </div>
      <div ref={flash} className="fixed inset-0 z-[5] pointer-events-none opacity-0 bg-[radial-gradient(circle,#FDE68A,#FF7A00_55%,#5c0d00)] mix-blend-screen" />
      {/* vignette */}
      <div className="fixed inset-0 z-[4] pointer-events-none bg-[radial-gradient(ellipse_at_center,transparent_45%,rgba(0,0,0,.75)_100%)]" />

      <div ref={c1} className={capCls}>IT SEES YOU.</div>
      <div ref={c2} className={capCls}>IT ROARS.</div>
      <div ref={c3} className={capCls}>ENTER THE JAWS.</div>

      <div ref={hero} className="fixed inset-0 z-[6] pointer-events-none px-6 md:px-12 py-7 flex flex-col justify-between">
        <div className="flex items-start justify-between gap-4">
          <div>
            <p className="font-royal text-lg md:text-2xl tracking-[0.18em] text-white">HIYYA DINO MANDI <span className="text-amber-gold">·</span> GUNTUR</p>
            <p className="mt-2 font-mono text-[10px] md:text-[11px] tracking-[0.3em] uppercase text-amber-gold/70">India’s 1st Dinosaur-Themed Arabian Mandi</p>
          </div>
          <button onClick={() => setSoundOn(!soundOn)} className="pointer-events-auto font-mono text-[10px] tracking-[0.25em] uppercase border border-amber-gold/40 rounded-full px-4 py-2 text-amber-soft hover:bg-amber-gold/10">
            Sound {soundOn ? 'On' : 'Off'}
          </button>
        </div>
        <div className="flex items-end justify-between">
          <p className="font-mono text-[10px] md:text-xs tracking-[0.25em] text-gray-400">16.3132° N, 80.4208° E</p>
          <p className="hidden md:block font-mono text-[10px] tracking-[0.25em] text-gray-500">BRINDAVAN GARDENS · GUNTUR</p>
        </div>
      </div>
      <div ref={hint} className="fixed bottom-7 left-0 right-0 z-[6] flex justify-center pointer-events-none">
        <p className="font-mono text-[11px] md:text-xs tracking-[0.35em] uppercase text-amber-soft animate-[pulseHint_2.4s_ease-in-out_infinite]">Scroll to Enter the Beast ↓</p>
      </div>
    </>
  )
}
