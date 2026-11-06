// ⚠️  PRICES BELOW ARE PLACEHOLDERS — replace with the restaurant's real menu prices.
export const SIZES = [
  { id: 'single', label: 'Single', serves: '1 guest', base: 249, pieces: 3, scale: 0.72 },
  { id: 'duo',    label: 'Duo',    serves: '2 guests', base: 449, pieces: 5, scale: 0.84 },
  { id: 'quad',   label: 'Quad',   serves: '4 guests', base: 849, pieces: 8, scale: 0.95 },
  { id: 'mega',   label: 'Mega',   serves: '6 guests', base: 1299, pieces: 12, scale: 1.06 },
]
export const PROTEINS = [
  { id: 'chicken', label: 'Chicken Juicy', mult: 1, cuts: [
    { id: 'leg', label: 'Leg Quarter', add: 0 },
    { id: 'breast', label: 'Breast', add: 20 },
    { id: 'mixed', label: 'Mixed Cuts', add: 10 } ] },
  { id: 'mutton', label: 'Gongura Mutton', mult: 1.55, cuts: [
    { id: 'ribs', label: 'Ribs', add: 40 },
    { id: 'leg', label: 'Leg', add: 60 },
    { id: 'shoulder', label: 'Shoulder', add: 30 } ] },
]
export const ADDONS = [
  { id: 'chekkalu', label: 'Chicken Chekkalu starter', price: 149 },
  { id: 'raita', label: 'Cooling raita & salsa', price: 39 },
]
export const WHATSAPP = '919920986666'
export const PHONE_DISPLAY = '+91 99209 86666'
export const COORDS = { lat: 16.3132, lng: 80.4208 }
export const MAPS_URL = 'https://www.google.com/maps/search/?api=1&query=Hiyya+Dino+Mandi+Brindavan+Gardens+Guntur'

export const FEAST = [
  { name: 'Chicken Juicy Mandi', tag: "Guntur's #1 Rated", blurb: 'Slow-smoked until it surrenders from the bone, over saffron-gold basmati.', n: '01' },
  { name: 'Gongura Mutton Mandi', tag: 'Andhra x Arabia', blurb: 'Tangy gongura meets tender mutton in a Guntur-bold twist on the classic.', n: '02' },
  { name: '6-Pax Dino Monster Mega Platter', tag: 'Serves 6', blurb: 'A roaring tray built for the whole pack. Bring your biggest appetite.', n: '03' },
  { name: 'Chicken Chekkalu', tag: 'Starter', blurb: 'Crisp, golden, fiercely addictive. The perfect opening act.', n: '04' },
]
export const ZONES = [
  { name: 'Prehistoric Cave Cabanas', blurb: 'Private rock-hewn nooks lit by amber glow, made for family dinners.', hue: 'from-emerald-900/60 to-black' },
  { name: 'Apex T-Rex Arena', blurb: 'The main hall, where the king of the Cretaceous watches you eat.', hue: 'from-amber-800/50 to-black' },
  { name: 'Birthday Party Zones', blurb: 'Roar-worthy celebrations with themed seating and a feast to match.', hue: 'from-red-900/50 to-black' },
]
