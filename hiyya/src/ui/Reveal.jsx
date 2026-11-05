import { motion } from 'framer-motion'

const ease = [0.16, 1, 0.3, 1]

/** Masked word-by-word headline reveal ("smooth staggered typography"). */
export function Words({ text, as = 'h2', className = '', delay = 0, step = 0.06 }) {
  const Tag = motion[as]
  return (
    <Tag className={className} aria-label={text}>
      {text.split(' ').map((w, i) => (
        <span key={i} className="inline-block overflow-hidden align-bottom pb-[0.12em] -mb-[0.12em]" aria-hidden>
          <motion.span className="inline-block"
            initial={{ y: '110%' }} whileInView={{ y: 0 }} viewport={{ once: true, margin: '-10% 0px' }}
            transition={{ duration: 0.9, ease, delay: delay + i * step }}>
            {w}&nbsp;
          </motion.span>
        </span>
      ))}
    </Tag>
  )
}

export function Fade({ children, delay = 0, y = 28, className = '' }) {
  return (
    <motion.div className={className} initial={{ opacity: 0, y }} whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-8% 0px' }} transition={{ duration: 0.9, ease, delay }}>
      {children}
    </motion.div>
  )
}

export function Eyebrow({ children }) {
  return <p className="font-mono text-[11px] tracking-[0.35em] uppercase text-amber-gold/80 mb-5">{children}</p>
}
