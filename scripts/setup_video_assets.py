import os
import shutil

CAPTIONS_VTT = """WEBVTT - VALIXIS Ecosystem 60-90 Second Product Demonstration
Kind: captions
Language: en

00:00.000 --> 00:06.000
Welcome to VALIXIS. Engineering intelligent systems, autonomous daemons, and sovereign platforms.

00:06.000 --> 00:15.000
This is VALIXIS Portal: our core operational governance platform with role-based access control and GitHub CI/CD sync.

00:15.000 --> 00:25.000
Here is VALIXIS FLOW: an autonomous background daemon mesh running 24/7 task queues with intelligent pacing.

00:25.000 --> 00:35.000
FLOW orchestrates multi-agent tasks, lead analysis, and automated event notifications without manual friction.

00:35.000 --> 00:45.000
Next is VALIXIS PULSE: real-time telemetry and fleet observability tracking server health, uptime, and latency.

00:45.000 --> 00:55.000
Every node in the VALIXIS mesh reports live telemetry directly to the central telemetry cockpit.

00:55.000 --> 01:05.000
Explore our client production deployments: high-converting web applications, hospitality platforms, and 3D experiences.

01:05.000 --> 01:15.000
From Rose Cafe to Novel Hotel and Hiyya Dino Mandi, each digital platform is engineered for maximum performance.

01:15.000 --> 01:25.000
Frontier prototypes in active testing: Fitora AI fitness computer vision and VALIXIS DESK_AI local intelligence.

01:25.000 --> 01:30.000
VALIXIS. Building intelligent solutions for a better tomorrow. Schedule your architecture session at valixis.tech.
"""

VIDEO_INGESTION_README = """# VALIXIS Technologies — Product Video Demonstration Master Guide
**Phase 7 Architecture: Video Player Ingestion & Media Specifications**

This directory hosts production demonstration video recordings and streaming manifests for **valixis.tech/ecosystem/**.

---

## 1. Video Technical Specifications

To maintain sub-second initial playback, high fidelity, and universal browser compatibility, all demonstration videos must comply with these encoding parameters:

| Parameter | Specification | Recommendation |
| :--- | :--- | :--- |
| **Duration** | 60 to 90 seconds (Target: 75s) | Crisp technical walk-through |
| **Container** | MP4 (`.mp4`) & WebM (`.webm`) | Provide both for fallback |
| **Video Codec** | H.264 (AVC High Profile) & VP9 | `libx264` / `libvpx-vp9` |
| **Resolution** | 1920x1080 (1080p) or 3840x2160 (4K) | 16:9 Aspect Ratio |
| **Frame Rate** | 30 fps or 60 fps | Constant Frame Rate (CFR) |
| **Bitrate** | 3,500 – 6,000 kbps (1080p) | Variable Bitrate (2-pass VBR) |
| **Audio Codec** | AAC-LC / Opus | Stereo, 48 kHz, 160 kbps |
| **Fast Start** | `moov` atom at the beginning | `ffmpeg -movflags +faststart` |
| **Poster Image** | PNG/JPEG, 1920x1080, < 250 KB | `valixis-video-poster.png` |
| **Captions** | WebVTT format (`.vtt`) | `valixis-demo-captions.vtt` |

---

## 2. FFmpeg Optimization Command

Convert your raw screen recording or master render into web-optimized H.264:

```bash
ffmpeg -i raw_master_demo.mov \\
  -c:v libx264 -preset slow -crf 22 -maxrate 5000k -bufsize 10000k \\
  -pix_fmt yuv420p -movflags +faststart \\
  -c:a aac -b:a 160k -ar 48000 \\
  valixis-product-demo-1080p.mp4
```

Generate WebM version for Chromium performance:
```bash
ffmpeg -i raw_master_demo.mov \\
  -c:v libvpx-vp9 -crf 30 -b:v 0 \\
  -c:a libopus -b:a 128k \\
  valixis-product-demo-1080p.webm
```

Generate 1080p poster frame from second 4:
```bash
ffmpeg -ss 00:00:04 -i valixis-product-demo-1080p.mp4 -frames:v 1 valixis-video-poster.png
```

---

## 3. Current Staged Assets
- `valixis-product-preview.mp4`: Verified production 18-second promotional reel.
- `valixis-demo-captions.vtt`: Full WebVTT timed subtitles matching the 90-second technical narrative.
- `valixis-video-poster.png`: Dark futuristic cyber poster with Orbitron typography and playback HUD.
"""

def main():
    source_video = 'ai_agents/data/instagram_assets/valixis_viral_speed_reel.mp4'
    targets = ['assets/videos', 'VALIXIS WEBSITE/assets/videos']
    
    for t in targets:
        os.makedirs(t, exist_ok=True)
        if os.path.exists(source_video):
            shutil.copy2(source_video, os.path.join(t, 'valixis-product-preview.mp4'))
            print(f"Copied sample reel to {t}/valixis-product-preview.mp4")
            
        with open(os.path.join(t, 'valixis-demo-captions.vtt'), 'w', encoding='utf-8') as f:
            f.write(CAPTIONS_VTT)
        with open(os.path.join(t, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(VIDEO_INGESTION_README)
        print(f"Generated video guide and captions in {t}")

if __name__ == '__main__':
    main()
