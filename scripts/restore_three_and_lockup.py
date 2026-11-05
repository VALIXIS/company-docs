import os
import glob

# 1. Update index.html and valixis_company_homepage.html
three_files = [
    'index.html',
    'VALIXIS WEBSITE/index.html',
    'valixis_company_homepage.html',
    'VALIXIS WEBSITE/valixis_company_homepage.html'
]

for fpath in three_files:
    if not os.path.exists(fpath): continue
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Restore Material with alphaTest: 0.05 and PlaneGeometry(5.2, 4.35)
    text = text.replace(
'''        const vMatFront = new THREE.MeshBasicMaterial({
          map: texture,
          transparent: true,
          blending: THREE.AdditiveBlending,
          side: THREE.FrontSide,
          depthWrite: false
        });
        const vGeo = new THREE.PlaneGeometry(5.0, 5.0);''',
'''        const vMatFront = new THREE.MeshBasicMaterial({
          map: texture,
          transparent: true,
          alphaTest: 0.05,
          side: THREE.FrontSide,
          depthWrite: false
        });
        const vGeo = new THREE.PlaneGeometry(5.2, 4.35);'''
    )

    text = text.replace(
'''        const vMatBack = new THREE.MeshBasicMaterial({
          map: texture,
          transparent: true,
          blending: THREE.AdditiveBlending,
          side: THREE.FrontSide,
          depthWrite: false
        });''',
'''        const vMatBack = new THREE.MeshBasicMaterial({
          map: texture,
          transparent: true,
          alphaTest: 0.05,
          side: THREE.FrontSide,
          depthWrite: false
        });'''
    )

    # Bump texture cache-buster to ?v=7 so clients fetch the restored original transparent asset
    text = text.replace('valixis-logo-transparent.png?v=6', 'valixis-logo-transparent.png?v=7')
    text = text.replace('valixis-logo-transparent.png?v=5', 'valixis-logo-transparent.png?v=7')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Restored Three.js material & geometry in {fpath}")

# 2. Update cache-buster for valixis-horizontal-lockup.png from ?v=4 to ?v=5 across all HTML files
count = 0
for f in glob.glob('./**/*.html', recursive=True):
    if '.git' in f or 'node_modules' in f or 'scratch' in f:
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if 'valixis-horizontal-lockup.png?v=4' in c:
        c = c.replace('valixis-horizontal-lockup.png?v=4', 'valixis-horizontal-lockup.png?v=5')
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        count += 1

print(f"Updated lockup cache buster to ?v=5 in {count} HTML files!")
