"""Find the exact loop seam: the frame of the last clip that best matches the first clip's opening frames.

Veo (Frames to Video with an end frame) usually lands on the end frame about 0.3 s BEFORE the clip ends and then
drifts. Cut the last scene there with `clip_end`, so the video restarts on the same picture (no visible jump).

    python tools/loop_seam.py episodes/<name>/clips/s13.mp4 episodes/<name>/clips/s01.mp4 [--from 5.5]

Prints the best matches (mean pixel difference out of 255; under ~3 is invisible) and the clip_end to use.
"""
import argparse
import subprocess

import numpy as np


def frames(path, start, length, fps=24):
    out = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", str(start), "-t", str(length), "-i", path,
         "-vf", f"fps={fps},scale=90:160,format=gray", "-f", "rawvideo", "-"],
        capture_output=True, check=True).stdout
    return np.frombuffer(out, dtype=np.uint8).reshape(-1, 160, 90).astype(float)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("last")
    ap.add_argument("first")
    ap.add_argument("--from", dest="start", type=float, default=5.5, help="search the last clip from this second")
    ap.add_argument("--first-window", type=float, default=0.5, help="seconds of the first clip to compare against")
    a = ap.parse_args()
    first = frames(a.first, 0, a.first_window)
    last = frames(a.last, a.start, 8 - a.start)
    res = []
    for i, f in enumerate(last):
        d = [np.abs(f - g).mean() for g in first]
        j = int(np.argmin(d))
        res.append((d[j], a.start + i / 24, j / 24))
    res.sort()
    for diff, t_last, t_first in res[:5]:
        print(f"diff {diff:5.1f}   last@{t_last:.2f} s  ->  first@{t_first:.2f} s")
    diff, t_last, t_first = res[0]
    print(f"\nUse in script.yaml: clip_end: {t_last:.2f}  (and clip_start: {t_last:.2f} - scene seconds)")
    if t_first > 0.05:
        print(f"Best match is {t_first:.2f} s into the first clip: also set clip_start: {t_first:.2f} on the first scene.")
    if diff > 3:
        print("Warning: no near-identical frame (diff > 3); the loop will show a small jump.")


if __name__ == "__main__":
    main()
