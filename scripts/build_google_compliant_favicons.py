import os
from PIL import Image, ImageFilter

SRC_PATH = r"C:/Users/nagas/.gemini/antigravity/brain/3c4026c5-4a50-4416-958a-28a247ac3adc/.user_uploaded/media_1793731599872_de2213cd.png"

img = Image.open(SRC_PATH).convert("RGBA")
print("Source image loaded:", img.size)

sizes = {
    "favicon-16x16.png": 16,
    "favicon-32x32.png": 32,
    "favicon-48x48.png": 48,
    "favicon-96x96.png": 96,
    "favicon-144x144.png": 144,
    "apple-touch-icon.png": 180,
    "android-chrome-192x192.png": 192,
    "android-chrome-512x512.png": 512,
}

target_dirs = ["assets", "VALIXIS WEBSITE/assets"]

for tdir in target_dirs:
    os.makedirs(tdir, exist_ok=True)
    for fname, dim in sizes.items():
        resized = img.resize((dim, dim), Image.Resampling.LANCZOS)
        # Apply gentle unsharp mask on small icons for razor sharpness
        if dim <= 48:
            resized = resized.filter(ImageFilter.UnsharpMask(radius=0.8, percent=120, threshold=2))
        out_path = os.path.join(tdir, fname)
        resized.save(out_path, "PNG", optimize=True)
        print(f"Saved: {out_path} ({dim}x{dim})")

# Generate favicon.ico (multi-size 16, 32, 48, 64)
ico_sizes = [16, 32, 48, 64]
ico_images = [img.resize((s, s), Image.Resampling.LANCZOS) for s in ico_sizes]

for ico_dst in ["favicon.ico", "assets/favicon.ico", "VALIXIS WEBSITE/favicon.ico", "VALIXIS WEBSITE/assets/favicon.ico"]:
    os.makedirs(os.path.dirname(ico_dst) if os.path.dirname(ico_dst) else ".", exist_ok=True)
    ico_images[1].save(ico_dst, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print(f"Saved multi-resolution ICO: {ico_dst}")

# Also copy 48x48, 32x32, 16x16, apple-touch-icon to site roots
for root_dst in [".", "VALIXIS WEBSITE"]:
    img.resize((48, 48), Image.Resampling.LANCZOS).save(os.path.join(root_dst, "favicon-48x48.png"), "PNG")
    img.resize((32, 32), Image.Resampling.LANCZOS).save(os.path.join(root_dst, "favicon-32x32.png"), "PNG")
    img.resize((16, 16), Image.Resampling.LANCZOS).save(os.path.join(root_dst, "favicon-16x16.png"), "PNG")
    img.resize((180, 180), Image.Resampling.LANCZOS).save(os.path.join(root_dst, "apple-touch-icon.png"), "PNG")
    print(f"Saved root fallbacks in {root_dst}")

print("All Google-compliant favicon sizes generated successfully!")
