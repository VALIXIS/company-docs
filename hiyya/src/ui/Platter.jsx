import { useMemo, useState } from 'react'
import { AnimatePresence, motion, useSpring, useTransform } from 'framer-motion'
import { SIZES, PROTEINS, ADDONS, WHATSAPP } from '../lib/menu'
import { Words, Fade, Eyebrow } from './Reveal'

function Price({ value }) {
  const sp = useSpring(value, { stiffness: 140, damping: 22 })
  sp.set(value)
  const txt = useTransform(sp, (v) => '₹' + Math.round(v).toLocaleString('en-IN'))
  return <motion.span>{txt}</motion.span>
}

function piecePositions(n) {
  const out = [], outer = Math.min(n, 8), inner = n - outer
  for (let i = 0; i < outer; i++) { const a = (i / outer) * Math.PI * 2; out.push([Math.cos(a) * 98, Math.sin(a) * 98, a]) }
  for (let i = 0; i < inner; i++) { const a = (i / inner) * Math.PI * 2 + 0.4; out.push([Math.cos(a) * 48, Math.sin(a) * 48, a]) }
  return out
}

function PlatterArt({ size, protein }) {
  const grains = useMemo(() => Array.from({ length: 150 }, () => {
    const a = Math.random() * 6.283, r = Math.sqrt(Math.random()) * 138
    return [Math.cos(a) * r, Math.sin(a) * r, Math.random() * 180]
  }), [])
  const pieces = piecePositions(size.pieces)
  const meat = protein.id === 'mutton' ? ['#7a3b1c', '#3d1a0a'] : ['#c9792a', '#6b3412']
  return (
    <svg viewBox="-200 -200 400 400" className="w-full h-full drop-shadow-[0_30px_60px_rgba(255,122,0,.25)]">
      <defs>
        <radialGradient id="brass" cx="35%" cy="30%"><stop offset="0" stopColor="#fff0b8" /><stop offset=".45" stopColor="#d8a23a" /><stop offset="1" stopColor="#6b4413" /></radialGradient>
        <radialGradient id="well" cx="50%" cy="50%"><stop offset="0" stopColor="#3a2509" /><stop offset="1" stopColor="#8a5c1c" /></radialGradient>
        <radialGradient id="rice" cx="45%" cy="38%"><stop offset="0" stopColor="#fff2b5" /><stop offset=".6" stopColor="#f0c75a" /><stop offset="1" stopColor="#c98f2a" /></radialGradient>
        <radialGradient id="meat" cx="35%" cy="30%"><stop offset="0" stopColor={meat[0]} /><stop offset="1" stopColor={meat[1]} /></radialGradient>
      </defs>
      <circle r="196" fill="url(#brass)" />
      <circle r="184" fill="none" stroke="#3a2509" strokeOpacity=".5" strokeWidth="1.5" strokeDasharray="2 9" />
      <circle r="170" fill="url(#well)" />
      <circle r="150" fill="url(#rice)" />
      {grains.map(([x, y, r], i) => <ellipse key={i} cx={x} cy={y} rx="4" ry="1.3" transform={`rotate(${r} ${x} ${y})`} fill="#fff8d6" opacity=".55" />)}
      <AnimatePresence>
        {pieces.map(([x, y, a], i) => (
          <motion.g key={`${size.id}-${protein.id}-${i}`} initial={{ scale: 0, opacity: 0 }} animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0, opacity: 0 }} transition={{ delay: i * 0.04, type: 'spring', stiffness: 220, damping: 16 }}
            style={{ transformOrigin: `${x}px ${y}px` }}>
            <ellipse cx={x} cy={y} rx="30" ry="17" transform={`rotate(${(a * 180) / Math.PI + 90} ${x} ${y})`} fill="url(#meat)" stroke="#2a1306" strokeWidth="1.5" />
            <ellipse cx={x - 6} cy={y - 5} rx="11" ry="4" transform={`rotate(${(a * 180) / Math.PI + 90} ${x} ${y})`} fill="#fff" opacity=".18" />
          </motion.g>
        ))}
      </AnimatePresence>
      {[[-20, -20], [22, 12], [-6, 26], [30, -26]].map(([x, y], i) => <circle key={i} cx={x} cy={y} r="4" fill={i % 2 ? '#7a1f1f' : '#e9d9a6'} opacity=".9" />)}
    </svg>
  )
}

export default function Platter() {
  const [sizeId, setSizeId] = useState('duo')
  const [proteinId, setProteinId] = useState('chicken')
  const [cutId, setCutId] = useState('leg')
  const [addons, setAddons] = useState([])
  const size = SIZES.find((s) => s.id === sizeId)
  const protein = PROTEINS.find((p) => p.id === proteinId)
  const cut = protein.cuts.find((c) => c.id === cutId) || protein.cuts[0]
  const total = Math.round(size.base * protein.mult) + cut.add * (SIZES.indexOf(size) + 1) + ADDONS.filter((a) => addons.includes(a.id)).reduce((s, a) => s + a.price, 0)

  const pickProtein = (id) => { setProteinId(id); setCutId(PROTEINS.find((p) => p.id === id).cuts[0].id) }
  const toggle = (id) => setAddons((a) => (a.includes(id) ? a.filter((x) => x !== id) : [...a, id]))

  const msg = `Hi HIYYA DINO MANDI! 🦖 I'd like to order:\n• ${size.label} Mandi platter (${size.serves})\n• ${protein.label} · ${cut.label}${addons.length ? '\n• Add-ons: ' + ADDONS.filter((a) => addons.includes(a.id)).map((a) => a.label).join(', ') : ''}\nEstimated total: ₹${total.toLocaleString('en-IN')}`
  const wa = `https://wa.me/${WHATSAPP}?text=${encodeURIComponent(msg)}`

  const chip = (on) => `px-4 py-2.5 rounded-full text-sm border transition-all duration-300 ${on ? 'bg-amber-gold text-obsidian border-amber-gold font-semibold shadow-[0_0_24px_rgba(245,158,11,.45)]' : 'border-amber-gold/25 text-gray-300 hover:border-amber-gold/70'}`

  return (
    <section id="platter" className="relative px-5 md:px-12 py-28 md:py-40 max-w-7xl mx-auto">
      <Eyebrow>Chapter II · The Golden Dastarkhwan</Eyebrow>
      <Words text="Build your platter. Send it to the kitchen." className="font-royal text-4xl md:text-6xl leading-[1.05] max-w-4xl" />
      <div className="mt-16 grid lg:grid-cols-2 gap-10 lg:gap-16 items-center">
        <Fade>
          <div className="relative mx-auto w-full max-w-[520px] aspect-square flex items-center justify-center">
            <div className="absolute inset-[-10%] rounded-full bg-[radial-gradient(circle,rgba(255,122,0,.22),transparent_65%)]" />
            <motion.div className="w-full h-full" animate={{ scale: size.scale }} transition={{ type: 'spring', stiffness: 120, damping: 16 }}>
              <motion.div className="w-full h-full" animate={{ rotate: 360 }} transition={{ repeat: Infinity, duration: 90, ease: 'linear' }}>
                <PlatterArt size={size} protein={protein} />
              </motion.div>
            </motion.div>
          </div>
        </Fade>
        <Fade delay={0.1}>
          <div className="glass hairline rounded-2xl p-6 md:p-9 space-y-7">
            <div>
              <p className="font-mono text-[10px] tracking-[0.3em] uppercase text-gray-500 mb-3">Scale</p>
              <div className="flex flex-wrap gap-2">{SIZES.map((s) => <button key={s.id} onClick={() => setSizeId(s.id)} className={chip(s.id === sizeId)}>{s.label} <span className="opacity-60 text-xs">· {s.serves}</span></button>)}</div>
            </div>
            <div>
              <p className="font-mono text-[10px] tracking-[0.3em] uppercase text-gray-500 mb-3">Meat</p>
              <div className="flex flex-wrap gap-2">{PROTEINS.map((p) => <button key={p.id} onClick={() => pickProtein(p.id)} className={chip(p.id === proteinId)}>{p.label}</button>)}</div>
            </div>
            <div>
              <p className="font-mono text-[10px] tracking-[0.3em] uppercase text-gray-500 mb-3">Cut</p>
              <div className="flex flex-wrap gap-2">{protein.cuts.map((c) => <button key={c.id} onClick={() => setCutId(c.id)} className={chip(c.id === cut.id)}>{c.label}</button>)}</div>
            </div>
            <div>
              <p className="font-mono text-[10px] tracking-[0.3em] uppercase text-gray-500 mb-3">Add-ons</p>
              <div className="flex flex-wrap gap-2">{ADDONS.map((a) => <button key={a.id} onClick={() => toggle(a.id)} className={chip(addons.includes(a.id))}>{a.label} <span className="opacity-60 text-xs">+₹{a.price}</span></button>)}</div>
            </div>
            <div className="flex items-end justify-between pt-5 border-t border-amber-gold/15">
              <div>
                <p className="font-mono text-[10px] tracking-[0.3em] uppercase text-gray-500">Estimated total</p>
                <p className="font-royal text-4xl md:text-5xl gold-text mt-1"><Price value={total} /></p>
              </div>
              <a href={wa} target="_blank" rel="noopener noreferrer"
                className="rounded-full bg-gradient-to-r from-amber-gold to-amber-molten text-obsidian font-semibold px-6 py-3.5 text-sm md:text-base shadow-[0_0_40px_rgba(255,122,0,.4)] hover:scale-[1.04] active:scale-95 transition-transform">
                Dispatch to WhatsApp →
              </a>
            </div>
          </div>
        </Fade>
      </div>
    </section>
  )
}
