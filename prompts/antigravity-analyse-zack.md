# Prompt for Antigravity: analyse the other four reference videos

Open `G:\Apps\animated-explainers` in Antigravity and paste everything in the box into the agent.

```
You're in G:\Apps\animated-explainers, the HowZit 3D explainer project. Read CLAUDE.md, docs\zack-style-analysis.md, prompts\flow.md and tools\analyse_reference.py first.

GOAL
Claude analysed 4 of the 8 reference Reels in "C:\Users\E GUNASELAN\Downloads\zack samples" (Part 1 of docs\zack-style-analysis.md). Analyse the other 4 the same way, add Part 2, and suggest precise improvements to our Google Flow style and scene rules so our videos match the reference look, motion and sound more closely.

VIDEOS TO ANALYSE (only these four)
- downloadmedia-20261018 (3).mp4
- downloadmedia-20261018 (4).mp4
- downloadmedia-20261018 (5).mp4
- downloadmedia-20261018 (6).mp4

STEPS
1. Setup: use .venv\Scripts\python.exe (create it and install requirements.txt if it's missing). ffmpeg must work.
2. Measure: run
   .venv\Scripts\python.exe tools\analyse_reference.py "C:\Users\E GUNASELAN\Downloads\zack samples\downloadmedia-20261018 (3).mp4" "C:\Users\E GUNASELAN\Downloads\zack samples\downloadmedia-20261018 (4).mp4" "C:\Users\E GUNASELAN\Downloads\zack samples\downloadmedia-20261018 (5).mp4" "C:\Users\E GUNASELAN\Downloads\zack samples\downloadmedia-20261018 (6).mp4"
   Keep the printed table. Open every contact sheet and spectrogram it writes in docs\reference-analysis\.
3. Watch each video in full (with sound) and note, per video:
   - the story in one line, and the first and last narration lines (write the narration out so we can study the script structure; it stays in this private repo, never published);
   - how many shots, and which camera moves (push-in, orbit, POV hands, top-down, cutaway/x-ray, whip-pan) appear most;
   - character look (proportions, skin, eyes, clothes), environments, lighting, colour palette;
   - graphics added in the scene (numbers, icons, thought bubbles, phone screens, glowing outlines) and when they appear;
   - every kind of sound effect you hear and when; whether there is any music;
   - how the narration paces itself (speed, pauses, emphasis) and how the video ends.
4. Write "## Part 2 — four more videos (Antigravity, <today's date>)" in docs\zack-style-analysis.md, replacing the placeholder text there, with the same table columns and the same headings as Part 1 (Look, Camera and editing, Story and narration, Captions, Sound). Then add "### Differences from Part 1" and "### Combined rules (all 8 videos)" with the final numbers (ranges across all 8).
5. Suggest improvements, don't apply them yet: add a section "### Suggested changes" with exact new wording for
   - the F-STYLE block in prompts\flow.md,
   - the rules list at the end of prompts\flow.md,
   - any setting in presets\explainer.yaml (caption position, sfx volumes, pacing).
   Explain each suggestion in one line with the evidence (which video, what time).
6. Delete docs\reference-analysis\ afterwards (contact sheets are only for you), and don't copy any video into the repo.

RULES
- Never upload these videos anywhere or post them; they are private study material.
- Don't touch episodes\, studio\ or brand\.
- Finish with a short summary of the biggest 5 differences between our current rules and what you found.
```

When it's done, tell Claude in the main chat: "Antigravity finished the analysis, apply the suggested changes."
Claude then reviews Part 2, updates `prompts/flow.md` and the preset, and re-renders a test.
