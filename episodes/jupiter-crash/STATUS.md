# Episode Status: NASA Crashed Its Own Spacecraft Into Jupiter (jupiter-crash)

- **Current Phase:** final (ready to post)
- **Active AI:** Claude Code
- **Last Updated:** 2026-10-21 IST
- **Initial Account Credits:** 860
- **Total Flow Credits Spent:** 180 / 300 limit (C1–C7 + redos of C3 and C7)

## 1. Decision Log
- 2026-10-21 (Antigravity): Switched to account with 860 credits. Flow project "HowZit - Jupiter crash" created. Reference images ref_01 through ref_10 downloaded.
- 2026-10-21 (Antigravity & Owner): All 7 keyframe pictures (K0, K1, K2, K3, K4, K5, K6) generated in Flow and saved to `images/K0.png` through `K6.png`. Contact sheet generated at `images/keyframes_contact_sheet.png`. 0 credits spent (image generation free). Pausing for owner approval before any video credit is spent.
- 2026-10-20 (Owner): Picked pitch #1, "NASA crashed its own spacecraft into Jupiter on purpose" (space, "oh that's genius").
- 2026-10-20 (Owner): Workflow:
  1. Claude researches, gathers reference pictures and writes the script.
  2. The owner reviews it and records the voice in ElevenLabs.
  3. Claude writes detailed prompts for Antigravity.
  4. Antigravity generates and downloads the Flow clips.
- 2026-10-21 (Claude Code):
  - Research done: 10 claims, 2 sources each, in `story.md`.
  - Script written in `script.yaml`: 12 scenes, 136 words, about 47–50 s with Mark's pace.
  - The script follows `docs/owner-creative-rules.md`:
    - the hook zooms in from a wide mission-control shot, with emotion by 3 s;
    - Easter egg: microbes on the foil in s02–s03, paid off in s08;
    - the "why" is held back until s08–s09;
    - climax in s10 and twist in s11 (Cassini);
    - loop in s12 back to s01@0.
- 2026-10-21 (Claude Code): Reference pictures listed in `images/REFERENCES.md` (NASA, public domain). Only ref 06 was downloaded, because Chrome blocked further automatic downloads. Antigravity should download the rest.

- 2026-10-21 (Owner): Voiceover recorded (ElevenLabs, Mark), `audio/voiceover.mp3`, 56.45 s. No cuts: the clips must flow as one continuous video, and retries must be avoided.
- 2026-10-21 (Claude Code): Flow prompt sheet written: `output/jupiter-crash_flow_prompts.md` (made by `make_prompts.py`).
  - 7 keyframe images K0–K6 first (Flow image model, free); the owner approves them before any video credit.
  - 7 Frames-to-Video clips C1–C7, each START = previous keyframe and END = next keyframe, so every seam is the same picture. C7 ends on K0 for the loop.
  - Budget 140 credits; at most one retry per clip (280 max, under the 300 cap).
- 2026-10-21 (Owner): Flow prompt sheet approved as written. Hand-off prompt for Antigravity: `ANTIGRAVITY_PROMPT.md`.
- 2026-10-21 (Claude Code) keyframe review:
  - K0, K1, K3, K4, K5 and K6 pass.
  - K2 must be fixed: the three germs are missing, although they are on K1, K4 and K5, so C2 would make them vanish. Fix with a free image edit of K2 (attach K1): add the same three germs in the same spot.
  - K2 also shows the same three-quarter front view as K1, not a view from behind. The probe is kept consistent this way, so the C2 and C3 prompts were changed to match K2 (`make_prompts.py` and the prompt sheet regenerated). Antigravity must copy C2 and C3 from the NEW sheet.
  - 2026-10-21 03:43 (Claude Code): K2 fixed in Flow (account with 860 credits, manual mode, 0 credits) and saved over `images/K2.png`. Flow's new UI: turn "Agent" off for manual generation; Agent settings now set to "Always confirm", video default Veo 3.1 Fast, 9:16, x1. Keyframes are uploaded to the Flow project as KEY_K0…KEY_K6 (use these names; the older "K1.png/K2.png" assets in the project are NASA reference uploads, not keyframes).
  - 2026-10-21 03:55 (Claude Code): C1 set up in Flow (Frames, Veo 3.1 Fast, 9:16, x1, KEY_K0 → KEY_K1, prompt verbatim) but Flow refused it twice: "We noticed some unusual activity… browser extensions that modify the page may cause issues" (bot check on automated generation). 0 credits charged (balance still 860). Next: the owner clicks Generate/↻ himself, or Antigravity generates the clips from Step 4.
  - 2026-10-21 03:56 (Owner): clicked ↻ on C1 himself; it generated (20 credits). The owner went to sleep and asked Claude Code to finish.
  - 2026-10-21 04:00 (Claude Code): C1 downloaded (new Flow UI downloads 720p directly) → `clips/c01.mp4`. PASS: wide room → she turns with an excited grin and presses the button → through the wall screen → lands on K1 (diff 1.5/255 at 7.75 s).
  - 2026-10-21 04:02 (Claude Code): C2 set up (KEY_K1 → fixed K2 "Editing probe image with…", prompt verbatim) but Flow refused Claude's Generate click again (bot check, 0 credits). The failed C2 tile in Flow keeps the right frames and prompt: the owner clicks its ↻. Claude Code will not keep submitting while Flow flags it.
  - 2026-10-21 04:10 (Claude Code): new `tools/join_continuous.py` joins c01–c07 into one take (`clips/visual.mp4`): finds where each clip lands on its end keyframe, drops the still tail, time-fits it to its 8.06 s window; missing clips become keyframe crossfades. script.yaml: every scene now uses `clips/visual.mp4` with `clip_start`/`clip_end` = its voice window. Draft animatic built: `output/jupiter-crash_howzit_draft.mp4` (56.5 s).
  - 2026-10-21 04:06 (Owner clicked ↻; Claude Code checked): C2 PASS → `clips/c02.mp4`. The dish flaps like a wind-flipped umbrella for ~2 s (1.0–3.5 s) then settles jammed, which fits "like a broken umbrella"; signal rings to a tiny Earth, thruster puffs, lands on K2 (diff 1.6). C3 filled in Flow (fixed K2 → KEY_K3); waiting for the owner's Generate click.
  - 2026-10-21 04:15–04:27 (owner clicks Generate, Claude Code fills the frames and prompts, downloads and checks):
    - C3 PASS with notes → `clips/c03.mp4`: flyby, cyan "lightning" field lines, dive through a crack into the ocean, lands on K3. Weak spots: for ~2 s Europa takes on Jupiter's banded colours, and a dark disc flickers at ~1.5–2 s. Candidate for a redo if credits allow.
    - C4 PASS → `clips/c04.mp4`: fast continuous pull-back (no hard cut, checked frame by frame), innocent probe ("why?"), glowing tank, sputtering puffs, lands on K4. The dish looks a little rounder mid-clip.
    - C5 PASS → `clips/c05.mp4`: germs wake, yawn, cheer; dotted path and a glowing red crack; lands on K5 with the dotted line (7.6 s).
    - C6 PASS → `clips/c06.mp4`: germs slide down the path and splash into the ocean, a friendly blue microbe greets them; engine flare; dive to Jupiter; the fiery glow pops in during the last 0.2 s and lands on K6.
    - C7 refused once by Flow: "might violate our policies about generating prominent people" (refunded). Prompt re-filled without the engineer's face description (`THE ENGINEER` block removed; "the room and the people look exactly as in the end frame").
    - Seams 1–5 measured in `clips/visual.mp4`: jump at each seam 0.2–0.7/255, the same as normal motion (invisible).
  - 2026-10-21 09:20 (Claude Code): C7 v1 (owner click after the refill) → `clips/c07.mp4`. FAIL on story: Saturn looks like Jupiter with a ring, the second probe fires at Enceladus and the moon bursts (reads as "they crashed into the moon"), and the engineer morphs into a different person at 6–7 s. Loop landing on K0 is good.
  - Full video v1 built with C1–C7 v1: `output/jupiter-crash_howzit.mp4` (56.5 s, luma 0.36, dark 0.39 (space-heavy), −15.1 LUFS); delivery copy (28 MB) in Downloads as "HowZit - NASA Crashed Its Own Spacecraft Into Jupiter (v1).mp4" and `output/jupiter-crash_howzit_v1.mp4`. Seams 1–5 invisible; seam 6 within the fast dive's own motion.
  - Owner asked Claude Code to redo the weak clips on its own. Claude's Generate click was flagged again ("unusual activity", 0 credits). Ready for the owner's click: C7 redo = ↻ on the failed top tile (prompt C7v2: pale-yellow Saturn, probe into Saturn far from Enceladus, gentle plumes, same people); C3 redo = Generate in the prompt box (prompt C3v2: Europa stays white with no bands, no dark disc, gentle field lines).
  - 2026-10-21 10:45 (owner clicked both redos; Claude Code checked): C3 v2 PASS (Europa stays white with red cracks, no bands, no dark disc; field lines still a little electric). C7 v2 PASS (pale-yellow ringed Saturn, second probe streaks into Saturn, Enceladus sprays untouched, pull-back into the room lands on K0). v1 clips kept in `clips/old/`.
  - FINAL built: `output/jupiter-crash_howzit.mp4` (56.5 s, luma 0.37, dark 0.39, −15.1 LUFS); delivery copy `output/HowZit - NASA Crashed Its Own Spacecraft Into Jupiter.mp4` (28 MB) + caption file in Downloads. Seams 1–5 invisible (0.2–0.5); seam 6 inside the fast fiery dive; loop end→start 4.2.
  - Music: none in assets/music. Plan: add a trending/licensed track in the Instagram/YouTube app when posting.
  - The small sparkle mark at the bottom-right of every keyframe stays (it isn't removed). It is in the same place on every frame.

## 2. Clip Progress & Verification Table

| Clip ID | Scene | Target Time (s) | Status | Notes |
|---|---|---|---|---|
| K0–K6 | keyframes | — | Approved | K2 fixed by Claude Code (germs added, free edit, Nano Banana 2.1); old one kept as `images/K2_v1_no_germs.png`. |
| C1 | K0→K1 | 0.00–8.06 | Approved (20 cr) | room → button → through the wall screen → probe at Jupiter |
| C2 | K1→K2 | 8.06–16.13 | Approved (20 cr) | jammed dish, beams to Earth, turn to Europa |
| C3 | K2→K3 | 16.13–24.19 | Approved v2 (40 cr total) | Europa flyby, field lines, dive into the ocean |
| C4 | K3→K4 | 24.19–32.26 | Approved (20 cr) | pull out, "why?", fuel drains, tumble |
| C5 | K4→K5 | 32.26–40.32 | Approved (20 cr) | germs wake up, dotted path to Europa |
| C6 | K5→K6 | 40.32–48.39 | Approved (20 cr) | what-if splash, dive into Jupiter |
| C7 | K6→K0 | 48.39–56.45 | Approved v2 (40 cr total) | Saturn, Enceladus plumes, back out into the room (loop) |

## 3. Current Blockers & Next Immediate Step
- **Owner:** post it (Instagram Reel Collab with Lowkey Genius + YouTube Short in the HowZit playlist) at 7 PM ET = 4:30 AM IST; copy in `output/jupiter-crash_post.md`. Add a licensed track in-app (no music in the file).
