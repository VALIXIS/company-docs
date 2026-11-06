/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        obsidian: '#060907',
        cavern: '#09120C',
        amber: { molten: '#FF7A00', gold: '#F59E0B', soft: '#FDE68A' },
        biolum: '#10B981',
      },
      fontFamily: {
        display: ['Syne', 'sans-serif'],
        royal: ['"Cinzel Decorative"', 'Cinzel', 'serif'],
        serif: ['Cinzel', 'serif'],
        sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
        mono: ['"Space Mono"', 'monospace'],
      },
    },
  },
  plugins: [],
}
