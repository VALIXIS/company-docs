import os
import shutil
from PIL import Image

SRC_PATH = r"C:/Users/nagas/.gemini/antigravity/brain/3c4026c5-4a50-4416-958a-28a247ac3adc/.user_uploaded/media_1793731599872_de2213cd.png"
ASSETS_DIR = "assets"
MIRROR_ASSETS_DIR = os.path.join("VALIXIS WEBSITE", "assets")

img = Image.open(SRC_PATH)
print("Source image loaded:", img.size, img.mode)

# Ensure RGBA and RGB
img_rgba = img.convert("RGBA")
img_rgb = img.convert("RGB")

targets = [ASSETS_DIR, MIRROR_ASSETS_DIR]

for tdir in targets:
    os.makedirs(tdir, exist_ok=True)
    
    # 1. valixis-logo-transparent.png (Save uploaded PNG directly)
    dst_trans = os.path.join(tdir, "valixis-logo-transparent.png")
    img_rgba.save(dst_trans, "PNG", optimize=True)
    print("Saved:", dst_trans)
    
    # 2. valixis-logo-full.jpg (Save uploaded JPEG with high quality)
    dst_full = os.path.join(tdir, "valixis-logo-full.jpg")
    img_rgb.save(dst_full, "JPEG", quality=95, optimize=True)
    print("Saved:", dst_full)
    
    # 3. Favicons
    img_rgba.resize((180, 180), Image.Resampling.LANCZOS).save(os.path.join(tdir, "apple-touch-icon.png"), "PNG")
    img_rgba.resize((192, 192), Image.Resampling.LANCZOS).save(os.path.join(tdir, "android-chrome-192x192.png"), "PNG")
    img_rgba.resize((32, 32), Image.Resampling.LANCZOS).save(os.path.join(tdir, "favicon-32x32.png"), "PNG")
    img_rgba.resize((16, 16), Image.Resampling.LANCZOS).save(os.path.join(tdir, "favicon-16x16.png"), "PNG")
    print("Generated favicons in:", tdir)

print("All asset targets updated successfully!")
