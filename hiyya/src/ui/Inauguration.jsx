import { useState } from 'react'
import { Words, Fade, Eyebrow } from './Reveal'

export default function Inauguration() {
  const [hasPhoto, setHasPhoto] = useState(true)
  return (
    <section id="spotlight" className="relative overflow-hidden px-5 md:px-12 py-28 md:py-40">
      <div className="absolute left-1/2 -translate-x-1/2 top-0 w-[140%] h-full pointer-events-none bg-[conic-gradient(from_180deg_at_50%_-10%,transparent_38%,rgba(253,230,138,.10)_46%,rgba(253,230,138,.16)_50%,rgba(253,230,138,.10)_54%,transparent_62%)]" />
      <div className="relative max-w-7xl mx-auto grid md:grid-cols-[1fr_1.1fr] gap-12 items-center">
        <Fade>
          <div className="relative mx-auto w-full max-w-[420px] aspect-[4/5] rounded-t-[999px] rounded-b-2xl overflow-hidden hairline bg-gradient-to-b from-amber-gold/15 to-black">
            {hasPhoto && <img src="/images/inauguration.jpg" alt="Bhagyashri Borse at the HIYYA DINO MANDI inauguration" onError={() => setHasPhoto(false)} className="absolute inset-0 w-full h-full object-cover" loading="lazy" />}
            {!hasPhoto && <div className="absolute inset-0 flex items-end justify-center pb-10 font-mono text-[10px] tracking-[0.3em] uppercase text-amber-gold/60 text-center px-6">Add your photo at<br />public/images/inauguration.jpg</div>}
          </div>
        </Fade>
        <div>
          <Eyebrow>Chapter III · Celebrity Inauguration Spotlight</Eyebrow>
          <Words text="Inaugurated by Bhagyashri Borse." className="font-royal text-4xl md:text-6xl leading-[1.05]" />
          <Fade delay={0.2}>
            <p className="mt-8 text-gray-400 max-w-md leading-relaxed">Guntur’s first dinosaur-themed Arabian Mandi house opened its jaws to the public, with actress Bhagyashri Borse as chief guest.</p>
            <p className="mt-10 font-royal text-5xl md:text-6xl gold-text tracking-wide">28 · 07 · 2026</p>
          </Fade>
        </div>
      </div>
    </section>
  )
}
