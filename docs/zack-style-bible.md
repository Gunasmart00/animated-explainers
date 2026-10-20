# Zack D. Films Animation Bible & Style Reference

Comprehensive production bible synthesized from empirical reference video analysis (Claude Code measurements) and narrative/visual deconstruction (Gemini Pro analysis).

---

## 1. Narrative Architecture (The 30–45s Formula)

Every video strictly follows a three-part retention architecture:

```
┌─────────────────────────────────────────────────────────────┐
│ 00:00 - 00:03 │ VISUAL DISRUPTION HOOK                     │
│               │ Instant premise inversion (< 10 words)      │
├─────────────────────────────────────────────────────────────┤
│ 00:04 - 00:18 │ MECHANICAL ESCALATION                       │
│               │ Cross-section ("X-ray"), step-by-step logic │
├─────────────────────────────────────────────────────────────┤
│ 00:19 - 00:35 │ CLIMACTIC PAYOFF / ABSURD TWIST             │
│               │ Explosion, paradox, or dark comedy punchline│
└─────────────────────────────────────────────────────────────┘
```

### 1.1 The Hook (00:00 – 00:03)
- **Rule:** The lead line MUST be under 10 words and start mid-action.
- **Negative Premise Inversion:** Introduce an impossible action or counter-intuitive fact immediately:
  - *"If you grab a tube light and stick it into the ground... nothing happens. But..."*
  - *"They built a light bulb that lasted 2,000 hours... but there was a problem."*
  - *"The teacher turned her back, so students thought they were safe..."*
- **Forbidden:** No channel greetings ("Hey guys"), no "Did you know?", no slow setup.

### 1.2 Mechanical Escalation & Cutaways (00:04 – 00:18)
- **Rule:** Explain the "hidden mechanism" through cross-sections or step-by-step logic.
- **Visual Cross-Sections / Cutaways:**
  - Slicing through a glass tube to expose mercury ($Hg$) electron collision.
  - Slicing through horse ribs/muscle tissue down to burning oxygen.
  - Looking beneath floorboards to inspect hidden release pegs and ropes.
  - Anatomical hologram showing cellular dehydration in kidneys and brain.
- **Hidden Mechanism Glow:** Mechanism or pivotal element gets a subtle colored glow or bounding box (yellow/green outline).

### 1.3 Climactic Payoff / Punchline (00:19 – 00:35)
- **Rule:** End with an unmistakable visual revelation, explosion, paradox, or comedic twist.
- **Forbidden:** No moralizing summaries, no preachy outro, no "follow for more" / "like and subscribe".

### 1.4 The Seamless Reel Loop
- **Rule:** The final frame of the final clip must visually match the first frame of scene 1 (`end_frame: "s01@0"`).
- The narration's closing clause seamlessly connects back to the hook sentence so viewers replay the video without noticing the seam.

---

## 2. Visual & Aesthetic Standards

### 2.1 The "Clean 3D Simulation" Look
- **Stylized Family-Feature 3D:** Rounded proportions, larger expressive head, big eyes with bright specular catchlights, smooth soft skin, chunky simplified hands.
- **Neither photorealistic nor flat cartoon:** Resembles clean, high-end stylized CAD/game-engine character assets (similar to modern Illumination/Pixar family films or polished Sims 4).
- **Clothes & Props:** Solid saturated colors (yellow, teal, cream, orange, navy). No fine logos, no tiny text labels printed on shirts or papers.

### 2.2 Lighting & Color Palette
- **High-Key Bright Daylight:** Average brightness $\ge 0.35$; dark pixels $\le 15\%$ (up to $30\%$ only for nighttime/space/underground scenes).
- **Color Temperature Contrast:** Cool backgrounds (pale teal, turquoise, cyan, blue walls) against warm subjects (skin tones, warm honey-wood, orange/red clothing).
- **Never Dark or Muddy:** Soft ambient daylight, gentle highlight bloom, clean soft contact shadows.

### 2.3 Camera Rigidity & Framing
- **Linear Spline Motions:** Camera moves along clean, rigid paths (smooth dolly-in, straight tracking, top-down tactical angles, or snap-zooms).
- **No Handheld Float:** Avoid disorienting wobble, drunken drift, or chaotic panning.
- **Pacing:** A new camera angle or punchy visual cut every **1.0 to 2.8 seconds**.
- **Keep-Clear Zones:** Keep the main action centered. Top-right is reserved for the HowZit logo watermark; bottom 25% is reserved for subtitles.

---

## 3. Audio & Foley Architecture

- **Narration Cadence:** Fast, conversational delivery at **4.3 to 5.1 syllables/second** (~170–190 WPM) with minimal pauses ($< 250\text{ ms}$).
- **Micro-Action Sync:** 1–2 visual actions for every beat of narration (e.g., foot taps, head turns, paper flies, spark fires).
- **Dense Tactical Sound Effects (Foley):** Crisp shoe clicks, lens zoom whirrs, paper rustles, electrical sparks, sub-bass impacts.
- **Strict Audio Bans:**
  - **NO Background Music** (allowed only for pure technical/engineering episodes).
  - **NO Whoosh Sounds on Scene Cuts** (tested and removed; sounds artificial and distracting).
  - Target mix loudness: **−14 LUFS**.

---

## 4. Subtitles & On-Screen Graphics

- **Font:** Open Sans ExtraBold, centered around $y \approx 1500$ (on 1080×1920 canvas).
- **Highlighting:** Single Lime-green highlight per phrase (`#a3e635`). Text on lime uses `ink` (`#0f172a`).
- **Pop-ups:** Rendered programmatically via `studio.build` (never generated inside AI clips). Numbers, questions ("?"), warnings ("!"), or key words (e.g., "4K", "REC").
- **Hashtags:** Exactly 5 relevant hashtags per post (Instagram standard).
