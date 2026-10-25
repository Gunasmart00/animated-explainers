"""Writes output/ice-cream-machine_flow_prompts.md: keyframes K0-K6 (free) + 7 continuous Frames-to-Video clips.
Clip n: START = K(n-1), END = K(n); C7 ends on K0 (loop). No brand names, logos or text in any prompt."""
from pathlib import Path

STYLE = ("Soft stylised 3D animation in a high-end animated-family-film look: natural proportions with normal head sizes, "
         "only slightly larger expressive eyes, softly stylised faces with clean simplified detail, smooth skin, realistic hair "
         "and clothes with clean simplified folds. Bright, cheerful, high-key lighting with clean saturated colours (warm red, "
         "sunny yellow, cream, mint); glossy stainless steel. Not a big-headed cartoon, not chibi, not photorealistic, not 2D, "
         "not gritty, never dark or gloomy.")
MOTION = ("Smooth, fluid, natural motion with gentle easing; the camera moves in one continuous smooth path, never shakes, "
          "never cuts, never jumps. Everything keeps exactly the same look for the whole clip.")
ROOM = ("THE RESTAURANT: a bright, clean, cheerful generic fast-food restaurant: red and yellow walls, warm lights, a long "
        "counter, a menu board with only pictures of a burger, fries and a swirl ice-cream cone (no words, no prices, no logos), "
        "a few customers at tables.")
MACHINE = ("THE MACHINE: a shiny stainless-steel soft-serve ice-cream machine, about 1 m tall, on the back counter: two pull "
           "levers with nozzles, a small front panel with a few round coloured lights (no text), a lid on top, and ONE small "
           "brass-and-glass sand hourglass standing on top of it.")
BOY = ("THE BOY: a cheerful 8-year-old boy (soft stylised 3D, natural child proportions), short messy ginger hair, freckles, "
       "a bright orange hoodie, blue jeans, white sneakers; about 1.3 m tall.")
BOY_SHORT = "THE BOY: a young boy in a bright orange hoodie, exactly as in the attached frame."
WORKER = ("THE WORKER: a friendly teenage restaurant worker in a red cap, a plain yellow polo shirt with no logo and a red "
          "apron; about 1.75 m tall.")
CITY = ("THE TOWN MAP: a bright, toy-like miniature 3D town seen from above in daylight: little streets, houses, parks and "
        "dozens of tiny fast-food restaurants; above each restaurant floats a small glowing map pin: green for working, red "
        "with a tiny melting ice-cream-cone icon for broken; a little more than one in ten pins are red.")
GERMS = ("THE GERMS: small cute cartoon germs: round purple blobs with tiny happy faces and stubby arms (playful, never gross "
         "or scary).")
TECH = ("THE TECHNICIAN: a repair technician seen from behind: navy blue coveralls, a navy cap, a big red toolbox; "
        "about 1.8 m tall.")
COMP = ("Composition: vertical 9:16; the main subject in the middle of the frame; keep the bottom quarter simple (captions go "
        "there) and nothing important in the top-right corner (logo).")
NOTEXT = "No text, letters, numbers, prices or logos anywhere (menu board, panel, clothes, map)."
AVOID = ("Avoid: any text, letters, numbers, prices, labels, subtitles, logos or brand marks anywhere; golden arches; a second "
         "copy of the machine or the hourglass; extra fingers or warped faces; photorealism; dark or muddy lighting; "
         "morphing, a person changing into a different person, teleporting; any cut or scene change inside the clip; music; "
         "any speech, voices or narration.")
SOUND_TAIL = "No music. No speech, no voices, no narration."
SCALE = ("Real-world scale: the boy is about 1.3 m, the worker about 1.75 m, the machine about 1 m tall on a counter about "
         "0.9 m high; the hourglass is small (about 15 cm).")

KEYS = {
 "K0": ("Wide restaurant (first AND last frame)", "none (make this one first; it sets the look)",
        f"""{STYLE}
Single still frame, vertical 9:16.
{ROOM}
{MACHINE}
{BOY}
{WORKER}
Picture: a WIDE shot from the restaurant entrance at standing eye level, looking across the bright restaurant to the counter in the middle of the frame. The boy stands at the counter seen from behind and slightly to the side, on tiptoes, excitedly pointing up at the ice-cream-cone picture on the menu board. Behind the counter, the worker smiles at him, and on the back counter the soft-serve machine with the small hourglass on top is clearly visible. A few customers at tables, small.
{COMP}
{NOTEXT}"""),
 "K1": ("The boy's face drops at the counter (end of C1)", "K0",
        f"""{STYLE}
Single still frame, vertical 9:16. Same restaurant, boy, worker and machine as the attached image.
{MACHINE}
{BOY}
{WORKER}
Picture: a medium shot at the counter. Behind it, the worker gives an apologetic shrug with both palms up, standing next to the soft-serve machine; one small red light glows on the machine's panel and the hourglass sits on top. In the front left of the frame, the boy faces the camera with a comically devastated face: jaw dropped, eyebrows up, shoulders slumped (funny, not sad).
{COMP}
{NOTEXT}"""),
 "K2": ("The town map with broken-machine pins (end of C2)", "K0 (for the look)",
        f"""{STYLE}
Single still frame, vertical 9:16.
{CITY}
Picture: a three-quarter bird's-eye view of the whole toy town filling the frame, sunny and cheerful, dozens of glowing map pins floating over the little restaurants: mostly green, and a little more than one in ten red with a tiny melting-cone icon.
{COMP}
{NOTEXT}"""),
 "K3": ("X-ray of the machine: germ buffet (end of C3)", "K1 (for the machine)",
        f"""{STYLE}
Single still frame, vertical 9:16. Same machine as in the attached image.
{MACHINE}
{GERMS}
Picture: a close shot of the soft-serve machine on the back counter, its front and sides see-through like a soft glowing blue x-ray. Inside the hopper at the top, creamy white milk mix, and five or six cute purple germs happily feasting in it like a buffet, holding tiny spoons. The small hourglass still stands on top. Warm restaurant background softly blurred.
{COMP}
{NOTEXT}"""),
 "K4": ("Frosty clean machine at night (end of C4)", "K0, K3",
        f"""{STYLE}
Single still frame, vertical 9:16. Same restaurant and machine as the attached images.
{MACHINE}
Picture: night. The restaurant is empty and calm, lit by soft warm night lights and moonlight from the windows (cosy, never gloomy). The soft-serve machine on the back counter glows a soft frosty blue, covered in sparkling frost; its x-ray view shows clean cold mix and no germs. The hourglass on top has golden sand pouring down.
{COMP}
{NOTEXT}"""),
 "K5": ("Locked machine, technician at the keypad (end of C5)", "K4",
        f"""{STYLE}
Single still frame, vertical 9:16. Same night restaurant and machine as the attached image.
{MACHINE}
{TECH}
Picture: night, cosy warm light. The technician stands in front of the machine, seen from behind and slightly to the side, his finger on a small glowing keypad on the machine's front panel (blank keys, no numbers). A big glowing red padlock symbol hovers on the machine's panel. His red toolbox sits on the floor. The hourglass is on top.
{COMP}
{NOTEXT}"""),
 "K6": ("Town map: one technician van, many red pins (end of C6)", "K2",
        f"""{STYLE}
Single still frame, vertical 9:16. Same toy town as the attached image.
{CITY}
Picture: the same three-quarter bird's-eye view of the toy town in morning sunlight. ONE tiny white repair van with a red stripe drives along a long winding road in the middle of the frame, and many red map pins wait over the restaurants around it.
{COMP}
{NOTEXT}"""),
}

CLIPS = [
 dict(id="C1", s="K0", e="K1", used="0.0–8.0 s", vo="Why is the McDonald's ice cream machine ALWAYS broken? / You walk in, you're craving a McFlurry... \"Sorry, machine's broken.\"",
  chars=[ROOM, MACHINE, BOY, WORKER],
  shot="""0-1.5 s: starting exactly on the start frame, the camera is already gliding forward across the bright restaurant toward the counter.
1.5-3.5 s: at the counter, the boy bounces on his tiptoes, beaming, pointing at the ice-cream-cone picture on the menu board.
3.5-5.5 s: the worker glances back at the soft-serve machine; a small red light blinks on its panel; the worker turns back with an apologetic shrug, palms up.
5.5-7.6 s: the camera swings around to face the boy as his face drops comically: jaw dropped, eyebrows up, shoulders slumping (funny, not sad); land exactly on the end frame.""",
  cam="one continuous glide forward from the entrance to the counter, then a gentle swing around to the boy's face. No cuts.",
  sound="busy restaurant chatter, a fryer sizzle, a cheerful bell, a sad little cartoon 'wah-wah' as his face drops",
  must="the hourglass is on the machine the whole time; the worker and boy keep the same look", never="a logo or golden arches; text on the menu board"),
 dict(id="C2", s="K1", e="K2", used="8.0–16.0 s", vo="\"Again.\" / And it's not just you. Right now, more than one in ten in the US are down. There's literally a website tracking it live.",
  chars=[BOY_SHORT, WORKER, ROOM, CITY],
  shot="""0-1.5 s: the boy slumps dramatically onto the counter with a huge sigh.
1.5-4.0 s: the camera rises straight up and back, through the ceiling and high into the sunny sky above the town.
4.0-7.6 s: the town below becomes a bright toy-like map; small glowing map pins pop up over the little restaurants one by one, mostly green and some red with a tiny melting-cone icon; land exactly on the end frame.""",
  cam="one continuous rise up through the ceiling into a bird's-eye view of the town. No cuts.",
  sound="a big comic sigh, a whoosh up into the sky, soft birdsong, cheerful 'blip' sounds as each pin pops up",
  must="pins pop up gradually; about one in ten red", never="text or numbers on the map; a cut"),
 dict(id="C3", s="K2", e="K3", used="16.0–23.5 s", vo="...tracking it live. / So what's going on? Okay... milk is basically a buffet for bacteria.",
  chars=[CITY, ROOM, MACHINE, GERMS],
  shot="""0-2.0 s: one red pin pulses; the camera dives down toward it, through the restaurant roof.
2.0-4.0 s: the camera swoops over the counter to the soft-serve machine, whose front and sides turn see-through like a soft glowing blue x-ray.
4.0-7.6 s: inside the hopper, cute purple germs pop up in the creamy milk mix and happily feast with tiny spoons like an all-you-can-eat buffet; land exactly on the end frame.""",
  cam="one continuous dive from the sky into the restaurant and up to the machine. No cuts.",
  sound="a whoosh down, restaurant chatter fading, a soft x-ray hum, tiny squeaky munching and giggling germs",
  must="germs are cute and playful; the hourglass stays on top", never="gross or scary germs; text"),
 dict(id="C4", s="K3", e="K4", used="23.5–31.6 s", vo="So every single night, the machine cooks itself clean. It heats the mix hot enough to kill the germs, then chills it all the way back down.",
  chars=[MACHINE, GERMS, ROOM],
  shot="""0-1.2 s: behind the machine, the restaurant lights dim to a calm, empty night.
1.2-4.0 s: the mix glows orange-hot and bubbles; the germs panic comically, drop their spoons and vanish in little harmless puffs.
4.0-6.5 s: the orange glow turns icy blue and sparkling frost creeps over the machine.
6.5-7.6 s: the camera pulls back to show the frosty machine in the empty, cosy night restaurant, the hourglass sand pouring; land exactly on the end frame.""",
  cam="close on the x-ray machine, then a slow pull-back to a medium shot. No cuts.",
  sound="lights clicking off, a rising heating hum and bubbling, squeaky 'eek!' and soft puffs, then an icy crackle of frost",
  must="the germs just puff away (funny, no harm shown); frost is bright and sparkly", never="fire or flames; anything scary; text"),
 dict(id="C5", s="K4", e="K5", used="31.6–39.4 s", vo="And that can take up to four hours. / Oh, and if one tiny step fails? It locks itself. And only a technician with a secret code...",
  chars=[MACHINE, TECH, ROOM],
  shot="""0-2.3 s: time-lapse: the hourglass sand pours fast and moonlight shadows sweep across the floor (hours passing).
2.3-4.0 s: one light on the panel blinks red; a big glowing red padlock symbol snaps shut on the machine's panel with a clunk.
4.0-7.6 s: the technician walks in from the side, back to the camera, sets down his red toolbox and types on a small glowing keypad on the panel; land exactly on the end frame.""",
  cam="steady medium shot of the machine during the time-lapse, then a slow push-in as the technician arrives. No cuts.",
  sound="a ticking clock speeding up, a warning beep, a heavy padlock clunk, footsteps, soft keypad beeps",
  must="the padlock is a glowing symbol on the panel; the technician is seen from behind", never="numbers on the keypad; text; a face close-up"),
 dict(id="C6", s="K5", e="K6", used="39.4–47.3 s", vo="...can unlock it. / So when they say \"broken\"... they usually mean \"cleaning.\" Or \"waiting for that one guy.\"",
  chars=[MACHINE, TECH, CITY],
  shot="""0-2.5 s: morning sunlight floods in; the technician has gone; the machine happily cleans itself, little soapy bubbles floating out of it and its panel lights twinkling (clearly not broken).
2.5-4.5 s: the camera rises up through the roof into the bright morning sky.
4.5-7.6 s: the toy town map appears below with many red pins waiting, and ONE tiny white repair van with a red stripe driving along a long winding road; land exactly on the end frame.""",
  cam="slow push on the bubbling machine, then one continuous rise up into a bird's-eye view. No cuts.",
  sound="birdsong, gentle bubbly cleaning sounds, a whoosh up, a tiny van engine humming far away",
  must="only one van; many red pins", never="text on the van or map; a cut"),
 dict(id="C7", s="K6", e="K0", used="47.3–55.56 s (lands on K0 for the loop; cut on the matching frame)", vo="It got so bad, the US government stepped in. / And in 2024, restaurants finally won the right to fix their own ice cream machines.",
  chars=[CITY, ROOM, MACHINE, BOY_SHORT, WORKER],
  shot="""0-2.0 s: a giant shiny golden official rubber stamp (a plain round seal, no letters) comes down from the sky and stamps the town with a big friendly glowing burst; every red pin flips to an open padlock and then turns green.
2.0-4.5 s: the camera dives back down into the bright restaurant from the start.
4.5-6.3 s: the worker gives the soft-serve machine a quick twist with a wrench; its light turns green and he gives a happy thumbs-up.
6.3-7.6 s: the camera pulls straight back to the wide shot from the restaurant entrance, settling exactly on the end frame (the boy at the counter on tiptoes, pointing at the ice-cream picture).""",
  cam="the stamp from above, a dive into the restaurant, then one continuous pull-back to the wide entrance shot. No cuts.",
  sound="a deep official 'thunk' of the stamp, a sparkling chime, padlocks clicking open, a wrench clink, restaurant chatter returning",
  must="the stamp has no letters; land exactly on the end frame", never="flags, letters or numbers; a person changing into a different person; a cut"),
]


def clip_prompt(c):
    chars = "\n".join(c["chars"])
    return f"""Animate starting EXACTLY from the attached start frame: same art style, same objects, same camera position and same light as that picture.
{STYLE}
{MOTION}
{chars}
Shot, 8 seconds, vertical 9:16:
{c['shot']}
Camera: {c['cam']}
The clip ENDS EXACTLY on the attached end frame: in the last moment the camera settles precisely into that picture.
{SCALE}
{COMP}
Sound: {c['sound']}. {SOUND_TAIL}
{AVOID}
Must be true: {c['must']}.
Never show: {c['never']}."""


out = ["# Ice cream machine: Flow prompts (continuous, no cuts)\n\n",
       "Voice: `audio/voiceover.mp3`, 55.56 s. Follow `docs/owner-flow-workflow.md`.\n\n",
       "**Keyframes first (Nano Banana, 9:16, x1, free)** in this order: **K0, K1, K3, K4, K5, K2, K6** "
       "(attach the images listed). Save as `images/K0.png` ... `K6.png`.\n\n",
       "**Clips (Veo 3.1 Fast, Frames, 9:16, x1, 20 credits each = 140):** Start = the first keyframe, End = the second. "
       "Save as `clips/c01.mp4` ... `c07.mp4`. If Flow says \"prominent people\", delete THE BOY's long description from that "
       "prompt (keep the short one) and retry.\n\n",
       "Join windows (s): 8.0, 8.0, 7.5, 8.1, 7.8, 7.9, 8.26\n\n---\n## Keyframes\n"]
for k, (title, refs, text) in KEYS.items():
    out.append(f"\n### {k}: {title}\nAttach: {refs}\n\n```\n{text}\n```\n")
out.append("\n---\n## Clips\n")
for c in CLIPS:
    out.append(f"\n### {c['id']}: START = {c['s']}, END = {c['e']}\nUsed: {c['used']}  \nVoice over it: {c['vo']}\n\n```\n{clip_prompt(c)}\n```\n")
Path("output").mkdir(exist_ok=True)
Path("output/ice-cream-machine_flow_prompts.md").write_text("".join(out), encoding="utf-8")
print("ok", sum(map(len, out)))
