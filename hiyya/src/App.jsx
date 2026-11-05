import { useCallback, useEffect, useRef, useState } from 'react'
import Lenis from 'lenis'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import DinoScene from './scene/DinoScene'
import Hud from './ui/Hud'
import Loader from './ui/Loader'
import Sanctum from './ui/Sanctum'
import { store } from './lib/store'
import { unlockAudio } from './lib/roar'

gsap.registerPlugin(ScrollTrigger)

export default function App() {
  const [active, setActive] = useState(true)   // 3D canvas renders only while the dive is in view
  const [soundOn, setSoundOn] = useState(true)
  const lenis = useRef()

  useEffect(() => { 
    store.sound = soundOn 
    const params = new URLSearchParams(window.location.search)
    const d = params.get('dive')
    if (d !== null) {
      const val = parseFloat(d)
      store.target = val
      store.dive = val
    }
  }, [soundOn])

  useEffect(() => {
    const l = new Lenis({ lerp: 0.1, smoothWheel: true, syncTouch: false }) // responsive smooth scroll
    lenis.current = l
    l.stop()                                       // locked until the model has loaded
    l.on('scroll', ScrollTrigger.update)
    const raf = (t) => l.raf(t * 1000)
    gsap.ticker.add(raf); gsap.ticker.lagSmoothing(0)

    const dive = ScrollTrigger.create({
      trigger: '#dive', start: 'top top', end: 'bottom bottom',
      onUpdate: (s) => {
        store.target = s.progress
        const run = s.progress < 0.999
        setActive((a) => (a === run ? a : run))
        if (!run) store.dive = 1
      },
    })
    const after = ScrollTrigger.create({
      trigger: '#sanctum', start: 'top bottom', end: 'top 15%',
      onUpdate: (s) => { store.after = s.progress },
    })
    const unlock = () => unlockAudio()
    ;['pointerdown', 'keydown', 'touchend'].forEach((e) => window.addEventListener(e, unlock, { passive: true }))
    const onResize = () => ScrollTrigger.refresh()
    window.addEventListener('resize', onResize)
    return () => {
      dive.kill(); after.kill(); gsap.ticker.remove(raf); l.destroy()
      ;['pointerdown', 'keydown', 'touchend'].forEach((e) => window.removeEventListener(e, unlock))
      window.removeEventListener('resize', onResize)
    }
  }, [])

  const onLoaded = useCallback(() => { lenis.current?.start(); ScrollTrigger.refresh() }, [])

  return (
    <>
      <Loader onDone={onLoaded} />
      <div className="fixed inset-0 z-0 bg-obsidian"><DinoScene active={active} /></div>
      <Hud soundOn={soundOn} setSoundOn={setSoundOn} />
      {/* scroll track for the jaws dive (tight, cinematic, responsive) */}
      <div id="dive" className="relative h-[340svh] md:h-[380svh] pointer-events-none" aria-hidden />
      <Sanctum />
    </>
  )
}
