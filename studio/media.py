"""ffmpeg helpers: probing, scene clips (image + camera move, or video clip), brand cards."""
from __future__ import annotations

import glob
import math
import os
import shutil
import subprocess
import textwrap
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=None)
def tool(name: str) -> str:
    """Find ffmpeg / ffprobe, including winget's install folder when PATH isn't refreshed yet."""
    exe = shutil.which(name)
    if exe:
        return exe
    hits = glob.glob(os.path.expandvars(
        rf"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg*\*\bin\{name}.exe"))
    if hits:
        return hits[0]
    raise SystemExit(f"{name} not found. Install it: winget install Gyan.FFmpeg (then reopen PowerShell)")


def run(cmd: list[str], cwd: Path | None = None) -> None:
    if cmd[0] in ("ffmpeg", "ffprobe"):
        cmd = [tool(cmd[0]), *cmd[1:]]
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"Command failed: {Path(cmd[0]).name} {' '.join(cmd[1:6])} ...\n{result.stderr[-2000:]}")


def probe_duration(path: Path) -> float:
    out = subprocess.run([tool("ffprobe"), "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    try:
        return float(out.stdout.strip())
    except ValueError:
        raise SystemExit(f"Could not read duration of {path}")


MOTIONS = ("zoom_in", "zoom_out", "pan_left", "pan_right", "pan_up", "pan_down", "none")


def has_audio(path: Path) -> bool:
    out = subprocess.run([tool("ffprobe"), "-v", "error", "-select_streams", "a", "-show_entries",
                          "stream=index", "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    return bool(out.stdout.strip())


def clip_fit(source: Path, seconds: float, start: float = 0.0, end: float | None = None) -> dict:
    """How a generated clip (e.g. an 8 s Flow/Veo shot) is fitted to a scene of `seconds`:
    trim if it's long enough, slow it down a little (up to 1.25x) if it's slightly short,
    otherwise hold the last frame."""
    dur = probe_duration(source)
    avail = max((min(float(end), dur) if end else dur) - start, 0.1)  # `clip_end` drops a bad tail
    if seconds <= avail:
        return {"start": start, "speed": 1.0, "hold": 0.0, "use": seconds}
    if seconds <= avail * 1.25:
        return {"start": start, "speed": avail / seconds, "hold": 0.0, "use": avail}
    return {"start": start, "speed": 0.8, "hold": seconds - avail / 0.8, "use": avail}


def render_scene(source: Path, kind: str, seconds: float, motion: str, zoom: float,
                 w: int, h: int, fps: int, out: Path, fast: bool, clip_start: float = 0.0,
                 loop_in: dict | None = None, clip_end: float | None = None) -> dict | None:
    frames = max(int(round(seconds * fps)), 1)
    # Scene clips are an intermediate step (they are encoded again in the final mix), so keep them near-lossless.
    enc = ["-c:v", "libx264", "-preset", "ultrafast" if fast else "medium", "-crf", "20" if fast else "10",
           "-pix_fmt", "yuv420p", "-r", str(fps), "-an"]
    if kind == "clip":
        fit = clip_fit(source, seconds, clip_start, clip_end)
        vf = f"setpts=PTS/{fit['speed']:.5f}," if fit["speed"] != 1.0 else ""
        if fit["hold"] > 0:
            vf += f"tpad=stop_mode=clone:stop_duration={fit['hold']:.3f},"
        vf += (f"scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h},"
               f"fps={fps},setsar=1")
        if loop_in:
            # Loop seam: start at the last scene's final framing (zoom Z, shifted down by dy of the frame height) and
            # ease back to the clip's own framing over `ease` seconds, so the replay has no visible jump.
            z, dy, ease = float(loop_in.get("zoom", 1.0)), float(loop_in.get("dy", 0.0)), float(loop_in.get("ease", 1.0))
            f = f"(0.5+0.5*cos(PI*min(t/{ease},1)))"            # 1 → 0, smooth
            zt = f"(1+{z - 1:.5f}*{f})"
            vf += (f",scale=w='2*ceil({w}*{zt}/2)':h='2*ceil({h}*{zt}/2)':eval=frame:flags=bicubic,"
                   f"crop={w}:{h}:x='(iw-{w})/2':y='(ih-{h})/2+{dy * h:.3f}*{zt}*{f}'")
        run(["ffmpeg", "-y", "-v", "error", "-ss", f"{fit['start']:.3f}", "-t", f"{fit['use']:.3f}",
             "-i", str(source), "-vf", vf, "-frames:v", str(frames), *enc, str(out)])
        return fit
    if motion not in MOTIONS:
        raise SystemExit(f"Unknown motion '{motion}'. Use one of: {', '.join(MOTIONS)}")
    _render_still(source, frames, motion, zoom, w, h, fps, out, enc, fast)
    return None


def scene_fx(source: Path | None, fit: dict | None, seconds: float, out: Path) -> None:
    """The clip's own sound (Flow/Veo sound effects) fitted like the picture; silence for stills."""
    if source is None or fit is None or not has_audio(source):
        run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
             "-t", f"{seconds:.3f}", str(out)])
        return
    af = f"atempo={max(fit['speed'], 0.5):.5f}," if fit["speed"] != 1.0 else ""
    fade = min(0.04, seconds / 4)
    af += (f"aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d={fade:.3f},"
           f"apad=whole_dur={seconds:.3f},afade=t=out:st={max(seconds - 0.06, 0):.3f}:d=0.06")
    run(["ffmpeg", "-y", "-v", "error", "-ss", f"{fit['start']:.3f}", "-t", f"{fit['use']:.3f}",
         "-i", str(source), "-af", af, "-t", f"{seconds:.3f}", "-c:a", "pcm_s16le", str(out)])


def _render_still(source: Path, frames: int, motion: str, zoom: float, w: int, h: int, fps: int,
                  out: Path, enc: list[str], fast: bool = False) -> None:
    """Slow camera move on a still with sub-pixel precision (no stepping or wobble), piped to ffmpeg."""
    from PIL import Image

    img = Image.open(source).convert("RGB")
    margin = 1 + max(zoom, 0) + 0.004
    s = max(w * margin / img.width, h * margin / img.height)
    base = img.resize((max(int(round(img.width * s)), 1), max(int(round(img.height * s)), 1)), Image.LANCZOS)
    bw, bh = base.size
    s0 = min(bw / w, bh / h)  # window scale at zoom 1 (just covers the frame, with the margin)

    proc = subprocess.Popen([tool("ffmpeg"), "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                             "-s", f"{w}x{h}", "-r", str(fps), "-i", "-", *enc, str(out)],
                            stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    n = max(frames - 1, 1)
    resample = Image.BILINEAR if fast else Image.BICUBIC

    def frame_at(i: int) -> bytes:
        p = 0.5 - 0.5 * math.cos(math.pi * i / n)  # ease in and out
        if motion == "zoom_in":
            z = 1 + zoom * p
        elif motion == "zoom_out":
            z = 1 + zoom * (1 - p)
        elif motion == "none":
            z = 1.0
        else:
            z = 1 + zoom
        ww, wh = w * s0 / z, h * s0 / z
        cx, cy = bw / 2, bh / 2
        if motion in ("pan_left", "pan_right"):
            cx = ww / 2 + (bw - ww) * (p if motion == "pan_right" else 1 - p)
        elif motion in ("pan_up", "pan_down"):
            cy = wh / 2 + (bh - wh) * (p if motion == "pan_down" else 1 - p)
        x0, y0 = cx - ww / 2, cy - wh / 2
        return base.transform((w, h), Image.AFFINE, (ww / w, 0, x0, 0, wh / h, y0), resample=resample).tobytes()

    workers = max(1, (os.cpu_count() or 2))
    try:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for start in range(0, frames, workers * 2):  # small batches keep memory low
                for data in pool.map(frame_at, range(start, min(start + workers * 2, frames))):
                    proc.stdin.write(data)
        proc.stdin.close()
    except BrokenPipeError:
        pass
    err = proc.stderr.read().decode(errors="replace")
    if proc.wait() != 0:
        raise SystemExit(f"Encoding the camera move for {source.name} failed:\n{err[-1500:]}")


def upscaler() -> str | None:
    """Real-ESRGAN (ncnn-vulkan build) if it is installed, for sharper pictures."""
    root = Path(__file__).resolve().parent.parent
    for p in (root / "tools" / "realesrgan" / "realesrgan-ncnn-vulkan.exe",
              root / "tools" / "realesrgan" / "realesrgan-ncnn-vulkan"):
        if p.exists():
            return str(p)
    return shutil.which("realesrgan-ncnn-vulkan")


def prepare_picture(src: Path, w: int, h: int, zoom: float, cache: Path, mode: str) -> Path:
    """Upscale small pictures with Real-ESRGAN before the camera move (final renders only)."""
    if mode in (None, False, "off", "lanczos"):
        return src
    from PIL import Image

    with Image.open(src) as im:
        need = max(w * (1 + zoom) / im.width, h * (1 + zoom) / im.height)
    if need <= 1.0:
        return src
    exe = upscaler()
    if not exe:
        return src
    cache.mkdir(parents=True, exist_ok=True)
    st = src.stat()
    out = cache / f"{src.stem}_{int(st.st_mtime)}_{st.st_size}_x4.png"
    if not out.exists():
        print(f"    upscaling {src.name} with Real-ESRGAN …")
        r = subprocess.run([exe, "-i", str(src), "-o", str(out), "-n", "realesrgan-x4plus", "-s", "4"],
                           capture_output=True, text=True, cwd=str(Path(exe).parent))
        if r.returncode != 0 or not out.exists():
            print(f"  ! Real-ESRGAN failed on {src.name}; using the original picture")
            return src
    return out


def _rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def brand_background(w: int, h: int, ground: str, lime: str):
    """`ground` with the lime honeycomb at 12% opacity (brand guide)."""
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (w, h), _rgb(ground))
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    s = w / 1080 * 36 / 2  # hexagon size matching the 36 px pattern on a 1080 canvas
    col = (*_rgb(lime), 255)
    for row in range(int(h / (s * 1.733)) + 2):
        for colm in range(int(w / (s * 2)) + 2):
            cx = colm * 2 * s + (s if row % 2 else 0)
            cy = row * s * 1.733
            pts = [(cx + s * math.cos(math.radians(a)), cy + s * math.sin(math.radians(a))) for a in range(30, 390, 60)]
            d.line(pts, fill=col, width=max(1, round(w / 1080 * 1.4)))
    alpha = layer.getchannel("A").point(lambda v: int(v * 0.12))
    layer.putalpha(alpha)
    img.paste(layer, (0, 0), layer)
    return img


def placeholder_card(scene: dict, index: int, w: int, h: int, out: Path, font: Path | None, colors: dict) -> None:
    """A labelled card for scenes whose picture isn't ready yet, so drafts still render."""
    from PIL import ImageDraw, ImageFont

    img = brand_background(w, h, colors["ground"], colors["lime"])
    d = ImageDraw.Draw(img)

    def f(size):
        try:
            return ImageFont.truetype(str(font), size) if font else ImageFont.load_default()
        except OSError:
            return ImageFont.load_default()

    s = w / 1080
    ink, forest = _rgb(colors["ink"]), _rgb(colors["forest"])
    d.rounded_rectangle((w * 0.1, h * 0.27, w * 0.9, h * 0.53), radius=int(28 * s), outline=forest, width=max(2, int(5 * s)))
    d.text((w / 2, h * 0.30), f"SCENE {index:02d}  ·  picture not added yet", font=f(int(30 * s)), fill=forest, anchor="mm")
    prompt = scene.get("visual") or ""
    for i, line in enumerate(textwrap.wrap(prompt, 30)[:8]):
        d.text((w / 2, h * 0.35 + i * 50 * s), line, font=f(int(38 * s)), fill=ink, anchor="mm")
    img.save(out)


def end_card(w: int, h: int, logo: Path, width_frac: float, out: Path, colors: dict) -> None:
    from PIL import Image

    img = brand_background(w, h, colors["ground"], colors["lime"])
    lg = Image.open(logo).convert("RGBA")
    lw = int(w * width_frac)
    lg = lg.resize((lw, int(lg.height * lw / lg.width)), Image.LANCZOS)
    img.paste(lg, ((w - lw) // 2, int(h * 0.42 - lg.height / 2)), lg)
    img.save(out)
