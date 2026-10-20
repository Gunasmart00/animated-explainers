# Episode Status: How Seatbelts Know When To Lock (how-seatbelts-know-when-to-lock)

- **Current Phase:** `voice_and_flow_ready`
- **Active AI:** Antigravity (Gemini Pro)
- **Last AI:** Claude Code
- **Last Updated:** 2026-10-20 19:15 IST
- **Audio:** Estimated 37.9 s (10 scenes, ~110 words, pace 4.5 syllables/s)
- **Flow Project:** `how-seatbelts-know-when-to-lock`, Veo 3.1 Fast, 9:16 portrait, Upscaled 1080p
- **Total Flow Credits Spent:** 0 / 300 limit

---

## 1. Decision Log
- **2026-10-20 (Owner):** Topic approved: *How Seatbelts Know When To Lock*.
- **2026-10-20 (Antigravity):** Scaffolding initialized via `studio.new`.
- **2026-10-20 (Antigravity):** Sourced 8 engineering claims (2 sources each) in `story.md`.
- **2026-10-20 (Antigravity):** Designed 10-scene script in `script.yaml` with dual-locking mechanics (inertia pendulum + centrifugal clutch) and infinite Reel loop (`end_frame: "s01@0"`).
- **2026-10-20 (Antigravity):** Ran `studio.flow --offline` to verify timings (37.9 s total) and generate Flow/Veo 3.1 prompts in `output/how-seatbelts-know-when-to-lock_flow_prompts.md`.

---

## 2. Clip Progress & Verification Table

| Clip ID | Target Time | Narration Line | Verification Status | Notes |
|---|---|---|---|---|
| C01 | 0.00 – 3.22 | "Pull a seatbelt gently, and it glides smoothly." | not_started | Smooth pull across chest |
| C02 | 3.22 – 6.45 | "But yank it fast, and it instantly locks." | not_started | Sudden yank, snaps rock-solid |
| C03 | 6.45 – 10.39 | "You might think this uses sensors, but it's pure mechanics." | not_started | Tracking into B-pillar, transparent trim |
| C04 | 10.39 – 14.38 | "Inside the pillar, the belt wraps around a spring-loaded spool." | not_started | Polished spool, clockwork spiral spring |
| C05 | 14.38 – 17.61 | "Inside this spool sits a tiny centrifugal clutch." | not_started | Spool hub, weighted lever + spring |
| C06 | 17.61 – 21.21 | "When yanked, centrifugal force flings the weighted lever outward..." | not_started | Slow-mo lever swinging outward |
| C07 | 21.21 – 25.20 | "...catching a heavy ratchet gear that freezes the belt cold." | not_started | Ratchet tooth engagement, solid stop |
| C08 | 25.20 – 29.16 | "And during a crash, a weighted steel ball swings forward..." | not_started | Inertia pendulum/ball in cup rolls forward |
| C09 | 29.16 – 33.14 | "...tripping a second steel arm before you can even move." | not_started | Dual pawls wedging into ratchet gear |
| C10 | 33.14 – 37.87 | "So when you pull it slowly, you're always free to buckle up." | not_started | Relaxed smile, loops cleanly to s01@0 |

---

## 3. Immediate Next Step & AI Handoff
- **Task:** Generate ElevenLabs narration audio (`episodes/how-seatbelts-know-when-to-lock/audio/voiceover.mp3`) using the script in `how-seatbelts-know-when-to-lock_flow_prompts.md`.
- **Character Reference (F0):** Generate reference image for "the driver" in yellow hoodie.
- **Next Prompt for AI:**
  ```
  Read ACTIVE_PRODUCTION.md and episodes/how-seatbelts-know-when-to-lock/STATUS.md. Generate voiceover or start Flow clip renders from output/how-seatbelts-know-when-to-lock_flow_prompts.md.
  ```
