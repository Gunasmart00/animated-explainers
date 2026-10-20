# CLAUDE.md — animated-explainers

Renders **HowZit** 3D explainer Reels (Instagram `@howzit.explains`) from `episodes/<name>/script.yaml`.
Each Reel is posted on HowZit as an Instagram **Collab with the Lowkey Genius Instagram page**
(the clips page). A Lowkey Genius YouTube Short export exists but is optional (`--profile youtube`).
Sister repo: `G:\Apps\youtube_clipping` (github.com/Gunasmart00/lowkey-genius) — **its brand, rules and
knowledge base apply here**. Owner: Gunaseelan (India, IST, Windows 11, PowerShell, MX450 laptop);
prefers step-by-step instructions with exact values.

## Cross-AI Collaboration & The 95% Limit Rule (Claude Code <-> Antigravity / Gemini)
This project is worked on interchangeably by **Claude Code** and **Antigravity (Gemini Pro)**. Follow `docs/ai-handoff-protocol.md`.
1. **Always read `ACTIVE_PRODUCTION.md` and `episodes/<current>/STATUS.md`** at the start of any session to know current phase and decisions.
2. **The 95% Limit Rule:** When nearing 95% of your context window, rate limit, or weekly message quota:
   - **PAUSE** generation immediately. Do not leave broken downloads or half-finished renders.
   - **UPDATE** `episodes/<current>/STATUS.md` with all decisions, approved clips, and spent credits.
   - **UPDATE** `ACTIVE_PRODUCTION.md` with the immediate next step and the handoff prompt for Antigravity.
   - Notify the owner with the handoff prompt.
3. Master production bibles:
   - `docs/zack-style-bible.md` (3-part structure, hook <10 words, cutaway cross-sections, micro-pacing, no music, no whooshes, reel loop)
   - `docs/flow-ai-pitfalls-and-rules.md` (Prompt engineering defenses against AI video failure modes)
   - `docs/ai-handoff-protocol.md` (Full specification of multi-AI state tracking)

## Owner decisions (latest 2026-10-18; these override older notes and the brand guide for these videos)
- **Look, pacing and sound follow the owner's Zack D. Films reference Reels** (`docs/zack-style-analysis.md`):
  bright, cartoonish, stylised 3D (not dark, not photoreal), 30–45 s, a new shot every 1–3 s (or one continuous
  camera journey for demonstrations), fast continuous narration,
  dense sound effects, **no music** (allowed for design/engineering episodes), captions in Open Sans ExtraBold.
- **Scenes are made in Google Flow (Veo)** with sound effects; **narration in ElevenLabs** with the voice the owner
  selected there (never change it); fallback voice: built-in Brian (+14%) when there are no ElevenLabs credits.
- **Branding = the HowZit logo on screen.** No end card.
- **One cartoon style for every video** (owner, 2026-10-18): the cartoon 3D family-film look of the F-STYLE block in
  `prompts/flow.md`; recurring people and objects keep one fixed look (`characters:` and `objects:` in script.yaml).
  Story figures look like their famous image (e.g. D.B. Cooper: dark suit, black sunglasses, thin black tie).
- **Every clip is checked before the next one is made, and the owner approves all clips before the final build.**
- **Prompts are written from the narration timing** (what is on screen while each line is spoken) and every clip's
  opening and final frames are planned so clip-to-clip transitions are smooth.
- **Every Reel loops** (owner, 2026-10-18): the last clip ends on the video's own first frame (`end_frame: "s01@0"`),
  so it replays seamlessly on Instagram and YouTube Shorts and people watch it at least twice.
- **No whoosh on scene changes** (owner, 2026-10-18: it sounded odd). `sfx.cuts` stays off; clips keep their own Flow sound.
- **No basic mistakes, no wasted Flow credits** (owner, 2026-10-18): research and write the visual fact sheet, then
  engineer each prompt per "Before spending a single credit" in `prompts/flow.md` (absolute geometry, directions,
  `must:`/`never:`, neighbour frames). Check the prompt on paper before generating.
- **Real-world size ratios** (owner, 2026-10-18): people, animals, vehicles and objects keep their true relative sizes
  in every clip (no cat half the height of a man). Every character and object gets a researched `size:`; check it on
  every clip sheet.
- Never clone or imitate a real creator's voice.

## "Create New video: <topic or full story>"
The owner starts this from Claude Code in this folder (`claude --chrome`, inside Antigravity or a terminal) with
Chrome signed in to Google and ElevenLabs. Do every step yourself; stop only where marked **ASK**.
1. **Read** `docs/zack-style-analysis.md`, `prompts/scene-script.md`, `prompts/flow.md`, `prompts/elevenlabs.md`,
   `ideas/backlog.csv`.
2. **Research** with web search: every claim needs 2 reliable sources. If the owner gave a full story, still check
   its facts and say which ones don't hold up.
3. **Folder:** `.venv\Scripts\python.exe -m studio.new "<title>"`; put the research and sources in `story.md`;
   set the idea's status to `scripting` in `ideas/backlog.csv` (add it if missing).
4. **Script:** write `script.yaml` per `prompts/scene-script.md` (narration, very detailed `shot`, `camera`, `sfx`,
   characters, pop-ups, shared clips, caption, 5 hashtags, facts). Check the length with
   `python -m studio.flow episodes\<name> --offline` (30–45 s; up to 60 s only if the story needs it).
5. **ASK** once: show the narration (one line per scene) and a short shot list, with the cost (Flow clips × 20 credits,
   narration characters). Go on when the owner says yes; apply any changes first.
6. **Voice:** follow `prompts/elevenlabs.md` in Chrome → `audio/voiceover.mp3` + `voiceover:` line. No credits → skip
   it (built-in voice) and say so.
7. **Timing + prompts:** `python -m studio.flow episodes\<name>` → `output/<name>_flow_prompts.md` with each clip's
   length, mode and full prompt.
8. **Flow** in Chrome, per `prompts/flow.md`: one project; **one clip at a time**: generate it, download it, run
   `python tools\clip_check.py clips\<id>.mp4 <seconds>` and look at the sheet (right action inside the narration
   window, true real-world sizes, same cartoon style, same character look, right vehicle type, no text, smooth, opening/final frames
   connect to the neighbours). Fix the prompt and regenerate until it passes, then move to the next clip. Never put a
   real person's name in a Flow prompt. Keep a running credit count; **ASK** before going past 300 credits for one
   video or using Quality.
8b. **ASK:** show the owner every clip (the draft and a one-frame-per-scene sheet) and wait for approval of all
   clips before the final build. Download the approved clips as Upscaled 1080p.
9. **Draft:** `python -m studio.build episodes\<name> --draft`; grab frames (CLAUDE.md "Checking a render") and fix
   timing with `clip_start`, or regenerate a clip.
10. **Final:** `python -m studio.build episodes\<name>`, then `python tools\analyse_reference.py` on the result:
    brightness ≥ 0.35, dark pixels ≤ 0.2 (≤ 0.3 for space, night or underground episodes), loudness ≈ −14 LUFS.
11. **Deliver:** copy `output/<name>_howzit.mp4` to `%USERPROFILE%\Downloads\HowZit - <title>.mp4` and
    `output/<name>_post.md` to `...\HowZit - <title> - caption.md`; set the backlog status to `ready`. Report the
    length, credits used, anything regenerated or skipped, and paste the caption + 5 hashtags.
Never post to Instagram, never type passwords, stop at sign-in pages and CAPTCHAs, never buy credits.

## Hard rules (from youtube_clipping/CLAUDE.md)
1. **Brand colours only from `brand/tokens.json`.** Pop-up colours: white, ink, lime. Fonts: Open Sans (video), Bricolage Grotesque (logos).
2. **Lime for one thing per frame.** Text on lime is `ground`. `forest` is never text.
3. **No invented numbers.** Every claim in `facts:` with 2 reliable sources before posting; if unsure, say so.
4. **Licensed audio only**, licensed for the platform it's posted on.
5. **Disclose:** Flow scenes are AI-generated, so turn on Instagram's AI label. Never clone a real person's voice.
6. **No Ben 10 IP** (names, Omnitrix hourglass, characters).
7. Media (`episodes/*/output`, `.cache`, clips and audio files) is git-ignored. Never commit video or audio.
8. **Never use OpusClip** (the connector or the app) unless the owner asks for it in that conversation.
9. Instagram allows 5 hashtags per post; scripts carry exactly 5.

## Layout
- `studio/build.py` — `python -m studio.build <episode> [--draft] [--offline] [--only sNN] [--profile howzit|youtube]`.
  Scenes render once (voice → duration → clip fitted by trim / slight slow-down / hold, its Flow sound kept), then each
  export profile adds captions, pop-ups, logo, optional end card, pop track (no whoosh on scene changes: owner 2026-10-18), ducked clip sound and the −14 LUFS mix.
- `studio/flow.py` — `python -m studio.flow <episode> [--offline]`: times scenes to the voiceover and writes the Flow prompts.
- `tools/analyse_reference.py` — measures a video (brightness, darkness, saturation, shots, loudness, pace, sound effects).
- `studio/voice.py` — edge-tts with WordBoundary timings (cached by text+voice); per-scene recordings; one `voiceover:` file
  split across scenes by faster-whisper word timings matched to the script; `--offline`.
- `studio/voices.py` — writes `voice-tests/*.mp3` for candidate voices. `studio/audio.py` — music pick (auto) and the sfx track.
- `studio/media.py` also does the sub-pixel camera move (PIL affine, threaded, piped to ffmpeg) and optional Real-ESRGAN upscaling.
- `studio/captions.py` — one .ass per export: captions + lime word highlight, pop-ups, hook box, text watermark. Tracks lime use.
- `studio/media.py` — ffmpeg lookup (winget path too), zoompan moves, brand placeholder and end cards.
- `studio/post.py` — `output/<episode>_post.md` from `templates/descriptions/explainer.md` (youtube_clipping).
- `brand/brand.yaml` — export profiles (watermark, end card, close line), hook box, progress bar.
- `presets/*.yaml` — video size, voice, caption and pop-up styling.
- `prompts/gemini.md` — the exact Gemini prompts G0–G8 (G0 viral ideas, script, fact check, retention, reference sheet,
  scene pictures, Veo clips, caption, AI Studio voice). G0 comes from the owner's `prompts/viral-ideas-generator.md`.
- `ideas/backlog.csv` — video ideas: title, format (6 viral formats), status (idea → scripting → in-production → posted), episode, notes.
- `prompts/scene-script.md` — how to write a Flow-pipeline script. `prompts/flow.md` — Flow settings, style block, F0/F1 templates.
- `prompts/elevenlabs.md` — ElevenLabs steps, settings, licence. `docs/zack-style-analysis.md` — the reference analysis.
- `prompts/antigravity-analyse-zack.md` — prompt for Antigravity to analyse the other 4 reference videos.
- Older manual route (Gemini pictures, G0–G8 in `prompts/gemini.md`, the checklist) still works; G0 is still the idea generator.
- `docs/checklist/howzit-reel-checklist.html` — the step-by-step checklist, built by `tools/make_checklist.py` from `template.html` + gemini.md; published at https://claude.ai/artifact/YJ3HHR3zK3ZS1STaPKjcn8 (db doc `progress/current` holds the ticks; republish to the same URL).
- `tools/sync_brand.py` — re-copy brand files from youtube_clipping.

## When asked for ideas
1. Follow G0 in `prompts/gemini.md` (the 6 viral formats, 3–10 word titles, titles only unless asked).
2. Read `ideas/backlog.csv` first and don't repeat or closely copy anything in it.
3. Only ideas that are true and checkable; survival ideas show how people get out safely; no gore or self-harm.
4. Add the ones the owner likes to `ideas/backlog.csv` with status `idea` and the matching format.
5. When an episode folder is made for an idea, set its status to `scripting` and fill `episode`.

## When asked to write a script
1. Read `episodes/<name>/story.md`, `prompts/gemini.md` (G1–G3) and `prompts/script_writer.md`; write `script.yaml`
   (140–160 words; `structure: hook` or `reveal`; no close line).
2. Every `at_word` verbatim in its scene's narration; lime pop-up at most once.
3. Run `python -m studio.build episodes/<name> --draft --profile howzit`; fix any "pop-up word not found" or long-hook warnings.
4. Give the per-scene Gemini prompts (G4 reference sheets, G5 pictures, G6 clips) from `prompts/gemini.md`, filled in.
5. Add the topic to `youtube_clipping/templates/trackers/explainer-ideas.csv` status if the user wants it tracked there.

## Checking a render
Grab frames with ffmpeg at the hook (1 s), at each pop-up (`grep "Dialogue: 3" .cache/<draft|full>/captions_howzit.ass`)
and on the end card, and look at them: captions readable, nothing in the keep-clear zones
(top 220, right 120 px; bottom 420 px except the captions, which sit at y ≈ 1500 like the reference),
watermark and end card correct for the export.

## Conventions
Markdown, short sentences, kebab-case names, dates YYYY-MM-DD. Episode folders are kebab-case topic names.
Scene ids `s01`, `s02` …; pictures auto-match `images/<id>.*`, clips `clips/<id>.*`.
