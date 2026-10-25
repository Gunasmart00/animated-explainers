"""Builds output/bobbie-walks-home_flow_prompts.md: E1 (dog reference, Canva) + K0-K5 (Canva) + C1-C6 (Flow, Veo).
Clip n: START = K(n-1), END = K(n); C6 ends on K0 (loop). No names, logos or text in prompts."""
from pathlib import Path
import re

STYLE = '3D animation that looks like a real-time video-game engine render (an Unreal Engine cutscene), the look of popular 3D explainer shorts: realistic human proportions with video-game character faces (smooth, slightly plastic skin, simple realistic hair, natural-sized eyes, a little stiff); animals are realistic game-asset models with simplified fur; simple game-level environments with plain painted walls, basic textures and few props; bright, flat, even lighting with soft shadows; clean saturated colours (sky blue, white, warm wood); a slightly wide-angle camera. Not a photograph, not cinematic film lighting, not Pixar or cartoon style, not anime, no text anywhere.'
MOTION = ("Smooth, natural motion with believable weight; the camera moves in one continuous smooth path, never shakes, "
          "never cuts, never jumps. Everything keeps exactly the same look for the whole clip.")
DOG = 'THE DOG: a medium-sized collie-shepherd mix with upright pointed ears, a long chocolate-brown coat, tan cheeks, tan legs and a tan patch on the thigh, a big fluffy white ruff around the neck and chest, white lower legs and paws, a thin white blaze up his face and a white tip on his long bushy tail; about 60 cm at the shoulder; exactly as in the attached frames.'
GIRL = ("THE GIRL: a 15-year-old girl with a brown chin-length bob, a soft round face, a grey knitted beanie, a long "
        "blue-grey wool coat over a brown plaid skirt, a red-and-cream plaid scarf, grey wool stockings and brown lace-up "
        "boots; about 1.6 m tall; exactly as in the attached frames.")
FAMILY = ("THE FAMILY (1920s summer): the father (about 45, short dark hair, moustache, flat cap, waistcoat), the mother (about 40, brown hair in a low bun, cloche hat, light summer dress) and the same teenage girl in a light summer dress; a dark-green 1920s open touring car with spoked wheels and no logos.")
FARMDOGS = "THREE FARM DOGS: big barking mixed-breed dogs (comic chase, no biting, no injuries)."
WOMAN = ("THE FARM WOMAN: a kind middle-aged woman in a 1920s apron and shawl, holding a lantern.")
COMP = ("Composition: vertical 9:16; the main subject in the middle of the frame; keep the bottom quarter simple "
        "(captions go there) and nothing important in the top-right corner (logo).")
AVOID = ("Avoid: any text, letters, numbers, words on signs, newspapers, letters or maps; logos; cartoon style or big "
         "cartoon eyes; a second copy of the dog; the dog changing colour or breed; extra legs or fingers; warped faces; "
         "dark or muddy lighting; morphing, a person changing into a different person, teleporting; any cut or scene "
         "change inside the clip; music; any speech, voices or narration.")
SCALE = ("Real-world scale: the dog is about 60 cm at the shoulder (reaching a standing girl's hip); people 1.6-1.8 m; "
         "a 1920s car is about 4 m long.")

E1 = f"""{STYLE}
Vertical 9:16 character reference picture on a plain, light blue-grey studio background. One medium-sized collie-shepherd mix dog with upright pointed ears, a chocolate-brown coat, tan cheeks and legs, a big white ruff around the neck and chest, white paws, a thin white blaze up his face and a white tip on his bushy tail, standing in full side view facing left, healthy and clean, kind brown eyes. Full body visible from nose to tail, centred, soft even light. No text, letters, numbers or logos."""

DOG_LOOK = ("a medium-sized collie-shepherd mix dog with upright pointed ears, a chocolate-brown coat, tan cheeks and legs, "
            "a big white ruff around the neck and chest, white paws, a thin white blaze up his face and a white tip on his bushy tail")
GIRL_LOOK = ("a 15-year-old girl with a brown chin-length bob, a soft round face, a grey knitted beanie, a long blue-grey wool "
             "coat over a brown plaid skirt, a red-and-cream plaid scarf, grey wool stockings and brown lace-up boots")
PARENTS = ("her father (about 45, short dark hair, moustache, white shirt with rolled sleeves, a white cook's apron) and her mother "
           "(about 40, brown hair in a low bun, a green wool cardigan over a cream dress)")
TAIL = ("Composition: vertical 9:16; keep the bottom quarter of the frame simple (captions go there) and the top-right corner "
        "empty (logo). No text, letters, numbers, signs with writing or logos anywhere.")
KEYS = [
 ("K0", "Main Street, winter 1924: they see each other (first AND last frame)", "E1 (the dog)", f"""{STYLE}
Vertical 9:16 still frame. STORY MOMENT: after six months lost, a skinny dog limps into his home town, and the girl who loves him sees him and freezes in disbelief.
SETTING: the snowy Main Street of a small 1920s Oregon town on a bright, cold winter morning. Two-storey brick and wooden shopfronts line both sides with snow on the awnings; a black iron street lamp; far back, one parked dark-green 1920s car; trampled snow and slush on the road. No signs with writing.
CAMERA: at about 1 m high (a child's eye level), three-quarter view along the street, looking slightly to the right.
THE DOG: {DOG_LOOK}. He is skinny after a long journey: thin body, ribs showing under matted, muddy fur, wet clumps on his ruff, dirty paws worn raw. He is in the LEFT-CENTRE of the frame, about 4 m from the camera, seen in three-quarter side view walking from LEFT to RIGHT toward the girl, limping on his front right paw. His head is raised and turned toward her, his eyes locked on her face, ears lifting, the tip of his tail just starting to wag. A long trail of his paw prints runs behind him through the snow to the left edge of the frame.
THE GIRL: {GIRL_LOOK}. She stands on the RIGHT, on the snowy sidewalk right outside the open door of her family's small diner, about 3 m from the dog. Her whole body and face are turned to the LEFT toward the dog; her eyes are wide and locked on his, eyebrows raised, one gloved hand pressed over her mouth in shock, the other hand has just dropped a small tin milk pail into the snow beside her boots. Her expression: disbelief turning into hope.
THE DINER: warm golden light inside, a big front window with no lettering. Taped inside the window, at the girl's shoulder height, a hand-drawn paper map of America with no words at all, and a dotted trail of tiny paw prints drawn across it from the middle of the map to the top-left (Oregon).
LIGHT: low morning sun from the left, long soft shadows to the right, blue-white snow, warm window glow.
{TAIL}"""),
 ("K1", "The reunion hug", "K0", f"""{STYLE}
Vertical 9:16 still frame, the same street, girl and dog as the reference image. STORY MOMENT: "It was Bobbie": she has run to him and the family is reunited.
CAMERA: medium shot at kneeling height, in front of the diner, slightly to the left of the pair.
THE GIRL ({GIRL_LOOK}) kneels in the snow in the centre of the frame, her beanie slipping back, both arms wrapped tightly around the dog's neck, cheek pressed into his white ruff, eyes shut, a huge smile with happy tears on her cheeks.
THE DOG ({DOG_LOOK}, still skinny, matted and muddy) leans his whole body into her, his head resting over her shoulder toward the camera, eyes half-closed in relief, ears soft, tail curled up and wagging (a slight blur on the tail tip).
BEHIND THEM, in the open diner doorway on the right, {PARENTS}, both frozen with joy: the father with a dish towel in his hand, the mother with both hands over her heart.
The tin milk pail lies tipped over in the snow at the bottom left. Snow flakes drifting. Warm golden light from the doorway against the blue morning.
{TAIL}"""),
 ("K2", "Flashback: the gas station in Indiana, summer 1923", "E1 (the dog)", f"""{STYLE}
Vertical 9:16 still frame. STORY MOMENT (six months earlier): on a road trip, three farm dogs chase him away from a gas station; this is how he got lost.
SETTING: a hot, sunny summer afternoon at a tiny rural 1920s gas station beside a dirt road in flat Indiana farmland: a small white wooden station hut, one tall old red gravity gas pump with a round glass globe on top (no writing), a dark-green 1920s open touring car with spoked wheels and its canvas top folded down, parked at the pump on the LEFT. Tall green cornfields fill the right side of the frame. Bright blue sky, white clouds, dust in the air.
CAMERA: eye level, wide shot.
THE FAMILY (small, background left): {PARENTS}, in summer clothes (the father in a flat cap and waistcoat, the mother in a cloche hat and a light summer dress), and the girl in a light summer dress, standing by the car looking at a folded paper road map with no writing; none of them have noticed the chase yet.
THE DOG ({DOG_LOOK}): healthy, clean and fluffy, in the RIGHT-CENTRE of the frame, sprinting RIGHT toward the cornfield, ears flattened back, eyes wide and frightened, all four paws off the ground, dust kicking up behind him.
THREE FARM DOGS chase him from the centre-left: big scruffy mixed-breed dogs (one black, one grey, one spotted), mouths open barking, comic rather than scary, no biting.
{TAIL}"""),
 ("K3", "The family drives home without him; he watches from the hill", "K1 (for the family)", f"""{STYLE}
Vertical 9:16 still frame. STORY MOMENT: "The family searched for days, then drove all the way home to Oregon without him." / "But Bobbie never gave up."
SETTING: a high, wide view of endless flat summer farmland at golden sunset; a long, straight dirt road runs from the bottom-right corner diagonally to the top-left, disappearing into the glowing sunset on the horizon (west).
THE CAR: far up the road toward the top-left, small, the dark-green 1920s open touring car driving away into the sunset, a thin trail of dust behind it; inside, tiny, the father driving, the mother beside him, and the girl in the back seat turned around looking back sadly over the seat.
THE DOG ({DOG_LOOK}, healthy but dusty): in the bottom-right foreground, standing alone on top of a small grassy hill, seen from behind in three-quarter view, looking up the road after the car toward the sunset; head high, ears up, chest out, wind ruffling his fur: not sad, determined. His long shadow stretches toward the road.
Mood: bittersweet but hopeful, warm orange and pink sky.
{TAIL}"""),
 ("K4", "The journey: swimming a wide river toward the mountains", "E1 (the dog)", f"""{STYLE}
Vertical 9:16 still frame. STORY MOMENT: "He crossed plains and deserts, swam rivers..."; he is going west, always moving right to left.
SETTING: a wide, cold, blue-green river in late autumn; on the far LEFT bank, golden cottonwood trees, and far behind them on the horizon the snow-capped peaks of the Rocky Mountains (where he is heading); on the near right bank, dry prairie grass. Crisp autumn light, a few golden leaves floating on the water.
CAMERA: low, just above the water surface, side view.
THE DOG ({DOG_LOOK}, now thinner, his fur wet and darker): swimming hard from RIGHT to LEFT across the middle of the river, only his head, ruff and back above the water, chin up, eyes fixed on the far bank, a V-shaped wake spreading behind him to the right.
{TAIL}"""),
 ("K5", "A stranger feeds him on a snowy porch at night", "E1 (the dog)", f"""{STYLE}
Vertical 9:16 still frame. STORY MOMENT: "...strangers who had fed him along the way": kindness on his journey.
SETTING: night in the snowy mountains of the West; the wooden front porch of a small log farmhouse, snow piled on the railings, deep blue night with soft falling snow and a few stars; warm golden light pours out of the open front door.
CAMERA: medium shot at porch-floor level, from the left of the porch steps.
THE FARM WOMAN: about 55, grey hair in a bun, round kind face, a long brown 1920s work dress, a flowered apron and a knitted shawl. She kneels on the porch on the RIGHT, holding up an oil lantern in one hand and setting down a tin bowl of stew with the other, smiling softly at the dog.
THE DOG ({DOG_LOOK}, very thin now, snow on his back and ears, icy fur): on the LEFT, standing on the top step, head down eating from the bowl gratefully, his tail giving a small wag.
Snowy boot prints and his paw prints lead up the steps. Warm vs. cool light, cosy and kind.
{TAIL}"""),
]

CLIPS = [
 dict(id="C1", s="K0", e="K1", used="0.0-8.6 s", vo='"A skinny dog limped down Main Street, his toenails worn down to almost nothing, when a girl outside her family\'s diner froze. It was Bobbie."',
  chars=[DOG, GIRL, "THE PARENTS: " + PARENTS + "."],
  shot="""0-2.0 s: starting on the opening frame, the camera is already moving: a slow push in along the snowy street as the skinny dog limps toward the girl and she stares back at him, both holding each other's gaze.
2.0-3.5 s: the camera dips low beside him: close on his worn, sore, muddy paws limping through the snow.
3.5-5.5 s: their eyes meet: his ears lift and his tail starts to wag; she slowly lowers her hand from her mouth, her face breaking into a trembling smile as she recognises him (her lips move silently, no sound of speech).
5.5-7.6 s: she runs to him, drops to her knees in the snow and hugs him tightly, eyes shut, smiling through happy tears; her parents appear in the diner doorway behind her with their hands over their hearts; end on a steady final picture.""",
  cam="one continuous push in down the street, a low pass by his paws, then settling on the hug. No cuts.",
  sound="a quiet snowy street, soft crunching paw steps in snow, a gasp, running footsteps, a happy sob and a dog's soft whine",
  must="the dog is skinny and matted; the girl's coat, hat and scarf stay the same", never="any text on the diner or signs; a cut"),
 dict(id="C2", s="K1", e="K2", used="8.6-15.4 s", vo='"Six months earlier, on a road trip to Indiana, three dogs had chased him away from a gas station."',
  chars=[DOG, FAMILY, FARMDOGS],
  shot="""0-1.5 s: the camera slowly pushes in to the dog's eye over the girl's shoulder.
1.5-3.0 s: the camera goes into the reflection in his eye, and the snowy street brightens and warms into a sunny summer day: a smooth flashback transition, not a cut.
3.0-5.0 s: a 1920s open touring car pulls up at a small rural gas station beside tall cornfields; the healthy, clean, fluffy dog hops out and sniffs around the old red gas pump.
5.0-7.6 s: three big farm dogs burst out barking; the dog bolts across the dirt road toward the cornfield, ears back; end on a steady final picture.""",
  cam="one continuous push into the eye and out into the summer scene, then a smooth follow of the chase. No cuts.",
  sound="a soft heartbeat, a warm whoosh into summer, a 1920s car engine chugging, cicadas, loud comic barking, running paws",
  must="in the flashback the dog is healthy and clean; exactly three farm dogs", never="biting or injuries; text on the pump; a cut"),
 dict(id="C3", s="K2", e="K3", used="15.4-22.0 s", vo='"The family searched for days, then drove all the way home to Oregon without him." / "But Bobbie never gave up."',
  chars=[FAMILY, DOG],
  shot="""0-1.0 s: the running dogs leave the frame to the right; the camera turns gently toward the cornfield. 1.0-2.5 s: the father, mother and girl walk in from the left and search along the cornfield, calling out with cupped hands and peering between the corn rows (worried, not crying).
2.5-4.5 s: the sky turns to golden sunset as they sadly climb back into the car and drive off along the long, straight dirt road.
4.5-7.6 s: the camera rises high and wide over the endless fields: the car shrinks into the distance, and far behind it the dog steps out onto a grassy hill and stands watching the road, determined; end on a steady final picture.""",
  cam="a gentle follow of the family, then one continuous rise into a high wide shot. No cuts.",
  sound="voices calling in the distance (no words), crickets, the car engine fading away, a soft wind over the fields",
  must="the family looks for him; the dog watches from the hill at the end", never="crying close-ups; text; a cut"),
 dict(id="C4", s="K3", e="K4", used="22.0-28.6 s", vo='"He crossed plains and deserts, swam rivers, and climbed the Rocky Mountains in the middle of winter."',
  chars=[DOG],
  shot="""0-2.0 s: the dog runs down the hill and trots to the LEFT (west) across endless golden grass plains, the camera tracking beside him; he always moves from right to left.
2.0-4.0 s: still in one tracking move, the land turns to a dusty desert with red rocks; he keeps trotting, panting, determined.
4.0-7.6 s: the camera swings ahead as he reaches a wide, cold, blue river and swims bravely across it, only his head and back above the water; end on a steady final picture.""",
  cam="one long continuous side-tracking shot through changing landscapes, then a swing to the river. No cuts.",
  sound="steady paw steps, wind over grass, a dry desert wind, splashing water and paddling",
  must="the same dog the whole time; the landscapes change smoothly", never="other animals attacking; text; a cut"),
 dict(id="C5", s="K4", e="K5", used="28.6-34.6 s", vo='"...2,551 miles." / "And when his story hit the newspapers,..."',
  chars=[DOG, WOMAN],
  shot="""0-2.5 s: he climbs out of the river and the camera rises with him onto a snowy mountain pass in a blizzard; he pushes on through deep snow, thinner and tired but never stopping.
2.5-4.5 s: the camera follows him down the mountain into a quiet snowy farm at night; warm light glows in a farmhouse window.
4.5-7.6 s: the farmhouse door opens and the kind farm woman steps onto the porch with a lantern, kneels and sets down a bowl of food; the thin, snowy dog eats gratefully; end on a steady final picture.""",
  cam="one continuous follow from the river up the snowy pass and down to the farmhouse porch. No cuts.",
  sound="howling wind and crunching snow, then quiet night, a creaking door, soft footsteps on wooden boards, a bowl set down",
  must="the dog gets thinner and snowier; the porch scene is warm and kind", never="the dog collapsing; text; a cut"),
 dict(id="C6", s="K5", e="K0", used="34.6-40.5 s (C6 ends on K0: cut on the matching frame for the loop)", vo='"...letters poured in from strangers who had fed him along the way." / "They used them to map his whole journey home."',
  chars=[DOG, WOMAN, GIRL],
  shot="""0-2.0 s: on the porch, the farm woman gently pats the dog; the camera rises up into the starry night sky.
2.0-5.0 s: from high above, a giant hand-drawn map of America with no words spreads out below like the land itself; from little houses all across it, white envelopes flutter up into the sky and drift west, and where each one lands a tiny glowing paw print appears, forming a trail from Indiana to Oregon.
5.0-7.6 s: the camera follows the paw-print trail west and swoops down into the snowy Main Street of the small town at morning, settling exactly on the end frame (the skinny dog limping left to right toward the girl, the two of them looking at each other, the girl frozen outside the diner with her hand over her mouth, the paw-print map in the diner window).""",
  cam="a rise into the night sky, a glide over the map following the trail, then one continuous swoop down into Main Street. No cuts.",
  sound="a soft pat, a gentle whoosh upward, fluttering paper, soft chimes as each paw print appears, then a quiet snowy street",
  must="envelopes and the map have no readable writing; land exactly on the end frame", never="text or words; a cut"),
]


ENDS = {'C2': 'a wide sunny summer view of the gas station: the dog sprinting right toward the tall green cornfield with three farm dogs barking behind him, the green 1920s car at the red gas pump on the left', 'C3': 'a high wide golden-sunset view: the long straight dirt road running to the top-left horizon, the small green car far away driving into the sunset, and the dog standing alone on a grassy hill in the bottom-right foreground, seen from behind, watching the road, determined', 'C4': 'a low side view just above the water: the dog swimming from right to left across a wide blue-green river, head and back above the water, golden cottonwoods and snowy mountain peaks on the far left bank', 'C5': 'night on the snowy porch of a log farmhouse: the kind farm woman kneeling on the right with a lantern, setting down a bowl, and the thin, snowy dog on the left eating gratefully, warm light from the open door'}


def clip(c):
    chars = "\n".join(c["chars"])
    if c["id"] == "C1":
        chars = chars.replace("; exactly as in the attached frames", "")
        k0 = dict((k, x) for k, _, _, x in KEYS)["K0"].split("STORY MOMENT:", 1)[1].rsplit("Composition:", 1)[0]
        return f"""TEXT TO VIDEO (no start or end frame attached).
{STYLE}
{MOTION}
OPENING FRAME (hold it for the first half second, it is also the video's last frame for the loop):{k0}
{chars}
Shot, 8 seconds, vertical 9:16:
{c['shot']}
Camera: {c['cam']}
FINAL PICTURE: in the last second the camera slows to a steady hold on a medium shot at kneeling height: the girl kneeling in the snow in the centre, hugging the skinny dog tightly, eyes shut, happy tears; the dog's head over her shoulder, tail wagging; her parents in the diner doorway on the right, hands over their hearts.
{SCALE}
{COMP}
Sound: {c['sound']}. No music. No speech, no voices, no narration.
{AVOID}
Must be true: {c['must']}.
Never show: {c['never']}."""
    if c["id"] in ENDS:
        end_line = ("No end frame is attached. In the last second the camera slows to a steady hold on this final picture "
                    "(it becomes the next clip's start frame): " + ENDS[c["id"]] + ".")
    else:
        end_line = "The clip ENDS EXACTLY on the attached end frame: in the last moment the camera settles precisely into that picture."
    return f"""Animate starting EXACTLY from the attached start frame: same style, same characters, same camera position and same light as that picture.
{STYLE}
{MOTION}
{chars}
Shot, 8 seconds, vertical 9:16:
{c['shot']}
Camera: {c['cam']}
{end_line}
{SCALE}
{COMP}
Sound: {c['sound']}. No music. No speech, no voices, no narration.
{AVOID}
Must be true: {c['must']}.
Never show: {c['never']}."""


kf = "".join(f"### {k}: {t}\nCanva reference image: **{r}**\n\n```\n{x}\n```\n\n" for k, t, r, x in KEYS)
out = ["# Bobbie walks home: everything to generate (in this order)\n\n",
       "Voice: `audio/voiceover.mp3`, 40.52 s. Steps: `docs/owner-flow-workflow.md`.\n\n",
       "**NO PICTURES NEEDED (owner, 2026-10-24).** C1 is text-to-video; every next clip starts on the previous clip's last frame; C6 ends on C1's first frame (loop).\n"
       "1. **C1:** Flow, Video, **Text to video** (no Start/End). Download -> `clips/c01.mp4`. Then save its first frame AND last frame:\n"
       "   `.venv\\Scripts\\python.exe tools\\last_frame.py episodes\\bobbie-walks-home\\clips\\c01.mp4 episodes\\bobbie-walks-home\\images\\K0.jpg --first`\n"
       "   `.venv\\Scripts\\python.exe tools\\last_frame.py episodes\\bobbie-walks-home\\clips\\c01.mp4 episodes\\bobbie-walks-home\\images\\K1.jpg`\n",
       "2. **C2-C5:** Frames, Start = the previous clip's last frame (K1.jpg, K2.jpg, ...), no End. After each, save its last frame:\n"
       "   `python tools\\last_frame.py episodes\\bobbie-walks-home\\clips\\c02.mp4 episodes\\bobbie-walks-home\\images\\K2.jpg` "
       "(c03 -> K3, c04 -> K4, c05 -> K5), then upload that JPEG as the next clip's Start frame.\n",
       "3. **C6:** Start = K5.jpg, End = **K0.jpg** (loop). All clips: Veo 3.1 Fast, 9:16, x1, 20 credits each = 120; download 1080p as `clips/c01.mp4 ... c06.mp4`.\n"
       "4. **Send me each clip (or its last frame) as you go** so a problem is caught before it carries into the next clip.\n"
       "(The E1 and K0-K5 picture prompts below are kept only as reference descriptions; you don't need to make them.)\n\n",
       "Join windows (s): 8.6, 6.8, 6.6, 6.6, 6.0, 5.92\n\n---\n## E1: the dog (reference picture)\n\n```\n" + E1 + "\n```\n\n---\n## Keyframes (Canva)\n\n",
       kf, "\n---\n## Clips (Flow)\n"]
START = {"C1": "none (text to video)", "C2": "last frame of C1 (images/K1.jpg)", "C3": "last frame of C2 (images/K2.jpg)", "C4": "last frame of C3 (images/K3.jpg)", "C5": "last frame of C4 (images/K4.jpg)", "C6": "last frame of C5 (images/K5.jpg)"}
END = {"C1": "none", "C6": "FIRST frame of C1 (images/K0.jpg)", "C2": "none", "C3": "none", "C4": "none", "C5": "none"}
for c in CLIPS:
    out.append(f"\n### {c['id']}: START = {START.get(c['id'], c['s'])}, END = {END.get(c['id'], c['e'])}\nUsed: {c['used']}  \nVoice over it: {c['vo']}\n\n```\n{clip(c)}\n```\n")
Path("output/bobbie-walks-home_flow_prompts.md").write_text("".join(out), encoding="utf-8")
Path("output/bobbie-walks-home_keyframes.md").write_text("# Bobbie: keyframes (Canva), same as in the full prompt sheet\n\n" + kf, encoding="utf-8")
print("ok", sum(map(len, out)))
