# Episode: Don't Underestimate Gen Z Teachers (genz-teacher)

Format: vertical 9:16 Reel, Zack-style (no music, fast narration over sound effects), ~32 s.
Narration: ElevenLabs "Mark – Natural Conversations", 33.0 s file, mono 44.1 kHz, **−25.0 LUFS** (raise to −14 LUFS in the build).

## 1. Narration, timed from the audio (recogniser + silence detection, 2026-10-19)

| # | Time (s) | Line | Pause after |
|---|---|---|---|
| 1 | 0.00 – 3.11 | The teacher turned her back and slowly walked down the aisle, | 0.21 |
| 2 | 3.33 – 4.79 | so the students thought they were safe. | 0.74 |
| 3 | 5.53 – 7.60 | Papers started flying across the desks, | 0.32 |
| 4 | 7.92 – 9.85 | one kid passed his whole answer sheet, | 0.27 |
| 5 | 10.12 – 12.18 | and another grabbed a cheat sheet off the floor. | 0.64 |
| 6 | 12.82 – 15.80 | But behind her back, she was holding her phone sideways, | – |
| 7 | 15.85 – 18.38 | with the ultra-wide camera pointed right at them. | 0.53 |
| 8 | 18.90 – 20.44 | And as it recorded in 4K, | 0.37 |
| 9 | 20.81 – 23.25 | it locked onto every single face in the room. | 0.53 |
| 10 | 23.78 – 26.22 | So by the time one kid looked up and saw the screen, | 0.32 |
| 11 | 26.54 – 27.51 | it was already too late, | 0.51 |
| 12 | 28.03 – 31.77 | and the only thing they passed that day was the paper… not the exam. | (end) |

- Pace ≈ 4.4 syllables/s (reference 4.3–5.1). Pause before "not the exam": 30.53–30.92.
- There is a short extra sound at **32.35–32.75 s** after "exam" (breath or stray word). The cut ends at **31.95 s** unless it is meant to be there.
- Key hit points for sound effects: record scratch + sub-bass impact at **12.82** ("But"), soft lens-focus whirr at **15.9** ("ultra-wide"), "4K" pop-up at **19.9**, face boxes popping **20.8–23.2**, freeze boom at **24.9** ("looked up"), slow-motion whoosh at **28.0**.

## 2. Visual facts (geometry the prompts must keep true)

- **Room:** a bright college exam hall. Pale teal walls, big windows on the LEFT wall with soft sunlight, white ceiling, light honey-wood floor. A dark green chalkboard (completely blank) across the FRONT wall. A plain round white wall clock with tick marks only (no numbers). Two columns of single wooden exam desks, 4 rows on each side, with one 1.2 m wide **centre aisle** between them. **Every desk and every student faces the chalkboard.**
- **Where she walks:** the teacher walks from the BACK of the hall UP the centre aisle TOWARD the chalkboard. The students she has passed sit BEHIND her and see only her back. She never looks back until the last shot.
- **The phone:** held horizontally (long edge parallel to the floor) behind her lower back, at about 1 m above the floor. Both hands cradle it loosely, fingers relaxed. The **screen faces her back** (forward). The **rear camera lenses face backward**, toward the students behind her and the back of the hall.
- **Sizes:** teacher 1.65 m. Students 1.60–1.80 m (seated head height ~1.25 m). Desk 75 cm tall, top 60 × 45 cm. Phone 16 × 7.7 cm (spans her two palms). A4 exam sheet 21 × 29.7 cm. Cheat slip 7 × 5 cm (smaller than a palm). Chalkboard 1.2 m tall × 3.6 m wide.
- **No text:** papers show fine grey scribble lines only, never readable writing. The phone screen shows no numbers or words, only a red dot and thin yellow squares. "4K", "REC" and captions come from the build.
- **Ages:** all students are young-adult college students (19–20).

## 3. Characters (same words in every prompt)

- **TEACHER:** a young woman teacher in her mid-20s, 1.65 m tall, warm light-brown skin, dark brown hair in a sleek high ponytail, small gold hoop earrings, thin black smartwatch on her left wrist, oversized cream knit cardigan over a plain white T-shirt, high-waisted sage-green wide-leg trousers, black loafers with a low block heel. Calm, composed, faint knowing half-smile.
- **PHONE:** a modern smartphone, 16 cm long and 7.7 cm wide, matte black back with a square camera bump in one corner holding three round lenses.
- **STUDENTS:** eight young-adult college students, about 19 years old, all in the same uniform: plain white short-sleeved collared shirts with navy-blue trousers or navy-blue knee-length skirts, each at their own single wooden exam desk.
- **GLASSES BOY:** lanky, curly black hair, big round black glasses.
- **SPIKY BOY:** stocky, short spiky brown hair, freckles, wide cheeky grin.
- **FRINGE BOY (the one who looks up):** neat side-swept black fringe, thick eyebrows. He sits in the middle row, right-hand desk beside the aisle.
- **BRAIDS GIRL:** two long black braids. She sits in the middle row, left-hand desk beside the aisle, across the aisle from FRINGE BOY.

## 4. Flow settings
- Project: **genz-teacher**. **Portrait 9:16**. **Veo 3.1 – Fast**, sound on, 8 s clips, 1 output first (2 if a clip fails twice).
- Ingredients: R1 (teacher) + R2 (exam hall with students) on every clip that shows them.
- Download each clip: **Upscaled 1080p**. Leave any Veo watermark as it is.
- About **9 clips × 20 credits = 180 credits**, plus retries.

## 5. Reference images (Flow image tool, 9:16)

**R1 – Teacher**
```
Character reference for a stylised 3D animated explainer, vertical 9:16, full body, standing in a neutral pose on a plain light grey background, soft even studio light.
Character: a young woman teacher in her mid-20s, 1.65 m tall, warm light-brown skin, dark brown hair in a sleek high ponytail, small gold hoop earrings, thin black smartwatch on her left wrist, oversized cream knit cardigan over a plain white T-shirt, high-waisted sage-green wide-leg trousers, black loafers with a low block heel; calm, composed, faint knowing half-smile; she holds a matte black smartphone (16 cm long) loosely in her right hand at her side.
Stylised cartoon 3D animation in the look of a modern animated family feature film: rounded, slightly exaggerated proportions (larger head, big expressive eyes with bright highlights, small nose, smooth soft skin, chunky simplified hands); simple clean clothes in solid colours, no logos or writing on clothes. Crisp, high-detail render. Not photorealistic.
No text, letters, numbers or logos.
```

**R2 – Exam hall with students**
```
Environment and cast reference for a stylised 3D animated explainer, vertical 9:16. A bright college exam hall seen from the front corner of the room, beside the chalkboard, looking back across the class so every student's face is clearly visible: pale teal walls, big windows along one side wall with soft sunlight, white ceiling, light honey-wood floor, a dark green chalkboard that is completely blank on the front wall at the edge of the frame, a plain round white wall clock with tick marks only on the back wall. Two columns of single wooden exam desks, four rows on each side, with one wide centre aisle between them; every desk and every student faces the chalkboard. Eight young-adult college students, about 19 years old, all in the same uniform (plain white short-sleeved collared shirts, navy-blue trousers or navy-blue knee-length skirts), heads down writing on white exam papers. Among them: a lanky boy with curly black hair and big round black glasses; a stocky boy with short spiky brown hair and freckles; a boy with a neat side-swept black fringe and thick eyebrows at the middle-row desk right of the aisle; a girl with two long black braids at the middle-row desk left of the aisle.
Stylised cartoon 3D animation in the look of a modern animated family feature film: rounded, slightly exaggerated proportions, big expressive eyes, smooth soft skin, chunky simplified hands; clean cartoon-styled furniture with smooth rounded shapes and bevelled edges. Bright, clean, high-key daylight with soft shadows, teal surroundings against warm wood and skin tones. Crisp, high-detail render. Not photorealistic.
No text, letters, numbers or logos; the papers show only fine grey scribble lines.
```

## 6. Clip prompts (F1)

`[F-STYLE]` = the style block in `prompts/flow.md`, pasted in full at the top of every prompt.
Every prompt ends with the same Composition and Avoid lines:
> Composition: the main action in the middle of the frame; keep the bottom quarter simple (captions go there) and nothing important in the top-right corner (logo).
> Avoid: any text, letters, numbers, labels, subtitles, captions, logos or watermarks drawn in the scene; dark, muddy or gloomy lighting; photorealism; extra fingers or warped faces; characters changing appearance; jittery, morphing or teleporting motion; sudden scene changes or cuts inside the clip.

---
### C01 · 0.00–3.30 · "The teacher turned her back and slowly walked down the aisle,"
Use: clip 0.0–3.3 s.
```
[F-STYLE]
Characters: TEACHER: a young woman teacher in her mid-20s, 1.65 m tall, warm light-brown skin, dark brown hair in a sleek high ponytail, small gold hoop earrings, thin black smartwatch, oversized cream knit cardigan over a plain white T-shirt, high-waisted sage-green wide-leg trousers, black low block-heel loafers, calm faint half-smile. STUDENTS: eight young-adult college students about 19 years old in identical uniforms (plain white short-sleeved collared shirts, navy-blue trousers or knee-length skirts), each at a single wooden exam desk.
Objects: a matte black smartphone 16 cm long with a three-lens camera bump; white A4 exam papers covered in fine grey scribble lines.
Shot, 8 seconds, vertical 9:16: 0-1 s: the teacher stands in the centre aisle of a bright exam hall, facing the camera, holding the phone in both hands at her waist, calmly looking over the class. 1-2.5 s: she turns around smoothly to face the chalkboard at the front of the room, and as she turns she moves both hands behind her lower back, cradling the phone horizontally (long edge level with the floor) so its three camera lenses point straight back at the camera. 2.5-8 s: with her hands loosely clasped behind her back holding the phone, she walks slowly and steadily up the centre aisle AWAY from the camera toward the chalkboard; on both sides of the aisle the students sit bent over their desks, writing, all facing the chalkboard.
Timing: the turn is finished by 2.5 s; from then on she walks at a slow, relaxed pace.
Opening frame: the teacher facing the camera in the centre aisle, students on both sides with heads down writing.
Final frame: the teacher seen from behind, halfway up the aisle, hands and phone resting behind her lower back, students writing on both sides.
Camera: eye level at 1.2 m, directly behind her in the aisle; smooth slow follow at walking pace keeping her hands and the phone in the centre of the frame.
Setting and light: a college exam hall with pale teal walls, big sunlit windows on the left wall, white ceiling, light honey-wood floor, a completely blank dark green chalkboard on the front wall, two columns of single wooden desks with one wide centre aisle, every desk facing the chalkboard; bright soft high-key light, clean saturated colours.
Real-world scale: teacher 1.65 m; seated students' heads at about 1.25 m; desks 75 cm tall; the phone spans her two palms.
Composition: …   Sound: slow loud clock ticking, soft shoe clicks on a wood floor, pencils scratching on paper, quiet room tone. No music. No speech, no voices, no narration, no singing.
Avoid: …; the teacher looking back; the phone held upright; the students facing the camera.
```
must: students and desks all face the chalkboard; she walks AWAY from the camera toward the board; phone horizontal behind her lower back, lenses toward the camera.
never: students facing the back of the room; phone held vertically; teacher walking toward the camera after the turn.

---
### C02 · 3.30–5.50 · "so the students thought they were safe."
Use: 0.3–2.5 s.
```
[F-STYLE]
Characters: FRINGE BOY: a college student about 19, neat side-swept black fringe, thick eyebrows, white short-sleeved collared shirt, navy trousers. BRAIDS GIRL: a college student about 19, two long black braids, white short-sleeved collared shirt, navy knee-length skirt. Other students in the same uniform behind them, heads down.
Objects: single wooden exam desks; white exam papers with fine grey scribble lines; pencils.
Shot, 8 seconds, vertical 9:16: FRINGE BOY sits at the desk to the right of the centre aisle and BRAIDS GIRL at the desk to the left of it, both facing the camera (the front of the room). The teacher is out of frame, walking away from them toward the front, just to the side of the camera. 0-1 s: both slowly lift their eyes from their papers and look past the camera at the teacher's back. 1-2.5 s: they turn their heads to each other across the aisle with big sly, mischievous grins and raised eyebrows; he gives a tiny thumbs-up low by his desk. 2.5-8 s: they lean toward the aisle, rubbing their hands together, and slide their papers toward the edge of their desks.
Opening frame: both students bent over their papers, writing.
Final frame: both leaning into the aisle with papers held out, grinning.
Camera: desk height, in front of the pair, looking at their faces with the aisle between them; slow smooth push-in.
Setting and light: the same bright exam hall: pale teal walls, sunlit windows on the right side of the frame, light wood floor and desks, more rows of students behind them; bright soft high-key light, clean saturated colours.
Real-world scale: desks 75 cm tall; seated, their heads are at about 1.25 m.
Sound: a clock ticking, a chair creaking, paper sliding on wood, quiet room tone. No music. No speech, no voices, no narration, no singing.
```
must: no teacher in frame; both look past the camera, never into it (looking into the lens is saved for C08).

---
### C03 · 5.50–7.90 · "Papers started flying across the desks,"
Use: 0.0–2.4 s.
```
[F-STYLE]
Characters: STUDENTS: eight young-adult college students about 19 in identical uniforms (white short-sleeved collared shirts, navy trousers or skirts) at single wooden desks, including a boy with curly black hair and round glasses, a stocky boy with spiky brown hair, a boy with a side-swept black fringe and a girl with two long braids. TEACHER (far away, seen from behind): cream cardigan, sage-green trousers, high ponytail, hands with a black phone clasped behind her back.
Objects: white A4 exam papers with fine grey scribble lines, a crumpled paper ball.
Shot, 8 seconds, vertical 9:16: a high-angle view from above the back row looking down the length of the exam hall toward the chalkboard; the teacher is far ahead near the front, walking slowly away with her back to us. 0-1 s: the whole class bursts into frantic, comedic motion all at once. 1-8 s: students on both sides pass exam papers back and forth across the centre aisle, lean far over their desks, swap whole sheets, flick a crumpled paper ball to a friend; sheets flutter through the air between desks; everyone moves fast and gleefully while the teacher keeps walking calmly away.
Opening frame: the class sitting still, heads down, the teacher far ahead.
Final frame: papers mid-air over the aisle, students stretched across desks.
Camera: high angle about 3 m up behind the back row; a smooth slow crane forward and down over the desks.
Setting and light: the same bright exam hall: pale teal walls, sunlit windows on the left wall, light wood floor, blank dark green chalkboard; bright soft high-key light, clean saturated colours.
Real-world scale: an A4 sheet is about the size of a desk's half-top; the teacher looks small because she is 8 m away.
Sound: rapid paper rustling and flapping, sheets whooshing through the air, chairs creaking and scraping, fast comic scramble foley, quiet room tone. No music. No speech, no voices, no narration, no singing.
```

---
### C04 · 7.90–10.10 · "one kid passed his whole answer sheet,"
Use: 0.2–2.4 s.
```
[F-STYLE]
Characters: GLASSES BOY: a lanky college student about 19, curly black hair, big round black glasses, white short-sleeved collared shirt, navy trousers. BRAIDS GIRL: a college student about 19, two long black braids, white collared shirt, navy skirt.
Objects: a thick stapled answer booklet of white A4 pages with fine grey scribble lines (no readable writing).
Shot, 8 seconds, vertical 9:16: close-up across the centre aisle between two desks. 0-1.5 s: GLASSES BOY confidently holds out his ENTIRE thick stapled answer booklet across the aisle with one hand; BRAIDS GIRL grabs it with both hands, eyes wide with delight. 1.5-3 s: rack focus up to his face: a proud, smug grin and a wink, pushing his glasses up his nose. 3-8 s: she hugs the booklet to her chest and quickly starts copying, while he leans back with his arms crossed, very pleased with himself.
Opening frame: his hand holding the booklet out over the aisle.
Final frame: him leaning back smugly, her copying.
Camera: low close-up at desk-top height looking along the aisle, a quick smooth whip-pan following the booklet, then a slow push-in on his face. Shallow depth of field.
Setting and light: the same bright exam hall: pale teal walls, light wood desks and floor; bright soft high-key light, clean saturated colours.
Real-world scale: the A4 booklet is about as long as his forearm.
Sound: a fast paper whoosh as the booklet crosses the aisle, a crisp page flap, a chair creak, quiet room tone. No music. No speech, no voices, no narration, no singing.
```

---
### C05 · 10.10–12.80 · "and another grabbed a cheat sheet off the floor."
Use: 0.0–2.7 s.
```
[F-STYLE]
Characters: SPIKY BOY: a stocky college student about 19, short spiky brown hair, freckles, wide cheeky grin, white short-sleeved collared shirt, navy trousers, black school shoes.
Objects: a small folded white paper slip 7 cm by 5 cm (smaller than his palm) with fine grey scribble lines; wooden desk legs.
Shot, 8 seconds, vertical 9:16: 0-1 s: floor-level view of the light wood floor of the aisle; the small folded paper slip lies beside a wooden desk leg and his black shoe. 1-2 s: his hand swoops down fast and snatches the slip off the floor. 2-4 s: the camera tilts up smoothly following his hand to his face as he sits back up, hiding the slip under his desk, and unfolds it with a sneaky grin, wiggling his eyebrows. 4-8 s: he glances left and right, then copies from it, delighted.
Opening frame: the slip on the floor by the desk leg.
Final frame: him grinning over the open slip held under his desk.
Camera: starts at floor level with a wide lens, smooth tilt and rise up to a medium close-up of his face.
Setting and light: the same bright exam hall: light honey-wood floor, wooden desks, pale teal walls; bright soft high-key light, clean saturated colours.
Real-world scale: the slip is smaller than his palm; his shoe is about four times its length.
Sound: a quick swoosh as the hand dives, a crisp paper snatch, paper unfolding, a sneaky chair creak, quiet room tone. No music. No speech, no voices, no narration, no singing.
```

---
### C06 · 12.80–18.90 · "But behind her back, she was holding her phone sideways, with the ultra-wide camera pointed right at them."
Use: 0.0–6.1 s. Continuous push-in, no cut.
```
[F-STYLE]
Characters: TEACHER, seen from behind: oversized cream knit cardigan, sage-green wide-leg trousers, dark brown high ponytail, thin black smartwatch on her left wrist; she keeps walking slowly away from the camera.
Objects: PHONE: a matte black smartphone 16 cm long and 7.7 cm wide with a square camera bump in one corner holding three round glass lenses.
Shot, 8 seconds, vertical 9:16: one continuous shot, no cuts. 0-2 s: medium shot at waist height directly behind the teacher as she walks slowly up the aisle: her hands are loosely clasped behind her lower back, cradling the phone horizontally (long edge level with the floor), its black back and three lenses facing straight at the camera. 2-5 s: the camera pushes smoothly in until the phone's camera bump fills the frame, the three lenses gleaming, a soft cyan glowing outline tracing the largest lens ring. 5-8 s: an extreme macro on the largest lens: in its curved dark glass we see a tiny, fish-eye-curved reflection of the bright classroom behind the camera, with students passing papers.
Opening frame: the teacher's back and clasped hands holding the horizontal phone, the bright exam hall around her.
Final frame: the lens glass filling the frame with the curved reflection of the classroom.
Camera: waist height (1 m), smooth steady dolly push-in from a medium shot to an extreme macro. Shallow depth of field.
Setting and light: the same bright exam hall: pale teal walls, light wood floor; bright soft high-key light, a glinting highlight on the lens glass, clean saturated colours.
Real-world scale: the phone spans both of her palms; each lens is about 1.5 cm across.
Sound: a deep sub-bass swell, a soft camera focus whirr and tick, slow footsteps on wood, quiet room tone. No music. No speech, no voices, no narration, no singing.
Avoid: …; the phone held upright; the screen facing the camera; a phone with one lens.
```

---
### C07 · 18.90–23.75 · "And as it recorded in 4K, it locked onto every single face in the room."
Use: 0.0–4.85 s.
```
[F-STYLE]
Characters: STUDENTS (seen on the phone screen): young-adult college students in white collared shirts passing papers at wooden desks. TEACHER: only her hands and cream cardigan cuffs at the edges of the frame.
Objects: PHONE: a matte black smartphone 16 cm long held horizontally, its bright screen showing a live camera view.
Shot, 8 seconds, vertical 9:16: a close-up looking down onto the phone's screen, held horizontally in the teacher's two hands behind her back, her fingers around its edges. The screen shows a live, wide-angle video view of the classroom behind her: students mid-cheat, passing papers across the aisle. 0-1 s: a small glowing red dot appears in the top-left corner of the screen. 1-5 s: thin bright yellow square outlines pop onto the students' faces one after another, snapping into place and following each face as they move, until every face on the screen is boxed. 5-8 s: the camera pushes slowly into the screen until the classroom view fills the frame.
Opening frame: the phone screen in her hands, the classroom view on it, no boxes yet.
Final frame: the screen view filling the frame, every face inside a yellow square.
Camera: high angle from just above her shoulder looking down at the screen; smooth slow push-in.
Setting and light: the screen glows bright and sharp; around it soft cream cardigan fabric; bright soft high-key light, clean saturated colours.
Real-world scale: the phone screen is about 15 cm wide; the students on it are tiny.
Sound: a soft electronic record chirp, a quick digital tick each time a yellow box locks on, a low tense sub-bass drone, quiet room tone. No music. No speech, no voices, no narration, no singing.
Avoid: …; any numbers, letters, timers or icons on the screen other than the red dot and yellow squares.
```

---
### C08 · 23.75–27.90 · "So by the time one kid looked up and saw the screen, it was already too late,"
Use: 0.0–4.15 s. The freeze lands at ~1.2 s in the clip (= 24.9 s, "looked up").
```
[F-STYLE]
Characters: FRINGE BOY: a college student about 19, neat side-swept black fringe, thick eyebrows, white short-sleeved collared shirt, navy trousers. Other students behind him in the same uniform.
Objects: a white exam paper with fine grey scribble lines in his outstretched hand.
Shot, 8 seconds, vertical 9:16: seen from the phone's point of view: low, at waist height, slightly wide-angle, looking straight at him. 0-1 s: FRINGE BOY leans across the aisle, grinning, mid-way through passing his paper to a classmate. 1-2 s: his eyes rise and lock straight into the camera lens. 2-3.5 s: he freezes completely: the grin melts away, his mouth falls open, his eyes go huge with horror, the paper slips from his fingers and flutters down. 3.5-8 s: a slow push-in on his frozen, horrified face while the students behind him, unaware, keep passing papers.
Opening frame: him grinning, arm stretched across the aisle with the paper.
Final frame: a close-up of his frozen horrified face, paper falling.
Camera: waist height (1 m), slight wide-angle lens, smooth slow push-in from a medium shot to a close-up.
Setting and light: the same bright exam hall: pale teal walls, sunlit windows, wooden desks; bright soft high-key light, clean saturated colours.
Real-world scale: seated, his head is at about 1.25 m, just above the camera.
Sound: a single deep sub-bass boom as he freezes, a paper fluttering down, the room going quiet except a ticking clock. No music. No speech, no voices, no narration, no singing.
```

---
### C09 · 27.90–31.95 · "and the only thing they passed that day was the paper… not the exam."
Use: 0.0–4.05 s. Slow motion. (Optional build grade: desaturate to near black and white from 28.0 s, as in the original script.)
```
[F-STYLE]
Characters: STUDENTS: eight young-adult college students about 19 in identical uniforms (white short-sleeved collared shirts, navy trousers or skirts), including a lanky boy with curly black hair and round glasses, a stocky boy with spiky brown hair and freckles, a boy with a side-swept black fringe, a girl with two long black braids. TEACHER: a young woman in her mid-20s, dark brown high ponytail, oversized cream knit cardigan, sage-green wide-leg trousers, a matte black phone in her hand.
Objects: white exam papers with fine grey scribble lines.
Shot, 8 seconds, vertical 9:16, everything in smooth slow motion: a wide view of the whole class from the front corner of the exam hall. 0-3 s: the students react all at once to being caught: the boy with glasses slaps both hands onto his head, the girl with braids buries her face in her hands, the spiky-haired boy slowly slides a paper under his desk, the fringe boy smiles sheepishly down at the floor; papers drift down through the air. 3-8 s: in the foreground at the front of the room the teacher calmly turns her head toward the class, raises one eyebrow and gives a tiny satisfied smile, the phone held loosely at her side.
Opening frame: the whole class frozen mid-cheat, papers in the air.
Final frame: the defeated class, the teacher's calm smile in the foreground.
Camera: head height in the front corner, a smooth slow push-in across the rows. Slow motion.
Setting and light: the same bright exam hall: pale teal walls, sunlit windows on the left, light wood floor, blank green chalkboard behind the teacher; bright soft high-key light, clean saturated colours.
Real-world scale: teacher 1.65 m standing; seated students' heads at about 1.25 m; desks 75 cm tall.
Sound: a slow-motion low whoosh, muffled, deep room tone, papers drifting, a slow heartbeat thump. No music. No speech, no voices, no narration, no singing.
```
**Loop:** not used on this one. The payoff needs the students' faces, and the opening camera (behind the teacher) can't see them. The line "…not the exam." lands hard and the Reel restarts on "The teacher turned her back…", which still reads as a loop.

## 7. Build notes
- Normalise the narration to −14 LUFS, cut at 31.95 s.
- Captions: 1–3 words, white heavy rounded sans, centred at 78% height.
- Pop-ups: red "REC ●" at 18.9 s, big "4K" at 19.9 s (lime, impact sound), "!" over FRINGE BOY at 24.9 s, "💀" at 30.9 s with "not the exam".
- Sound effects on top of the Veo sound: record scratch + sub-bass impact at 12.82, whoosh on every cut in 5.5–12.2.

## 8. Post captions
See `genz-teacher-captions.md`.
