"""Writes output/jupiter-crash_flow_prompts.md: keyframe image prompts (K0-K6) and continuous video prompts (C1-C7).

Design: one unbroken camera journey. Every clip is Frames-to-Video with START = the previous keyframe and
END = the next keyframe, so clip N ends on exactly the picture clip N+1 starts on (no cuts, no jumps).
The last clip ends on K0, the first clip's start, so the Reel loops.
"""
from pathlib import Path

STYLE = ("Soft stylised 3D animation in a high-end animated-film look: natural adult body proportions with a normal head size, "
         "only slightly larger expressive eyes, softly stylised faces with clean simplified detail, smooth skin with subtle texture, "
         "realistic hair and clothes with clean simplified folds. Spacecraft, planets and moons have accurate real shapes and proportions "
         "with clean, simplified materials (crisp gold foil, white mesh, metal). Space scenes are rich and beautiful: deep blue-black space "
         "full of crisp stars, planets and moons lit brightly by sunlight from the left with glowing rims, vivid true colours, never murky "
         "or grey. Indoor scenes are bright, soft and cheerful with clean saturated colours (teal, mint, warm golden light). "
         "Not a big-headed cartoon, not chibi, not photorealistic, not live action, not 2D, not gritty.")
MOTION = ("Smooth, fluid, natural motion with believable weight and gentle easing; the camera moves in one continuous smooth path, "
          "never shakes, never cuts, never jumps. Everything keeps exactly the same look for the whole clip.")

PROBE = ("THE PROBE: an uncrewed space probe about 6 m tall. An octagonal main body wrapped in shiny gold and black thermal blankets. "
         "On top, ONE large white umbrella-like mesh dish antenna, 4.8 m across, that is JAMMED HALF-OPEN: lopsided, with three of its "
         "thin ribs still folded against the central mast so one side of the dish sags in like a broken umbrella. Two long thin booms stick "
         "out sideways, each ending in a dark finned cylinder. One very long thin straight pole with two small sensor pods, about twice as "
         "long as the booms. Exactly one probe. No text, no logos, no flags.")
GERMS = ("THE GERMS: three tiny, cute, pale-green rounded cartoon microbes with little smiling faces and stubby arms, clinging to the "
         "probe's gold foil near the bottom of the main body. Each is about the size of a grain of rice on the foil: only visible up close.")
ENGINEER = ("THE ENGINEER: a cheerful young flight engineer in her late 20s (soft stylised 3D, natural proportions), curly black hair in a "
            "high puff, warm brown skin, round tortoiseshell glasses, a plain mint-green polo shirt with no logo, navy trousers, a slim "
            "black headset with a small microphone. About 1.65 m tall.")
ROOM = ("THE ROOM: a bright, modern, cheerful mission control room: three curved rows of light-grey consoles with glowing teal "
        "screens showing only abstract shapes and lines, a pale teal back wall, warm ceiling lights, and ONE giant curved wall screen "
        "across the front wall. No readable text, numbers or logos anywhere.")
JUPITER = ("JUPITER: the giant planet with cream, tan, orange and brown cloud bands, swirling storms and the Great Red Spot, lit from the "
           "left. About 11 Earths wide: always enormous next to the probe.")
EUROPA = ("EUROPA: Jupiter's moon, a smooth white-to-tan ball of ice criss-crossed by long thin reddish-brown crack lines. "
          "Much smaller than Jupiter.")
OCEAN = ("EUROPA CUTAWAY: a clean cross-section slice: a thick white ice crust with cracks on top, below it a vast, deep, glowing blue "
         "salty ocean many times deeper than the ice, and a dark rocky seafloor at the very bottom.")
SATURN = ("SATURN: the planet with pale gold and cream bands and huge flat bright rings. "
          "ENCELADUS: Saturn's small bright-white icy moon spraying tall feathery plumes of sparkling ice from its south pole. "
          "THE SECOND PROBE: a tall cylindrical spacecraft wrapped in gold foil with one big round white dish antenna on top and one long "
          "thin pole; tiny next to Saturn.")
COMP = ("Composition: vertical 9:16; the main subject in the middle of the frame; keep the bottom quarter simple (captions go there) "
        "and nothing important in the top-right corner (logo).")
AVOID = ("Avoid: any text, letters, numbers, labels, subtitles, captions, logos or flags drawn anywhere (including on screens and "
         "spacecraft); a second copy of any spacecraft, planet or moon; the dish antenna opening fully or changing shape; extra fingers "
         "or warped faces; photorealism; dark, muddy or grey lighting; morphing or teleporting; any cut, flash cut or scene change inside "
         "the clip; music; any speech, voices or narration.")
SOUND_TAIL = "No music. No speech, no voices, no narration, no singing."

KEYS = {
 "K0": dict(title="Mission control, wide (opening frame AND final frame of the Reel)", refs="ref 04 (Jupiter)",
   text=f"""{STYLE}
Single still frame, vertical 9:16.
{ROOM}
{ENGINEER}
Picture: a WIDE establishing shot from the back of the room at standing eye level, looking down the centre aisle toward the giant curved wall screen. The screen shows glowing banded Jupiter with a tiny gold space probe beside it. The engineer sits at the front-centre console in the middle of the frame, seen from behind and slightly to the side so her profile, glasses and headset are visible, her hand resting near a big round green button on the console. Two or three other engineers sit at the side consoles, small, seen from behind.
Light: bright, warm, high-key; the wall screen glows.
{COMP}
No text, letters, numbers or logos anywhere."""),
 "K1": dict(title="The probe in front of Jupiter (end of C1)", refs="ref 01 (probe shape), ref 02 (probe at Jupiter), ref 04 (Jupiter)",
   text=f"""{STYLE}
Single still frame, vertical 9:16.
{PROBE}
{GERMS}
{JUPITER}
Picture: a three-quarter front view of the probe in the middle of the frame, close enough that it fills the middle third, sunlit from the left so its gold foil gleams; the half-open lopsided dish is clearly visible on top. Behind it, giant Jupiter fills the lower two-thirds of the background with its bands and the Great Red Spot. Deep blue-black space with crisp stars above. The three tiny germs are just visible on the gold foil near the bottom of the body (small, not the focus).
{COMP}
No text, letters, numbers or logos anywhere."""),
 "K2": dict(title="Behind the probe, heading for Europa (end of C2)", refs="K1, ref 05 (Europa), ref 04",
   text=f"""{STYLE}
Single still frame, vertical 9:16. Same probe, same look as the attached probe image.
{PROBE}
{EUROPA}
{JUPITER}
Picture: the camera is just behind and slightly above the probe, which sits in the lower-middle of the frame seen from the back (dish on top, booms to the sides). Ahead, in the centre of the frame, small bright Europa with its reddish cracks. On the right edge, a huge slice of Jupiter's banded edge. Sunlight from the left, crisp stars.
{COMP}
No text, letters, numbers or logos anywhere."""),
 "K3": dict(title="Inside Europa: the hidden ocean (end of C3)", refs="ref 06 (Europa interior), ref 05",
   text=f"""{STYLE}
Single still frame, vertical 9:16.
{OCEAN}
Picture: a close cross-section view filling the whole frame: the thick white cracked ice crust runs across the top quarter of the frame, with a jagged crack where the camera has just come through; below it, a vast, deep, glowing bright-blue ocean fills the middle of the frame, with soft light rays filtering down through the ice; a dark rocky seafloor is just visible along the very bottom. Calm, beautiful, mysterious. No creatures, no fish.
{COMP}
No text, letters, numbers or logos anywhere."""),
 "K4": dict(title="Close on the drifting probe's gold foil above Europa (end of C4)", refs="K1, ref 05",
   text=f"""{STYLE}
Single still frame, vertical 9:16. Same probe, same look as the attached probe image.
{PROBE}
{GERMS}
{EUROPA}
Picture: a close shot of the lower half of the probe's gold-and-black foil body, slightly tilted as it slowly tumbles, filling the upper-middle of the frame; part of the lopsided dish edge is visible at the top. The three tiny smiling germs are clearly visible on the foil in the centre of the frame (still small, about the size of rice grains on the foil). Below, Europa's white-tan cracked icy surface fills the bottom of the frame. Sunlight from the left.
{COMP}
No text, letters, numbers or logos anywhere."""),
 "K5": dict(title="The what-if path: a glowing dotted line from the probe down to Europa (end of C5)", refs="K1, K4, ref 05",
   text=f"""{STYLE}
Single still frame, vertical 9:16. Same probe and germs as the attached images.
{PROBE}
{GERMS}
{EUROPA}
Picture: a medium-wide shot. The whole probe floats in the upper-left of the frame. A softly glowing cyan dotted line curves from the bottom of the probe down to one reddish crack on Europa's icy surface, which fills the lower half of the frame. The three tiny germs sit at the top of the dotted line on the probe's foil, peering down at it with curious faces. Jupiter's edge glows at the top-right, kept dim and out of the logo corner. Sunlight from the left.
{COMP}
No text, letters, numbers or logos anywhere."""),
 "K6": dict(title="The final dive into Jupiter (end of C6)", refs="ref 03 (probe's end), ref 04",
   text=f"""{STYLE}
Single still frame, vertical 9:16.
{JUPITER}
Picture: a chase view from just behind and above the probe as it plunges steeply down into Jupiter's swirling cream, orange and brown cloud bands, which fill most of the frame. The probe is wrapped in a bright orange-white glowing plasma trail, so it reads as a fiery streak with the probe's silhouette (lopsided dish on top) at its head, in the centre of the frame. Bright, dramatic, beautiful, not scary.
{COMP}
No text, letters, numbers or logos anywhere."""),
}

CLIPS = [
 dict(id="C1", start="K0", end="K1", used="0.00-8.06 s of the Reel",
  lines='"NASA crashed a billion-dollar spacecraft into Jupiter... on purpose." / "This is Galileo, the first spacecraft ever to orbit Jupiter..."',
  chars=[ENGINEER, ROOM, PROBE, JUPITER],
  shot="""0-1.5 s: starting exactly on the start frame, the camera is already moving: it glides smoothly forward down the centre aisle of the bright mission control room toward the engineer at the front console.
1.5-3.5 s: the camera arrives beside her; she takes a breath, eyes wide behind her glasses, with a nervous, excited grin, and firmly presses the big round green button on her console with her whole palm.
3.5-5.0 s: on the giant wall screen in front of her, the tiny probe turns toward Jupiter; the camera keeps gliding forward past her shoulder straight into the wall screen and through it, so the screen's picture becomes real space all around the camera.
5.0-7.6 s: the camera flies on through real space toward the probe and settles in front of it, Jupiter enormous behind; land exactly on the end frame.""",
  opening="exactly the start frame (wide mission control room, engineer at the front console, Jupiter on the wall screen)",
  final="exactly the end frame (three-quarter front view of the probe with its half-open dish, giant Jupiter behind)",
  camera="one continuous forward dolly: down the aisle, past her shoulder, through the wall screen into space, ending on the probe. No cuts.",
  sound="busy mission-control murmur, soft console beeps, a chunky button press, a deep whoosh as the camera passes into space, a low engine rumble",
  must="she is the only person whose face is seen; the probe's dish is lopsided and half-open; one continuous camera move through the screen",
  never="text on screens; a second probe; a cut between the room and space"),
 dict(id="C2", start="K1", end="K2", used="8.06-16.13 s",
  lines='"...ever to orbit Jupiter." / "Its main antenna jammed half-open, like a broken umbrella. It worked anyway." / "Then, flying past..."',
  chars=[PROBE, GERMS, JUPITER, EUROPA],
  shot="""0-1.5 s: the camera slowly circles the probe in front of Jupiter.
1.5-4.5 s: the camera rises to the big white umbrella-like dish on top: the dish jerks as it tries to open, the stuck ribs strain against the mast, one rib springs back, and the dish stays lopsided and half-open like a broken umbrella.
4.5-6.5 s: the camera drifts down the gold foil (the three tiny smiling germs cling to the foil, small, in passing) to a small antenna below, which starts pulsing soft glowing rings that travel away toward a tiny blue dot (Earth) far in the distance.
6.5-7.6 s: the probe fires small thruster puffs and turns; the camera swings smoothly around behind it as small bright Europa appears ahead; land exactly on the end frame.""",
  opening="exactly the start frame (three-quarter front view of the probe, Jupiter behind)",
  final="exactly the end frame (behind the probe, small Europa ahead in the centre, Jupiter's edge at the right)",
  camera="slow orbit, rise to the dish, drift down the foil, then a smooth swing around behind the probe. No cuts.",
  sound="deep space hum, metal creaks, a sad little 'sproing' from a stuck rib, then cheerful soft data beeps and small thruster puffs",
  must="the dish never opens fully; the germs are tiny and only glimpsed; exactly one probe",
  never="the dish becoming round and fully open; text; a cut"),
 dict(id="C3", start="K2", end="K3", used="16.13-24.19 s",
  lines='"...the icy moon Europa, it sensed something strange." / "Under the ice: a salty ocean holding over twice the water..."',
  chars=[PROBE, EUROPA, OCEAN, JUPITER],
  shot="""0-1.6 s: following the probe, the camera races toward Europa; the probe sweeps low past Europa's white-tan cracked icy surface, which grows huge.
1.6-3.2 s: the probe's very long thin pole glows soft cyan, and faint glowing cyan magnetic field lines around Europa bend and twist strangely.
3.2-4.5 s: the camera leaves the probe and dives straight down toward one reddish crack in the ice.
4.5-7.6 s: the camera plunges through the crack and the ice opens up like a clean cutaway: the thick white ice crust slides up to the top of the frame and a vast, deep, glowing blue ocean is revealed below; land exactly on the end frame.""",
  opening="exactly the start frame (behind the probe, Europa ahead)",
  final="exactly the end frame (cross-section: cracked white ice crust across the top, vast glowing blue ocean below, dark seafloor at the very bottom)",
  camera="fast chase past Europa, then one continuous dive down into the crack and through the ice. No cuts.",
  sound="a fast flyby whoosh, a rising electronic 'ping... ping...' detection tone, deep ice cracking, a muffled underwater boom",
  must="Europa is white-tan ice with reddish cracks; one continuous dive into the ocean",
  never="fish or creatures in the ocean; Europa looking grey and rocky; a cut"),
 dict(id="C4", start="K3", end="K4", used="24.19-32.26 s",
  lines='"...Earth\'s oceans." / "So why destroy the spacecraft that found it?" / "By 2003, it was nearly out of fuel. Soon,..."',
  chars=[OCEAN, EUROPA, PROBE, GERMS],
  shot="""0-1.3 s: the camera pulls smoothly back up out of the cross-section until the whole of Europa is seen as a cutaway globe: a thin white ice shell, a glowing blue ocean layer wrapped around the entire moon, and a rocky core.
1.3-3.6 s: the camera keeps pulling back into space and turns to find the probe floating above Europa; it pushes slowly toward the probe, whose small lights blink innocently.
3.6-6.4 s: the probe's body becomes softly see-through like an x-ray, showing one round fuel tank inside; the last glowing fuel drains down to the bottom of the tank.
6.4-7.6 s: the x-ray fades, the probe's small thrusters sputter a few weak puffs, and it starts to tumble slowly; the camera ends close on its gold foil with Europa below; land exactly on the end frame.""",
  opening="exactly the start frame (cross-section of the ice and the glowing ocean)",
  final="exactly the end frame (close on the probe's gold foil, slightly tilted, the tiny germs visible, Europa's ice below)",
  camera="one continuous pull-back out of Europa, a turn to the probe and a slow push-in to its foil. No cuts.",
  sound="a deep rising whoosh out of the water, soft blinking beeps, a draining gurgle, weak sputtering thruster puffs, a slow warning beep",
  must="the ocean layer wraps the whole moon; one probe with a lopsided dish",
  never="fish or creatures; the dish opening; a cut"),
 dict(id="C5", start="K4", end="K5", used="32.26-40.32 s",
  lines='"...nobody could steer it." / "And anything built on Earth can carry tiny hitchhikers: Earth germs." / "If it hit Europa, they could reach that ocean,..."',
  chars=[PROBE, GERMS, EUROPA],
  shot="""0-1.1 s: the probe tumbles slowly, drifting; the camera stays close on its gold foil.
1.1-3.3 s: the camera pushes in macro onto the foil: the three tiny pale-green germs wake up, yawn and stretch their stubby arms.
3.3-5.0 s: the germs wave cheerfully at the camera and then hold on tight to the foil like passengers on a bus, grinning.
5.0-7.6 s: the camera pulls smoothly back to show the whole probe; a softly glowing cyan dotted line appears, curving from the probe down to a reddish crack on Europa below, and the germs peer down at it curiously; land exactly on the end frame.""",
  opening="exactly the start frame (close on the probe's gold foil, germs visible, Europa below)",
  final="exactly the end frame (whole probe upper-left, glowing dotted line curving down to a crack on Europa, germs peering down)",
  camera="macro push-in onto the germs, then one smooth pull-back to the medium-wide. No cuts.",
  sound="tiny squeaky yawns and giggles, a cute cartoon 'boing', a soft magical chime as the dotted line appears",
  must="the germs are cute, friendly and tiny; exactly three germs",
  never="scary, slimy or gross germs; more than three germs; a cut"),
 dict(id="C6", start="K5", end="K6", used="40.32-48.39 s",
  lines='"...and any life we found might just be ours." / "So NASA dove it straight into Jupiter at almost 108,000 miles an hour."',
  chars=[PROBE, GERMS, EUROPA, JUPITER],
  shot="""0-2.9 s: a playful what-if: the three tiny germs slide down the glowing dotted line like a playground slide, zip into the crack in Europa's ice and, seen through the translucent ice, splash into the glowing blue ocean below, where a tiny friendly local microbe (a soft glowing blue blob) floats up and blinks at them, puzzled. The camera stays steady on this view.
2.9-3.4 s: the dotted line and the what-if fade away; the probe's main engine flares bright.
3.4-7.6 s: the probe turns away from Europa and dives toward giant Jupiter; the camera chases it smoothly from behind as Jupiter's cloud bands rush up to fill the frame and the probe glows hotter and hotter until it is a bright orange-white fiery streak; land exactly on the end frame.""",
  opening="exactly the start frame (probe upper-left, dotted line down to Europa)",
  final="exactly the end frame (chase view of the fiery streak plunging into Jupiter's cloud bands)",
  camera="steady wide during the what-if, then one continuous chase behind the probe into Jupiter. No cuts.",
  sound="a squeaky slide 'wheee', a tiny splash and bubbles, a curious 'bloop', then an engine roar rising into a fiery rushing entry",
  must="the what-if is clearly playful and imaginary; Jupiter fills the frame by the end; one probe",
  never="an explosion with debris; anything scary or sad; a cut"),
 dict(id="C7", start="K6", end="K0", used="48.39-56.45 s (Veo lands on the end frame about 0.3 s before the clip ends: cut on the matching frame with tools/loop_seam.py)",
  lines='"...an hour." / "Fourteen years later, they did it again: Cassini, into Saturn, to protect another ocean moon." / "That\'s why..."',
  chars=[JUPITER, SATURN, ROOM, ENGINEER],
  shot="""0-0.8 s: the fiery streak disappears into Jupiter's clouds with a soft bright glow.
0.8-2.7 s: the camera swings smoothly away across starry space; Jupiter slides out of view and golden Saturn with its huge bright rings swings into view.
2.7-4.6 s: in one wide view, the second gold probe with its big white dish dives between Saturn's rings and the planet and becomes a bright streak into Saturn's clouds.
4.6-6.3 s: in the foreground, small bright Enceladus sprays tall sparkling plumes of ice from its south pole, glittering in the sunlight.
6.3-7.6 s: the camera pulls straight back, and the whole view shrinks into the giant curved wall screen of the bright mission control room (the screen now showing Jupiter with a tiny gold probe), settling exactly on the end frame: the wide room with the engineer at the front console.""",
  opening="exactly the start frame (fiery streak plunging into Jupiter's clouds)",
  final="exactly the end frame (the wide mission control room, engineer at the front console, Jupiter on the wall screen); this is also the Reel's first frame",
  camera="a smooth swing from Jupiter to Saturn, then one continuous pull-back out of the wall screen into the room. No cuts.",
  sound="a soft glowing whoosh, a sweeping swoosh across space, a rising entry roar, a sparkling icy hiss, then mission-control murmur and console beeps returning",
  must="Enceladus plumes clearly visible; the second probe is tiny next to Saturn; land exactly on the end frame",
  never="text on screens; a second engineer in close-up; a cut"),
]

def clip_prompt(c):
    chars = "\n".join(c["chars"])
    return f"""Animate starting EXACTLY from the attached start frame: same art style, same objects, same camera position and same light as that picture.
{STYLE}
{MOTION}
{chars}
Shot, 8 seconds, vertical 9:16:
{c['shot']}
Opening frame: {c['opening']}
Final frame: {c['final']}
Camera: {c['camera']}
The clip ENDS EXACTLY on the attached end frame: in the last moment the camera settles precisely into that picture.
Real-world scale: the probe is about 6 m tall and always a tiny speck next to any planet or moon; Jupiter is about 11 Earths wide; Europa is a little smaller than Earth's Moon; Enceladus is small; the engineer is 1.65 m tall.
{COMP}
Sound: {c['sound']}. {SOUND_TAIL}
{AVOID}
Must be true: {c['must']}.
Never show: {c['never']}."""

out = ["# Jupiter crash: Flow prompts (continuous, no cuts)\n",
       "Voiceover: `audio/voiceover.mp3` (owner, ElevenLabs Mark), 56.45 s. Line starts (s): "
       "0.00, 5.26, 9.75, 14.96, 19.97, 25.53, 28.47, 33.46, 38.05, 43.89, 49.24, 55.47.\n",
       "## How this works (read first)\n",
       "1. **Keyframes K0–K6 first.** Make them with Flow's image model (Nano Banana, 9:16, 1 output each). This was free last time; check the credit count after the first one.\n"
       "   - **Owner approves all 7 keyframes before any video credit is spent.**\n"
       "   - They lock the look of the probe, Europa and the room, so the clips need no retries.\n",
       "2. **Clips C1–C7.** Each is **Veo 3.1 Fast, Frames to Video, 8 s, 9:16, 1 output, sound on**.\n"
       "   - START frame = the keyframe before; END frame = the keyframe after.\n"
       "   - Clip N ends on exactly the picture clip N+1 starts on, so the video is one unbroken camera journey.\n"
       "   - C7 ends on K0, the first frame, so the Reel loops.\n",
       "3. **Budget.** 7 clips × 20 = **140 credits**, keyframes free. At most one retry per clip, and only if a check fails. Hard cap 300 (ask the owner first).\n",
       "4. **Check every clip before the next:** `python tools/clip_check.py clips/C<n>.mp4 8` (right action, one probe, lopsided dish, no text, lands on the end frame).\n",
       "5. **Never put a real person's or spacecraft's name in a prompt.** These prompts say \"the probe\" and \"the second probe\" on purpose.\n",
       "\n---\n## Keyframe image prompts (Flow image model, 9:16)\n"]
for k, v in KEYS.items():
    out.append(f"\n### {k}: {v['title']}\nAttach as image references: {v['refs']}.\n\n```\n{v['text']}\n```\n")
out.append("\n---\n## Clip prompts (Veo 3.1 Fast, Frames to Video, 8 s)\n")
for c in CLIPS:
    out.append(f"\n### {c['id']}: START = {c['start']}, END = {c['end']}\nUsed in the Reel: {c['used']}  \nNarration over it: {c['lines']}\n\n```\n{clip_prompt(c)}\n```\n")
Path("output").mkdir(exist_ok=True)
Path("output/jupiter-crash_flow_prompts.md").write_text("".join(out), encoding="utf-8")
print("written", sum(len(x) for x in out), "chars")
