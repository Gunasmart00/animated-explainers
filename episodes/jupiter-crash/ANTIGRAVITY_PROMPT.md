# Antigravity prompt: Jupiter crash, keyframes + Flow clips

Paste everything inside the box into Antigravity (repo `G:\Apps\animated-explainers` open, Chrome signed in to Google).

```
You are producing the Flow clips for the HowZit episode "NASA Crashed Its Own Spacecraft Into Jupiter"
(repo G:\Apps\animated-explainers, episode folder episodes\jupiter-crash).

READ FIRST, in this order:
1. ACTIVE_PRODUCTION.md and docs\ai-handoff-protocol.md (the 95% pause rule applies to you).
2. episodes\jupiter-crash\STATUS.md (decisions so far).
3. episodes\jupiter-crash\output\jupiter-crash_flow_prompts.md: THE ONLY SOURCE OF PROMPTS. Copy each prompt
   exactly as written, inside its ``` box. Do not shorten, reword, translate or "improve" it, and do not paste the
   "Narration over it" lines.
4. episodes\jupiter-crash\images\REFERENCES.md (reference pictures).

GOAL: one continuous 56 s video with no cuts. 7 keyframe pictures (K0-K6), then 7 Frames-to-Video clips (C1-C7).
Each clip STARTS on the keyframe before it and ENDS on the keyframe after it, so every clip ends on exactly the
picture the next clip starts on. C7 ends on K0 so the Reel loops.

HARD RULES (never break these):
- Never buy credits; ignore every "Add AI credits" / upgrade button.
- Never type a password; stop at any sign-in page or CAPTCHA and tell the owner.
- Never put a real person's or spacecraft's name in any prompt (no "Galileo", no "Cassini", no "NASA").
  The prompts already say "the probe" and "the second probe".
- Never use the Quality model (100 credits). Only Veo 3.1 Fast (20 credits per clip).
- Never remove the Flow watermark. Never post anything anywhere. Don't touch the AITOPIA extension.
- Budget: 140 credits planned. At most ONE retry per clip. Hard stop at 300 credits for this episode: ASK the owner
  before going past it.
- Keep a running credit count. Read the credit balance in Flow before you start and after every generation, and write
  it in STATUS.md every time.
- Generate ONE thing at a time. Never queue several clips.

STEP 1: Reference pictures (no credits)
Download refs 01-05 and 07-10 from images\REFERENCES.md (ref 06 is already in images\ as
ref_06_europa_interior_ocean.jpg). On each Wikimedia Commons file page, use Download → a 1600 px or original size.
Save them as images\ref_01_probe_model.png, ref_02_probe_at_jupiter.jpg, ref_03_probe_end.jpg, ref_04_jupiter.jpg,
ref_05_europa.jpg, ref_07_second_probe_saturn.jpg, ref_08_second_probe_dive.jpg, ref_09_enceladus_plumes.png,
ref_10_saturn.jpg. If Chrome blocks repeated downloads, allow downloads for commons.wikimedia.org /
upload.wikimedia.org when Chrome asks, or save them one per page visit.
IMPORTANT: ref 02 shows the dish antenna fully open. Ours must be JAMMED HALF-OPEN; the prompts say so. Never let a
keyframe copy the fully open dish.

STEP 2: Flow project
Open https://labs.google/fx/tools/flow . Create ONE new project named "HowZit - Jupiter crash". Everything for this
episode goes in this project.

STEP 3: Keyframes K0-K6 (Flow image model "Nano Banana", aspect 9:16, 1 output each)
Generate in this order, because K1 defines the probe and the others copy it:
  K1 → K0 → K2 → K3 → K4 → K5 → K6
For each one: paste its prompt from the prompt sheet and attach the images listed under "Attach as image references"
(the ref_NN files from images\, plus any keyframe listed there, e.g. K1, that you already made in this project).
After the FIRST image, check the credit balance. If image generation cost credits, STOP and ask the owner.
Check each keyframe before making the next:
- exactly one probe; its white umbrella dish is lopsided and HALF-OPEN (never a full round dish);
- no text, letters, numbers or logos anywhere (screens included);
- K0: wide room, the engineer at the front-centre console, Jupiter + tiny probe on the giant wall screen;
- K1/K2/K4/K5: the probe looks the same as in K1 (gold-and-black foil body, two side booms with dark cylinders,
  one long thin pole);
- K3: ice crust on top, big glowing blue ocean, no fish or creatures;
- K4/K5: exactly three tiny cute pale-green smiling germs on the foil, small;
- bright, colourful, soft stylised 3D (not photoreal, not dark, not big-headed cartoon);
- main subject in the middle, bottom quarter simple, top-right corner empty.
If a keyframe fails a check, regenerate it (images are free) until it passes. Download every approved keyframe
(full size) to episodes\jupiter-crash\images\K0.png ... K6.png.

>>> STOP HERE AND ASK THE OWNER. Show all 7 keyframes (one contact sheet is fine). Do not spend any video credit until
the owner says the keyframes are approved. Apply any change the owner asks for, then ask again.

STEP 4: Clips C1-C7 (only after the owner approves the keyframes)
Settings for every clip: Veo 3.1 Fast, Frames to Video, 8 s, aspect 9:16, 1 output per prompt, sound ON.
For clip Cn: START frame = the keyframe named "START" in its heading, END frame = the keyframe named "END"
(C1: K0→K1, C2: K1→K2, C3: K2→K3, C4: K3→K4, C5: K4→K5, C6: K5→K6, C7: K6→K0).
Pick the start and end frames from the keyframes in this Flow project (never a different or regenerated copy, so the
seams match pixel for pixel). Paste the clip's prompt exactly. Generate. Wait for it to finish.
Then, before making the next clip:
a) Download it: More (⋮) → Download → Upscaled 1080p (free). Save as episodes\jupiter-crash\clips\c01.mp4 ... c07.mp4.
   Chrome may ask to allow multiple downloads from labs.google: allow it.
b) Run:  .venv\Scripts\python.exe tools\clip_check.py episodes\jupiter-crash\clips\c0N.mp4 8
   and LOOK at the contact sheet it writes (c0N_check.jpg). Pass only if ALL are true:
   - it starts on the start keyframe and lands on the end keyframe in the last ~0.5 s;
   - no cut, flash or scene jump inside the clip; the camera moves smoothly;
   - the actions in the prompt's timeline happen roughly on time (each beat within ~1 s);
   - exactly one probe; the dish stays lopsided and half-open; no text or logos anywhere;
   - same art style and the same engineer look (C1, C7); germs cute and tiny (C2, C4-C6);
   - no warped faces or hands; the clip has sound and no speech or music.
c) For C2-C7, check the seam with the previous clip:
   .venv\Scripts\python.exe tools\loop_seam.py episodes\jupiter-crash\clips\c0(N-1).mp4 episodes\jupiter-crash\clips\c0N.mp4 --from 6.5
   Write the printed best match and clip_end in STATUS.md. A match under ~3 is invisible; above ~8, tell the owner.
   After C7 also run:  loop_seam.py clips\c07.mp4 clips\c01.mp4 --from 6.5  (the loop seam).
d) Update the clip row in STATUS.md (Approved / Needs retry, credits, notes) and the credit total.

If a clip FAILS: retry it ONCE. Before retrying, fix the prompt only where it went wrong, and write the change in
STATUS.md:
- it cut or jumped → add at the top: "One single continuous shot, no cuts, no transitions."
- it didn't land on the end frame → add: "In the final second the camera slows and settles exactly into the end frame."
- the dish opened fully → add: "The dish stays jammed half-open the whole time; it never opens."
- text appeared → add: "Absolutely no text, letters or numbers on any surface or screen."
- too much happens / rushed → remove the weakest beat of the timeline (say which) and give its time to the next beat.
If the retry ALSO fails, STOP and ask the owner (show both versions). Never do a third attempt on your own.

STEP 5: Hand back
When C1-C7 all pass (or when you stop for any reason, or reach ~95% of your limits):
- STATUS.md: phase "review", every clip row filled, each seam's clip_end, total credits, any prompt changes.
- ACTIVE_PRODUCTION.md: active episode jupiter-crash, phase review, Last Active AI: Antigravity (Gemini Pro),
  next step "Owner approves all clips; then Claude Code maps the clips onto script.yaml and builds the draft".
- Tell the owner: credits used, which clips were retried and why, and where the contact sheets are.
Do NOT build the video, do NOT edit script.yaml, and do NOT post anything. The owner approves all clips first.
```

## Short version (if Antigravity already has the repo open and reads files well)

```
Read ACTIVE_PRODUCTION.md, docs\ai-handoff-protocol.md and episodes\jupiter-crash\STATUS.md, then do exactly what
episodes\jupiter-crash\ANTIGRAVITY_PROMPT.md says, step by step. Stop and ask me after the keyframes.
```
