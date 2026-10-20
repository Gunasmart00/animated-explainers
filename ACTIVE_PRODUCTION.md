# Active Production Dashboard

This file tracks the real-time production status across AI switches (Claude Code <-> Antigravity).

---

## Current Status

- **Active Episode:** `genz-teacher` (Don't Underestimate Gen Z Teachers)
- **Current Phase:** `final_published_pending` (Video rendered, YouTube draft awaiting final publish click)
- **Active AI:** Antigravity (Gemini Pro)
- **Last AI Active:** Claude Code
- **Last Updated:** 2026-10-20 14:40 IST
- **Total Flow Credits Spent:** ~240 credits (within 300 limit)

---

## Episode Pipeline Summary

| Episode Slug | Title | Status | Output File | YouTube Shorts Link |
|---|---|---|---|---|
| `db-cooper` | The Man Who Vanished Mid-Flight | **Published** | `episodes/db-cooper/output/db-cooper_howzit.mp4` | [Live Link](https://youtube.com/shorts/Xn5k2dD12MA) |
| `stop-drinking-water` | What Happens When You Stop Drinking Water | **Published** | `episodes/stop-drinking-water/output/stop-drinking-water_howzit.mp4` | [Live Link](https://youtube.com/shorts/TbRr7Y8m5Hw) |
| `genz-teacher` | She Caught the Whole Class Cheating in 4K 💀 | **Draft on Studio** | `episodes/genz-teacher/output/HowZit - Dont Underestimate Gen Z Teachers.mp4` | Draft in YouTube Studio |

---

## Active Tasks & Handover Notes

### Task 1: Complete Gen Z Teacher YouTube Shorts Publish
1. Open YouTube Studio (**Content -> Shorts**).
2. Edit draft *"She Caught the Whole Class Cheating in 4K 💀"*.
3. Confirm settings:
   - Paid promotion: No
   - Altered content (AI): Yes
   - Category: Education
   - Tags: `teacher catches students cheating, exam cheating, gen z teacher, caught in 4k, school animation, 3d animation, funny shorts, howzit`
4. Visibility: **Public** -> Click **Publish**.
5. Pin channel comment: *"Tag the friend who'd pass you the whole answer sheet 👇😂"*

### Task 2: Ready for Next Episode Selection
When the owner is ready for the next video, pick from `ideas/backlog.csv` or user topic:
- *How Seatbelts Know When To Lock* (how-it-works / cross-section mechanics)
- *Why Pen Caps Have A Tiny Hole* (hidden-function / airflow physics)
- *What Happens If You Step In Quicksand* (survival / density physics)
- *Trapped In A Sinking Car* (survival / water pressure)

---

## Handoff Prompt for Incoming AI
When starting or resuming in Claude Code or Antigravity, use this prompt:
```
Read ACTIVE_PRODUCTION.md, docs/ai-handoff-protocol.md, and the active episode's STATUS.md. Continue from the immediate next task.
```
