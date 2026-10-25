"""Flow video prompts for "A Whale Pushed A Diver Away From A Shark" (Zack look).

    python make_prompts.py   -> output/whale-shark_flow_prompts.md

Every clip animates an approved still (images/s1-s8.jpg): Flow Frames, Start = s<n>, no End frame. The loop is a soft
cut: C8 ends on the notched fluke ("It was the same whale") and the video restarts on S1, the same whale.
The voice windows are short, so each clip's key action happens in its first seconds (the build uses the clip start).
"""
from pathlib import Path

EP = "whale-shark"
WINDOWS = [(0.0, 6.75), (6.75, 13.95), (13.95, 17.32), (17.32, 23.16), (23.16, 27.14), (27.14, 30.70),
           (30.70, 35.58), (35.58, 40.28)]  # voiceover pauses, 2026-10-25

LOOK = ("Keep EXACTLY the look of the attached start frame for the whole clip: realistic 3D video-game cutscene render "
        "(not cartoon, not Pixar, not a photograph), the same woman, whale, shark, boat, water colour, light and framing.")
MOTION = ("Smooth, natural motion with real weight: the whale moves slowly and powerfully like a real 30-ton animal, "
          "the shark glides with slow side-to-side tail strokes, the woman moves like a real swimmer. The camera moves in "
          "one continuous smooth path, never shakes, never jumps, never cuts. Nobody looks into the camera.")
SIZES = ("Real sizes all the time: the humpback is 14 m long (more than eight times the woman's height, its head alone "
         "longer than she is tall); the tiger shark is 4.5 m (nearly three times her height).")
WOMAN = "The woman wears a black wetsuit, ONE clear dive mask on her face, an orange snorkel and orange fins."
COMP = ("Composition: vertical 9:16; the main subject in the middle of the frame; keep the bottom quarter simple "
        "(captions go there) and nothing important in the top-right corner (logo).")
NO_TALK = "No music. No talking, no words, no narration, no screaming."
AVOID = ("Avoid: any text, letters, numbers or logos anywhere; blood or bites; the shark touching anyone; extra whales, "
         "people, fish or sharks (there is only ever ONE shark); new white spots or marks appearing on the whale's skin; animals or people changing shape, size or colour; the whale's scar moving or disappearing; "
         "cartoon style or big cartoon eyes; extra fingers or fins; murky or dark water; warm golden or sunset light; "
         "lens flares; blur or depth of field; music; any talking.")

CLIPS = [
    dict(id="C1", start="s1.jpg",
         voice="A 25-ton whale wouldn't stop shoving this scientist through the water... and she thought it was going to kill her.",
         shot="""0-2.5 s: the whale's huge head pushes forward and shoves the woman sideways through the water; she tumbles, arms flailing, a burst of bubbles from her snorkel, eyes wide with fear.
2.5-5.0 s: she kicks hard to get away, but the whale glides after her and nudges her again with its bumpy head, pushing her further.
5.0-7.6 s: she twists to look back at the enormous eye right next to her, terrified. End on a steady picture.
The whole clip: exactly ONE shark, the same tiny faint shape far below in the deep blue; it never comes closer, never gets bigger, and no other sharks or fish appear. The whale's skin stays exactly as in the start frame (dark blue-grey, one pale scar on top of the head, no white spots).""",
         camera="The camera drifts sideways with them, keeping both in the frame. No cuts.",
         sound="Deep underwater rumble, a muffled whale moan, bubbles, the woman's fast breathing through her snorkel.",
         must="The whale only pushes with its closed head (mouth closed, never biting); the shark stays faint and far below."),
    dict(id="C2", start="s2.jpg",
         voice="For ten minutes, it pushed her with its head, tucked her under its giant fin... and even lifted her out of the water.",
         shot="""0-2.5 s: the whale swims slowly upward with the woman held snugly under its long white pectoral fin against its grooved belly; she pushes at the fin with both hands.
2.5-5.0 s: the fin hugs her tighter as the whale rises toward the bright surface.
5.0-7.6 s: the whale's head and fin break the surface and lift her up out of the water, water pouring off them both, then lower her gently back. End on a steady picture.""",
         camera="The camera rises with them toward the surface. No cuts.",
         sound="A deep whale moan, rushing water, a big splash as they break the surface, the woman gasping (no words).",
         must="She stays held by the same white fin; the whale is always far bigger than her; one woman, one whale."),
    dict(id="C3", start="s3.jpg",
         voice="Bruised and terrified, she swam for her boat. Then she saw why.",
         shot="""0-3.4 s: the woman swims hard toward the boat with fast strokes, splashing; the two men lean over the side reaching for her; the whale's head and white fin stay right beside her.
3.4-7.6 s: she reaches the boat and the men grab her arms and start to pull her up; she looks back at the water. End on a steady picture.""",
         camera="The camera follows behind her at the waterline, slowly. No cuts.",
         sound="Splashing strokes, heavy breathing, the boat's engine idling, waves lapping (no words).",
         must="The boat stays in place; the whale does not hit the boat; nobody falls in."),
    dict(id="C4", start="s4.jpg",
         voice="Then she saw why. A fifteen-foot tiger shark was lurking right next to them.",
         shot="""0-3.0 s: the tiger shark glides slowly across the frame from left to right, close to the camera, its stripes and blunt snout clear; it turns its head up toward the woman above.
3.0-5.8 s: the humpback rolls its huge body between the shark and the woman, spreading its white pectoral fin like a wall; the woman kicks up to the boat's hull above.
5.8-7.6 s: the shark circles slowly below the whale. End on a steady picture.""",
         camera="A slow, low-angle drift looking up toward the surface. No cuts.",
         sound="A low, tense underwater drone, the swish of the shark's tail, the whale's deep moan, muffled kicks.",
         must="The shark never touches or bites anyone; the whale stays between the shark and the woman."),
    dict(id="C5", start="s5.jpg",
         voice="You see, humpbacks have been seen protecting seals from killer whales.",
         shot="""0-4.0 s: the humpback, floating on its back, lifts the small seal higher on its chest between its two white pectoral fins, keeping it out of the water, while the two killer whales circle closer, their tall black fins slicing the water.
4.0-7.6 s: one killer whale lunges toward the seal and the humpback rolls slightly and sweeps a white fin to push the water at it; the killer whale turns away. The seal stays safe on the chest. End on a steady picture.""",
         camera="A slow, high orbit around the humpback. No cuts.",
         sound="Wind, gentle waves, killer whale blows, a seal's small bark, a deep whale moan.",
         must="The seal stays on the humpback's chest the whole time; no blood; the ice floes stay in place."),
    dict(id="C6", start="s6.jpg",
         voice="And a second whale was slapping its tail to keep the shark away.",
         shot="""0-2.0 s: the second humpback brings its huge tail fluke down hard at the surface, a thunderous burst of white bubbles exploding underwater.
2.0-3.6 s: the tiger shark flinches, turns sharply away and swims off fast into the deep blue.
3.6-7.6 s: the second whale slams its tail once more; the shark is gone; in the distance the first whale and the woman stay calm. End on a steady picture.""",
         camera="A fixed wide camera underwater. No cuts.",
         sound="A huge underwater thump and rush of bubbles, the shark's fast tail swish, a deep whale moan.",
         must="The shark swims AWAY and gets smaller; it never comes back; one shark, two whales, one woman."),
    dict(id="C7", start="s7.jpg",
         voice="A year later, a humpback swam straight up to her boat, ignored everyone else...",
         shot="""0-2.5 s: the humpback's head rises a little higher beside the boat, its eye looking up only at the woman; the two men step back in surprise.
2.5-4.9 s: the woman slowly lowers her hand from her mouth and reaches down, laying her palm on the whale's bumpy head; the whale stays still under her hand.
4.9-7.6 s: she smiles with tears in her eyes; the whale breathes out a gentle spray of mist from its blowhole. End on a steady picture.""",
         camera="A slow push-in toward the woman and the whale's eye. No cuts.",
         sound="Waves lapping, a soft whale blow, a quiet amazed gasp (no words).",
         must="The whale's pale scar stays the same; the boat does not move; the whale never hits the boat."),
    dict(id="C8", start="s8.jpg",
         voice="...and gently nudged her. Two notches on its tail. It was the same whale.",
         shot="""0-1.2 s: the whale gently nudges the woman with its head; she laughs and pats its head.
1.2-3.5 s: the whale slowly turns and glides past her and past the camera; its huge tail fluke sweeps close past the camera, and the TWO small notches in the trailing edge of the fluke are clearly visible.
3.5-7.6 s: the camera holds on the fluke as it swims away into the bright blue, the two notches still clear. End on a steady picture.""",
         camera="The camera turns smoothly to follow the whale as it passes, ending close on the tail fluke. No cuts.",
         sound="A soft whale song, gentle bubbles, a happy laugh through the snorkel.",
         must="The fluke shows exactly TWO notches; the whale keeps its pale head scar; no shark."),
]


def prompt(c):
    return "\n".join(["Animate starting EXACTLY from the attached start frame.", LOOK, MOTION, SIZES, WOMAN,
                      "Shot, 8 seconds, vertical 9:16:", c["shot"], "Camera: " + c["camera"], COMP,
                      "Sound: " + c["sound"] + " " + NO_TALK, AVOID, "Must be true: " + c["must"]])


out = [f"# {EP}: Flow video prompts (from the approved stills)\n",
       "Every clip: Flow → Video → **Frames**, Veo 3.1 Fast, 9:16, x1 (20 credits), Start = the still, End = none. "
       "8 clips = 160 credits. Download **1080p**.\n"]
for i, c in enumerate(CLIPS):
    a, b = WINDOWS[i]
    out.append(f"\n### {c['id']}: Start = {c['start']}, End = none\nUsed: {a:.2f}-{b:.2f} s ({b - a:.1f} s)  \n"
               f"Voice over it: \"{c['voice']}\"\n\n```\n{prompt(c)}\n```\n")
p = Path(__file__).parent / "output" / f"{EP}_flow_prompts.md"
p.write_text("".join(out), encoding="utf-8")
print("wrote", p)
