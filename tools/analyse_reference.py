"""Measure reference videos (or our own renders) the same way every time, so results can be compared.

  python tools/analyse_reference.py "C:\\Users\\E GUNASELAN\\Downloads\\zack samples\\video.mp4" [more.mp4 ...]
  python tools/analyse_reference.py episodes\\db-cooper\\output\\db-cooper_howzit.mp4      (check our own video)

For each video prints one line of numbers and writes, next to this repo's docs/reference-analysis/:
  <name>_sheet.jpg      one frame per second with the time stamped on it (look at it!)
  <name>_spectrum.png   spectrogram of the first 20 s (horizontal lines = music, vertical bursts = sound effects)

Numbers (all 8 reference videos, analysed 2026-10-18, for comparison):
  luma      average brightness 0-1          reference 0.36-0.52 (mean 0.42) · our first D.B. Cooper pictures 0.12-0.17
  dark      share of very dark pixels       reference 0.05-0.14 (0.21-0.28 in space/night scenes) · ours 0.63-0.72
  sat       average saturation 0-1          reference 0.30-0.53
  shots     estimated shot changes          reference 1.0-1.6 s/shot (montage) or 3.5-5.2 s (continuous camera journey)
  lufs      loudness                        reference -14.1 to -14.2
  syl/s     syllable peaks per second       reference 4.3-5.1 (fast, nearly continuous narration)
  fx/10s    short high-frequency bursts     reference 0-6 per 10 s (whooshes, pops, clicks)
  music     tonal background in pauses      reference: none
"""
import colorsys
import shutil
import statistics as st
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "reference-analysis"


def ff(name):
    exe = shutil.which(name)
    if exe:
        return exe
    import glob, os
    hits = glob.glob(os.path.expandvars(rf"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg*\*\bin\{name}.exe"))
    if hits:
        return hits[0]
    sys.exit(f"{name} not found (winget install Gyan.FFmpeg)")


def duration(f):
    return float(subprocess.run([ff("ffprobe"), "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                                capture_output=True, text=True).stdout.strip())


def video_stats(f):
    w, h = 72, 128
    raw = subprocess.run([ff("ffmpeg"), "-v", "error", "-i", str(f), "-vf", f"scale={w}:{h},format=gray", "-f", "rawvideo", "-"],
                         capture_output=True).stdout
    a = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32)
    d = np.abs(np.diff(a, axis=0)).mean(axis=(1, 2))
    hist = [np.histogram(x, bins=32, range=(0, 255))[0] / x.size for x in a]
    hd = np.array([np.abs(hist[i + 1] - hist[i]).sum() for i in range(len(hist) - 1)])
    score = d / (np.median(d) + 1e-6)
    fps = len(a) / duration(f)
    cuts = []
    for i in range(1, len(d) - 1):
        if (d[i] > 25 or (score[i] > 6 and d[i] > 12) or hd[i] > 0.5) and d[i] >= d[i - 1] and d[i] >= d[i + 1]:
            t = (i + 1) / fps
            if not cuts or t - cuts[-1] > 0.3:
                cuts.append(t)
    raw = subprocess.run([ff("ffmpeg"), "-v", "error", "-i", str(f), "-vf", "fps=1,scale=180:320", "-f", "rawvideo",
                          "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    px = np.frombuffer(raw, np.uint8).reshape(-1, 3).astype(np.float32) / 255
    r, g, b = px[:, 0], px[:, 1], px[:, 2]
    mx, mn = px.max(1), px.min(1)
    luma = 0.2126 * r + 0.7152 * g + 0.0722 * b
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    idx = np.where(sat > 0.25)[0][::7]
    hues = [colorsys.rgb_to_hsv(r[i], g[i], b[i])[0] * 360 for i in idx]
    names = ["red/brown", "orange", "yellow", "green", "teal/cyan", "blue", "purple", "pink"]
    hh = np.histogram(hues, bins=[0, 30, 60, 90, 150, 210, 270, 330, 360])[0]
    hh = hh / max(hh.sum(), 1)
    top = ", ".join(f"{n} {v:.0%}" for n, v in sorted(zip(names, hh), key=lambda x: -x[1])[:3])
    return {"shots": len(cuts) + 1, "luma": float(luma.mean()), "dark": float((luma < 0.15).mean()),
            "sat": float(sat.mean()), "hues": top}


def audio_stats(f):
    sr = 16000
    x = np.frombuffer(subprocess.run([ff("ffmpeg"), "-v", "error", "-i", str(f), "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"],
                                     capture_output=True).stdout, np.int16).astype(np.float32) / 32768
    if len(x) < sr:
        return {"lufs": "n/a", "syl": 0, "fx": 0, "music": "no audio"}
    err = subprocess.run([ff("ffmpeg"), "-hide_banner", "-i", str(f), "-af", "ebur128", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    lines = [l for l in err.splitlines() if l.strip().startswith("I:")]
    lufs = lines[-1].split()[1] if lines else "n/a"
    win = 640
    m = len(x) // win
    seg = x[:m * win].reshape(m, win)
    W = np.abs(np.fft.rfft(seg * np.hanning(win), axis=1))
    fq = np.fft.rfftfreq(win, 1 / sr)
    tot = W.sum(1) + 1e-9
    high = W[:, (fq >= 5000) & (fq < 8000)].sum(1)
    wdb = 20 * np.log10(np.sqrt((seg ** 2).mean(1)) + 1e-9)
    floor = np.percentile(wdb, 10)
    sfx = (high / tot > 0.18) & (wdb > floor + 15)
    ev = int(np.sum(sfx[1:] & ~sfx[:-1]))
    quiet = wdb < np.percentile(wdb, 20)
    flat = np.exp(np.log(W[:, 5:] + 1e-9).mean(1)) / (W[:, 5:].mean(1) + 1e-9)
    if quiet.sum() == 0 or wdb.max() < -60:
        music = "n/a"
    else:
        music = "likely" if flat[quiet].mean() < 0.25 and (wdb[quiet].mean() - floor) > 6 else "none/low"
    hop = int(sr * 0.02)
    fr = x[: len(x) // hop * hop].reshape(-1, hop)
    env = np.convolve(np.sqrt((fr ** 2).mean(1)), np.ones(4) / 4, "same")
    thr = np.percentile(env, 45)
    pk = sum(1 for i in range(1, len(env) - 1) if env[i] > env[i - 1] and env[i] >= env[i + 1] and env[i] > thr)
    dur = len(x) / sr
    return {"lufs": lufs, "syl": pk / dur, "fx": ev / dur * 10, "music": music}


def sheets(f, name):
    OUT.mkdir(parents=True, exist_ok=True)
    n = int(np.ceil(duration(f)))
    rows = (n + 9) // 10
    font = "C\\:/Windows/Fonts/arialbd.ttf" if sys.platform == "win32" else "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    subprocess.run([ff("ffmpeg"), "-v", "error", "-y", "-i", str(f), "-vf",
                    f"fps=1,scale=216:384,drawtext=fontfile='{font}':text='%{{eif\\:t\\:d}}':x=6:y=6:fontsize=22:"
                    f"fontcolor=yellow:box=1:boxcolor=black@0.6,tile=10x{rows}", "-frames:v", "1",
                    str(OUT / f"{name}_sheet.jpg")])
    subprocess.run([ff("ffmpeg"), "-v", "error", "-y", "-t", "20", "-i", str(f), "-lavfi",
                    "showspectrumpic=s=1400x360:legend=1:scale=log:fscale=lin:stop=8000", str(OUT / f"{name}_spectrum.png")])


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    print(f"{'video':32} {'len':>5} {'shots':>5} {'s/shot':>6} {'luma':>5} {'dark':>5} {'sat':>5} {'lufs':>6} {'syl/s':>5} {'fx/10s':>6} music     main hues")
    for arg in sys.argv[1:]:
        f = Path(arg)
        name = f.stem.replace(" ", "_")[:40]
        d = duration(f)
        v, a = video_stats(f), audio_stats(f)
        sheets(f, name)
        print(f"{f.name[:32]:32} {d:5.1f} {v['shots']:5d} {d / v['shots']:6.2f} {v['luma']:5.2f} {v['dark']:5.2f} {v['sat']:5.2f} "
              f"{a['lufs']:>6} {a['syl']:5.2f} {a['fx']:6.1f} {a['music']:9} {v['hues']}")
    print(f"Contact sheets and spectrograms: {OUT}")


if __name__ == "__main__":
    main()
