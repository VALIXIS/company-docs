import os
from PIL import Image

SRC_PATH = r"C:/Users/nagas/.gemini/antigravity/brain/3c4026c5-4a50-4416-958a-28a247ac3adc/.user_uploaded/media_1793731599872_de2213cd.png"

img = Image.open(SRC_PATH).convert("RGBA")
print("Loaded source logo for favicon/search icon:", img.size)

targets = ['assets', 'VALIXIS WEBSITE/assets']

for tdir in targets:
    os.makedirs(tdir, exist_ok=True)
    
    # 32x32
    f32 = img.resize((32, 32), Image.Resampling.LANCZOS)
    f32.save(os.path.join(tdir, "favicon-32x32.png"), "PNG")
    
    # 16x16
    f16 = img.resize((16, 16), Image.Resampling.LANCZOS)
    f16.save(os.path.join(tdir, "favicon-16x16.png"), "PNG")
    
    # 180x180 Apple touch icon
    f180 = img.resize((180, 180), Image.Resampling.LANCZOS)
    f180.save(os.path.join(tdir, "apple-touch-icon.png"), "PNG")
    
    # 192x192 Android chrome
    f192 = img.resize((192, 192), Image.Resampling.LANCZOS)
    f192.save(os.path.join(tdir, "android-chrome-192x192.png"), "PNG")
    
    # 512x512
    f512 = img.resize((512, 512), Image.Resampling.LANCZOS)
    f512.save(os.path.join(tdir, "android-chrome-512x512.png"), "PNG")
    
    # favicon.ico (holds 16x16, 32x32, 48x48)
    ico_path = os.path.join(tdir, "favicon.ico")
    f32.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    
    print(f"Generated tab & search icons in {tdir}")

# Also place favicon.ico in root and VALIXIS WEBSITE root for crawlers checking /favicon.ico directly
img.resize((32, 32), Image.Resampling.LANCZOS).save("favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
img.resize((32, 32), Image.Resampling.LANCZOS).save("VALIXIS WEBSITE/favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
print("Placed favicon.ico in site roots!")
