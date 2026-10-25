"""Flow prompts for "Could We Stop An Asteroid?" (owner 2026-10-25: no keyframe stills; one chained, camera-heavy flight).

    python make_prompts.py   -> output/asteroid-dart_flow_prompts.md

C1: Flow Ingredients (real reference pictures). C2-C7: Flow Frames, Start = the frame Claude cuts the previous clip at
(images/cut_cN.jpg, saved after review). C7 also End = C1's first frame (seamless loop).
Only what is in each shot is named (whale lesson). Cap 200 credits: 7 clips = 140.
"""
from pathlib import Path

EP = "asteroid-dart"
# voiceover 42.92 s, silencedetect 2026-10-25
WINDOWS = [(0.0, 7.28), (7.28, 14.16), (14.16, 20.94), (20.94, 26.67), (26.67, 32.55), (32.55, 39.28), (39.28, 42.92)]

LOOK1 = ("Render everything as a realistic 3D video-game cinematic (a modern game-engine cutscene, not a photograph, "
         "not a cartoon): crisp, clean surfaces, bright high-key light with the sunlit side of everything facing the "
         "camera, black space with faint stars, everything in sharp focus, no grain.")
LOOK = ("Continue EXACTLY the look of the attached start frame: the same realistic 3D video-game cinematic render, the "
        "same colours, light and level of detail (not a photograph, not a cartoon).")
MOTION = ("Cinematic and fast: the camera never stops moving; one continuous, smooth, unbroken camera move with no "
          "cuts and no shaking. Objects keep their real sizes and shapes.")
CRAFT = ("THE SPACECRAFT: a gold-foil box the size of a vending machine with one round dish antenna and one camera lens "
         "on its front, and two long, thin, flat dark-blue solar panels sticking straight out on opposite sides (each "
         "about seven times as long as the box).")
PAIR = ("THE ASTEROIDS: a big grey asteroid shaped like a spinning top with a ridge around its middle, and a small "
        "egg-shaped grey moonlet made of loose boulders circling it (about one fifth of its size).")
COMP = ("Composition: vertical 9:16; the main subject in the middle; keep the bottom quarter simple (captions go there) "
        "and nothing important in the top-right corner (logo).")
NO_TALK = "No music. No talking, no narration."
AVOID = ("Avoid: any text, letters, numbers, flags or logos anywhere (no agency logos on the spacecraft or buildings); "
         "a second Earth or any extra planet; faces or eyes on any object; dark or underexposed pictures; "
         "anything not listed in this clip appearing; objects changing shape; fire or flames in space; cartoon style; "
         "blur or depth of field; lens flares; music; talking.")

CLIPS = [
    dict(id="C1", mode="Ingredients", frames="Ingredients: the asteroid picture + the Earth picture (take 2)",
         voice="If an asteroid was heading straight for Earth... could we actually stop it? / In the movies, we'd just nuke it.",
         cast=("In this clip there is exactly: ONE asteroid, ONE Earth and ONE rocket. There is only ever one Earth; no "
               "second planet, no moon."),
         layout=("FRAME LAYOUT (from 2 s to the end): the Earth is ALWAYS in the lower half of the picture and the "
                 "asteroid is ALWAYS in the upper half; they never overlap and never pass in front of each other. "
                 "SCALE: the Earth is a whole planet; the asteroid is a mountain-sized rock, far smaller than the Earth, "
                 "and only looks big because it is much closer to the camera."),
         shot="""0-2.0 s: the asteroid's bright, sunlit grey rocky surface fills the whole picture; the camera glides fast just above the rocks.
2.0-4.3 s: the camera pulls straight back: the whole tumbling asteroid appears in the upper half of the picture, and far below it, in the lower half, the bright blue Earth comes into view; the asteroid drifts slowly downward, toward the Earth.
4.3-7.3 s: from the Earth's surface in the lower half, one white rocket with a thin white exhaust trail climbs straight UP, away from the Earth, toward the asteroid. At the same time the camera descends toward the Earth, so the rocket rises past the camera and leaves through the top of the picture. At 7.3 s the Earth's sunlit blue oceans and white clouds fill the lower two thirds of the picture.
7.3-8.0 s: hold that picture, the camera still drifting slowly down toward the Earth.""",
         camera="Glide, straight pull-back reveal, then a steady descent toward the Earth. One continuous move.",
         must=("Exactly one Earth, always below the asteroid; the rocket only ever moves upward, away from the Earth; "
               "nothing explodes; the picture stays bright.")),
    dict(id="C2", mode="Frames", frames="Start = images/cut_c1.jpg (C1 at 7.25 s)",
         voice="In 2022, NASA decided to find out for real. / They built a spacecraft the size of a vending machine...",
         cast=("In this clip there is exactly: the Earth (seen from space, then from the air), one plain white "
               "building, two engineers and one spacecraft."),
         layout=("START FRAME: the Earth fills the picture (North America on the left, the Atlantic in the middle, "
                 "Africa on the right) with one small asteroid floating in space in front of the ocean. The asteroid "
                 "stays out in space: as the camera descends it slides up and out of the top of the picture in the "
                 "first second and is never seen again."),
         shot="""0-2.0 s: the camera dives toward the east coast of North America on the left side of the picture; the coastline grows larger.
2.0-3.2 s: the camera plunges through a layer of white clouds and swoops down over green trees toward one plain white two-storey building with a large open door (no signs, no logos), and flies in through the door.
3.2-6.9 s: inside a bright white clean room with a grey floor, the camera glides past two engineers in full white clean-room suits, hoods and face masks, and reveals the small spacecraft standing on a low metal stand between them: a gold-foil box the size of a vending machine (its body reaches only to their chest) with one round dish antenna and one round camera lens on its front face; its two solar panels are rolled up into thin white cylinders fixed to its two sides. The camera ends in a slow push-in toward the spacecraft's single round camera lens on its front face.""",
         camera="Dive, plunge through the clouds, swoop in through the door, glide past the engineers, push in. One continuous move.",
         must=("The asteroid leaves the picture in the first second and never returns; exactly two engineers; the "
               "spacecraft is a vending-machine-sized box with its two solar panels ROLLED UP as thin white cylinders "
               "on its sides (not unfolded) indoors; no logos or writing anywhere.")),
    dict(id="C3", mode="Frames", frames="Start = images/cut_c2.jpg (C2 at 6.85 s)",
         voice="...and flew it seven million miles. / Its target: a harmless asteroid as wide as a football stadium.",
         cast=("In this clip there is exactly: (indoors, first second only) the spacecraft; then in space: the SAME "
               "spacecraft, one tiny shoebox-sized satellite, one big asteroid and one small moonlet. No engineers, no "
               "room and no Earth after the first second."),
         layout=("START FRAME: indoors, a close view of the gold-foil spacecraft (dish antenna on a short mast on top, two "
                 "round lenses on its front, solar panels rolled up as cylinders on its sides) with two engineers "
                 "behind it. IN SPACE the spacecraft keeps exactly the same gold-foil body, dish and lenses; it flies "
                 "AWAY from the camera, in the lower third of the picture; the two asteroids are far ahead in the "
                 "upper middle of the picture, small."),
         shot="""0-1.0 s: the camera pushes straight into the spacecraft's upper round lens until the lens fills the picture and everything goes black.
1.0-2.2 s: out of the black: deep space with stars; the camera is directly behind the same spacecraft as it flies away from the camera; its two rolled-up panels unroll into two long, flat, narrow dark-blue solar panels that stick straight out to the left and right (each about five times as long as the box).
2.2-6.8 s: chase camera following just behind and slightly above the spacecraft, faint stars streaming past; the camera slides out to the right of the spacecraft and reveals, far ahead in the upper middle of the picture, a big grey asteroid shaped like a spinning top with a small egg-shaped grey moonlet beside it (about one fifth of its size). A tiny shoebox-sized satellite with two little solar wings detaches from the underside of the spacecraft and drifts back, small, on the left.""",
         camera="Push into the lens, black, emerge behind the craft, chase, slide out to the right. One continuous move.",
         pair=True,
         must=("The same gold-foil spacecraft before and after the black; it always flies away from the camera, toward "
               "the asteroids; exactly one big asteroid and one small moonlet; no Earth, no people and no room in space.")),
    dict(id="C4", mode="Frames", frames="Start = images/cut_c3.jpg (C3 at 6.75 s)",
         voice="Fourteen thousand miles per hour. One shot... / It smashed straight into it.",
         cast=("In this clip there is exactly: the same gold spacecraft, the tiny satellite far behind on the left, "
               "the big cone-shaped asteroid and the small round moonlet."),
         layout=("START FRAME: the gold spacecraft is in the lower middle of the picture, seen from behind, flying away "
                 "from the camera; the big cone-shaped grey asteroid is at the top left; the small round bumpy moonlet "
                 "is to its right; the tiny satellite is on the left. The spacecraft's target is the SMALL moonlet, "
                 "never the big asteroid."),
         shot="""0-2.0 s: the spacecraft speeds straight toward the small moonlet; the camera follows close behind it and the moonlet grows fast in the middle of the picture; the big asteroid slides out of the left side of the picture.
2.0-3.4 s: slow motion: the moonlet's grey boulder-covered surface fills the picture; the spacecraft is a small dark silhouette just in front of it.
3.4-4.2 s: the spacecraft hits the middle of the moonlet's surface: one bright white flash at the impact point.
4.2-7.0 s: the flash fades into a huge fan-shaped spray of grey dust and boulders blasting outward from the moonlet; the camera recoils backward; the moonlet is still in one piece.""",
         camera="Chase close behind, slow-motion push, impact, recoil backward. One continuous move.",
         must=("Only the small moonlet is hit (the big asteroid is untouched and off to the left); the moonlet does not "
               "shatter or break apart; the tiny satellite stays far away; no fire, only a white flash and grey dust.")),
    dict(id="C5", mode="Frames", frames="Start = images/cut_c4.jpg (C4 at 5.7 s)",
         voice="But here's the thing: the plan was never to blow it up. Just to nudge it, so it would miss us.",
         cast=("In this clip there is exactly: grey dust and rocks (at the start), ONE small round moonlet asteroid "
               "with a dust tail, and ONE bigger round grey asteroid. No spacecraft, no fire."),
         layout=("START FRAME: the camera is inside a cloud of grey dust and boulders flying toward it. SCALE: the "
                 "moonlet is about one fifth the size of the bigger asteroid it circles. The moonlet stays in ONE PIECE "
                 "the whole clip."),
         shot="""0-2.5 s: the camera flies backward out of the dust cloud; the dust thins and the small round moonlet is revealed in one piece in the middle of the picture, with a long grey plume of dust streaming off one side of it like a comet tail.
2.5-5.9 s: the camera keeps pulling back and rises; the bigger round grey asteroid comes into view on the left; the moonlet, still trailing its dust tail, is pushed slightly sideways along its curved path around the bigger asteroid. End on a wide view of both asteroids, the moonlet on the right.""",
         camera="One long, smooth backward pull-out of the dust, rising at the end.",
         must=("The moonlet is whole (not shattered, not exploding); exactly two asteroids, the moonlet much smaller; "
               "grey dust only, no fire, no flames, no orange glow; no spacecraft.")),
    dict(id="C6", mode="Frames", frames="Start = images/cut_c5.jpg (C5 at 5.85 s)",
         voice="NASA only needed its orbit to change by seventy-three seconds. / It changed by thirty-two minutes.",
         cast=("In this clip there is exactly: ONE big round asteroid, ONE small moonlet, and two thin glowing circle "
               "lines (one cyan, one orange). No spacecraft, no other rocks."),
         layout=("START FRAME: the big round grey asteroid fills the left side; the small moonlet is to its right with a "
                 "grey dust trail curving around the big asteroid. FROM 2 s: seen from straight above, the big asteroid "
                 "is in the CENTRE of the upper two thirds of the picture; both circle lines are centred on it; the "
                 "orange circle is slightly SMALLER than the cyan one and sits just inside it."),
         shot="""0-2.0 s: the camera rises fast and tilts down until it looks straight down on the big asteroid; the grey dust thins away.
2.0-3.5 s: the small moonlet circles the big asteroid, and a thin glowing cyan line draws itself along its path, making one full circle around the big asteroid.
3.5-6.7 s: the moonlet shifts slightly inward, and a thin glowing orange line draws a second circle just inside the cyan one, a little smaller; the moonlet now travels along the orange circle. The camera turns slowly around the centre.""",
         camera="Fast rise to a top-down view, then a slow turn around the centre.",
         must=("Exactly two circle lines, both centred on the big asteroid, the orange one slightly smaller and inside "
               "the cyan one; only one moonlet; no text, no numbers, no arrows.")),
    dict(id="C7", mode="Frames", frames="Start = images/cut_c6.jpg (C6 at 6.7 s), End = images/c1_first.jpg (C1's first frame, loop). Build uses 4.36-8.0 s",
         voice="So... could we stop an asteroid? We already moved one.",
         cast=("In this clip there is exactly: ONE big round asteroid, ONE small moonlet and the two glowing circle "
               "lines (which fade away). No spacecraft."),
         layout=("START FRAME: seen from straight above, the big round asteroid in the centre with a cyan circle and "
                 "an orange circle around it. END FRAME: a close view skimming just above a grey boulder-covered "
                 "surface. The camera dives onto the BIG asteroid in the centre."),
         shot="""0-4.4 s: the camera keeps looking straight down and turns slowly around the centre; the two glowing circles slowly fade away; the moonlet keeps circling.
4.4-8.0 s: the camera dives fast straight down onto the big asteroid in the centre, its grey boulder surface rushing up, and levels out to skim just above the rocks, settling exactly into the attached end frame.""",
         camera="Slow turn from above, then one fast dive that lands exactly on the end frame.",
         must="The dive ends exactly on the attached end frame; no text, no fire, no spacecraft."),
]


def prompt(c):
    lines = [("Use the attached pictures only as references for the asteroid's rocky surface and for the Earth. " + LOOK1)
             if c["mode"] == "Ingredients" else
             ("Animate starting EXACTLY from the attached start frame" +
              (" and end EXACTLY on the attached end frame. " if "End =" in c["frames"] else ". ") + LOOK),
             MOTION, c["cast"]] + ([c["layout"]] if c.get("layout") else [])
    if c.get("craft"):
        lines.append(CRAFT)
    if c.get("pair"):
        lines.append(PAIR)
    lines += ["Shot, 8 seconds, vertical 9:16:", c["shot"], "Camera: " + c["camera"], COMP,
              "Sound: deep cinematic space rumble and whooshes that follow the camera. " + NO_TALK, AVOID] + (
        ["Must be true: " + c["must"]] if c.get("must") else [])
    return "\n".join(lines)


out = [f"# {EP}: Flow prompts (chained, no stills)\n",
       "C1: Flow → Video → **Ingredients**, Veo 3.1 Fast, 9:16, x1. C2-C7: **Frames**, Start = the frame Claude cuts "
       "the previous clip at. 7 clips = 140 credits (cap 200). Download **1080p**.\n"]
for i, c in enumerate(CLIPS):
    a, b = WINDOWS[i]
    out.append(f"\n### {c['id']} ({c['mode']}): {c['frames']}\nVoice window {a:.2f}-{b:.2f} s ({b - a:.1f} s): "
               f"\"{c['voice']}\"\n\n```\n{prompt(c)}\n```\n")
p = Path(__file__).parent / "output" / f"{EP}_flow_prompts.md"
p.write_text("".join(out), encoding="utf-8")
print("wrote", p)
