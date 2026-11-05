import os
import subprocess

video_path = 'ai_agents/data/instagram_assets/valixis_viral_speed_reel.mp4'
print("Exists:", os.path.exists(video_path), "Size:", os.path.getsize(video_path))

# Check with ffprobe if available, or just read headers
try:
    res = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration,size:stream=width,height,codec_name', '-of', 'json', video_path], capture_output=True, text=True)
    print("ffprobe output:", res.stdout)
except Exception as e:
    print("ffprobe error:", e)
