"""Flow prompts for "378 Strangers Bought Each Other Coffee" (Zack look, docs/zack-structure.md).

    python make_prompts.py            -> output/drive-through-378_flow_prompts.md

Plan (2026-10-24, after two failed text-to-video tries): every clip animates an approved still (images/s1-s5.jpg,
made by hand in AI Studio from images.yaml): Flow Frames, Start = s<n>; C5 also End = s1 (loop). Cuts between clips.
"""
from pathlib import Path

EP = "drive-through-378"
WINDOWS = [(0.0, 7.56), (7.56, 12.47), (12.47, 20.59), (20.59, 27.57), (27.57, 35.24)]  # voiceover pauses, 2026-10-24

STYLE = Path(__file__).resolve().parents[2].joinpath("docs/zack-structure.md").read_text(encoding="utf-8") \
    .split("> ", 1)[1].split("\n", 1)[0]
MOTION = ("Smooth, natural motion with believable weight; the camera moves in one continuous smooth path, never shakes, "
          "never cuts, never jumps. Everything keeps exactly the same look for the whole clip.")
SHOP = ("THE COFFEE SHOP: a small modern drive-through coffee kiosk with smooth teal-painted walls, a white window frame "
        "and a wide sliding service window; inside, plain white counters and one bright ceiling light; NO signs, NO menu "
        "boards, NO logos, plain white paper cups with white lids and no printing; a smooth grey asphalt drive-through "
        "lane with a white kerb, a few palm trees and a clear blue Florida sky.")
BARISTA = ("THE BARISTA: a friendly man in his mid-20s with short black curly hair and a short neat beard, a plain teal cap, "
           "a plain white T-shirt and a plain navy apron with no logo; about 1.78 m tall; he stays inside the window.")
W1 = ("THE FIRST DRIVER: a woman about 40 with an auburn ponytail and a bright orange T-shirt, seated in the driver's "
      "seat of a small red hatchback with no logos.")
W2 = ("THE SECOND DRIVER: a different woman, about 30, with a short platinum-blonde bob and a lemon-yellow T-shirt, "
      "seated in the driver's seat of a light-blue sedan with no logos.")
W379 = ("THE LAST DRIVER: a woman about 55 with a grey bun and big black sunglasses, a plain white T-shirt, in a small "
        "mint-green car with no logos.")
GEOMETRY = ("GEOMETRY (how a real drive-through works): the service window is cut into the long SIDE wall of the kiosk, "
            "about 1 m above the ground. The lane runs straight along that side wall. Cars drive along the lane PARALLEL to "
            "the wall, nose pointing forward along the lane, and stop with the DRIVER'S DOOR (the car's left side) right "
            "beside the service window, about an arm's length from the wall. The driver's side window is rolled down and "
            "the driver stays seated inside her car; the barista stays inside the kiosk; they pass cups and cards "
            "SIDEWAYS through the gap between the car window and the service window. A car's windshield NEVER faces the "
            "window and a car NEVER drives toward the wall. Waiting cars queue nose-to-tail behind it in the same lane.")
SCALE = "Real-world scale: people 1.6-1.8 m; cars about 4-4.5 m long; a coffee cup about 15 cm tall."
COMP = ("Composition: vertical 9:16; the main subject in the middle of the frame; keep the bottom quarter simple "
        "(captions go there) and nothing important in the top-right corner (logo).")
AVOID = ("Avoid: any text, letters, numbers or logos anywhere (cups, signs, cars, aprons, the window); menu boards; "
         "brand colours of real coffee chains; warm golden or sunset light; lens flares; blur or depth of field; "
         "cartoon style or big cartoon eyes; extra fingers; warped faces; people changing into other people; "
         "morphing cars; any cut inside the clip; music; any speech, voices or narration.")
NO_SPEECH = "No music. No speech, no voices, no narration."

LOOK = ("Keep EXACTLY the look of the attached start frame for the whole clip: realistic 3D video-game cutscene render "
        "(not cartoon, not Pixar, not a photograph), the same people, faces, clothes, kiosk, colours, light and framing.")
STILL = ("Every car stays exactly where it is unless the shot says it moves; a car that moves only drives FORWARD (nose "
         "first), never backwards, never sideways, never turns around. People move only a little, like real people.")
GEO_SHORT = ("GEOMETRY: the service window is in the kiosk's side wall; cars stop parallel to that wall, driver's side "
             "at the window; drivers stay seated in their cars; the barista stays inside the kiosk.")

CLIPS = [
    dict(id="C1", start="s1.jpg", end=None,
         voice="A woman at a coffee drive-through paid for her iced coffee... and then for the stranger's caramel macchiato in the car behind her.",
         shot="""0-2.5 s: the camera pushes in slowly toward the gap between the car and the service window; the first driver takes the iced-coffee cup from the barista and smiles.
2.5-5.0 s: she holds out a plain card to him and points her thumb back over her shoulder, toward the car behind her (off screen); the barista's eyebrows rise in surprise.
5.0-7.6 s: the barista breaks into a big grin, takes the card and nods, glancing past her toward the car behind; she smiles back. End on a steady picture.""",
         camera="One slow, steady push-in from the start frame's position. No cuts, no other camera moves.",
         sound="A car engine idling, ice rattling in the cup, a card reader beep, a surprised little laugh (no words).",
         must="The red car never moves; mouths stay closed (no talking)."),
    dict(id="C2", start="s2.jpg", end=None,
         voice="So that driver paid for the next car. And that driver paid for the one after that.",
         shot="""0-2.5 s: inside the kiosk, the barista takes the plain card from the second driver; she laughs, delighted, with a hand on her chest.
2.5-5.0 s: she points her thumb back over her shoulder at the car behind her (off screen) and nods firmly: she will pay for them too.
5.0-7.6 s: the barista grins and gives her a thumbs-up; she smiles. End on a steady picture.""",
         camera="A slow push-in toward the window over the barista's shoulder. No cuts.",
         sound="A card reader beep, a soft delighted laugh (no words), a car engine idling, birds outside.",
         must="The light-blue car never moves; she stays seated; mouths closed (no talking)."),
    dict(id="C3", start="s3.jpg", end=None,
         voice="The baristas started counting, and told every driver how long the chain was. You see, now nobody wanted to be the one who broke it.",
         shot="""0-2.5 s: the barista finishes the tally line on the whiteboard and caps the marker, grinning.
2.5-5.0 s: he turns to the service window and holds up both hands with all ten fingers spread toward the driver of the white car, eyebrows raised (showing how long the chain is, no talking); the second barista laughs.
5.0-7.6 s: the driver's eyes widen, he nods firmly and holds out a plain card through his window: he is not going to break the chain. End on a steady picture.""",
         camera="A slow, gentle push-in toward the barista and the window. No cuts.",
         sound="A marker squeak, a cap click, soft laughter (no words), a card reader beep.",
         must="The whiteboard shows ONLY straight tally lines (no digits, no letters) and keeps its marks; the white car never moves; mouths closed."),
    dict(id="C4", start="s4.jpg", end=None,
         voice="For eleven hours, car after car kept paying. 378 people in a row.",
         shot="""0-7.6 s: time-lapse from high above: every parked car stays exactly where it is; only the shadows of the cars, palm trees and kiosk sweep slowly across the ground as the sun moves through the day, and a few tiny white cups flash at the service window. The camera slowly rises higher and pulls back, so the long line of cars looks even longer. End on a steady picture.""",
         camera="One slow, smooth rise and pull-back. No cuts.",
         sound="A gentle ticking clock, a soft whoosh of time passing, distant engines idling, birds.",
         must="No car moves, appears or disappears; no people grow or change; the kiosk keeps exactly the same look."),
    dict(id="C5", start="s5.jpg", end="s1.jpg",
         voice="Finally, at six in the evening, a woman pulled up, heard her coffee was already paid for... and just paid for her own, and drove off.",
         shot="""0-2.5 s: the barista, beaming, holds out the cup and waves his other hand to show it is already paid; the last driver looks confused.
2.5-4.5 s: she politely shakes her head, puts a few coins in his open palm and takes the cup.
4.5-6.0 s: her mint-green car drives slowly FORWARD (away from the camera, nose first) along the lane past the window and out of the picture; the barista freezes, jaw dropped, coins still in his open hand.
6.0-7.6 s: a small red hatchback drives in FORWARD from behind the camera into exactly the same spot beside the window, and the picture settles exactly into the attached end frame.""",
         camera="A fixed camera at the start frame's position (no camera movement), so the clip lands exactly on the end frame.",
         sound="Coins clinking, a cup handed over, a small car pulling away, a beat of stunned silence, a new car rolling up.",
         must="Every car only drives forward; the clip ENDS EXACTLY on the attached end frame; mouths closed."),
]


def prompt(c):
    first = ("Animate starting EXACTLY from the attached start frame and end EXACTLY on the attached end frame."
             if c["end"] else "Animate starting EXACTLY from the attached start frame.")
    lines = [first, LOOK, MOTION, STILL, GEO_SHORT, "Shot, 8 seconds, vertical 9:16:", c["shot"],
             "Camera: " + c["camera"], SCALE, COMP, "Sound: " + c["sound"] + " " + NO_SPEECH, AVOID,
             "Must be true: " + c["must"]]
    return "\n".join(lines)


out = [f"# {EP}: Flow video prompts (from the approved stills)\n",
       "Every clip: Flow → Video → **Frames**, Veo 3.1 Fast, 9:16, x1 (20 credits). 5 clips = 100 credits "
       "(40 already spent on the two text-to-video tries). Download 1080p.\n",
       "Stills: episodes\\drive-through-378\\images\\s1.jpg ... s5.jpg (approved 2026-10-24).\n"]
for i, c in enumerate(CLIPS):
    a, b = WINDOWS[i]
    frames = f"Start = {c['start']}" + (f", End = {c['end']}" if c["end"] else ", End = none")
    out.append(f"\n### {c['id']}: {frames}\nUsed: {a:.2f}-{b:.2f} s  \nVoice over it: \"{c['voice']}\"\n\n```\n"
               f"{prompt(c)}\n```\n")
p = Path(__file__).parent / "output" / f"{EP}_flow_prompts.md"
p.write_text("".join(out), encoding="utf-8")
print("wrote", p)
