import { useEffect, useState } from 'react'
import { COORDS, MAPS_URL, PHONE_DISPLAY, WHATSAPP } from '../lib/menu'
import { Words, Fade, Eyebrow } from './Reveal'

// Typical crowd pattern per hour (12:00–23:00). This is a pattern, NOT a live sensor.
const PATTERN = [0.35, 0.4, 0.25, 0.2, 0.25, 0.45, 0.8, 0.95, 1, 0.95, 0.7, 0.2]
const RUSH = [18 * 60, 22 * 60 + 30]

function istMinutes() {
  const [h, m] = new Date().toLocaleTimeString('en-GB', { timeZone: 'Asia/Kolkata', hour: '2-digit', minute: '2-digit', hour12: false }).split(':').map(Number)
  return h * 60 + m
}

export default function Radar() {
  const [now, setNow] = useState(istMinutes())
  useEffect(() => { const id = setInterval(() => setNow(istMinutes()), 30000); return () => clearInterval(id) }, [])
  const inRush = now >= RUSH[0] && now <= RUSH[1]
  const building = now >= 17 * 60 && now < RUSH[0]
  const level = inRush ? { t: 'Peak rush', c: '#FF7A00', b: 9, tip: 'Expect a wait. Message us on WhatsApp to hold a cabana.' }
    : building ? { t: 'Filling up', c: '#F59E0B', b: 5, tip: 'Perfect time to arrive before the rush.' }
    : { t: 'Calm', c: '#10B981', b: 2, tip: 'Tables are easy right now.' }
  const hr = Math.floor(now / 60)
  const blips = [[30, 40], [62, 28], [70, 62], [38, 70], [52, 52], [24, 58], [78, 44], [46, 24], [60, 78]]

  return (
    <section id="visit" className="relative px-5 md:px-12 py-28 md:py-40 max-w-7xl mx-auto">
      <Eyebrow>Chapter V · Live Queue Radar & Location Concierge</Eyebrow>
      <Words text="Time your arrival. Find the lair." className="font-royal text-4xl md:text-6xl leading-[1.05] max-w-4xl" />
      <div className="mt-16 grid lg:grid-cols-2 gap-6">
        <Fade>
          <div className="glass hairline rounded-2xl p-7 md:p-9 h-full">
            <div className="flex flex-col sm:flex-row gap-8 items-center">
              <div className="relative w-52 h-52 shrink-0 rounded-full border border-amber-gold/30 overflow-hidden bg-black/40">
                {[25, 50, 75].map((s) => <div key={s} className="absolute rounded-full border border-amber-gold/15" style={{ inset: `${(100 - s) / 2}%` }} />)}
                <div className="absolute inset-0 animate-[sweep_4s_linear_infinite] bg-[conic-gradient(from_0deg,rgba(245,158,11,0)_0deg,rgba(245,158,11,.45)_70deg,transparent_71deg)]" />
                {blips.slice(0, level.b).map(([x, y], i) => <span key={i} className="absolute w-2 h-2 rounded-full animate-[blip_2.4s_ease-in-out_infinite]" style={{ left: `${x}%`, top: `${y}%`, background: level.c, boxShadow: `0 0 10px ${level.c}`, animationDelay: `${i * 0.3}s` }} />)}
              </div>
              <div>
                <p className="font-mono text-[10px] tracking-[0.3em] uppercase text-gray-500">Right now (IST)</p>
                <p className="font-royal text-3xl mt-1" style={{ color: level.c }}>{level.t}</p>
                <p className="text-sm text-gray-400 mt-2 max-w-xs">{level.tip}</p>
                <p className="mt-4 font-mono text-[11px] text-amber-soft/80">Rush hour · 6:00 PM – 10:30 PM</p>
              </div>
            </div>
            <div className="mt-8 flex items-end gap-1.5 h-24">
              {PATTERN.map((v, i) => { const h = 12 + i; const cur = h === hr; return (
                <div key={h} className="flex-1 flex flex-col items-center gap-1">
                  <div className="w-full rounded-t-sm transition-all" style={{ height: `${v * 100}%`, background: cur ? '#FDE68A' : h >= 18 && h <= 22 ? 'rgba(255,122,0,.75)' : 'rgba(245,158,11,.28)' }} />
                  <span className="font-mono text-[9px] text-gray-500">{h > 12 ? h - 12 : h}{h >= 12 ? 'p' : 'a'}</span>
                </div>) })}
            </div>
            <p className="mt-4 text-[11px] text-gray-500">Typical crowd pattern based on opening hours, not a live occupancy sensor.</p>
          </div>
        </Fade>
        <Fade delay={0.12}>
          <div className="glass hairline rounded-2xl overflow-hidden h-full flex flex-col">
            <iframe title="HIYYA DINO MANDI location" loading="lazy" className="w-full h-56 md:h-64 border-0 [filter:invert(.9)_hue-rotate(180deg)_saturate(.6)_brightness(.9)]"
              src="https://maps.google.com/maps?q=Hiyya+Dino+Mandi+Brindavan+Gardens+Guntur&t=&z=16&ie=UTF8&iwloc=&output=embed" />
            <div className="p-7 md:p-9 flex-1 flex flex-col">
              <p className="font-serif text-xl text-white">Above Ratnadeep Super Market</p>
              <p className="text-gray-400 mt-1 text-sm">Kundula Road, Beside Ayyappa Swamy Temple, Brindavan Gardens, Guntur, Andhra Pradesh 522006</p>
              <p className="font-mono text-[11px] text-amber-gold/80 mt-3">{COORDS.lat}° N, {COORDS.lng}° E · Brundavan Gardens</p>
              <div className="mt-auto pt-7 flex flex-wrap gap-3">
                <a href={MAPS_URL} target="_blank" rel="noopener noreferrer" className="rounded-full bg-gradient-to-r from-amber-gold to-amber-molten text-obsidian font-semibold px-6 py-3 text-sm">Get directions</a>
                <a href={`https://wa.me/${WHATSAPP}?text=${encodeURIComponent('Hi HIYYA DINO MANDI! I would like to reserve a table.')}`} target="_blank" rel="noopener noreferrer" className="rounded-full border border-amber-gold/50 text-amber-soft px-6 py-3 text-sm hover:bg-amber-gold/10">Reserve on WhatsApp</a>
                <a href={`tel:+${WHATSAPP}`} className="rounded-full border border-white/15 text-gray-300 px-6 py-3 text-sm hover:bg-white/5">{PHONE_DISPLAY}</a>
              </div>
            </div>
          </div>
        </Fade>
      </div>
    </section>
  )
}
