import { useMemo, useRef } from 'react'
import * as THREE from 'three'
import { useFrame } from '@react-three/fiber'
import { store } from '../lib/store'

const vert = /* glsl */ `
  uniform float uTime; uniform float uPx;
  attribute float aSeed; attribute float aSpeed;
  varying float vSeed; varying float vFade;
  void main(){
    vec3 p = position;
    p.y = mod(p.y + uTime * aSpeed, 10.0);
    p.x += sin(uTime * 0.4 + aSeed * 6.283) * 0.5;
    p.z += cos(uTime * 0.3 + aSeed * 9.0) * 0.5;
    vec4 mv = modelViewMatrix * vec4(p, 1.0);
    gl_Position = projectionMatrix * mv;
    gl_PointSize = (1.5 + aSeed * 2.5) * uPx * (2.8 / -mv.z);
    vSeed = aSeed; vFade = smoothstep(0.0, 1.5, p.y) * (1.0 - smoothstep(7.5, 10.0, p.y));
  }`
const frag = /* glsl */ `
  varying float vSeed; varying float vFade;
  void main(){
    float d = length(gl_PointCoord - 0.5);
    float a = smoothstep(0.5, 0.0, d);
    vec3 c = mix(vec3(1.0,0.78,0.25), vec3(1.0,0.38,0.05), vSeed);
    gl_FragColor = vec4(c, a * vFade * 0.9);
  }`

export default function Embers({ count = store.isMobile ? 220 : 520 }) {
  const mat = useRef()
  const geo = useMemo(() => {
    const g = new THREE.BufferGeometry()
    const pos = new Float32Array(count * 3), seed = new Float32Array(count), speed = new Float32Array(count)
    for (let i = 0; i < count; i++) {
      pos.set([(Math.random() - 0.5) * 26, Math.random() * 10, -6 + Math.random() * 22], i * 3)
      seed[i] = Math.random(); speed[i] = 0.15 + Math.random() * 0.4
    }
    g.setAttribute('position', new THREE.BufferAttribute(pos, 3))
    g.setAttribute('aSeed', new THREE.BufferAttribute(seed, 1))
    g.setAttribute('aSpeed', new THREE.BufferAttribute(speed, 1))
    return g
  }, [count])
  useFrame((s) => { mat.current.uniforms.uTime.value = s.clock.elapsedTime; mat.current.uniforms.uPx.value = s.gl.getPixelRatio() * 40 })
  return (
    <points geometry={geo} frustumCulled={false}>
      <shaderMaterial ref={mat} vertexShader={vert} fragmentShader={frag} transparent depthWrite={false}
        blending={THREE.AdditiveBlending} fog={false} uniforms={{ uTime: { value: 0 }, uPx: { value: 40 } }} />
    </points>
  )
}
