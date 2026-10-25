"""Join keyframe-chained Flow clips into ONE continuous visual track (no cuts) for a one-take episode.

Each clip i was made with Frames to Video: START = keyframe K(i-1), END = keyframe K(i). Veo usually reaches the
end frame early (often 1-2.5 s before the clip ends) and then holds still. This tool finds, in each clip, the
moment it lands on its end keyframe, drops the still tail, and time-fits the used part to the clip's window, so
every seam is the same picture and the camera never stops.
A missing clip is replaced by a placeholder: a slow zoom crossfade from K(i-1) to K(i) (for animatics).

    python tools/join_continuous.py episodes/jupiter-crash --total 56.45 [--windows 8.06,8.06,...] [--ends c05=6.9]

Writes clips/visual.mp4 (1080x1920, 24 fps, with the clips' own sound) and prints a seam report.
Keyframes: images/K0.png|jpg ... images/K<n-1>.png; clips: clips/c01.mp4 ... ; the last clip ends on K0 (loop).
"""
import argparse
import subprocess
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image

W, H, FPS = 1080, 1920, 24


def gray_frames(path, start=0.0, length=None):
    cmd = ["ffmpeg", "-v", "error", "-ss", str(start)] + (["-t", str(length)] if length else []) + [
        "-i", str(path), "-vf", f"fps={FPS},scale=90:160,format=gray", "-f", "rawvideo", "-"]
    out = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(out, dtype=np.uint8).reshape(-1, 160, 90).astype(float)


def gray_image(path):
    return np.asarray(Image.open(path).convert("L").resize((90, 160)), dtype=float)


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, check=True).stdout
    return float(out.strip())


def landing_time(clip, key_img, search_from=3.0):
    """Earliest time (after search_from) where the clip is about as close to the end keyframe as it ever gets."""
    fr = gray_frames(clip, search_from)
    ref = gray_image(key_img)
    d = np.abs(fr - ref).mean(axis=(1, 2))
    best = d.min()
    idx = int(np.argmax(d <= best + max(1.0, best * 0.15)))  # first frame within ~15% of the best match
    return search_from + idx / FPS, float(d[idx]), float(best)


def run(cmd):
    subprocess.run(cmd, check=True, capture_output=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    ap.add_argument("--total", type=float, required=True, help="length of the voiceover (s)")
    ap.add_argument("--count", type=int, default=7)
    ap.add_argument("--windows", help="comma-separated seconds per clip (default: equal)")
    ap.add_argument("--starts", default="", help="skip the head of a clip, e.g. c04=0.9 (drops a held frame + cut)")
    ap.add_argument("--ends", default="", help="manual end times, e.g. c05=6.9,c07=7.2 (overrides the landing search)")
    a = ap.parse_args()
    ep = Path(a.episode)
    n = a.count
    windows = [float(x) for x in a.windows.split(",")] if a.windows else [a.total / n] * n
    def key(i):
        for ext in ("png", "jpg"):
            if (ep / "images" / f"K{i}.{ext}").exists():
                return ep / "images" / f"K{i}.{ext}"
        return ep / "images" / f"K{i}.png"
    keys = [key(i) for i in range(n)] + [key(0)]
    starts = {k: float(v) for k, v in (x.split("=") for x in a.starts.split(",") if x)}
    tmp = Path(tempfile.mkdtemp())
    parts = []
    report = []
    for i in range(1, n + 1):
        win = windows[i - 1]
        clip = ep / "clips" / f"c{i:02d}.mp4"
        part = tmp / f"p{i:02d}.mp4"
        manual = dict(x.split("=") for x in a.ends.split(",") if x)
        if clip.exists():
            end, dist, best = landing_time(clip, keys[i])
            end = min(end + 1 / FPS, duration(clip))
            if f"c{i:02d}" in manual:
                end = float(manual[f"c{i:02d}"])
            st = starts.get(f"c{i:02d}", 0.0)
            speed = (end - st) / win  # <1 = slowed down
            vf = (f"trim={st:.4f}:{end:.4f},setpts=(PTS-STARTPTS)/{speed:.5f},fps={FPS},"
                  f"scale={W}:{H}:flags=lanczos,setsar=1")
            af = f"atrim={st:.4f}:{end:.4f},asetpts=PTS-STARTPTS,atempo={max(speed, 0.5):.5f},apad,atrim=0:{win:.4f}"
            run(["ffmpeg", "-y", "-v", "error", "-i", str(clip), "-filter_complex",
                 f"[0:v]{vf}[v];[0:a]{af}[a]", "-map", "[v]", "-map", "[a]", "-t", f"{win:.4f}",
                 "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p",
                 "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(part)])
            report.append(f"c{i:02d}: lands on K{i % n} at {end:.2f} s (diff {dist:.1f}, best {best:.1f}); "
                          f"used {st:.2f}-{end:.2f} s at {speed:.2f}x -> {win:.2f} s")
        else:
            a_img, b_img = keys[i - 1], keys[i]
            fade = min(1.2, win / 3)
            z = f"zoompan=z='1+0.06*on/({win * FPS:.0f})':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}"
            run(["ffmpeg", "-y", "-v", "error",
                 "-loop", "1", "-t", f"{win:.4f}", "-i", str(a_img), "-loop", "1", "-t", f"{win:.4f}", "-i", str(b_img),
                 "-f", "lavfi", "-t", f"{win:.4f}", "-i", "anullsrc=r=48000:cl=stereo",
                 "-filter_complex",
                 f"[0:v]scale={W}:{H},setsar=1,{z}[a];[1:v]scale={W}:{H},setsar=1,{z}[b];"
                 f"[a][b]xfade=transition=fade:duration={fade:.3f}:offset={win - fade - 0.2:.3f},trim=0:{win:.4f}[v]",
                 "-map", "[v]", "-map", "2:a", "-t", f"{win:.4f}",
                 "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-ar", "48000", str(part)])
            report.append(f"c{i:02d}: MISSING -> placeholder K{i - 1} -> K{i % n} ({win:.2f} s)")
        parts.append(part)
    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts))
    out = ep / "clips" / "visual.mp4"
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(out)])
    print("\n".join(report))
    print(f"-> {out} ({duration(out):.2f} s)")


if __name__ == "__main__":
    main()
