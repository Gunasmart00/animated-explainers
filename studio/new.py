"""Start a new episode folder.

  python -m studio.new "How does UPI send money in 2 seconds"
  python -m studio.new "The Thirsty Crow" --preset kids
"""
from __future__ import annotations

import argparse
import re

from .config import ROOT

STORY = """# {title}

Paste your story or notes here. Then use prompt G1 in prompts/gemini.md (or ask Claude)
to turn it into script.yaml.
"""

SCRIPT = """# Write this per prompts/scene-script.md (Claude does it when you say "Create New video: ...").
title: "{title}"
preset: {preset}
structure: hook             # hook | reveal
caption: |
  ...
hashtags: []                # exactly 5, no #
cover_text: ""
alt_text: ""
characters: []
setting: "a bright, clean modern interior"
facts: []

scenes:
  - id: s01
    narration: "First beat of the narration."
    shot: "0-2 s: ...; 2-4 s: ..."
    camera: "smooth slow push-in"
    sfx: "..."
"""


STATUS_TEMPLATE = """# Episode Status: {title} ({slug})

- **Current Phase:** scripting
- **Active AI:** Unassigned
- **Last Updated:** {now}
- **Total Flow Credits Spent:** 0 / 300 limit

## 1. Decision Log
- {now}: Episode initialized via studio.new.

## 2. Clip Progress & Verification Table

| Clip ID | Target Time | Narration Line | Verification Status | Notes |
|---|---|---|---|---|
| C01 | ... | ... | not_started | ... |

## 3. Immediate Next Step & AI Handoff
- **Task:** Research facts (2 sources per claim) in story.md and draft script.yaml.
- **Next Prompt for AI:** "Read episodes/{slug}/story.md and write script.yaml following docs/zack-style-bible.md."
"""


def main():
    import datetime
    ap = argparse.ArgumentParser()
    ap.add_argument("title")
    ap.add_argument("--preset", default="explainer")
    a = ap.parse_args()
    slug = re.sub(r"[^a-z0-9]+", "-", a.title.lower()).strip("-")[:60]
    d = ROOT / "episodes" / slug
    if d.exists():
        raise SystemExit(f"{d} already exists")
    for sub in ("images", "clips", "audio"):
        (d / sub).mkdir(parents=True)
        (d / sub / ".gitkeep").touch()
    title = a.title.rstrip("?")
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M IST")
    (d / "story.md").write_text(STORY.format(title=title), encoding="utf-8")
    (d / "script.yaml").write_text(SCRIPT.format(title=title, preset=a.preset), encoding="utf-8")
    (d / "STATUS.md").write_text(STATUS_TEMPLATE.format(title=title, slug=slug, now=now_str), encoding="utf-8")

    # Update ACTIVE_PRODUCTION.md
    active_prod = ROOT / "ACTIVE_PRODUCTION.md"
    if active_prod.exists():
        text = active_prod.read_text(encoding="utf-8")
        text = re.sub(r"- \*\*Active Episode:\*\* .*", f"- **Active Episode:** `{slug}` ({title})", text)
        text = re.sub(r"- \*\*Current Phase:\*\* .*", "- **Current Phase:** `scripting`", text)
        text = re.sub(r"- \*\*Last Updated:\*\* .*", f"- **Last Updated:** {now_str}", text)
        active_prod.write_text(text, encoding="utf-8")

    print(f"Created episodes/{slug}/ (with story.md, script.yaml, and STATUS.md)")


if __name__ == "__main__":
    main()

