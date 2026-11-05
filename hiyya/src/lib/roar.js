// Synthesised T-Rex roar (no audio file needed). Web Audio only starts after a user gesture,
// so main App unlocks the context on first pointer/key/touch.
let ctx

export function unlockAudio() {
  if (!ctx) {
    const AC = window.AudioContext || window.webkitAudioContext
    if (!AC) return null
    ctx = new AC()
  }
  if (ctx.state === 'suspended') ctx.resume()
  return ctx
}

function makeDistortion(c, amount = 40) {
  const n = 2048, curve = new Float32Array(n)
  for (let i = 0; i < n; i++) {
    const x = (i * 2) / n - 1
    curve[i] = ((3 + amount) * x * 20 * (Math.PI / 180)) / (Math.PI + amount * Math.abs(x))
  }
  const s = c.createWaveShaper(); s.curve = curve; s.oversample = '2x'; return s
}

export function playRoar() {
  if (!ctx || ctx.state !== 'running') return
  const t0 = ctx.currentTime, dur = 3.6
  const master = ctx.createGain()
  master.gain.setValueAtTime(0, t0)
  master.gain.linearRampToValueAtTime(0.95, t0 + 0.3)
  master.gain.setValueAtTime(0.95, t0 + 1.8)
  master.gain.exponentialRampToValueAtTime(0.001, t0 + dur)

  // Warm, low-passed output to eliminate any harsh high-frequency chirping
  const lp = ctx.createBiquadFilter(); lp.type = 'lowpass'
  lp.frequency.setValueAtTime(450, t0)
  lp.frequency.linearRampToValueAtTime(750, t0 + 0.8)
  lp.frequency.exponentialRampToValueAtTime(160, t0 + dur)
  
  // Gentle soft saturation (warm tape style, amount 8 instead of harsh 60)
  const dist = makeDistortion(ctx, 10)

  // Guttural sub-bass predator foundation (rich low triangle & sawtooth waves)
  const growl = ctx.createGain(); growl.gain.value = 0.65
  const am = ctx.createOscillator(); am.frequency.value = 16  // Slow 16 Hz chest tremor
  const amDepth = ctx.createGain(); amDepth.gain.value = 0.35
  am.connect(amDepth); amDepth.connect(growl.gain)

  ;[1.0, 1.48].forEach((m, i) => {
    const o = ctx.createOscillator()
    o.type = i ? 'triangle' : 'sawtooth'
    o.frequency.setValueAtTime(68 * m, t0)
    o.frequency.exponentialRampToValueAtTime(32 * m, t0 + dur)
    const g = ctx.createGain()
    g.gain.value = i ? 0.35 : 0.5
    o.connect(g); g.connect(growl)
    o.start(t0); o.stop(t0 + dur)
  })
  am.start(t0); am.stop(t0 + dur)

  // Deep cavern breath (filtered resonant bandpass noise)
  const buf = ctx.createBuffer(1, ctx.sampleRate * dur, ctx.sampleRate)
  const d = buf.getChannelData(0)
  for (let i = 0; i < d.length; i++) d[i] = Math.random() * 2 - 1
  const noise = ctx.createBufferSource(); noise.buffer = buf
  const bp = ctx.createBiquadFilter(); bp.type = 'bandpass'; bp.Q.value = 1.4
  bp.frequency.setValueAtTime(300, t0)
  bp.frequency.linearRampToValueAtTime(580, t0 + 0.9)
  bp.frequency.exponentialRampToValueAtTime(140, t0 + dur)
  const ng = ctx.createGain(); ng.gain.value = 0.45
  noise.connect(bp); bp.connect(ng); ng.connect(dist)

  // Subwoofer pressure wave (deep 42 Hz -> 24 Hz sine rumble)
  const sub = ctx.createOscillator(); sub.type = 'sine'
  sub.frequency.setValueAtTime(46, t0)
  sub.frequency.exponentialRampToValueAtTime(22, t0 + dur)
  const sg = ctx.createGain(); sg.gain.value = 0.85
  sub.connect(sg); sg.connect(master)

  growl.connect(dist); dist.connect(lp); lp.connect(master); master.connect(ctx.destination)
  noise.start(t0); sub.start(t0); sub.stop(t0 + dur)
}
