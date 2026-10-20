"""Music selection and the sound-effects track (whoosh on cuts, pop on pop-ups, impact on the lime reveal)."""
from __future__ import annotations

import wave
from pathlib import Path

import numpy as np

from .config import ROOT, resolve
from .media import run

SR = 48000
AUDIO_EXT = (".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac")


def pick_music(cfg: dict, episode_dir: Path) -> Path | None:
    m = cfg.get("music") or {}
    f = m.get("file")
    if not f:
        return None
    if f != "auto":
        p = resolve(f, episode_dir)
        if not p:
            print(f"  ! music file not found: {f}")
        return p
    for folder in (episode_dir / "audio", ROOT / "assets" / "music"):
        if folder.exists():
            names = sorted(p for p in folder.iterdir() if p.suffix.lower() in AUDIO_EXT
                           and (folder.name != "audio" or p.stem.lower().startswith("music")))
            if names:
                return names[0]
    print("  ! no music: add a royalty-free track to assets\\music\\ (see assets\\music\\README.md)")
    return None


def _load(name: str, episode_dir: Path, cache: Path) -> np.ndarray | None:
    """A sound effect by name (assets/sfx/<name>.wav) or path, as float stereo at 48 kHz."""
    if not name:
        return None
    p = resolve(name, episode_dir) if any(c in name for c in "/\\.") else None
    p = p or (ROOT / "assets" / "sfx" / f"{name}.wav")
    if not p.exists():
        print(f"  ! sound effect not found: {name}")
        return None
    wav = cache / f"sfx_{p.stem}.wav"
    if not wav.exists() or wav.stat().st_mtime < p.stat().st_mtime:
        cache.mkdir(parents=True, exist_ok=True)
        run(["ffmpeg", "-y", "-v", "error", "-i", str(p), "-ar", str(SR), "-ac", "2", "-c:a", "pcm_s16le", str(wav)])
    with wave.open(str(wav)) as w:
        data = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    return data.reshape(-1, 2)


def sfx_track(total: float, cuts: list[float], popups: list[tuple[float, str | None]],
              cfg: dict, episode_dir: Path, out: Path) -> Path | None:
    s = cfg.get("sfx") or {}
    vol = float(s.get("volume", 0.35))
    track = np.zeros((int(total * SR) + SR, 2), np.float32)
    placed = 0
    cache = out.parent

    def place(name, at, gain=1.0):
        nonlocal placed
        snd = _load(name, episode_dir, cache)
        if snd is None:
            return
        i = max(int(at * SR), 0)
        j = min(i + len(snd), len(track))
        track[i:j] += snd[: j - i] * vol * gain
        placed += 1

    if s.get("cuts"):
        for t in cuts:
            place(s["cuts"], t - 0.18, 0.8)  # the swish peaks right on the cut
    for t, name in popups:
        if name == "reveal":  # the lime pop-up (the one reveal) gets the reveal sound, if set
            name = s.get("reveal") or "default"
        name = s.get("popups") if name in (None, "default") else name
        if name and name != "none":
            place(name, t - 0.02)
    if not placed:
        return None
    track = np.clip(track[: int(total * SR)], -1, 1)
    with wave.open(str(out), "wb") as w:
        w.setnchannels(2), w.setsampwidth(2), w.setframerate(SR)
        w.writeframes((track * 32767).astype(np.int16).tobytes())
    return out
