# Episode Status: This Dog Walked 2,551 Miles Home (bobbie-walks-home)

- **Current Phase:** prompts (owner: Canva E1 + K0-K5, then Flow C1-C6)
- **Active AI:** Claude Code (owner runs Canva + Flow)
- **Last Updated:** 2026-10-24 IST
- **Total Flow Credits Spent:** 0 / 300 (plan: 6 clips x 20 = 120)

## Decisions
- 2026-10-24 (Owner): touching true story #3; new semi-realistic Zack-style look; keyframes in Canva.
- 2026-10-24 (Claude Code): research + page in `README.md`; owner recorded the narration (40.52 s). `script.yaml` (6 scenes, vo_start from pauses) and `output/bobbie-walks-home_flow_prompts.md` (E1 dog reference, K0-K5, C1-C6; C6 ends on K0 for the loop).
- Join: `python tools/join_continuous.py episodes/bobbie-walks-home --total 40.52 --windows 8.6,6.8,6.6,6.6,6.0,5.92`

## Next
- Owner: generate, download (1080p), message "clips in". Claude: check, join, build, post copy, update README.md + docs/shorts-index.md.

## Clip log (2026-10-24)
- C1 ok (ears change floppy->pointed at 4 s, minor). C2 ok (blurry sign text, asphalt road, minor). C3 ok. C4 ok.
- Join note: C4 holds the K3 hill shot for ~0.9 s then hard-cuts to the plains; skip c04's first 0.9 s at join so the cut lands on the C3->C4 boundary.
- C5 ok (soft dissolves river->snow->night farm, fine). Credits: 100 after C5; C6 made twice (c06a chosen, lands on K0) = 140 total. FINAL built 2026-10-24: 40.5 s, luma 0.52, dark 0.09, -14.3 LUFS. Join: --windows 8.6,6.8,6.6,6.6,6.0,5.92 --starts c04=0.9 --ends c01..c05=8.0
