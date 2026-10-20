# Active Production Dashboard

This file tracks the real-time production status across AI switches (Claude Code <-> Antigravity).

---

## Current Status

- **Active Episode:** `how-seatbelts-know-when-to-lock` (How Seatbelts Know When To Lock)
- **Current Phase:** `scripting`
- **Active AI:** Antigravity (Gemini Pro)
- **Last AI Active:** Claude Code
- **Last Updated:** 2026-10-20 19:11 IST
- **Completed Episodes:** 3/3 published (`db-cooper`, `stop-drinking-water`, `genz-teacher`)

---

## Episode Pipeline Summary

| Episode Slug | Title | Status | Output File | YouTube Shorts Link |
|---|---|---|---|---|
| `db-cooper` | The Man Who Vanished Mid-Flight | **Published** | `episodes/db-cooper/output/db-cooper_howzit.mp4` | [Live Link](https://youtube.com/shorts/Xn5k2dD12MA) |
| `stop-drinking-water` | What Happens When You Stop Drinking Water | **Published** | `episodes/stop-drinking-water/output/stop-drinking-water_howzit.mp4` | [Live Link](https://youtube.com/shorts/TbRr7Y8m5Hw) |
| `genz-teacher` | She Caught the Whole Class Cheating in 4K 💀 | **Published** | `episodes/genz-teacher/output/HowZit - Dont Underestimate Gen Z Teachers.mp4` | [Live Link](https://youtube.com/shorts/z8e4bJj5_k0) |
| `how-seatbelts-know-when-to-lock` | How Seatbelts Know When To Lock | **Scripting** | TBD | In Production |

---

## Active Tasks & Handover Notes

### Task 1: Research & Story Construction
1. Research seatbelt dual-locking retractor mechanics:
   - Vehicle-sensitivity mechanism (steel inertia pendulum / weighted ball).
   - Webbing-sensitivity mechanism (centrifugal clutch / flyweight ratchet).
   - Pre-tensioner explosive micro-charge (optional twist / climax).
2. Write `episodes/how-seatbelts-know-when-to-lock/story.md` with exactly 2 credible engineering sources per claim.

### Task 2: Scene-by-Scene Script & Flow Prompts
1. Write `episodes/how-seatbelts-know-when-to-lock/script.yaml` following Zack D. Films retention formula:
   - 0:00–0:03 Hook: pull slow vs yank fast (< 10 words, premise inversion).
   - 0:04–0:18 Mechanical Escalation: transparent B-pillar cutaway, glowing mechanism, metallic ratchet clicks.
   - 0:19–0:35 Payoff: emergency braking lock, seamless loop back to the first frame.
2. Generate voiceover and run `.venv\Scripts\python.exe -m studio.flow episodes/how-seatbelts-know-when-to-lock`.


---

## Handoff Prompt for Incoming AI
When starting or resuming in Claude Code or Antigravity, use this prompt:
```
Read ACTIVE_PRODUCTION.md, docs/ai-handoff-protocol.md, and the active episode's STATUS.md. Continue from the immediate next task.
```
