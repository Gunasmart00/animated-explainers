# Owner creative rules (2026-10-20)

From the owner, Gunaseelan, 2026-10-20. These apply to every HowZit / Lowkey Genius episode, for Claude Code and Antigravity alike.
Where they differ from `docs/zack-style-bible.md` or older notes, **this file wins** (see "Changes to older rules" at the end).

## 1. Story shape: H-P-C plus a double payoff
- **H (Hook):** start with the hook, inside the first second. No greeting, no setup.
- **P (Progression):** each beat raises the question further. **Don't give the payoff early.** The answer lands at the end, never in the middle.
- **C (Climax):** the moment the topic is fully answered.
- **Double payoff:** everybody does hook → payoff. We add a **second payoff in the very last second: a twist** the viewer didn't see coming. It makes them rewatch and share.
- **Always loop:** the last frame and last words run straight back into the first (`end_frame: "s01@0"`; cut on the exact matching frame with `tools/loop_seam.py`).

## 2. The first seconds
1. **The camera zooms in as the video starts.** No static opening frame.
2. **Show the whole setting in one go first:** a wide shot from far away, then zoom in. The eye scans the scene and instantly knows where we are and what's going on.
3. **The first 3 seconds show an emotion:** surprise, shock, delight, confusion, comic panic. A face reacting, not just an object.

## 3. Easter eggs
4. **Hide one detail in the frames** that makes viewers ask "why is that there?" and pay attention. It should pay off later: the twist explains it, or it rewards the rewatch. Plan it in the script (`easter_egg:` field) like any other shot.

## 4. What we make
- **Main focus (owner, 2026-10-25): four lanes.** Happy-tears true stories, goosebump true stories, mystery stories, and space mysteries. Pitch ideas from these first; the other kinds below are secondary.
- **Universal appeal:** visual storytelling, biology, and curiosity-driven science work across cultures and languages. Explain with pictures first, words second.
- **Business stories:** "why does this company do this weird thing?" → we explain → the viewer goes "oh, that's genius".
- **Space:** celestial events, fun facts, beautiful deep-space visuals, imaginative stories set in space.
- **Make viewers feel smart** for watching and for sharing it.
- **Never sad or depressing.** The mood is curious, funny, exciting or mysterious.
- Prefer topic types that are **already performing** (Zack D. Films' best: brand stories, "what happens if", hidden functions, space and body facts). Skip tragedies and disasters as the main subject.

## 5. Everything fits together
Voiceover, footage, animation, editing, captions, music and sound effects are planned together for each beat, not added at the end.
- **Fast pacing, attention-grabbing, no pauses** in the narration.
- **Quick music:** a short, upbeat, licensed music bed, low under the voice.
- **Captions** on every line.
- **Questions:** on-screen and spoken questions that pull the viewer forward ("why?", "but how?").

## 6. Posting
- **Once a day**, every day: consistency beats bursts.
- **Post at the audience's peak time.** For our US-first market that's about 7 PM US Eastern (4:30 AM IST until 31 Oct 2026, 5:30 AM IST after). Check Studio → Analytics → "When your viewers are on YouTube" once there's data, and move the time to match.

## 7. Script checklist (add to every `script.yaml` review)
- [ ] Hook in the first second; an emotion on screen by 3 s
- [ ] Opening: wide establishing shot with a zoom in
- [ ] No payoff before the climax scene
- [ ] Climax = topic fully answered; **twist in the last second**
- [ ] Loop: last words + last frame run into the first
- [ ] One planned Easter egg, paid off by the twist or on rewatch
- [ ] Not sad: mood is curious / funny / exciting / mystery
- [ ] Music, SFX, captions and questions planned per beat; no pauses

## 8. Hashtags (owner, 2026-10-21)
Every post gets **20 hashtags: 5 about the video + 15 broad, popular ones**.
- **YouTube Shorts:** all 20 go in the description. `#shorts` goes first, then the 2 best video tags, because the first 3 hashtags show above the title. YouTube ignores *all* hashtags when there are more than 60, and can remove a video for misleading or unrelated hashtags. So the 15 popular tags must still be broad and honest (#viral, #fyp, #didyouknow, #science…), never another creator, film or celebrity.
- **Instagram:** a post or Reel accepts only **5 hashtags in the caption** (Instagram's limit since Dec 2025). Put the 5 video tags in the caption and the 15 popular tags (#reels instead of #shorts) in the first comment.
- `script.yaml` keeps `hashtags:` = the 5 video tags; add `viral_hashtags:` with the 15 popular tags.

## 9. Look and story format (owner, 2026-10-24)
- **New look: Zack's look for every video** (owner, 2026-10-24): a real-time video-game engine render: Character-Creator
  people in plain T-shirts, empty game-level sets with painted blue/teal walls, a cool blue palette with one warm accent,
  flat even light, everything in sharp focus, close-ups of hands and objects. Not cartoon, not cinematic, never photo-real.
  Style block (F-STYLE in `prompts/flow.md`) and the full study: `docs/zack-structure.md`. Never copy his characters or use
  his frames as Flow inputs.
- **Story writing follows his formula** (open mid-action, third person, "But / You see / Well / Finally", ending calls
  back the opening). Each short gets a wiki-style page `episodes/<name>/README.md` (`templates/short-page.md`), listed
  in `docs/shorts-index.md`; recurring cast in `docs/characters.md`.
- **Touching true stories are welcome** when the ending is uplifting (never a sad ending).
- **No keyframe images by default** (owner, 2026-10-24; Canva hit its limit): clips are text-to-video, or chained from the previous clip's last frame (JPEG, `tools/last_frame.py`); the last clip ends on the first clip's first frame for the loop.
- **Pitches:** ideas the owner doesn't pick are marked `rejected` in `ideas/backlog.csv` and never pitched again.

## 10. The question loop (owner, 2026-10-25)
Every video asks one question early and answers it in the very last line, so the answer is the twist and the loop
replays the question right after it (people rewatch to check, and comment their guess).
- **Ask it in the first 5 s,** in the narration or right after the hook line, and show it as a white pop-up with 🤔.
- **Answer it in the last 2 s** with the lime pop-up (the one lime moment) and ✅. Never answer it earlier.
- **Pick one of three kinds:**
  1. *Spot it:* "Watch her back. What else is she carrying?" (ties into the Easter egg; answer: her own baby).
  2. *Guess it:* "Guess how far he followed them." (a number; answer: 430 miles).
  3. *Could we / would you:* "Could we stop an asteroid?" (answer: "We already did.").
- **The caption and the pinned first comment repeat the question** ("Did you guess right? 👇").
- The answer must be true and sourced like every other claim.

## Changes to older rules
- **Music:** older notes said "no music" (`CLAUDE.md`, `docs/zack-style-bible.md`). From 2026-10-20 the owner wants **quick music**: keep it licensed, short, upbeat and low under the narration. Still **no whoosh on scene cuts**.
- **Payoff timing:** the style bible's "payoff 0:19–0:35" now means the climax sits at the end. Nothing is revealed early, and a twist lands in the final second.
