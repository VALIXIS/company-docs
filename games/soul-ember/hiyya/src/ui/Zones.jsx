import { motion } from 'framer-motion'
import { ZONES } from '../lib/menu'
import { Words, Fade, Eyebrow } from './Reveal'

export default function Zones() {
  return (
    <section id="zones" className="relative px-5 md:px-12 py-28 md:py-40 max-w-7xl mx-auto">
      <Eyebrow>Chapter IV · The Themed Zones</Eyebrow>
      <Words text="Choose your corner of the Cretaceous." className="font-royal text-4xl md:text-6xl leading-[1.05] max-w-4xl" />
      <div className="mt-16 grid md:grid-cols-3 gap-5">
        {ZONES.map((z, i) => (
          <Fade key={z.name} delay={i * 0.12}>
            <motion.div whileHover={{ y: -8 }} transition={{ type: 'spring', stiffness: 240, damping: 20 }}
              className={`relative h-[360px] rounded-2xl overflow-hidden hairline bg-gradient-to-b ${z.hue} p-8 flex flex-col justify-end`}>
              <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_0%,rgba(245,158,11,.25),transparent_60%)]" />
              <span className="absolute top-6 left-8 font-mono text-[10px] tracking-[0.3em] text-amber-gold/70">ZONE 0{i + 1}</span>
              <h3 className="relative font-serif text-2xl text-white">{z.name}</h3>
              <p className="relative mt-3 text-sm text-gray-300/80 leading-relaxed">{z.blurb}</p>
            </motion.div>
          </Fade>
        ))}
      </div>
    </section>
  )
}
