"""Save the last frame of a clip as a JPEG (Flow rejects some PNGs) (the start frame for the next chained clip).

    python tools/last_frame.py episodes/<name>/clips/c02.mp4 episodes/<name>/images/K2.jpg
    python tools/last_frame.py episodes/<name>/clips/c01.mp4 episodes/<name>/images/K0.jpg --first   (first frame, for the loop)

Uses the frame 0.05 s before the end (the very last decoded frame can be blank on some files)."""
import subprocess
import sys

src, dst = sys.argv[1], sys.argv[2]
if "--first" in sys.argv:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-frames:v", "1", "-q:v", "2", dst], check=True)
    print(f"saved {dst} (first frame)")
    sys.exit()
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src],
                           capture_output=True, text=True, check=True).stdout)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{max(dur - 0.05, 0):.3f}", "-i", src, "-frames:v", "1", "-q:v", "2", dst], check=True)
print(f"saved {dst} (from {dur - 0.05:.2f} s)")
