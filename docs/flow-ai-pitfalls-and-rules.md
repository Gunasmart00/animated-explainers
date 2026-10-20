# Google Flow & AI Video: Pitfalls, Rules, and Tool Alternatives

This document details why generative video models (Google Flow / Veo 3.1, Runway, Luma, Kling) struggle with technical 3D explainer shorts, and the exact defensive engineering required to prevent wasted credits.

---

## 1. Core AI Video Pitfalls (Why Models Fail)

### 1.1 Micro-Physics & Finger Interaction Failure
- **Pitfall:** Diffusion video models cannot render fingers manipulating small items (e.g., handing over paper bills, typing passwords, picking locks, holding tiny screws). They generate melted fingers, extra digits, or morphing blobs.
- **Defensive Rule:** Never prompt fingers performing delicate tasks. Instead:
  - Frame the shot at elbow or shoulder level.
  - Show the object in a loose palm or resting on a table surface.
  - Use fast cutaways or zoom shots where the hand simply enters the frame and drops/picks the item.

### 1.2 Cutaway / Cross-Section Mesh Warping
- **Pitfall:** Asking a text-to-video AI to "slice open an airplane" or "show inside the engine" often produces exploding debris or surreal surrealistic melting rather than a clean technical CAD cross-section.
- **Defensive Rule:**
  - Establish a separate dedicated shot for the interior cross-section rather than asking the AI to transition smoothly from exterior to interior inside one 8-second clip.
  - Describe the interior as an independent, lit diagram or hologram (e.g., *"Anatomical 3D glowing hologram of kidneys on a transparent teal glass pedestal"*).

### 1.3 Character & Wardrobe Incoherence
- **Pitfall:** Diffusion video re-rolls face geometry, clothing color, and hair style on every prompt unless strictly constrained.
- **Defensive Rule:**
  - Create a character reference block (R1, R2) with identical, copy-pasted physical descriptions across every single scene prompt.
  - Include specific distinct accessories (e.g., *"thin black smartwatch on left wrist, gold hoop earrings, high ponytail"*).
  - Use Flow's image ingredients tool with high fidelity.

### 1.4 Camera Wobble & Spatial Drift
- **Pitfall:** AI models default to cinematic floaty handheld drone cameras that rotate unpredictably.
- **Defensive Rule:**
  - Anchor the camera: specify exact height, angle, and motion (e.g., *"Camera: eye level at 1.2 m, static front angle, smooth linear push-in 5 cm/s along the center aisle"*).
  - Explicitly forbid camera turns: *"Avoid: camera rotation, dutch tilt, panning away from center aisle"*.

---

## 2. The Defensive Prompt Engineering Standard (F-STYLE)

Every Google Flow / Veo clip prompt must follow this structured template:

```markdown
[F-STYLE BLOCK]
Characters: [EXACT character description copied verbatim from story.md]
Objects: [Researched physical dimensions, e.g., phone 16x7.7 cm, desk 75 cm tall]
Shot ([X] seconds, vertical 9:16):
- [0-2 s]: [Explicit visual action and character posture]
- [2-5 s]: [Secondary action and reaction]
Timing: [Key milestone timestamps]
Opening frame: [Exact composition of frame 0]
Final frame: [Exact composition of final frame, matching next scene's frame 0]
Camera: [Rigid linear movement, height, lens focal length]
Setting and light: [High-key bright daylight, pale teal walls, warm subject tones]
Real-world scale: [Height of characters, objects relative to human hands]
Sound: [Tactile foley sounds. NO music. NO speech/voices]
Composition: [Center action, keep bottom 25% clear for captions, top-right for logo]
Avoid: [Any text/numbers drawn in scene, photorealism, extra fingers, dark lighting, morphing]
must: [Critical positive constraint]
never: [Critical negative constraint]
```

### Prompt Checklist (Before Spending 1 Credit)
1. **Real-World Size Check:** Are heights and proportions physically correct? (e.g., desk 75 cm, teacher 1.65 m, phone spans 2 palms).
2. **Text Prohibition:** Papers show fine grey scribble lines only; no readable text, no numbers, no fake subtitles.
3. **Neighbor Frame Alignment:** Does scene $N$'s final frame connect logically to scene $N+1$'s opening frame?
4. **Credit Discipline:** Generate 1 output first. Run `python tools/clip_check.py clips/<id>.mp4 <seconds>`. Only regenerate if it fails inspection. Do not exceed 300 credits per episode without owner approval.

---

## 3. Tool Stack & Alternatives Catalog

For reference and future pipeline expansion:

| Tool | Category | Best Used For | Cost / Access |
|---|---|---|---|
| **Google Flow (Veo 3.1 Fast)** | Generative Video | Primary rapid scene generation (9:16 portrait) | Pay-per-credit |
| **Blender** | 3D Simulation & Animation | Precise mechanical cross-sections (boolean cutaways), CAD models | 100% Free / Open Source |
| **Mixamo (Adobe)** | Character Rigging & Mocap | Auto-rigging human characters with instant walk/run/react cycles | 100% Free |
| **Cascadeur** | AI Physics Animation | Physically accurate character animation without keyframe tedium | Freemium |
| **Mootion AI / Krikey** | Full 3D AI Video | Generates full 3D animated scenes with camera/light controls | Commercial |
| **3D AI Studio** | 3D Asset Gen | Converts text/images into Mixamo-ready rigged meshes | Commercial |
| **DaVinci Resolve** | Video Post-Production | Multi-track audio mix, foley alignment, color grading | Free Version |
| **ElevenLabs** | Voice Synthesis | Fast, conversational voiceover (Mark - Natural Conversations) | Freemium / Paid |
| **Edge-TTS (`studio/voice.py`)** | Voice Synthesis (Fallback) | Free zero-credit narration (`BrianMultilingualNeural +10%`) | 100% Free |
