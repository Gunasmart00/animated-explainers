# Gemini prompts (copy, paste, fill the [BRACKETS])

Use these in the Gemini app (Gemini Pro). Start a **new chat for each episode**, and keep the image
prompts for one episode in **one chat** so the characters stay the same.
The interactive checklist has the same prompts with copy buttons, and every render writes
`output/<episode>_gemini_prompts.md` with G4–G6 already filled in for that episode's scenes.

---

## G0 — Viral idea generator (text)
Based on the owner's prompt `prompts/viral-ideas-generator.md` (added 2026-10-18), with HowZit rules added.
Use a new Gemini chat. Paste the titles from `ideas\backlog.csv` into the last HowZit rule so ideas don't repeat.
```
You are a viral short-video idea generator specialised in high-retention storytelling in the style of Zack D Films. Your goal is to generate ideas that follow formats PROVEN to go viral on real high-performing videos.

TASK
Generate 10 HIGHLY VIRAL titles for 45–60 second Instagram Reels and YouTube Shorts for HowZit, a page of 3D animated explainers for a US audience.

CORE VIRAL RULES (VERY IMPORTANT)
Each idea MUST follow at least ONE of these proven formats:
1. How something works. Example: How Gas Pumps Know When To Stop
2. What happens if / inside. Example: What Happens If You Swallow A Tooth
3. Dangerous or survival scenario. Example: Stuck In A Water Slide
4. Weird or disturbing concept. Example: Island Of Toenail Clippings
5. Body / medical curiosity. Example: Blown Veins Explained
6. Unknown truth or hidden function. Example: Why Soda Tabs Have That Hole

IDEA CHARACTERISTICS
- Must be instantly understandable in under 1 second
- Must create immediate curiosity
- Must feel slightly shocking, weird, or dangerous
- Must be VERY visual (easy to imagine scenes)
- Must feel like "I need to know this"

CONTENT FOCUS
- Human body reactions
- Dangerous environments
- Survival situations
- Hidden mechanisms
- Weird facts
- Rare or unknown scenarios

HOWZIT RULES
- Every idea must be true and explainable in 45–60 seconds with facts that can be checked on reliable sources. No myths presented as fact, no made-up events.
- Survival ideas show what really happens or how people get out safely; never how to hurt someone or do something dangerous.
- No gore and nothing about self-harm.
- Don't repeat or closely copy these ideas we already have: [PASTE THE TITLES FROM ideas\backlog.csv, or write "none"]

DO NOT
- Write generic ideas
- Write long titles
- Explain anything
- Use boring topics
- Repeat similar ideas

STYLE
- Short (3–10 words ideally)
- Clean and punchy
- Natural language
- Slight curiosity tone
- Occasionally use parentheses like (explained) or (what happens?)

OUTPUT FORMAT (STRICT)
1. Title
2. Title
3. Title
4. Title
5. Title
6. Title
7. Title
8. Title
9. Title
10. Title

Generate ONLY the titles. NO explanations.
```
Then pick the title that makes you most want to tap. Paste that title (plus anything you know about it) as MY STORY in G1.

## G1 — Story → script (text)
```
You are the script writer for HowZit, an Instagram page of 45–60 second 3D animated explainers for a US audience: how things work, how things are made, how inventions happened, true stories behind everyday things.

Turn MY STORY (at the end) into a Reel script in YAML, exactly in the FORMAT below.

CHOOSE THE STRUCTURE
- "hook": the topic has a surprising fact or a question people already ask. Scene 1 = that question plus the most surprising fact, inside the first 3 seconds.
- "reveal": the story has a twist, a mystery or a surprising ending. Scene 1 teases the ending without giving it away. Keep the answer hidden. Every 2–3 scenes add an open loop (for example "but that wasn't the strangest part"). The last scene is the reveal.
Write the one you chose in `structure:`.

RULES
- 140–160 words of narration in total, 7–10 scenes, each narration 8–20 words and one idea.
- Simple spoken English, short sentences, contractions are fine. Write numbers the way they are said.
- If MY STORY is only a title or a short idea, first use Google Search to research it, and build the story only from what reliable sources say.
- Scene 1 must stop the scroll in under 3 seconds. No "Hi", no "Today we will learn".
- Don't answer the hook before the last third of the video.
- Last scene: the payoff or reveal, a line people want to repeat or share. Do NOT write "follow" or "subscribe"; the video adds that.
- `hook`: 3–7 words shown in a box on screen for the first 3 seconds (a question or a teaser).
- `popups`: add one when a number or key word matters. `at_word` must be copied EXACTLY from that scene's narration, same spelling and punctuation. Colours: white (default), ink or lime. Use lime only once in the whole video: the most surprising number or the reveal.
- `visual`: one clear 3D shot: who or what, doing what, where, and the camera angle (close-up, wide, low angle, top-down). Never text, letters or numbers in the picture. Describe characters the same way every time, using the names from `characters`.
- `motion`: zoom_in, zoom_out, pan_left, pan_right, pan_up, pan_down or none.
- `veo`: on the 2–3 scenes that most need real movement only, one line saying what moves in an 8-second clip (for example "the chocolate bar slowly melts and drips"). Leave it out on the other scenes.
- `characters`: every recurring person, animal or object with a fixed look (age, build, hair, clothes, colours). For real historical people describe a generic look only (for example "a 1940s engineer in a white shirt and tie"), never a real person's face.
- `facts`: every factual claim in the script. Only list a source URL if you are sure it exists; otherwise leave `sources` empty. Never invent numbers.
- `caption`: Instagram caption, max 120 words. Line 1 = the hook (it shows before "more"). Then 2–3 short lines using the words people search for this topic. Then "Follow @howzit.explains for how things work in 60 seconds." Then one question that invites comments. No hashtags in the caption.
- `hashtags`: exactly 5, without the # sign: 1 broad (like howitworks), 2 about the topic, 1 niche, 1 community. Never reels, viral, explore or fyp.
- `cover_text`: 2–4 words. `alt_text`: one sentence describing the video.

FORMAT (return only this YAML, in one code block)
title: "..."
preset: explainer
structure: hook
hook: "..."
caption: |
  ...
hashtags: [howitworks, ..., ..., ..., ...]
cover_text: "..."
alt_text: "..."
characters:
  - name: "..."
    look: "..."
facts:
  - claim: "..."
    sources: []
scenes:
  - id: s01
    narration: "..."
    visual: "..."
    motion: zoom_in
    veo: "..."
    popups:
      - text: "..."
        at_word: "..."
        color: white

MY STORY:
[PASTE YOUR STORY HERE]
```

## G2 — Fact check (text, uses Google Search)
```
Use Google Search. Fact-check every claim in `facts` and every number and name in the narration of this script.

For each claim give: ✅ correct, ⚠️ partly correct or ❌ wrong; the corrected wording if needed; and 2 reliable sources with their URLs (official sites, encyclopedias, universities, textbooks, major news or science sites; no forums, no AI content sites).

Then return the full YAML again in one code block with the narration corrected and the source URLs filled into `facts`. Keep every `at_word` matching its narration exactly.

[PASTE script.yaml]
```

## G3 — Retention check (text, optional but recommended)
```
You are a short-form video editor. Read this Reel script as someone scrolling Instagram.
1. Score the first 3 seconds out of 10 for stopping the scroll, and say why.
2. Mark every line where a viewer might swipe away, and rewrite it shorter or more curious.
3. If `structure` is "reveal": check the answer stays hidden until the last scene and there is an open loop every 2–3 scenes.
4. Keep 140–160 words in total and keep every `at_word` matching its narration.
Give your notes first, then the improved YAML in one code block.

[PASTE script.yaml]
```

## 3D style block (used in G4–G5)
Matches the owner's reference Reel: polished, semi-realistic 3D (decided 2026-10-17, confirmed 2026-10-18).
```
High-end 3D animated render with the look of a polished 3D explainer short: semi-realistic 3D characters with natural skin, expressive faces and detailed clothing; clean, modern, well-lit spaces with soft pastel blue-grey walls and simple props; soft global illumination, gentle shadows and warm accent lights; shallow depth of field with a softly blurred background; crisp, sharp, highly detailed, rendered like Unreal Engine 5. Not a photograph and not a cartoon. Highest quality, sharp focus, no blur on the main subject.
```
If Gemini lets you pick an image size or quality, always pick the largest (2K or 4K when offered).

## G4 — Character or object reference sheet (image)
One per recurring character or key object, at the start of the image chat.
```
Create a reference sheet for a 3D animated explainer, vertical 9:16.
Subject: [PASTE the `look` line from characters, e.g. "a 1940s engineer, mid-30s, slim, short dark hair, white shirt, grey tie, rolled sleeves"]
Show: front view, three-quarter view, side view, and one close-up detail (the face, for a character), neutral pose, on a plain dark-green background (#13261A).
Style: [PASTE 3D STYLE BLOCK]
No text, letters, numbers, logos or watermarks.
```

## G5 — Scene picture (image), one per scene
First scene in the chat:
```
Use the attached reference for [CHARACTER NAME]: keep exactly the same look, shape, clothes and colours.
Create one frame of a 3D animated explainer, vertical 9:16 (1080x1920).
Scene: [PASTE the scene's `visual` line]
Composition: the main subject in the middle of the frame, between 20% and 62% of the height. Keep the area around 70% of the height calm, because captions go there, and put nothing important at the right edge or the bottom 20%.
Style: [PASTE 3D STYLE BLOCK]
No text, letters, numbers, logos or watermarks anywhere in the image.
```
Every next scene, same chat:
```
Same characters, same style, same composition rules. Next frame, vertical 9:16: [PASTE the next scene's `visual` line]. No text in the image.
```
Download each picture at full size (the download button, not a screenshot) and save it as `images\s01.png`,
`images\s02.png` … (the scene id). Reject any picture with text, letters, extra fingers or a blurry subject and regenerate.

## G6 — Moving clip (video, Veo), for 2–3 key scenes only
Gemini Pro has a daily limit on video generations, so use them on the moments that matter.
```
Animate the attached image into an 8-second vertical 9:16 video.
Motion: [WHAT MOVES, e.g. "the chocolate bar slowly melts and drips; the engineer looks down in surprise"].
Camera: [slow push-in / slow orbit / static].
Keep the characters, colours and 3D style exactly the same as the image. No text, no subtitles, no music, no talking, no new characters.
```
Pick 1080p if Gemini offers a resolution. Save as `clips\s03.mp4` (the scene id). Its sound is dropped; the narration is used.

## G7 — Caption and hashtags refresh (text, uses Google Search, optional)
Use when you want fresher wording than the caption in script.yaml.
```
Use Google Search to see how people currently talk about and search for this topic on Instagram: [TOPIC].
Write the Instagram caption for my HowZit Reel (script below):
- Line 1: the hook, max 10 words, makes people tap "more".
- 2–3 short lines that use the words people actually search for this topic.
- "Follow @howzit.explains for how things work in 60 seconds."
- One question that gets comments.
- Then exactly 5 hashtags (Instagram allows 5): 1 broad, 2 topic, 1 niche, 1 community. No #reels #viral #explore #fyp.
Also give: cover text (2–4 words), alt text (1 sentence), and 3 other first lines I could test.

[PASTE script.yaml]
```

## G8 — Narrator voice in Google AI Studio (free, optional, best-sounding)
The project's built-in voices are free Microsoft voices. For a more natural, expressive read, generate the
narration in Google AI Studio (aistudio.google.com → speech generation, single speaker; free tier, limits apply).
Try the voices **Puck** or **Fenrir** first. Paste this, then the full narration (the build writes it, ready to
paste, at the end of `output\<episode>_gemini_prompts.md`):
```
Read this as a young American male storyteller for a 60-second animated explainer: quick, energetic, curious and a little playful, like telling a friend a surprising story. Natural short pauses between sentences, a little extra emphasis on numbers and surprising words. Read every word exactly as written; don't add or change anything.
```
Download the WAV, save it as `audio\voiceover.wav` in the episode folder, and add `voiceover: audio\voiceover.wav`
to script.yaml. The build then times every caption to that recording (needs `pip install faster-whisper`).
Don't ask it to imitate a real creator's voice.

## Kids story variant (G1)
Replace the first paragraph of G1 with: "You are the script writer for short animated kids' stories and rhymes for ages 3–7." and add these rules: "Use `preset: kids`. Very simple words, repetition and sound words. Rhymes keep their rhythm, one couplet per scene. A gentle moral at the end. Nothing scary. No `hook` box."
