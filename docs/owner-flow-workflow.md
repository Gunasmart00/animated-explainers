# Owner workflow: you run Flow, Claude does the rest (2026-10-21)

Why: every browser click Claude makes costs a full model turn (it re-reads the whole conversation), and Flow blocks
Claude's Generate clicks anyway. Scripts (prompts, checks, join, build) are cheap for Claude, so Claude keeps those.

## Token savers
- **New Claude session per episode.** Paste: `Read ACTIVE_PRODUCTION.md and episodes\<name>\STATUS.md, then <task>.`
- **One message per stage**, not per clip. Don't ask Claude to wait or watch Flow.

## The episode, step by step
| # | Who | What |
|---|---|---|
| 1 | You | Pitch or pick an idea. |
| 2 | Claude | Research + narration in `episodes\<name>\story.md`. |
| 3 | You | Review, record the narration in ElevenLabs (Mark), save as `episodes\<name>\audio\voiceover.mp3`. Message: **"voice in"**. |
| 4 | Claude | Times it, writes `script.yaml` and `output\<name>_flow_prompts.md` (keyframe prompts K0–Kn + clip prompts C1–Cn). |
| 5 | You | Flow: keyframes, then clips (below). |
| 6 | You | Put the files in the repo with the exact names (below). Message: **"clips in"**. |
| 7 | Claude | Checks every clip (contact sheets + seam check), tells you which (if any) to redo with a fixed prompt, then joins and builds the final, and writes the post copy. |
| 8 | You | Post. |

## Flow (step 5)
**Settings:** turn **Agent off** (click "Agent" in the prompt bar). Model chip → **Video → Frames → 9:16 → Veo 3.1 - Fast → x1** (20 credits). For keyframes: **Image → 9:16 → Nano Banana → x1** (0 credits).

**Keyframes (free):**
1. For each K in the prompt sheet (in the order it says): paste its prompt, attach the listed reference pictures with **+**, generate.
2. Download each (download icon on the tile). Save as `episodes\<name>\images\K0.png`, `K1.png`, ... (Flow downloads .jpg/.png; the name must be exactly `K<n>.png`; a .jpg can be renamed .png, the tools read either).
3. Message Claude **"keyframes in"** if you want a check before spending credits (recommended, ~1 step for Claude).

**Clips (20 credits each):**
1. Click **Start** → search the keyframe → **Add to prompt**. Click **End** → search the next keyframe → **Add to prompt**.
2. Paste the clip's prompt from the sheet (everything inside its box). Click **→**.
3. You can set up the next clip while one renders. Max one retry per clip on your own; ask Claude before more.
4. Download each finished clip and save it as `episodes\<name>\clips\c01.mp4`, `c02.mp4`, ... (C1 → `c01.mp4`).
   If Flow says "prominent people" (false alarm, refunded), delete the character's face description from the prompt and retry.

## File names (step 6)
| What | Where | Name |
|---|---|---|
| Voice | `episodes\<name>\audio\` | `voiceover.mp3` |
| Keyframes | `episodes\<name>\images\` | `K0.png` … `K<n>.png` |
| Clips | `episodes\<name>\clips\` | `c01.mp4` … `c0<n>.mp4` |

Optional shortcut instead of renaming by hand (copies the newest N videos from Downloads, oldest first, as c01…):
`.venv\Scripts\python.exe tools\ingest_clips.py episodes\<name> 6 --dry-run` (check the list), then without `--dry-run`.
Download the clips **in order** (C1 first) for this to work.

## Commands Claude runs at step 7 (you can run them too)
- `python tools\clip_check.py episodes\<name>\clips\c01.mp4 8` → contact sheet next to the clip
- `python tools\join_continuous.py episodes\<name> --total <voice seconds>` → `clips\visual.mp4`, prints each seam
- `python -m studio.build episodes\<name> --profile howzit` → `output\<name>_howzit.mp4`
