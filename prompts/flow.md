# Google Flow prompts (Veo video scenes)

Flow: https://labs.google/fx/tools/flow · signed in with the owner's Google account (Google AI Pro).
Look and pacing come from `docs/zack-style-analysis.md` (the owner's Zack D. Films reference Reels).
`python -m studio.flow episodes\<name>` fills these templates for every scene, timed to the narration,
in `output\<name>_flow_prompts.md`. The blocks below are the source; keep their headings.

## Settings in Flow (every project)
- New project per episode, named after the episode folder.
- Aspect ratio **Portrait 9:16**. If only landscape is offered, use 16:9 and keep the subject in the centre third
  (the build crops the middle).
- Model **Veo 3.1 Fast** (20 credits a clip on Google AI Pro, 1,000 credits a month). Use **Quality** (100 credits)
  only for one hero shot, and only after asking the owner.
- Clip length: the one `studio.flow` prints for the scene (4, 6 or 8 s).
- Sound **on** (don't tick "return silent videos"): Veo makes the scene's sound effects.
- Outputs per prompt: 2 when credits allow, then keep the better one.
- Download: More → Download → **Upscaled 1080p** (free on Pro). Never a screen recording.
- Flow may add a small visible Veo watermark in India. Leave it; never crop or blur it out.

## Generate one clip at a time, and check it (owner rule, 2026-10-18)
1. Generate **one** clip. Download it (720p is enough to check), then look at frames every 0.5 s across the part the
   scene uses (`python tools/clip_check.py clips\sNN.mp4 <seconds>` makes the sheet) and listen to its sound.
2. Check: right subject and action in the first seconds; cartoon style matching the other clips; the same character
   look (D.B. Cooper-type figures: dark suit, black sunglasses); vehicles are the right type (an airliner is an
   airliner, never a fighter or private jet); no text; no warped hands or faces; smooth motion; the opening frame
   follows on from the previous clip and the final frame leads into the next.
3. If anything fails, rewrite the prompt to fix exactly that, and regenerate. Only then move to the next clip.
4. When all clips pass, show the owner the review reel (`python tools/clip_review.py episodes\<name>`) and **wait for
   approval** before building.

## Before spending a single credit: research → visual facts → engineered prompt (owner rule, 2026-10-18)
Flow credits are limited. A clip that shows the wrong thing is wasted money, so basic mistakes must be caught on paper.
The D.B. Cooper video wasted about 300 credits on avoidable errors: fighter jets for an airliner, passengers leaving
through the nose, the jump stairs on the side of the plane, stairs that went up instead of down, and engines under
the wings of a 727. Each rule below exists because of one of these.
1. **Visual fact sheet first** (`story.md` → "Visual facts for the animation"). For every real vehicle, place, object
   and action: the exact type and model, where each part physically is (engines, doors, stairs, hatches), which way
   things move (up/down, forward/back, toward or away from the camera), time of day, weather, and what people wore.
   Find **a real photo of each** (web image search) and describe what it shows, in words, in the fact sheet.
2. **Write geometry in absolute, physical words.** Not "the rear stairs" but "a stairway that folds down out of the
   BELLY of the plane directly under the tail, on the centre line between the rear engines, sloping down and backwards
   to its lower end". Name the viewpoint ("seen from behind and below") and every direction ("walks DOWN the steps
   toward the camera").
3. **`must:` and `never:` on every scene.** `must:` = the facts that make the shot true. `never:` = the wrong versions a
   video model will draw by default (see the list below). `studio.flow` adds both to the prompt.
4. **Use an approved neighbour's frame when it already shows the right thing** (`start_frame: "s08@4.04"` or
   `end_frame: "s01@0"` in script.yaml → Frames to Video). It locks the geometry, the look and the cut in one go, and
   is far more reliable than words. `studio.flow` prints the ffmpeg line that cuts the frame.
5. **Loop every Reel** (owner, 2026-10-18): the last scene has `end_frame: "<first clip>@0"` and
   `clip_start: 8 − its seconds`, so the video ends on its own first frame and replays without a visible seam (people
   watch twice). Write the last narration line so it runs naturally into the first.
   Veo lands on the end frame about 0.3 s before the clip ends, then drifts. Always run
   `python tools/loop_seam.py clips/sNN.mp4 clips/s01.mp4` and cut there with `clip_end` (stop-drinking-water: frame
   7.67 s matched s01@0 at diff 0.9/255). Veo also ignores "don't do X before the final frame": it plays the natural
   action (drinking) and then eases back into the end-frame pose. So pick a first frame that sits mid-action (e.g. the
   bottle at her lips), so the ease-in reads as one continuous movement.
6. **Read the finished prompt as the video model would.** It has never heard of the story. Would it draw exactly the
   right thing from these words alone? Does any sentence contradict another (for example a timed beat after the
   "hold the final moment" line)? Fix it on paper first.
7. **Real-world size, always** (owner, 2026-10-18). Every character and object in `script.yaml` has a `size:` (height,
   length; for example "1.78 m tall adult man", "house cat, 25 cm tall at the shoulder, 46 cm long"), taken from the
   research with a source. `studio.flow` adds a "Real-world scale" line naming the sizes of everything in the shot and
   warns when one is missing. Write relative sizes into the shot too ("the cat's head reaches just above his ankle").
   A cat half the height of a man, a car as tall as a house or a coin as big as a hand is a failed clip. Show size
   differences with camera distance and framing, never by resizing things. A scene can add `sizes:` for one-off things.
8. **When a clip fails:** name the exact failure, add it to `never:`, change the words that caused it (or switch to a
   start/end frame), and only then regenerate. Never resend the same prompt hoping for luck.

### Video-model defaults that cause wrong clips (always guard against these)
- Any jet gets **engines under the wings** and a **side door with a wheeled boarding staircase**. A 727, DC-9 or MD-80
  has its engines at the tail; a 727's jump stairway comes out of the belly under the tail.
- A person on stairs is drawn **walking up** unless the prompt says DOWN, says where the stairs lead, and shows the
  direction (getting closer to the camera, dropping lower in the frame).
- "Jet" or "plane" with no detail becomes a **fighter or private jet**. Always say airliner + exact model + look.
- People leaving a plane are drawn **from the nose**. Say which door (front left side door, just behind the cockpit).
- A take-off with no detail ends up **on the ground**, or in daylight. State in the air or on the ground, the height,
  wheels up or down, and day or night.
- "Parachute" alone becomes a **backpack or hiking bag**. Describe the harness straps, the ripcord handle and the
  canopy opening.
- **Sizes drift to "cute" or "readable":** animals, coins, tools and small objects get drawn too big next to people, and
  big things (planes, ships, buildings) too small. The "Real-world scale" line with exact sizes and a relative-size
  phrase in the shot prevents this.
- **A person's skin or clothes "turning see-through" (x-ray of a woman's body) is refused** by the policy filter. Show
  insides on a separate featureless anatomical hologram or medical model beside the character, who stays fully dressed.
- A real person's name gets the prompt **refused** (refunded). Use the character's look only.

## Style block (F-STYLE)
```
Stylised cartoon 3D animation in the look of a modern animated family feature film: every person is a cartoon character with rounded, slightly exaggerated proportions (larger head, big expressive eyes with bright highlights, small nose, smooth soft skin, chunky simplified hands), clear and exaggerated facial expressions and body language; simple clean clothes in solid saturated colours, no logos or writing on clothes. Objects, vehicles and buildings are also cartoon-styled: smooth rounded shapes, clean bevelled edges, slightly chunky proportions, simple clean materials (no grime, no photographic textures). Bright, clean, high-key lighting like sunny daylight, with soft shadows and a gentle glow on highlights; a dark setting (night, storm, space, underground) still has a brightly lit subject with strong rim light and vivid glowing accents, never muddy or gloomy. Warm and cool colour contrast (teal, cyan or blue surroundings against warm red, orange and golden subjects), saturated but clean, not neon. Hidden mechanisms are shown with clean x-ray cutaways and glowing outlines. Shallow depth of field on close-ups. Crisp, high-detail render with smooth, fluid, natural motion, believable weight and gentle easing; the camera moves smoothly, never shakes or jumps. Every character keeps exactly the same face, hair, clothes and colours for the whole clip. Not photorealistic, not live action, not gritty, not horror, not 2D flat illustration, not a video game screenshot.
```

## Reference image (F0), one per recurring character or key object
Make these first with Flow's image tool (or Gemini), keep the best, and add them as **Ingredients** for every
scene that shows that character. Ingredients clips are always 8 s.
```
Character reference for a stylised 3D animated explainer, vertical 9:16, full body, standing in a neutral pose on a plain light grey background, soft even studio light.
Character: [NAME]: [LOOK]
[F-STYLE]
No text, letters, numbers or logos.
```

## Scene clip (F1), one per scene (or per pair of scenes that share a clip)
```
[F-STYLE]
Characters: [NAME: LOOK, for each character in the shot, or "none"]
Objects: [OBJECTS]
Shot, [N] seconds, vertical 9:16: [WHAT HAPPENS, beat by beat with rough timings, e.g. "0-2 s: ...; 2-4 s: ..."]
Timing: [TIMING]
Opening frame: [OPEN]
Final frame: [END]
Camera: [CAMERA: lens and movement, e.g. "smooth slow push-in from a medium shot to a close-up on his hands"]
Setting and light: [SETTING], bright soft high-key light, clean saturated colours.
Composition: the main action in the middle of the frame; keep the bottom quarter simple (captions go there) and nothing important in the top-right corner (logo).
Sound: [SFX: every audible action, e.g. "paper rustle, cash register ding, soft footsteps on wood"], quiet room tone. No music. No speech, no voices, no narration, no singing.
Avoid: any text, letters, numbers, labels, subtitles, captions, logos or watermarks drawn in the scene; dark, muddy or gloomy lighting; photorealism; extra fingers or warped faces; characters changing appearance; jittery, morphing or teleporting motion; sudden scene changes or cuts inside the clip.
```

## How the reference Reels look (rules for writing `shot`, `camera` and `sfx`)
From all 8 reference Reels (`docs/zack-style-analysis.md`, Parts 1 and 2).
- **One idea per shot, a visible change every 1–3 seconds**, in one of two edits:
  - *Rapid montage* for stories, history and conspiracies: a cut on nearly every verb or noun, every 1–2 s
    (up to 39 shots in 38 s).
  - *Continuous journey* for physical or scientific demonstrations: one shot holds 3–5 s while the camera keeps
    travelling, from a wide view into a macro close-up and on into a cutaway, with no cut. One 8 s Flow clip can then
    cover two or three scenes (later scenes: `clip: clips/s03.mp4` and `clip_start: 4`).
- **Length 30–45 s** (reference 24–58 s, median 32 s). Up to 60 s only when the story needs it.
- **Camera always moving, always close.** Macro close-ups of hands, objects and seams; first-person (POV) hands
  using things; low hero angles and Dutch angles on big moments; top-down and aerial/satellite views; smooth
  push-ins that go inside objects. No static wide shot longer than 1.5 s.
- **Show the mechanism, down to the atoms.** Cut objects open, make outer shells see-through, slice cross-sections
  through walls, show floating atoms or electrons as coloured spheres. Trace hidden parts, travelling energy or thin
  fast things (a fishing line, a wire) with a luminous glowing outline (green, yellow or cyan) so they read against a
  busy background. Labels like "Hg" or "e" are pop-ups from the build, never drawn by Flow.
- **Readable acting.** Characters react big: wide astonished eyes, jaw drops, comedic shrugs, gasps, sly smiles,
  panicked pointing. Solid, iconic clothes.
- **Layered sound for every action, at every scale.** Whooshes and whips on fast moves; clicks and ratchets for
  dials, reels and counters; electrical hum, buzz and crackle; water churn and splashes; paper, coins, footsteps;
  deep sub-bass thuds and rumbles for shakes and big reveals. No music: fast narration over dense, realistic sound
  effects and room tone.
- **Bright, vivid and clean.** Reference brightness 0.36–0.52 (average 0.42; 0 = black, 1 = white), dark pixels
  usually under 14%, up to 20–28% only for space, underground or a secret night meeting where the subject is
  rim-lit and glowing. Saturation 0.30–0.53. Our first D.B. Cooper pictures were 0.12–0.17 with ~65% dark pixels.
- **Smooth transitions.** Plan each clip's opening frame to continue the previous clip's final frame (same
  direction of motion, matching subject or colour), and its final frame to set up the next clip. Write them in
  `opens:` and `ends:` in script.yaml.
- **No text in the clip.** Captions, numbers, counters, timers, labels and "!" "?" pop-ups are added by the build,
  so spelling, timing and brand colours stay right.
- **Real people and cases:** stylised, generic look only, never a real person's face. **Never write a real person's
  name in a Flow prompt** (Flow refuses "prominent people"): describe the look instead ("a calm man in a dark suit,
  black sunglasses, thin black tie"). Unknown people (like D.B.
  Cooper) seen from behind or in shadow.
