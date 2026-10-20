"""Hear candidate narrator voices side by side, then pick one.

  python -m studio.voices                                  test line, all candidates
  python -m studio.voices episodes/why-do-onions-make-you-cry   uses that episode's first scene

Writes voice-tests/<voice>.mp3. Play them, then set the winner in presets/explainer.yaml
(voice: name / rate / pitch) or per episode with `voice:` in script.yaml.

The reference Reel's narrator: young-sounding male, quick (about 4 syllables a second), lively pitch,
friendly storytelling tone. These are free Microsoft voices that come close. Cloning a real creator's
voice isn't done here; for an even closer, more natural read, see AI Studio in prompts/gemini.md (G8).
"""
from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from .config import ROOT, load_episode

CANDIDATES = [  # (voice, rate, pitch)
    ("en-US-AndrewMultilingualNeural", "+10%", "+0Hz"),
    ("en-US-BrianMultilingualNeural", "+10%", "+0Hz"),
    ("en-US-ChristopherNeural", "+12%", "+4Hz"),
    ("en-US-EricNeural", "+12%", "+4Hz"),
    ("en-US-GuyNeural", "+10%", "+2Hz"),
    ("en-US-RogerNeural", "+8%", "+0Hz"),
    ("en-US-SteffanNeural", "+12%", "+4Hz"),
    ("en-US-AndrewNeural", "+12%", "+3Hz"),
]
LINE = ("Three friends check into a hotel room that costs thirty dollars. "
        "But when the manager realizes he overcharged them, something strange happens.")


async def _say(text, voice, rate, pitch, out):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(str(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode", nargs="?", type=Path)
    a = ap.parse_args()
    text = LINE
    if a.episode:
        ep, _ = load_episode(a.episode.resolve())
        text = " ".join(s["narration"] for s in ep["scenes"][:2])
    out_dir = ROOT / "voice-tests"
    out_dir.mkdir(exist_ok=True)
    for voice, rate, pitch in CANDIDATES:
        out = out_dir / f"{voice.replace('en-US-', '')}_{rate.replace('%', 'pct')}.mp3"
        try:
            asyncio.run(_say(text, voice, rate, pitch, out))
            print(f"  {out.relative_to(ROOT)}   voice: {voice}  rate: \"{rate}\"  pitch: \"{pitch}\"")
        except Exception as exc:
            print(f"  ! {voice}: {exc}")
    print("Play them (double-click in Explorer) and copy the winner's three values into presets\\explainer.yaml.")


if __name__ == "__main__":
    main()
