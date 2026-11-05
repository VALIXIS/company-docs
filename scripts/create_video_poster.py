import os
from PIL import Image, ImageDraw, ImageFont

def create_video_poster(filepath):
    width, height = 1920, 1080
    im = Image.new('RGB', (width, height), color='#06090E')
    draw = ImageDraw.Draw(im)

    # 1. Subtle Radial / Gradient Glows
    for r in range(450, 0, -15):
        alpha = int(25 * (1 - r / 450))
        # Cyan center glow
        draw.ellipse([width//2 - r, height//2 - r, width//2 + r, height//2 + r], fill=(0, int(217 * (1 - r/450)), int(255 * (1 - r/450))))
    
    # Overlay dark tinted rectangle
    overlay = Image.new('RGBA', (width, height), (6, 9, 14, 210))
    im = Image.alpha_composite(im.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(im)

    # 2. Cyber Grid lines
    for x in range(0, width, 120):
        draw.line([(x, 0), (x, height)], fill=(20, 28, 42), width=1)
    for y in range(0, height, 90):
        draw.line([(0, y), (width, y)], fill=(20, 28, 42), width=1)

    # 3. Corner Bracket Accents
    pad = 80
    b_len = 50
    b_col = (0, 217, 255)
    # Top-Left
    draw.line([(pad, pad), (pad + b_len, pad)], fill=b_col, width=3)
    draw.line([(pad, pad), (pad, pad + b_len)], fill=b_col, width=3)
    # Top-Right
    draw.line([(width - pad, pad), (width - pad - b_len, pad)], fill=b_col, width=3)
    draw.line([(width - pad, pad), (width - pad, pad + b_len)], fill=b_col, width=3)
    # Bottom-Left
    draw.line([(pad, height - pad), (pad + b_len, height - pad)], fill=b_col, width=3)
    draw.line([(pad, height - pad), (pad, height - pad - b_len)], fill=b_col, width=3)
    # Bottom-Right
    draw.line([(width - pad, height - pad), (width - pad - b_len, height - pad)], fill=b_col, width=3)
    draw.line([(width - pad, height - pad), (width - pad, height - pad - b_len)], fill=b_col, width=3)

    # 4. HUD Telemetry Texts
    draw.text((pad + 20, pad + 15), "VALIXIS SYSTEM ARCHITECTURE // ECOSYSTEM_v2.0", fill=(0, 217, 255))
    draw.text((width - pad - 320, pad + 15), "TELEMETRY: STABLE • 60 FPS • 4K UHD", fill=(148, 163, 184))
    draw.text((pad + 20, height - pad - 35), "AUTONOMOUS DAEMONS • MESH ORCHESTRATION", fill=(148, 163, 184))
    draw.text((width - pad - 260, height - pad - 35), "VALIXIS.TECH / ECOSYSTEM", fill=(0, 217, 255))

    # 5. Play HUD Circle in Center
    cx, cy = width // 2, height // 2
    r_play = 70
    draw.ellipse([cx - r_play, cy - r_play, cx + r_play, cy + r_play], fill=(13, 17, 23), outline=(0, 217, 255), width=3)
    draw.ellipse([cx - r_play - 15, cy - r_play - 15, cx + r_play + 15, cy + r_play + 15], outline=(0, 217, 255, 100), width=1)
    
    # Play Triangle
    tri_pts = [(cx - 15, cy - 25), (cx + 25, cy), (cx - 15, cy + 25)]
    draw.polygon(tri_pts, fill=(0, 217, 255))

    # 6. Title and Subtitle Below Play Button
    draw.text((width // 2 - 240, cy + 110), "VALIXIS ECOSYSTEM DEMONSTRATION", fill=(255, 255, 255))
    draw.text((width // 2 - 200, cy + 145), "CLICK TO WATCH TECHNICAL WALKTHROUGH", fill=(0, 217, 255))
    draw.text((width // 2 - 160, cy + 180), "PORTAL • FLOW • CLOUD • DESK_AI • PULSE", fill=(148, 163, 184))

    im.save(filepath, "PNG", optimize=True)
    print(f"Generated video poster: {filepath} ({os.path.getsize(filepath)} bytes)")

for p in ['assets/videos/valixis-video-poster.png', 'VALIXIS WEBSITE/assets/videos/valixis-video-poster.png']:
    create_video_poster(p)
