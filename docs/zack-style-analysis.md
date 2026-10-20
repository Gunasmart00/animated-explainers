# Zack D. Films style analysis

What the owner's reference Reels (`C:\Users\E GUNASELAN\Downloads\zack samples`, 8 videos) do, measured and
watched, so HowZit videos can match the feel without copying the content. Part 1 (4 videos) was analysed by Claude
on 2026-10-18; Part 2 (the other 4) is added by Antigravity with `prompts/antigravity-analyse-zack.md`.
Measurements: `python tools/analyse_reference.py <video>`.

## Part 1 — four videos (Claude, 2026-10-18)

| File | Length | Story | Avg brightness | Dark pixels | Saturation | Main hues | Loudness | Syllables/s | Sound-effect bursts /10 s | Music |
|---|---|---|---|---|---|---|---|---|---|---|
| AQP3v6x…E.mp4 | 50.7 s | The "missing dollar" hotel riddle | 0.52 | 11% | 0.30 | teal, blue, red | −14.1 LUFS | 4.5 | 4.1 | none |
| downloadmedia-20261018.mp4 | 58.3 s | A sneaky way to win hide and seek | 0.39 | 14% | 0.37 | red/orange, teal | −14.1 | 4.6 | 6.4 | none |
| downloadmedia-20261018 (1).mp4 | 32.2 s | A horse in an oxygen chamber catches fire | 0.36 | 9% | 0.37 | blue, red/orange | −14.2 | 4.5 | low (fire roar) | none |
| downloadmedia-20261018 (2).mp4 | 32.6 s | How films fake footprints in snow | 0.50 | 8% | 0.30 | warm wood, blue | −14.2 | 4.3 | 5.5 | none |
| *Our D.B. Cooper pictures s01–s03* | — | — | *0.12–0.17* | *63–72%* | *0.25–0.45* | *blue, red* | — | — | — | — |

### Look
- **Stylised 3D, not photoreal.** Game-engine CG people with smooth skin, big expressive eyes and exaggerated
  reactions (wide eyes, finger on lips, hands up). Slightly uncanny, clearly animated. Simple clothes in solid
  saturated colours: yellow, orange, red, magenta T-shirts; uniforms with one strong colour (red bellhop vest).
- **Bright, high-key light.** Average brightness 0.36–0.52 with only 8–14% dark pixels. Soft daylight interiors, white
  ceilings, gentle bloom on highlights, soft shadows. Even dramatic moments (fire) stay well lit.
  **Our D.B. Cooper pictures were 3–4 times darker** (0.12–0.17, ~65% dark pixels) and photographic: the main reason
  they felt wrong.
- **Colour:** cool surroundings (teal/turquoise walls, pastel-blue, blue studio) against warm subjects (red, orange,
  wood, skin). Saturated but clean, never neon.
- **Environments:** tidy and simple: hotel lobby, family house, lab, film studio. Few props, each one meaningful.

### Camera and editing
- **A new shot or a big camera move every 1–2 seconds.** One video has ~41 shots in 58 s. Shots rarely last over 3 s
  unless the camera moves through them.
- **Always close and always moving:** macro close-ups of hands and objects, POV hands holding a phone, over-the-shoulder,
  low angles, top-down, and **cutaway / x-ray views** (a see-through floor plan, the underside of a stage floor) to
  show hidden mechanisms. Smooth push-ins, orbits, tracking, quick whip-pans.
- **Hidden parts glow:** a soft green outline highlights the mechanism being explained (the rope and pegs under the
  floor, the important part).
- **Graphics in the scene:** big red or glowing numbers ($30, $27, 9×3=27), simple equations on a pale blue gradient
  background, emoji-style icons (red "!", "?", lightning, crown, clock), thought bubbles, phone screens. HowZit adds
  numbers, "!" and "?" as pop-ups in the build (spelled right, brand colours), never inside Flow clips.

### Story and narration
- **Starts mid-action in the first line, no intro:** "Three people get a hotel room…", "Before playing hide and
  seek…", "The horse was put inside…", "They cut footprint openings…". No "did you know", no greeting.
- **One continuous, fast narration:** ~4.5 syllables a second (≈ 180 words a minute), only 1–7 pauses over 250 ms per
  video. Short clauses chained with "but", "so", "then", "and as". Past tense for true stories, "you" for tricks.
- **Ends right on the payoff or twist:** "…the missing dollar?", "…the winner.", "…and the person in charge.",
  "…into the snow." No outro, no "follow for more".
- **Length 32–58 s.**

### Captions
- 1–3 words at a time, centred at ~78% of the height, white heavy rounded sans, thin dark outline and soft shadow,
  sentence case, numbers as digits ("$30"). No colour highlight on the spoken word.

### Sound
- **No music in any of the four.** Narration over dense, realistic sound effects and room tone: whooshes on camera
  moves, pops on graphics, footsteps, paper, metal, fire. Loudness −14 LUFS.

### What this changes in HowZit (applied 2026-10-18)
- Flow (Veo) clips instead of still pictures; style block in `prompts/flow.md` asks for bright, stylised, cartoonish 3D.
- Music off by default (`presets/explainer.yaml`); sound effects come from each Flow clip plus pops on pop-ups (no added whoosh on scene changes: the owner found it odd, 2026-10-18).
- 12–20 scenes for 45–60 s, a visible change every 1–3 s, one 8 s clip can cover two short scenes.
- No end card; the HowZit logo stays on screen the whole time.
- Narration from ElevenLabs (the owner's chosen voice), timed to the scenes with faster-whisper.

## Part 2 — four more videos (Antigravity, 2026-10-18)

| File | Length | Story | Avg brightness | Dark pixels | Saturation | Main hues | Loudness | Syllables/s | Sound-effect bursts /10 s | Music |
|---|---|---|---|---|---|---|---|---|---|---|
| downloadmedia-20261018 (3).mp4 | 38.7 s | The Phoebus light bulb cartel and planned obsolescence | 0.39 | 21% | 0.33 | blue, red/brown, orange | −14.2 LUFS | 4.7 | 1.8 | none |
| downloadmedia-20261018 (4).mp4 | 24.1 s | Fisherman saves drowning swimmer with a fishing rod | 0.42 | 5% | 0.42 | teal/cyan, blue, yellow | −14.1 | 4.5 | 2.1 | none |
| downloadmedia-20261018 (5).mp4 | 31.1 s | Why fluorescent tube lights glow under power lines | 0.40 | 6% | 0.34 | teal/cyan, blue, green | −14.2 | 4.5 | 5.2 | none |
| downloadmedia-20261018 (6).mp4 | 32.0 s | The mysterious 26-second seismic pulse shaking Earth | 0.36 | 28% | 0.53 | teal/cyan, blue, red/brown | −14.1 | 5.1 | 0.3 | none |

### Look
- **Stylised 3D across diverse environments:** Game-engine CG characters with smooth skin, expressive oversized eyes, exaggerated expressions (comedic shrugs, jaw drops, conspiratorial smirks, wide panic eyes), and clean solid-colour clothing (Zack D. Films logo t-shirt, royal blue tees, grey suits with red shirts, striped fishing shirts). Environments expand far beyond domestic rooms: tropical beaches with palm trees and ocean surf (Video 4), open meadows with massive steel transmission towers (Video 5), underground volcanic magma chambers (Video 6), and deep space orbits around Earth (Video 6).
- **High-key lighting with selective high-contrast drama:** Average brightness remains consistently high (0.36–0.42, average 0.39). Dark pixels are very low in open daytime scenes (5% for the beach, 6% for the meadow), but increase to 21% in the dark cartel boardroom and 28% in outer space/magma scenes. Even in dark scenes, focal subjects are brightly highlighted with strong rim lighting, vibrant neon arcs, and glowing accents.
- **Colour Palette:** Saturated teal/cyan (46–50%) and deep blue (18–40%) remain the dominant surrounding/ambient hues in 3 of the 4 videos, contrasted against warm red/brown, orange, golden yellow, and grassy greens. Saturation ranges from 0.33 to 0.53 (mean 0.40).
- **Microscopic and atomic cutaways:** Visuals frequently penetrate inside objects. Video 5 dives inside a glass fluorescent tube, rendering translucent blue gas chambers, floating atoms labeled "Hg", orbiting electrons labeled "e", and a cross-section of the glass wall and phosphor coating. Video 6 slices into volcanic crust to reveal glowing red magma conduits.

### Camera and editing
- **Two editing styles depending on topic:**
  1. *Rapid montage (conspiracy / conceptual):* Video 3 has 39 shots in 38.7 s (~1.0 s/shot) and Video 6 has 20 shots in 32.0 s (~1.6 s/shot). Shots cut rapidly on every verb or noun.
  2. *Continuous journey (physical / scientific demonstration):* Video 4 has 7 shots in 24.1 s (3.45 s/shot) and Video 5 has 6 shots in 31.1 s (5.18 s/shot). Rather than cutting constantly, the camera pushes in continuously, traveling seamlessly from wide establishing shots to extreme macro details and x-ray interiors.
- **Dynamic camera choreography:**
  - Macro close-ups: tracking a fishing hook catching a denim belt loop (Video 4, 0:04), filament snapping inside a bulb (Video 3, 0:19), fountain pen signing a contract (Video 3, 0:34), seismograph needle vibrating on paper (Video 6, 0:06).
  - First-person (POV): fisherman casting line from shore (Video 4, 0:01), hands unrolling an antique map (Video 6, 0:23).
  - High-angle / drone / top-down: aerial town view (Video 3, 0:06), top-down conference table (Video 3, 0:12), satellite continental shelf view (Video 6, 0:16), flat Earth disk from above (Video 6, 0:24).
  - Dutch angles and low hero angles: straining fisherman reeling in catch (Video 4, 0:17), cartel executives surrounded by falling money (Video 3, 0:36), presenter holding illuminated tube like a lightsaber (Video 5, 0:29).
- **Graphics added in the scene:**
  - On-screen counters and HUD timers: 3D flip-digit counter box "0206 HOURS" ticking up to "2000 HOURS" (Video 3, 0:01–0:03); pill-shaped countdown HUD timer "00:19" counting down to "00:00" in upper left (Video 6, 0:00–0:03).
  - Glowing tracer outlines: thin fishing line rendered with a vibrant yellow glow outline so it remains easily trackable against breaking white waves and rocks (Video 4, 0:22–0:24).
  - Scientific particle labels: 3D spheres labeled "Hg" (Mercury) and particles labeled "e" (electrons) inside the vacuum tube (Video 5, 0:18–0:24).
  - Holographic / projection graphics: glowing wall map labeled "PLANNED OBSOLESCENCE" (Video 3, 0:16), expanding golden shockwave pulse rings rippling across Earth's crust (Video 6, 0:01, 0:17).
  - In-world physical text: competitor retail booth banners "Longer Lasting Light Bulbs" (Video 3, 0:28), antique map header "FLAT EARTH WORLD MAP" (Video 6, 0:23).

### Story and narration
- **Narrations (private study transcriptions):**
  - **Video 3 (Phoebus Cartel, 102 words, 38.7 s):**
    - *First line:* "They built a light bulb that lasted 2,000 hours, but there was a problem."
    - *Last line:* "All to protect a secret pact that made them richer by making their product worse."
    - *Full narration:* "They built a light bulb that lasted 2,000 hours, but there was a problem. The longer the bulbs lasted, the fewer new bulbs people had to buy. So light bulb makers from different countries made a secret deal. Instead of competing to make better bulbs, they agreed to make bulbs that burned out faster. That way, customers would keep buying replacements, without knowing the bulbs were being built to fail. Now, some companies tried selling longer-lasting bulbs again, but the group pressured them to stop. All to protect a secret pact that made them richer by making their product worse."
  - **Video 4 (Fisherman rescue, 73 words, 24.1 s):**
    - *First line:* "He cast his fishing line at the woman until the hook caught on her jeans."
    - *Last line:* "Then he pulled her in toward the shore, saving her life with just a hook and a line."
    - *Full narration:* "He cast his fishing line at the woman until the hook caught on her jeans. You see, she had jumped into the ocean to swim, but a current caught her, pulling her further from the shore. As people saw her struggling, the fisherman grabbed his rod, casting over and over until he finally caught her. Then he pulled her in toward the shore, saving her life with just a hook and a line."
  - **Video 5 (Tube light under power lines, 87 words, 31.1 s):**
    - *First line:* "If you grab a tube light and stick it into the ground like this, well nothing will happen."
    - *Last line:* "This releases invisible light that hits a white coating on the glass, turning it into visible light and causing the whole tube to glow."
    - *Full narration:* "If you grab a tube light and stick it into the ground like this, well nothing will happen. But if you try the same thing under high voltage power lines, the electricity flowing through them makes an electrical field in the air. This creates voltage between the two ends of the tube, and a special gas trapped inside the glass suddenly gets activated. This releases invisible light that hits a white coating on the glass, turning it into visible light and causing the whole tube to glow."
  - **Video 6 (Earth 26-second pulse, 84 words, 32.0 s):**
    - *First line:* "Every 26 seconds, the Earth makes a tiny shake."
    - *Last line:* "...and that the pulse comes from the machinery that holds up the sky."
    - *Full narration:* "Every 26 seconds, the Earth makes a tiny shake. You can't feel it, but seismic machines can. And for decades, scientists tried to figure out where it came from. Some think it's caused by underwater ocean waves, which hit the shallow edge of the continent and vibrate it like a drum. Others think it's the rumbling of a nearby volcano, but some people actually believe this proves the Earth is flat and that the pulse comes from the machinery that holds up the sky."
- **Storytelling formula:**
  - Immediate mid-action hook: establishes premise in line 1 without intro ("They built a light bulb...", "He cast his fishing line...", "If you grab a tube light...", "Every 26 seconds...").
  - Fast, conversational narration: 4.5 to 5.1 syllables/s (~180–205 wpm). Pauses > 250 ms occur only 6–10 times per video, strictly at sentence boundaries (averaging 0.35–0.45 s).
  - Hard landing: ends instantly on the final keyword ("...worse.", "...just a hook and a line.", "...cause the whole tube to glow.", "...machinery that holds up the sky."). Zero outro, zero channel plug.
  - Video length is tighter than Part 1: 24.1 to 38.7 s (mean 31.5 s).

### Captions
- **Precise placement:** Measured across all four videos, captions are consistently centered vertically at **78.3% of frame height** (`position_y: 0.783` or ~1002 px on a 1280 px frame, corresponding to 1503 px on 1920 px vertical video).
- **Format:** 1–3 words per line, heavy rounded white humanist sans with subtle dark drop shadow and blurred border. No word-by-word colour highlighting. Numbers are displayed as formatted digits ("2,000 hours", "26 seconds").

### Sound
- **Zero music in all four videos.** The entire audio track consists exclusively of voiceover, rich environmental foley, and tailored sound effects.
- **Loudness:** Locked to −14.1 to −14.2 LUFS integrated loudness with tight dynamic range (LRA 2.5–3.8 LU).
- **Sound design elements:**
  - Mechanical: clock counters clicking (Video 3, 0:02), cash register bell (Video 3, 0:22), fountain pen scratching (Video 3, 0:34), high-speed fishing reel ratchet clicking (Video 4, 0:17), seismograph drum motor whir (Video 6, 0:06), giant clockwork brass gears ticking and creaking (Video 6, 0:30).
  - Environmental / Foley: rustling cardboard boxes (Video 3, 0:08), falling dollar bills fluttering (Video 3, 0:37), crashing ocean surf and turbulent waves (Video 4, 0:08), wet sand dragging (Video 4, 0:20), dirt crunching around tube (Video 5, 0:02), coffee cup clinking on wood desk (Video 6, 0:04), parchment map unrolling (Video 6, 0:23).
  - Electrical / Sci-Fi: electrical switch click and buzz (Video 3, 0:01), filament snap/pop (Video 3, 0:19), 60 Hz power line hum and sizzling corona arcing (Video 5, 0:10), spark snap on metal cap (Video 5, 0:15), resonant energy ping on atom collision (Video 5, 0:21), fluorescent tube strike and ballast buzz (Video 5, 0:28), digital countdown beeps (Video 6, 0:01), deep sub-bass seismic impact thuds / rumbles (Video 6, 0:03, 0:18).

### Differences from Part 1
1. **Scientific atomic cutaways and microscopic cross-sections:** Part 1 noted architectural cutaways (room floor plans, stage undersides). Part 2 reveals deep microscopic and atomic visualization: penetrating inside a glass vacuum tube, showing labeled element spheres ("Hg", "e"), energy wavefronts, and multi-layered wall cross-sections (Video 5).
2. **Shot length flexibility (not always 1–2 s cuts):** While Video 3 (0.99 s/shot) and Video 6 (1.60 s/shot) follow the rapid 1–2 s cutting pattern, Videos 4 and 5 demonstrate that continuous physical demonstrations can hold shots for 3.5 to 5.2 s when the camera moves continuously through space (pushing from wide to macro to cutaway without cutting).
3. **In-scene HUD / timer overlays and tracer outlines:** Part 2 introduces floating UI countdown timer pills ("00:19" countdown), mechanical flip counters ("2000 HOURS"), labeled element spheres ("Hg"), and luminous glowing outlines around thin fast-moving objects (glowing yellow fishing line in Video 4) to ensure visual clarity against busy backgrounds.
4. **Shorter video lengths:** While Part 1 videos ranged from 32 to 58 s, Part 2 shows that videos can be as brief as 24.1 s (Video 4) and 31–32 s (Videos 5 & 6). The reference style frequently uses concise ~25–38 s runtimes for maximum retention.
5. **Dark pixel headroom for space and secret meetings:** Part 1 had a narrow dark pixel range of 8–14%. In Part 2, dark pixels reach 21% (cartel boardroom) and 28% (outer space, underground magma), demonstrating that moody or cosmic settings are acceptable as long as the focal subjects maintain strong rim lighting and vibrant luminous accents.
6. **Faster narration peak:** While Part 1 narration ranged from 4.3 to 4.6 syllables/s, Video 6 pushes speech speed up to 5.14 syllables/s (~205 wpm).

### Combined rules (all 8 videos)
- **Video length:** 24.1 – 58.3 s (mean: 37.6 s, median: 32.4 s). Aim for 30–45 s for standard explainers.
- **Average brightness:** 0.36 – 0.52 (mean: 0.42). High-key illumination is mandatory.
- **Dark pixel share:** 5% – 28% (mean: 13.9%; 6 of 8 videos are between 5% and 14%). Dark pixels above 20% are reserved exclusively for space, night, or underground scenes with luminous subjects.
- **Saturation:** 0.30 – 0.53 (mean: 0.38). Crisp, clean game-engine colours, never muddy or drab.
- **Loudness:** −14.1 to −14.2 LUFS across all 8 videos. Master mix strictly to −14.0 LUFS.
- **Music:** 0 of 8 videos have music (0%). Explainers rely entirely on narration, room tone, environmental foley, and punchy sound effects.
- **Speech pacing:** 4.3 – 5.1 syllables/s (mean: 4.6 syllables/s, ~180–205 wpm). Continuous delivery with only 6–10 brief pauses (> 250 ms) per video, strictly at sentence breaks.
- **Editing pace:** Average shot duration 1.0 – 5.2 s per shot. Rapid narrative cuts occur every 1–2 s; continuous demonstration shots run 3–5 s with active camera travel.
- **Captions:** White rounded heavy sans at **78.3% vertical height** (`position_y: 0.78`), 1–3 words at a time, soft dark outline/shadow, numbers as formatted digits, no word highlight.

### Suggested changes

**Applied by Claude on 2026-10-18**, with two adjustments: atom labels ("Hg", "e") and counters stay as build
pop-ups, never text inside Flow clips (Veo misspells text); captions moved to 0.78 but anchored at the bottom so
a 2-line caption grows upward, away from Instagram's buttons. `sfx.reveal: impact` is a new synthesised sound
(`assets/sfx/impact.wav`) played under the lime pop-up.

#### 1. F-STYLE block in `prompts/flow.md`
**Suggested replacement:**
```
Stylised 3D animation with the look of a polished, high-end game-engine animated explainer short. Slightly cartoonish CG people with smooth skin, large expressive eyes and clear, exaggerated facial expressions and body language; simple clean clothes in solid saturated colours (yellow, orange, red, magenta, royal blue, teal). Bright, clean, high-key lighting like sunny daylight, with soft shadows and a gentle glow on highlights; dark backgrounds (space, night, secret vaults) must feature luminous subjects with strong rim lighting and vivid accents, never muddy or gloomy. Environments range from tidy interiors (teal/pastel walls, warm wood floors) to crisp outdoor landscapes (sunny beaches, grassy meadows, coastlines, or celestial views) with clean, stylized props. Warm and cool colour contrast (teal, cyan or blue surroundings against warm red, orange, and golden subjects), saturated but clean, not neon. Seamless transitions from macroscopic real-world cameras into microscopic or x-ray cutaways showing labeled atoms, molecules, or glowing mechanisms with clean graphic clarity. Shallow depth of field on close-ups. Crisp, high-detail render with smooth, fluid, natural motion and believable weight. Not photorealistic, not gritty, not horror, not 2D flat illustration.
```
*Rationale:* Expands environment scope from indoor rooms to sunny outdoor landscapes (beach in Video 4 0:06, meadow in Video 5 0:00, space in Video 6 0:00) and explicitly guides Flow/Veo to support microscopic cutaways with labeled atoms (Video 5 0:18) and luminous subjects in dark space (Video 6 0:00).

#### 2. Rules list at the end of `prompts/flow.md`
**Suggested replacement:**
```markdown
## How the reference Reels look (rules for writing `shot`, `camera` and `sfx`)
- **One idea per shot, with a visible change every 1–3 seconds.** Fast-paced historical or conspiracy stories cut every 1–2 s (up to 39 shots in 38 s). Continuous physical or scientific demonstrations can run 3–5 s per shot if the camera travels continuously from wide to macro or penetrates into a cutaway without cutting. Total video lengths range from 24 to 58 s (sweet spot is 30–40 s).
- **Camera always moving, always close.** Macro close-ups of hands, objects, and seams; first-person (POV) hands manipulating props; low angles looking up at expressive characters; top-down cutaways; aerial satellite tracks; and smooth continuous push-ins penetrating inside objects. No static wide shots longer than 1.5 s.
- **Show the mechanism and atomic layers.** Cut objects open, make outer shells transparent, slice cross-sections through walls, or show internal floating atoms and electrons labeled with clean 3D text (e.g. "Hg", "e"). Use luminous glowing outlines (green, yellow, or cyan) to trace hidden parts, traveling energy waves, or thin moving elements (like a fishing line) against complex backgrounds.
- **Readable acting.** Characters react big: wide astonished eyes, comedic shrugs, gasps, conspiratorial smiles, or panicked pointing. Keep character clothing solid and iconic.
- **Layered sound for every action and scale.** High-frequency whooshes and whips on fast moves, mechanical clicks/ratchets for dials and counters, crackling electrical hums, water churn and splashes, and resonant sub-bass thuds/rumbles for earth shakes and dramatic reveals. The reference Reels use zero music: 100% fast narration over dense, realistic foley and room tone.
- **Bright, vibrant, and clean.** Average brightness across reference videos is 0.36–0.52 (average ~0.42) with dark pixels typically under 14% (expanding to 20–28% only for deep space, subterranean magma, or secret night meetings where focal subjects have vivid rim lights). Saturation is rich (0.30–0.53).
- **No text drawn inside the video clip.** Captions, numbers, counters, and pop-up icons are added by the build pipeline so spelling, timing, and brand colours stay pristine.
- **Real people and cases:** Stylised, generic 3D character avatars only; never photorealistic or real people's likenesses.
```
*Rationale:* Explicitly documents the 3–5 s continuous camera travel pattern (Video 4 at 0:14–0:17, Video 5 at 0:18–0:24), microscopic atomic labeling (Video 5 at 0:18), luminous tracer outlines on thin objects (Video 4 at 0:22), sub-bass reveal impacts (Video 6 at 0:03), and dark pixel ceiling exceptions for space (Video 6 at 0:00).

#### 3. Settings in `presets/explainer.yaml`
- **`captions.position_y: 0.78`** (change from `0.75`):
  All four Part 2 videos place captions centered at exactly 78.3% of frame height (Video 3 at 0:01.5, Video 4 at 0:01.5, Video 5 at 0:04.0, Video 6 at 0:01.5 all measure center Y = 0.782–0.784, ~1002 px of 1280 px).
- **`voice.rate: "+14%"`** (change from `"+10%"`):
  Speech pace across Part 2 averages 4.7 syllables/s (Video 6 reaches 5.14 syl/s at 0:00–0:32, Video 3 reaches 4.66 syl/s at 0:00–0:38), noticeably quicker than edge-tts Brian at +10% (~4.1 syl/s).
- **`sfx.volume: 0.32`** (change from `0.28`):
  Reference sound effects (mechanical ratchets in Video 4 0:17, electrical arcs in Video 5 0:10, cash register in Video 3 0:22) are mixed loud and punchy, sitting prominently beneath the voiceover at approximately −16 to −18 LUFS.
- **Add sub-bass impact sound option in presets (`sfx.reveal: impact_sub`)**:
  Video 6 uses heavy sub-bass impacts (at 0:03 and 0:18) rather than whooshes when the 26-second pulse or continental vibration occurs.

