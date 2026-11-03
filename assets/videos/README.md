# VALIXIS Technologies — Product Video Demonstration Master Guide
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
ffmpeg -i raw_master_demo.mov \
  -c:v libx264 -preset slow -crf 22 -maxrate 5000k -bufsize 10000k \
  -pix_fmt yuv420p -movflags +faststart \
  -c:a aac -b:a 160k -ar 48000 \
  valixis-product-demo-1080p.mp4
```

Generate WebM version for Chromium performance:
```bash
ffmpeg -i raw_master_demo.mov \
  -c:v libvpx-vp9 -crf 30 -b:v 0 \
  -c:a libopus -b:a 128k \
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
