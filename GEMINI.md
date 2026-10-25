# GEMINI.md — Antigravity (Gemini Pro) Directives

This project renders **HowZit** 3D explainer Reels (Instagram `@howzit.explains`) posted as a Collab with **Lowkey Genius**.
Shared workspace with Claude Code (`CLAUDE.md`). Both AIs follow the same rules and handoff protocol.

---

## 1. Startup Routine (Every Turn / Task)
1. **Read `ACTIVE_PRODUCTION.md`** first to determine the active episode, current phase, and immediate next task.
2. **Read `episodes/<current>/STATUS.md`** for specific episode history, approved clips, and decisions made.
3. **Reference Docs:**
   - **Owner creative rules (2026-10-20, override the bible where they differ):** `docs/owner-creative-rules.md`. Covers: hook, progression and climax, with a **twist in the last second**; zoom-in opening with a wide establishing shot; an emotion in the first 3 s; an Easter egg; never sad; **quick music**; post once a day at peak time.
   - Visual & Narrative style: `docs/zack-style-bible.md`
   - Flow / Veo Prompt Engineering: `docs/flow-ai-pitfalls-and-rules.md`
   - Cross-AI Rules: `docs/ai-handoff-protocol.md`
4. State the active episode and current phase in your opening sentence, then execute the mapped next step.

---

## 2. The 95% Resource Limit & Pause Rule (MANDATORY)
When nearing **95% of your context window, token budget, or rate limits**, or when ending your session:
1. **PAUSE immediately.** Do not start new renders or leave half-downloaded media.
2. **UPDATE `episodes/<current>/STATUS.md`** with all progress, verified clips, decisions made, and credit counts.
3. **UPDATE `ACTIVE_PRODUCTION.md`** with the exact immediate next task and the ready-to-paste handoff prompt.
4. Present a crisp summary to the owner with the next step.

---

## 3. Core Style Rules (Zack D. Films Standard)
- **Structure:** 0:00–0:03 Hook (< 10 words, premise inversion) -> 0:04–0:18 Mechanical Escalation (cross-sections/cutaways) -> 0:19–0:35 Payoff/Twist.
- **The Reel Loop:** Last clip ends on first clip's starting frame (`end_frame: "s01@0"`).
- **Audio:** Fast continuous narration (4.3–5.1 syllables/s). **NO music** (unless engineering), **NO whoosh sounds on scene transitions**. Target −14 LUFS.
- **Visuals:** Bright, high-key daylight (brightness $\ge 0.35$), stylized 3D family-feature look (rounded proportions, big expressive eyes, smooth skin). NOT dark, NOT photoreal.
- **Facts:** Exactly 2 reliable sources per claim in `story.md`. No invented numbers.
- **Subtitles & Popups:** Open Sans ExtraBold at $y \approx 1500$. Max one lime word highlight per frame. Exactly 5 hashtags.

---

## 4. Automation Commands (Windows PowerShell)
- Environment Python: `.venv\Scripts\python.exe`
- Start new episode: `.venv\Scripts\python.exe -m studio.new "<Title>"`
- Script timing & Flow prompts: `.venv\Scripts\python.exe -m studio.flow episodes/<name>`
- Verify downloaded clip: `.venv\Scripts\python.exe tools\clip_check.py episodes/<name>\clips\c<num>.mp4 <seconds>`
- Build draft video: `.venv\Scripts\python.exe -m studio.build episodes/<name> --draft`
- Build final video: `.venv\Scripts\python.exe -m studio.build episodes/<name>`
- Measure video metrics: `.venv\Scripts\python.exe tools\analyse_reference.py output/<name>_howzit.mp4`
