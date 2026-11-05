import { useProgress } from '@react-three/drei'
import { useEffect, useState } from 'react'

export default function Loader({ onDone }) {
  const { progress, active } = useProgress()
  const [gone, setGone] = useState(false)
  useEffect(() => {
    const done = () => { setGone(true); onDone?.() }
    if (progress >= 100 && !active) { const t = setTimeout(done, 450); return () => clearTimeout(t) }
    const fail = setTimeout(done, 15000) // never trap the visitor if the model is slow or missing
    return () => clearTimeout(fail)
  }, [progress, active, onDone])
  return (
    <div className={`fixed inset-0 z-[60] bg-obsidian flex flex-col items-center justify-center transition-opacity duration-1000 ${gone ? 'opacity-0 pointer-events-none' : 'opacity-100'}`}>
      <div className="flex gap-8">
        {[0, 1].map((i) => <span key={i} className="block w-6 h-3 rounded-[50%] bg-amber-gold shadow-[0_0_30px_10px_rgba(255,122,0,.6)] animate-pulse" style={{ animationDelay: `${i * 0.2}s` }} />)}
      </div>
      <p className="mt-10 font-royal tracking-[0.3em] text-sm text-white">HIYYA DINO MANDI</p>
      <p className="mt-3 font-mono text-[10px] tracking-[0.3em] text-amber-gold/70">WAKING THE BEAST · {Math.round(progress)}%</p>
    </div>
  )
}
