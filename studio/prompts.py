"""Fill the Gemini picture prompts (G4–G6 in prompts/gemini.md) for one episode.

  python -m studio.prompts episodes/why-do-onions-make-you-cry

Writes output/<episode>_gemini_prompts.md: one ready-to-paste block per character sheet,
per scene picture and per Veo clip. Also runs automatically with every build.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from .config import ROOT, load_episode


def gemini_blocks() -> dict[str, list[str]]:
    """Code blocks of prompts/gemini.md, keyed by section ('G1'…'G7', 'STYLE')."""
    text = (ROOT / "prompts" / "gemini.md").read_text(encoding="utf-8")
    blocks: dict[str, list[str]] = {}
    for sec in re.split(r"^## ", text, flags=re.M)[1:]:
        title = sec.splitlines()[0]
        key = "STYLE" if title.lower().startswith(("2d style", "3d style")) else title.split()[0]
        blocks[key] = re.findall(r"```\n(.*?)\n```", sec, flags=re.S)
    return blocks


def fill_prompts(episode: dict) -> str:
    b = gemini_blocks()
    style = b["STYLE"][0].strip()
    chars = episode.get("characters") or []
    names = ", ".join(str(c.get("name", "")).strip() for c in chars if c.get("name")) or "the main character"
    out = [f"# {episode.get('title', '')} — Gemini picture prompts",
           "",
           "Open a **new Gemini chat** for this episode and keep every picture in that one chat.",
           "Copy each block in order. Save each picture as `images\\<scene id>.png`, each clip as `clips\\<scene id>.mp4`.",
           ""]

    out += ["## G4 — Reference sheets (do these first, keep the ones you like)", ""]
    if not chars:
        out += ["_No `characters` in script.yaml — skip this step, or add the main object/character first._", ""]
    for c in chars:
        g4 = re.sub(r"Subject: \[.*?\]", f"Subject: {c.get('name', '')}: {c.get('look', '')}", b["G4"][0])
        g4 = g4.replace("[PASTE 3D STYLE BLOCK]", style)
        out += [f"### {c.get('name', 'character')}", "```", g4, "```", ""]

    out += ["## G5 — Scene pictures", ""]
    for i, s in enumerate(episode.get("scenes") or []):
        sid, visual = s.get("id", f"s{i + 1:02d}"), (s.get("visual") or "").strip()
        if i == 0:
            p = (b["G5"][0].replace("[CHARACTER NAME]", names)
                 .replace("[PASTE the scene's `visual` line]", visual)
                 .replace("[PASTE 3D STYLE BLOCK]", style))
            if not chars:
                p = "\n".join(l for l in p.splitlines() if not l.startswith("Use the attached reference"))
        else:
            p = b["G5"][1].replace("[PASTE the next scene's `visual` line]", visual)
        out += [f"### {sid} → save as `images\\{sid}.png`", f"_Narration: {s.get('narration', '')}_", "```", p, "```", ""]

    veo = [s for s in episode.get("scenes") or [] if s.get("veo")]
    out += ["## G6 — Moving clips (Veo)", ""]
    if not veo:
        out += ["_No scene has a `veo:` line. Optional: add `veo: \"what moves\"` to 2–3 key scenes._", ""]
    for s in veo:
        p = (b["G6"][0].replace("[WHAT MOVES, e.g. \"the chocolate bar slowly melts and drips; the engineer looks down in surprise\"]",
                                str(s["veo"]).strip())
             .replace("[slow push-in / slow orbit / static]", "slow push-in"))
        out += [f"### {s['id']} → attach `images\\{s['id']}.png`, save as `clips\\{s['id']}.mp4`", "```", p, "```", ""]
    if "G8" in b:
        narration = "\n\n".join((sc.get("narration") or "").strip() for sc in episode.get("scenes") or [])
        out += ["## G8 — Voiceover in Google AI Studio (optional)",
                "Paste the style line, then the narration below it. Save the WAV as `audio\\voiceover.wav` and add "
                "`voiceover: audio\\voiceover.wav` to script.yaml.", "```", b["G8"][0].strip(), "", narration, "```", ""]
    return "\n".join(out)


def write_prompts(episode: dict, path: Path) -> Path:
    path.write_text(fill_prompts(episode), encoding="utf-8")
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode", type=Path)
    d = ap.parse_args().episode.resolve()
    episode, _ = load_episode(d)
    (d / "output").mkdir(exist_ok=True)
    print(write_prompts(episode, d / "output" / f"{d.name}_gemini_prompts.md"))


if __name__ == "__main__":
    main()
