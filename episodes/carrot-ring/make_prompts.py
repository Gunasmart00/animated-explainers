"""Flow video prompts for "Her Lost Wedding Ring Grew On A Carrot" (Zack look).

    python make_prompts.py   -> output/carrot-ring_flow_prompts.md

Every clip animates an approved still (images/s1-s6.jpg): Flow Frames, Start = s<n>; C6 also End = s1 (loop).
The voice windows are shorter than 8 s, so the important action happens in each clip's first ~5 s (the build uses the
start of each clip). C6 is sped up to its window before the build (see STATUS.md) so it still lands on s1.
"""
from pathlib import Path

EP = "carrot-ring"
WINDOWS = [(0.0, 8.12), (8.12, 13.30), (13.30, 19.13), (19.13, 25.56), (25.56, 30.99), (30.99, 36.68)]  # 2026-10-25

LOOK = ("Keep EXACTLY the look of the attached start frame for the whole clip: realistic 3D video-game cutscene render "
        "(not cartoon, not Pixar, not a photograph), the same people, faces, hair, clothes, place, colours, light and "
        "framing.")
MOTION = ("Smooth, natural motion with believable weight; the camera moves in one continuous smooth path, never shakes, "
          "never jumps. People move like real people (no exaggerated cartoon acting); nobody looks into the camera.")
RING = ("THE RING: a plain white-gold band with seven tiny diamonds set flush in a row; it always looks exactly the same, "
        "about 2 cm across (real size).")
COMP = ("Composition: vertical 9:16; the main subject in the middle of the frame; keep the bottom quarter simple "
        "(captions go there) and nothing important in the top-right corner (logo).")
NO_TALK = "No music. No talking, no words, no narration."
AVOID = ("Avoid: any text, letters, numbers or logos anywhere; cartoon style or big cartoon eyes; extra fingers; warped "
         "hands or faces; people changing into other people; a second ring; the ring changing size or design; warm "
         "golden or sunset light; lens flares; blur or depth of field; music; any talking.")

CLIPS = [
    dict(id="C1", start="s1.jpg", end=None,
         voice="A woman almost threw away a tiny carrot from her garden... then she saw what was wrapped around it. Her wedding ring.",
         shot="""0-2.0 s: the camera pushes in slowly; Lena starts to toss the tiny carrot onto the pile, then stops mid-throw: something glinted.
2.0-4.5 s: she turns the carrot in her gloved fingers and brings it close to her face: the white-gold ring is wrapped tightly around the top of the carrot, where the green leaves meet the orange root (it was hidden behind the leaves); her eyes go wide.
4.5-7.6 s: she gasps, mouth wide open in a joyful shriek, and presses the carrot to her chest, laughing in disbelief. End on a steady picture.""",
         camera="One slow, steady push-in toward her face and the carrot. No cuts.",
         sound="Birds, rustling leaves, a soft magical glint, a gasp and a short happy shriek (no words).",
         must="The ring is ON THE CARROT (around its top), never on her finger; she stays kneeling at the same bed."),
    dict(id="C2", start="s2.jpg", end=None,
         voice="Sixteen years earlier, she'd set it down while doing her Christmas baking... and it vanished.",
         shot="""0-2.0 s: young Lena rolls the gingerbread dough, smiling; the camera slowly pushes in toward the ring lying on the counter beside the peelings bowl.
2.0-4.0 s: still looking at her dough, she sweeps the loose peelings and crumbs on the counter into the bowl with the side of her hand, in one quick sweep; the ring is swept along with them and drops INTO the bowl, hidden under the peelings. She does not notice.
4.0-7.6 s: she picks up the bowl and carries it out of the picture to the left; the counter where the ring lay is now completely EMPTY. End on a steady picture of the empty counter.""",
         camera="A slow push-in toward the ring and the bowl. No cuts.",
         sound="A rolling pin on dough, peelings swept into a bowl, a tiny metallic clink, a quiet Christmas-kitchen room tone.",
         must="After 4 s there is NO ring anywhere on the counter (it is inside the bowl); there is only ever one ring and it never changes design; she does not notice."),
    dict(id="C3", start="s3.jpg", end=None,
         voice="She searched everywhere. Years later, they even pulled up the kitchen floor. Nothing.",
         shot="""0-2.5 s: Ola heaves on the crowbar and the floorboard lifts with a creak; Lena leans in, shining the flashlight into the gap under the floor.
2.5-4.5 s: both peer into the gap, hopeful; the beam sweeps across dust and wooden joists: nothing there.
4.5-7.6 s: their shoulders drop; Lena sighs and sits back on her heels; Ola shakes his head. End on a steady picture.""",
         camera="A slow, gentle push-in toward the gap in the floor. No cuts.",
         sound="A creaking floorboard, a crowbar clink, a sigh (no words).",
         must="Nothing is found under the floor; the same two people throughout."),
    dict(id="C4", start="s4.jpg", end=None,
         voice="You see, it had probably fallen in with the vegetable peelings, gone into the compost, and been spread over the garden.",
         shot="""0-2.0 s: the peelings tumble from the bowl into the green compost bucket; the ring glints once and disappears under them.
2.0-4.0 s: the camera dives smoothly down into the bucket; the peelings darken and crumble into rich dark compost (a time-lapse transformation, no cut).
4.0-7.6 s: the camera rises out of the compost into the autumn garden behind the red house: a garden shovel spreads the dark compost over the vegetable bed, and a tiny glint of the ring disappears into the soil. End on a steady picture.""",
         camera="One continuous move: down into the bucket, then up and out into the garden (a smooth transition, no cut).",
         sound="Peelings dropping, a soft whoosh into the bucket, a shovel scraping, compost thudding onto soil.",
         must="The ring falls INTO the bucket with the peelings; the garden at the end is the same garden as the opening shot."),
    dict(id="C5", start="s5.jpg", end=None,
         voice="Then a single carrot seed landed right in the middle of it... and grew straight through.",
         shot="""0-7.6 s: time-lapse in the same underground cutaway view: the tiny carrot sprout grows; its root pushes down through the middle of the ring; the orange carrot swells and thickens until it fills the ring and the ring sits tight around its top, while feathery green leaves rise above the soil and the birch leaves in the background turn from green to yellow. End on a steady picture of the grown carrot with the ring around its top.""",
         camera="A fixed camera (only the growth is time-lapsed). No cuts.",
         sound="A soft growing creak, gentle magical chimes, a light breeze.",
         must="The ring stays the same size and in the same place; exactly one carrot grows through it."),
    dict(id="C6", start="s6.jpg", end="s1.jpg",
         voice="Finally, she had her ring back. But after sixteen years... it didn't fit anymore.",
         shot="""0-2.5 s: Lena pushes and twists the ring, but it will not go past her knuckle; she stares at it, puzzled; Anna laughs.
2.5-5.0 s: Lena laughs too and shrugs, slips the ring into her cardigan pocket and puts her green gardening gloves back on; Anna walks out of the picture to the right, toward the house.
5.0-7.6 s: Lena kneels back down at the carrot bed, pulls up another tiny carrot and holds it up with a slightly disappointed face, settling exactly into the attached end frame.""",
         camera="A fixed camera at the start frame's position, easing slightly so the clip lands exactly on the end frame.",
         sound="A small laugh from both (no words), birds, a carrot pulled from the soil.",
         must="The clip ENDS EXACTLY on the attached end frame (Lena alone, kneeling, holding up a tiny carrot)."),
]


def prompt(c):
    first = ("Animate starting EXACTLY from the attached start frame and end EXACTLY on the attached end frame."
             if c["end"] else "Animate starting EXACTLY from the attached start frame.")
    return "\n".join([first, LOOK, MOTION, RING, "Shot, 8 seconds, vertical 9:16:", c["shot"], "Camera: " + c["camera"],
                      COMP, "Sound: " + c["sound"] + " " + NO_TALK, AVOID, "Must be true: " + c["must"]])


out = [f"# {EP}: Flow video prompts (from the approved stills)\n",
       "Every clip: Flow → Video → **Frames**, Veo 3.1 Fast, 9:16, x1 (20 credits). 6 clips = 120 credits. "
       "Download 1080p.\n"]
for i, c in enumerate(CLIPS):
    a, b = WINDOWS[i]
    frames = f"Start = {c['start']}" + (f", End = {c['end']}" if c["end"] else ", End = none")
    out.append(f"\n### {c['id']}: {frames}\nUsed: {a:.2f}-{b:.2f} s ({b - a:.1f} s)  \nVoice over it: \"{c['voice']}\"\n\n"
               f"```\n{prompt(c)}\n```\n")
p = Path(__file__).parent / "output" / f"{EP}_flow_prompts.md"
p.write_text("".join(out), encoding="utf-8")
print("wrote", p)
