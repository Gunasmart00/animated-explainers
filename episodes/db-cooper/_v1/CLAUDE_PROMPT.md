# Claude Code prompt: make the D.B. Cooper Reel

Start it like this (PowerShell, Chrome open and signed in to your Google account, Claude in Chrome extension installed):
```
cd G:\Apps\animated-explainers
claude --chrome
```
Then paste everything in the box below.

```
You're in G:\Apps\animated-explainers, my HowZit 3D explainer project on Windows 11. Make the finished D.B. Cooper Reel and put it in my Downloads folder. Use Chrome for Gemini (I'm already signed in to Google there).

RULES
- Read CLAUDE.md, README.md, prompts\gemini.md, prompts\visuals.md, episodes\db-cooper\story.md and episodes\db-cooper\script.yaml first, and follow them.
- Don't change the narration, facts or pop-ups in script.yaml; every fact already has 2 sources. The video has no dates on purpose, opens on the mystery flap so viewers don't recognise the case, and only reveals the name D.B. Cooper in the last scene: keep it that way. Only touch script.yaml if a build warning forces it, and tell me.
- Voice is set: en-US-BrianMultilingualNeural at +10% in presets\explainer.yaml. Keep it.
- Never use OpusClip. Never post anything to Instagram. Never type passwords: if Google asks me to sign in or shows a CAPTCHA, stop and ask me.
- Ask me before downloading anything that isn't a Gemini picture or video for this episode.
- The hijacker must never show a clear face (from behind, in shadow, or turned away). No airline logos. No text, letters or numbers inside any picture.

STEPS
0. Resume, don't restart. The project is 3D (a short switch to 2D was cancelled). episodes\db-cooper\images\ already has good 3D pictures for s01, s02 and s03: keep them and don't regenerate them. If an episodes\db-cooper\_old_3d\ folder exists, move its pictures back into images\. Delete episodes\db-cooper\.cache\ and episodes\db-cooper\output\ (stale drafts; the build recreates them). In Gemini, reuse the chat that made s01-s03 if it's still open (its reference sheets keep the characters consistent); otherwise start a new chat and make the G4 reference sheets first.
1. Setup check. If .venv is missing, create it and install requirements.txt (use .venv\Scripts\python.exe for everything). If ffmpeg is missing, ask me, then run: winget install --id Gyan.FFmpeg -e
2. Draft. Run: .venv\Scripts\python.exe -m studio.build episodes\db-cooper --draft
   This checks the voice and timing and writes episodes\db-cooper\output\db-cooper_gemini_prompts.md with every picture prompt already filled in. Fix nothing yourself except setup problems; report any warning.
3. Music (required for this video). If episodes\db-cooper\audio\ has no music.* file: open https://pixabay.com/music/ in Chrome and search "suspense thriller", "mystery tension" and "cinematic heist". Shortlist 3 instrumental tracks that build tension (pulsing beat, no vocals, 1-3 min, no shield/Content ID icon). Tell me their titles, lengths and links, and download the one I pick only after I say yes. Save it as episodes\db-cooper\audio\music.mp3 (keep its real extension). The renderer loops it, fades it out at the end and dips it under the narrator automatically.
4. Reference sheets (G4). Skip this if you are continuing the chat that made s01-s03. Otherwise, in Chrome open https://gemini.google.com/app and start a New chat. Every picture must match the existing 3D pictures in style. If Gemini offers an image size or quality setting, pick the largest. Send the G4 block for each character from the prompts file (the hijacker, the flight attendant, the jet, the boy), one at a time. Wait for each picture, look at it, regenerate (at most twice) if it breaks a rule. Keep this chat open.
5. Scene pictures (G5), same chat. Change the first scene's line "Use the attached reference for ..." to "Use the reference sheets earlier in this chat for ...". Start at s04 (s01-s03 exist): if this is a new chat, send the full first-scene block with s04's visual line; otherwise send the short "Next frame" block for s04 to s11, in order. For each picture:
   - check it: same 3D style as s01-s03, vertical 9:16, no text or logos, hijacker's face hidden, matches the scene; regenerate at most twice if not;
   - download it at full size with Gemini's download button (not a screenshot);
   - move the newest file from %USERPROFILE%\Downloads to episodes\db-cooper\images\ and rename it to the scene id, keeping its extension (s01.png, s02.png …).
   If Gemini refuses a scene (for example the briefcase in s04), rewrite that one description more gently and honestly (for example "an open briefcase with tangled wires and red tubes, ominous lighting") and try once more; if it still refuses, tell me and continue.
6. Moving clips (G6), optional. For the scenes that have a veo: line (s03, s07, s09): in a new Gemini chat choose video generation (Veo), pick 1080p if offered, upload that scene's picture from episodes\db-cooper\images\, send its G6 block from the prompts file, wait for it, download it and save it as episodes\db-cooper\clips\<scene id>.mp4. If Gemini says the video limit is reached, skip the rest; still pictures with camera moves are fine.
7. Final render: .venv\Scripts\python.exe -m studio.build episodes\db-cooper
8. Check it. Use ffmpeg to grab frames at 1 s, 10 s, 25 s, 40 s and the last 2 s of episodes\db-cooper\output\db-cooper_howzit.mp4, and look at them: captions readable, no text inside pictures, watermark top-right, end card at the end, pictures sharp. If a picture is bad, regenerate just that scene in Gemini (steps 5/6) and render again.
9. Copy to my Downloads folder:
   - episodes\db-cooper\output\db-cooper_howzit.mp4 → %USERPROFILE%\Downloads\HowZit - DB Cooper.mp4
   - episodes\db-cooper\output\db-cooper_post.md → %USERPROFILE%\Downloads\HowZit - DB Cooper - caption.md
10. Report in a short table: what was made, which scenes are pictures vs clips, anything skipped or regenerated, the video length, and the caption + 5 hashtags from the posting note so I can paste them into Instagram.
```
