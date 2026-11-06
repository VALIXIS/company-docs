import { motion } from 'framer-motion'
import { FEAST } from '../lib/menu'
import { Words, Fade, Eyebrow } from './Reveal'

export default function Feast() {
  return (
    <section id="feast" className="relative px-5 md:px-12 py-28 md:py-40 max-w-7xl mx-auto">
      <Eyebrow>Chapter I · The Royal Feast Guild</Eyebrow>
      <Words text="Four reasons the pack keeps coming back." className="font-royal text-4xl md:text-6xl leading-[1.05] max-w-4xl" />
      <div className="mt-16 grid md:grid-cols-2 gap-5">
        {FEAST.map((f, i) => (
          <Fade key={f.name} delay={(i % 2) * 0.12}>
            <motion.article whileHover={{ y: -6 }} transition={{ type: 'spring', stiffness: 260, damping: 22 }}
              className="group relative overflow-hidden rounded-2xl hairline glass p-8 md:p-10 min-h-[260px] flex flex-col justify-between">
              <span className="absolute -right-4 -top-8 font-royal text-[10rem] leading-none text-amber-gold/[0.07] select-none">{f.n}</span>
              <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-700 bg-[radial-gradient(circle_at_80%_0%,rgba(255,122,0,.18),transparent_60%)]" />
              <span className="relative self-start font-mono text-[10px] tracking-[0.3em] uppercase px-3 py-1 rounded-full border border-amber-gold/40 text-amber-soft">{f.tag}</span>
              <div className="relative mt-10">
                <h3 className="font-serif text-2xl md:text-3xl text-white">{f.name}</h3>
                <p className="mt-3 text-sm md:text-base text-gray-400 max-w-md leading-relaxed">{f.blurb}</p>
              </div>
            </motion.article>
          </Fade>
        ))}
      </div>
    </section>
  )
}
