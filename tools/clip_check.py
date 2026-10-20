"""Check one generated Flow clip before moving on to the next (owner rule: generate, check, fix, then continue).

  python tools/clip_check.py episodes\\db-cooper\\clips\\s02.mp4 3.1 [--start 0]

Writes <clip>_check.jpg next to the clip: frames every 0.5 s across the part the scene uses (plus the final frame,
for the transition into the next clip), each stamped with its time. Prints length, size, brightness, dark pixels
and whether the clip has sound. Look at the sheet: right subject and action, same cartoon style and character look,
no text, no warped hands/faces, smooth motion.
"""
import argparse
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analyse_reference import duration, ff  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clip")
    ap.add_argument("seconds", type=float, help="how long the scene shows this clip")
    ap.add_argument("--start", type=float, default=0.0, help="clip_start, if the scene starts later in the clip")
    a = ap.parse_args()
    clip = Path(a.clip)
    total = duration(clip)
    times = list(np.arange(a.start, min(a.start + a.seconds, total) - 0.05, 0.5)) + [min(a.start + a.seconds, total) - 0.05]
    times.append(max(total - 0.1, 0))
    out = clip.with_name(clip.stem + "_check.jpg")
    tiles = []
    tmp = clip.with_name(clip.stem + "_check_tmp")
    tmp.mkdir(exist_ok=True)
    font = "C\\:/Windows/Fonts/arialbd.ttf" if sys.platform == "win32" else "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    for i, t in enumerate(times):
        f = tmp / f"{i:02d}.png"
        label = f"{t:.1f}s" + (" END" if i == len(times) - 1 else "")
        subprocess.run([ff("ffmpeg"), "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(clip), "-frames:v", "1", "-vf",
                        f"scale=270:-2,drawtext=fontfile='{font}':text='{label}':x=8:y=8:fontsize=24:fontcolor=yellow:"
                        "box=1:boxcolor=black@0.6", str(f)], check=True)
        tiles.append(f)
    cols = min(len(tiles), 6)
    rows = (len(tiles) + cols - 1) // cols
    inputs = sum((["-i", str(f)] for f in tiles), [])
    layout = "|".join(f"{'0' if i % cols == 0 else '+'.join(['w0'] * (i % cols))}_{'0' if i // cols == 0 else '+'.join(['h0'] * (i // cols))}"
                      for i in range(len(tiles)))
    subprocess.run([ff("ffmpeg"), "-v", "error", "-y", *inputs, "-filter_complex",
                    f"xstack=inputs={len(tiles)}:layout={layout}:fill=black", "-frames:v", "1", str(out)], check=True)
    for f in tiles:
        f.unlink()
    tmp.rmdir()
    raw = subprocess.run([ff("ffmpeg"), "-v", "error", "-ss", str(a.start), "-t", str(a.seconds), "-i", str(clip), "-vf",
                          "fps=4,scale=90:160", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    px = np.frombuffer(raw, np.uint8).reshape(-1, 3).astype(np.float32) / 255
    luma = 0.2126 * px[:, 0] + 0.7152 * px[:, 1] + 0.0722 * px[:, 2]
    has_audio = bool(subprocess.run([ff("ffprobe"), "-v", "error", "-select_streams", "a", "-show_entries", "stream=index",
                                     "-of", "csv=p=0", str(clip)], capture_output=True, text=True).stdout.strip())
    print(f"{clip.name}: {total:.1f} s, uses {a.start:.1f}-{a.start + a.seconds:.1f} s, brightness {luma.mean():.2f}, "
          f"dark {np.mean(luma < 0.15):.2f}, sound {'yes' if has_audio else 'NO'} -> {out}")


if __name__ == "__main__":
    main()
