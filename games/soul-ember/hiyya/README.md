# HIYYA DINO MANDI – 3D scrollytelling site

```bash
npm install
npm run dev        # http://localhost:5173
npm run build      # production build in /dist
```

## Model
`public/models/t-rex.glb` is already your T-Rex, converted + compressed (28 MB -> 3.2 MB):
spec-gloss -> metal-rough (modern three.js can't read the old extension), WebP textures, meshopt.
All 5 clips kept (idle, roar, bite, run, attack_tail).

## Where to tune
* `src/lib/cameraPath.js` -> `REST` : the Bezier points + look-at (metres). If the camera misses the mouth, only change these.
* `src/scene/Dino.jsx` -> `ROAR_START / ROAR_END` : which part of the roar clip scroll scrubs (jaw is fully open at 3.0 s).
* `src/lib/menu.js` -> prices (PLACEHOLDERS), cuts, zone copy, WhatsApp number.
* `src/App.jsx` -> `#dive` height (520svh / 560svh) = how long the dive takes to scroll.
* Optional photo: `public/images/inauguration.jpg`.

## Structure
```
src/
  App.jsx            Lenis + GSAP ScrollTrigger -> store.target (dive 0..1)
  lib/cameraPath.js  cubic Bezier camera + look-at maths
  lib/roar.js        Web Audio synthesized roar
  lib/store.js       shared mutable scroll state (no re-renders)
  scene/             DinoScene, CameraRig, Dino, Embers, Cavern
  ui/                Hud (hero text, captions, vortex), Feast, Platter, Inauguration, Zones, Radar
```
