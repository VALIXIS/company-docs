import os
from PIL import Image, ImageDraw, ImageFont

def create_monogram_badge(initials, stroke_color, glow_color, output_path):
    size = (600, 600)
    img = Image.new("RGB", size, "#06090E")
    draw = ImageDraw.Draw(img)
    
    # Outer subtle glow rings
    center = (300, 300)
    for r in range(260, 200, -8):
        alpha_val = int(25 * ((r - 200) / 60.0))
        draw.ellipse([300 - r, 300 - r, 300 + r, 300 + r], outline=glow_color, width=2)
    
    # Inner dark disc
    draw.ellipse([300 - 210, 300 - 210, 300 + 210, 300 + 210], fill="#0A0E14", outline=stroke_color, width=6)
    
    # Initials Text
    # Try finding system font or draw cleanly
    font = None
    font_paths = [
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/seguisb.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/calibrib.ttf"
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                font = ImageFont.truetype(fp, 180)
                break
            except Exception:
                pass
    if font is None:
        font = ImageFont.load_default()
        
    bbox = draw.textbbox((0, 0), initials, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    text_x = 300 - (text_w / 2) - bbox[0]
    text_y = 300 - (text_h / 2) - bbox[1]
    
    draw.text((text_x, text_y), initials, fill=stroke_color, font=font)
    
    # Subtle brand mark dot
    draw.ellipse([290, 440, 310, 460], fill=stroke_color)
    
    img.save(output_path, "JPEG", quality=95)
    print(f"Created monogram badge: {output_path}")

# Generate for Subhash Annam (Electric Cyan #00D9FF)
create_monogram_badge("SA", "#00D9FF", "#005577", "assets/subhash-annam.jpg")
create_monogram_badge("SA", "#00D9FF", "#005577", "VALIXIS WEBSITE/assets/subhash-annam.jpg")

# Generate for Jyothsna Sri (Vibrant Magenta #FF2ED6)
create_monogram_badge("JS", "#FF2ED6", "#770055", "assets/jyothsna-sri.jpg")
create_monogram_badge("JS", "#FF2ED6", "#770055", "VALIXIS WEBSITE/assets/jyothsna-sri.jpg")

print("All avatar badges generated successfully!")
