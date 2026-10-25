# Episode Status: Why McDonald's Ice Cream Machine Is Always Broken (ice-cream-machine)

- **Current Phase:** final (ready to post)
- **Active AI:** Claude Code (owner does Flow)
- **Last Updated:** 2026-10-21 IST
- **Total Flow Credits Spent:** 160 / 300 limit (7 clips + 1 redo of C4)

## 1. Decision Log
- 2026-10-21 (Owner): picked pitch #1; owner runs Flow himself from now on (token saving); Claude does research, script, prompts, checks, build.
- 2026-10-21 (Claude Code): research in `story.md` (2 sources per claim). Narration rewritten conversational at owner's request; owner recorded it (Mark), 55.56 s → `audio/voiceover.mp3`.
- 2026-10-21 (Claude Code): `script.yaml` (10 scenes, vo_start from the pauses, one continuous take via `clips/visual.mp4`) and `output/ice-cream-machine_flow_prompts.md` (made by `make_prompts.py`): keyframes K0–K6, clips C1–C7 (C7 ends on K0 = loop). Brand-free visuals (no logos/arches/text). Join windows: 8.0, 8.0, 7.5, 8.1, 7.8, 7.9, 8.26.

- 2026-10-21 17:10 (Claude Code): checked C1–C6 from Downloads. C1, C2, C3, C5, C6 PASS. C4 FAIL (jumped to the map and another restaurant, germs came back after the heat, no heat/frost, smeared end) → simpler locked-camera C4 prompt (`output/C4_redo_prompt.txt`). Old C4 in `clips/old/c04_v1.mp4`.
- 2026-10-21 17:45 (Claude Code): C4 redo PASS (orange heat, germs vanish, frost, pull back to night). C7 PASS (gold stamp on the map, pins unlock and turn green, worker fixes the machine, lands on the first frame). Menu board shows a small garbled word in C7 (minor).
- 2026-10-21 (Claude Code): keyframes taken from the clips' first frames (owner didn't download them); join windows 8.0, 8.0, 7.5, 8.1, 7.8, 7.9, 8.26 with `--ends c02=7.62` (the map looks the same for its last 3 s, so the auto cut was too early). Seams 0.1–6.2/255; loop 5.0.
- FINAL: `output/ice-cream-machine_howzit.mp4` (55.6 s, luma 0.57, dark 0.05, −15.0 LUFS); delivery copy in Downloads; post copy in `output/ice-cream-machine_post.md`.

## 2. Next
- **Owner:** post (Instagram Reel Collab + YouTube Short, HowZit playlist) at 7 PM ET; add a licensed track in-app.
