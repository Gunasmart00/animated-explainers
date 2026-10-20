# Cross-AI Collaboration & Handoff Protocol

This protocol governs how **Claude Code** and **Antigravity (Gemini Pro)** collaborate on video production, switching between episodes or mid-episode without loss of context, broken files, or duplicated work.

---

## 1. Single Source of Truth Architecture

To ensure perfect continuity across AI switches:

```
g:/Apps/animated-explainers/
├── ACTIVE_PRODUCTION.md          <-- GLOBAL POINTER: Current active episode, phase, and next prompt
├── episodes/
│   └── <episode-name>/
│       ├── story.md              <-- Fact research, geometry, scale, character definitions
│       ├── script.yaml           <-- Narration, timing, shots, SFX, popups, loop end frame
│       ├── STATUS.md             <-- EPISODE LOG: Decisions, clip audit, credit spend, AI handover
│       ├── clips/                <-- Generated MP4 clips
│       ├── audio/                <-- Voiceover & SFX
│       └── output/               <-- Rendered MP4, SRT, cover, caption
└── docs/
    ├── zack-style-bible.md       <-- Master pacing, visual, and narrative rules
    ├── flow-ai-pitfalls-and-rules.md <-- Prompt engineering defense
    └── ai-handoff-protocol.md    <-- This document
```

---

## 2. The 95% Resource Limit & Pause Rule (MANDATORY)

Both Claude Code and Antigravity have operational constraints (weekly token quotas, context window limits, or rate limits).

### The Trigger:
When **EITHER** AI notices:
- It has reached approximately **95% of its rate limit, message budget, or context window**, OR
- An API usage/quota warning is received, OR
- The user instructs to hand off to the other AI:

### The 4-Step Handover Procedure:
1. **PAUSE Immediately:** Stop launching new generations or downloads. Do NOT leave half-rendered drafts or broken files.
2. **AUDIT Current Work:** Run `python tools/clip_check.py` on any downloaded clips. Confirm which scenes are approved, which need retries, and total credits spent.
3. **UPDATE Files:**
   - Write/Update `episodes/<current>/STATUS.md`:
     - Record all decisions made during the session.
     - Update the Clip Status table (Approved, Rejected, Pending).
     - State exact credit count and remaining tasks.
   - Update `ACTIVE_PRODUCTION.md` at root:
     - Set `Last Active AI: [Claude Code | Antigravity (Gemini Pro)]`
     - Set `Current Phase`
     - Fill out `Next Step for Incoming AI` and `Exact Prompt to Continue`.
4. **NOTIFY The User:** Give a concise summary to the user indicating that the handoff state is cleanly persisted and paste the exact prompt to send to the next AI.

---

## 3. Starting Work (Initialization for Both AIs)

Whenever Claude Code or Antigravity starts a session or receives a user prompt:
1. **Read `ACTIVE_PRODUCTION.md`** first to know which episode is active, what phase it's in, and what the previous AI left behind.
2. **Read `episodes/<name>/STATUS.md`** to review the decision log, approved clips, and specific owner preferences for this episode.
3. **Acknowledge the current state** to the user in the opening line (e.g., *"Resuming Gen Z Teacher at Step 9 (Build Draft)..."*).
4. **Proceed directly** with the planned next step without re-asking questions that were already decided in the log.

---

## 4. Episode `STATUS.md` Standard Schema

Every episode folder MUST contain a `STATUS.md` formatted as follows:

```markdown
# Episode Status: <Title> (<slug>)

- **Current Phase:** [idea | scripting | audio | prompts | generation | review | draft | final | published]
- **Active AI:** [Claude Code | Antigravity (Gemini Pro)]
- **Last Updated:** YYYY-MM-DD HH:MM IST
- **Total Flow Credits Spent:** [X] / 300 limit

## 1. Decision Log
- [YYYY-MM-DD] [AI / Owner] Decision details (e.g., "Switched protagonist to female college student").
- [YYYY-MM-DD] [AI / Owner] "Removed scene-change whoosh sounds per owner feedback".

## 2. Clip Progress & Verification Table

| Clip ID | Scene | Target Time (s) | Status | Notes / Fix Needed |
|---|---|---|---|---|
| C01 | s01 | 0.0 – 3.3 | Approved | Teacher turn smooth, aisle walking accurate |
| C02 | s02 | 3.3 – 5.5 | Needs Retry | Student turned around too fast; fix prompt camera |
| C03 | s03 | 5.5 – 7.6 | Pending | Not generated yet |

## 3. Current Blockers & Next Immediate Step
- **Immediate Task:** [Clear actionable step]
- **Next Prompt for AI:** "[Pre-written prompt for incoming AI]"
```
