"""Make the built-in sound effects in assets/sfx (synthesised here, so no licence questions).

  python tools/make_sfx.py

whoosh.wav  soft air swish for scene cuts
pop.wav     short bubbly pop for pop-ups
ding.wav    light bell for a reveal
impact.wav  deep thud for the lime reveal pop-up, shakes and big moments (sfx.reveal)
Replace any of them with your own (e.g. from Pixabay) using the same file name.
"""
import wave
from pathlib import Path

import numpy as np

SR = 48000
OUT = Path(__file__).resolve().parent.parent / "assets" / "sfx"


def save(name, mono):
    mono = mono / (np.max(np.abs(mono)) + 1e-9) * 0.9
    stereo = np.stack([mono, mono], axis=1)
    OUT.mkdir(parents=True, exist_ok=True)
    with wave.open(str(OUT / name), "wb") as w:
        w.setnchannels(2), w.setsampwidth(2), w.setframerate(SR)
        w.writeframes((stereo * 32767).astype(np.int16).tobytes())
    print(OUT / name)


def whoosh(d=0.42):
    n = int(SR * d)
    t = np.linspace(0, 1, n)
    rng = np.random.default_rng(7)
    noise = rng.standard_normal(n)
    # sweep a resonant band-pass from low to high and back down
    out, y1, y2 = np.zeros(n), 0.0, 0.0
    centre = 300 + 2600 * np.sin(np.pi * t) ** 2
    for i in range(n):
        w0 = 2 * np.pi * centre[i] / SR
        r = 0.985
        a1, a2 = -2 * r * np.cos(w0), r * r
        y = noise[i] * (1 - r) - a1 * y1 - a2 * y2
        y2, y1 = y1, y
        out[i] = y
    env = np.sin(np.pi * t) ** 1.6
    return out * env


def pop(d=0.14):
    n = int(SR * d)
    t = np.arange(n) / SR
    f = 950 * np.exp(-t * 18) + 260
    phase = 2 * np.pi * np.cumsum(f) / SR
    env = np.exp(-t * 38) * (1 - np.exp(-t * 900))
    return np.sin(phase) * env + 0.15 * np.sin(2 * phase) * env


def ding(d=1.1):
    n = int(SR * d)
    t = np.arange(n) / SR
    tone = sum(a * np.sin(2 * np.pi * 1318.5 * k * t) * np.exp(-t * (3 + 2.5 * k)) for k, a in ((1, 1), (2, 0.35), (3, 0.18), (4.2, 0.08)))
    return tone * (1 - np.exp(-t * 600))


def impact(d=1.2):
    """Sub-bass drop with harmonics (so phone speakers still hear it) and a short noisy transient."""
    n = int(SR * d)
    t = np.arange(n) / SR
    f = 38 + 70 * np.exp(-t * 9)
    phase = 2 * np.pi * np.cumsum(f) / SR
    body = (np.sin(phase) + 0.45 * np.sin(2 * phase) + 0.2 * np.sin(3 * phase)) * np.exp(-t * 3.2)
    rng = np.random.default_rng(11)
    hit = rng.standard_normal(n) * np.exp(-t * 60)
    hit = np.convolve(hit, np.ones(24) / 24, "same")  # dull it: a thump, not a click
    return (body + 0.6 * hit) * (1 - np.exp(-t * 2000))


if __name__ == "__main__":
    save("whoosh.wav", whoosh())
    save("pop.wav", pop())
    save("ding.wav", ding())
    save("impact.wav", impact())
