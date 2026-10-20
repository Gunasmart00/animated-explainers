# Generate Animated Explanations (HowZit)

Turns a story into a 45–60 second **3D animated explainer Reel** for HowZit
(Instagram `@howzit.explains`), posted as a **Collab with the Lowkey Genius Instagram page**.

**Step-by-step checklist with every Gemini prompt:** `docs/checklist/howzit-reel-checklist.html`
(published: https://claude.ai/artifact/YJ3HHR3zK3ZS1STaPKjcn8 — ticks are saved). Rebuild after editing prompts: `python tools/make_checklist.py`, then republish to the same link.

## How a video is made now (2026-10-18)
In Claude Code in this folder (`claude --chrome`, Chrome signed in to Google and ElevenLabs) say:

> **Create New video: <topic, or paste the full story>**

Claude researches it (2 sources per fact), writes the scene-by-scene narration and very detailed Flow prompts
(`prompts/scene-script.md`), asks you once to approve the script and the credit cost, then:
1. **ElevenLabs** makes the narration with the voice you selected there (`prompts/elevenlabs.md`); no credits → the
   free built-in voice (Brian).
2. `python -m studio.flow` times every scene to the narration and fills the Flow prompts.
3. **Google Flow (Veo 3.1 Fast)** makes each scene as a short 9:16 clip with its own sound effects (`prompts/flow.md`),
   about 20 credits a clip, 7–12 clips a video.
4. `python -m studio.build` fits the clips to the voice, adds captions, pop-ups (with a pop sound), the HowZit logo, and mixes
   to −14 LUFS. No music unless the episode asks for it.
5. The video and its caption + 5 hashtags land in your **Downloads**. You post it on HowZit (Collab with Lowkey Genius).

The look, pacing and sound are measured from your Zack reference Reels: `docs/zack-style-analysis.md`.
To analyse the other four reference videos, give Antigravity `prompts/antigravity-analyse-zack.md`.

| Tool | Cost | Job |
|---|---|---|
| Claude Code + Chrome | your plan | Research, script, runs ElevenLabs and Flow in your browser, builds and checks the video |
| ElevenLabs | your plan | Narration (free plan: non-commercial, must credit elevenlabs.io) |
| Google Flow (Veo 3.1) | Google AI Pro: 1,000 credits/month | Scene clips with sound effects |
| This project (`studio/`) | free | Timing, captions, pop-ups, logo, sound mix, posting copy |
| edge-tts (Brian) | free | Fallback narrator |
| Gemini | your plan | Older still-picture route and the G0 idea generator |
| OpusClip | — | Not used unless you ask |

## Folders
```
brand/      tokens.json, brand guide, HowZit + Lowkey Genius logos, watermarks, fonts (Open Sans, Bricolage), brand.yaml
assets/     sfx\ (whoosh, pop, ding — made by tools\make_sfx.py), music\ (your royalty-free tracks)
presets/    explainer.yaml (default), kids.yaml: video size, voice, caption and pop-up style
prompts/    scene-script.md, flow.md, elevenlabs.md, antigravity-analyse-zack.md, gemini.md (G0 ideas + older route)
ideas/      backlog.csv: every video idea and its status
episodes/   one folder per video: story.md, script.yaml, images/, clips/, audio/, output/
studio/     the renderer (build, new, voice, captions, media, post, config)
tools/      sync_brand.py, make_checklist.py
docs/       zack-style-analysis.md, checklist (older manual route)
```

## Setup (once)
Double-click **`setup.bat`**: it installs ffmpeg and the Python packages, makes the voice samples and a test render.
`voices.bat` remakes the voice samples any time. Or do it by hand in PowerShell:
```powershell
cd G:\Apps\animated-explainers
winget install Gyan.FFmpeg
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
git init; git add .; git commit -m "Start HowZit animated explainers"
```

## One video by hand (what Claude runs for you)
```powershell
.venv\Scripts\Activate.ps1
python -m studio.new "Why pen caps have a hole"
# write script.yaml (prompts\scene-script.md), then check the length:
python -m studio.flow episodes\why-pen-caps-have-a-hole --offline
# ElevenLabs → episodes\...\audio\voiceover.mp3 and add  voiceover: audio/voiceover.mp3
python -m studio.flow episodes\why-pen-caps-have-a-hole        # timings + Flow prompts in output\
# Flow clips → episodes\...\clips\s01.mp4, s02.mp4 ...
python -m studio.build episodes\why-pen-caps-have-a-hole --draft
python -m studio.build episodes\why-pen-caps-have-a-hole
```
Results in `episodes\<name>\output\`: `<name>_howzit.mp4`, `.srt`, `<name>_post.md` (caption, 5 hashtags, Collab steps,
fact table). Flags: `--draft` half size · `--only s03` one scene · `--offline` no voice · `--profile youtube`.

## Hook or reveal
- `structure: hook` — scene 1 asks the question with the surprising fact; the lime hook box shows it for 3 s.
- `structure: reveal` — scene 1 teases the ending, open loops every 2–3 scenes, the answer only in the last
  scene (use the one lime pop-up for the reveal). The hook box shows the teaser.

## Brand rules the renderer applies
Colours only from `brand\tokens.json` (pop-ups: white, ink, lime; glow is lime) · HowZit watermark 110 px at
x 834 y 236 · no end card on HowZit · captions centred at y ≈ 1500 (78% of the height, like the reference);
2-line captions grow upward · the brand's lime hook box and lime word highlight are available but off.

## Voice
ElevenLabs with the voice you selected there (`prompts/elevenlabs.md`). Without credits the build uses the free
built-in voice `en-US-BrianMultilingualNeural` at +10% (`presets\explainer.yaml`; compare others with
`python -m studio.voices`). A recording of your own voice works the same way as `voiceover:`.

## Music and sound effects
Sound effects come from each Flow clip (Veo makes them from the prompt's `Sound:` line), plus a pop on pop-ups and a deep impact under the lime reveal. No added whoosh on scene changes (the owner turned it
off on 2026-10-18). **No music by default**, like the reference Reels. For design or engineering episodes add
`overrides: { music: { file: auto } }` and put a royalty-free track in `assets\music\` (Pixabay Music, no shield icon).

## Quality
Final renders are 1080×1920, 30 fps, H.264 High at CRF 16 (visually lossless), AAC 320 kbps. Flow clips are
downloaded as Upscaled 1080p; still pictures get sub-pixel camera moves so nothing steps or wobbles. `--draft` is deliberately half size and fast: use it
only to check timing. Sharpness depends mostly on the pictures: ask Gemini for its largest size, and install
Real-ESRGAN for small pictures.

## Kids stories
`preset: kids` and the kids variant of G1. Kids videos likely need their own page and "made for kids" handling.
