import Feast from './Feast'
import Platter from './Platter'
import Inauguration from './Inauguration'
import Zones from './Zones'
import Radar from './Radar'
import { PHONE_DISPLAY } from '../lib/menu'

export default function Sanctum() {
  return (
    <main id="sanctum" className="relative z-10 bg-obsidian grain">
      {/* molten lip where the sanctum emerges from the jaws */}
      <div className="absolute -top-px left-0 right-0 h-px bg-gradient-to-r from-transparent via-amber-molten to-transparent shadow-[0_-10px_80px_20px_rgba(255,122,0,.55)]" />
      <div className="absolute inset-x-0 top-0 h-72 bg-gradient-to-b from-[#2a0c02]/70 to-transparent pointer-events-none" />
      <div className="relative pt-20">
        <Feast />
        <Platter />
        <Inauguration />
        <Zones />
        <Radar />
        <footer className="px-6 py-14 text-center border-t border-amber-gold/10">
          <p className="font-royal tracking-[0.25em] text-white">HIYYA DINO MANDI</p>
          <p className="mt-3 font-mono text-[11px] tracking-[0.25em] text-gray-500">GUNTUR · {PHONE_DISPLAY}</p>
        </footer>
      </div>
    </main>
  )
}
