# Scene-by-scene script (Zack-style)

How Claude writes `episodes/<name>/script.yaml` for the Flow + ElevenLabs pipeline. Based on
`docs/zack-style-analysis.md`. Example: `episodes/db-cooper/script.yaml`.

## Narration
- **30–45 s, 90–130 words** (all 8 reference Reels: 24–58 s, median 32 s). Up to 60 s / 165 words only when the
  story truly needs it. The voice runs at ~4.6 syllables a second; pauses only at sentence ends.
  Check the length with `python -m studio.flow episodes\<name> --offline` before spending voice credits.
- **First line drops straight into the action or the strange detail.** No greeting, no "did you know", no topic
  announcement. For a famous story, open on a detail that doesn't give it away (D.B. Cooper opens on the flap).
- **Short clauses chained with "but", "so", "then", "until", "and as".** Simple spoken words. Numbers written the way
  they're said ("two hundred thousand dollars"); the pop-up shows the digits.
- **Open loops:** hold back the answer; every few lines, give a reason to keep watching.
- **End on the payoff or the reveal.** No outro, no "follow for more" (the caption does that).
- **Loop:** the last line should lead straight back into the first ("...D.B. Cooper." → "See this tiny flap..."), and the
  last clip ends on the first clip's opening frame (`end_frame`). See `prompts/flow.md`.
- Past tense for true stories, "you" for tricks and how-tos.

## Scenes
- **10–16 scenes, one beat each (2–5 s, 5–14 words).** Every scene must look different from the one before: new
  angle, new subject, or a big camera move.
- **Pick the edit:** stories, history and conspiracies use a *rapid montage* (a new clip every 1–2 beats);
  physical or scientific demonstrations use a *continuous journey*: one 8 s clip whose camera travels from wide
  to macro to cutaway, shared by 2–3 scenes.
- **Two or three short beats can share one 8 s Flow clip** when the action continues (saves 20 credits each): give the later
  scenes `clip: clips/<first id>.mp4` and `clip_start: <seconds into the clip>`, and no `shot`.
- Aim for **7–12 Flow clips per video** (140–240 credits on Veo 3.1 Fast; Google AI Pro has 1,000 a month).

## Fields
```yaml
title: "..."                    # also the episode name
preset: explainer
structure: hook                 # hook | reveal
caption: |                      # Instagram caption: hook line, 2-3 lines, follow line, a question
  ...
hashtags: [a, b, c, d, e]       # exactly 5, no #
cover_text: "..."               # 2-4 words
alt_text: "..."
voiceover: audio/voiceover.mp3  # added after ElevenLabs (leave out to use the built-in voice)
voice_credit: "Voice: elevenlabs.io"   # only if the ElevenLabs account is on the free plan
characters:                     # every recurring person/animal/object with a fixed look
  - name: "the bellhop"
    look: "a young man with a red vest, red cap with a gold band, white shirt, black trousers"
    size: "1.75 m tall adult man"        # real-world size, required for every character and object
setting: "default place and light for the episode"
facts:                          # every claim, 2 reliable sources each
  - claim: "..."
    sources: ["https://...", "https://..."]
overrides:                      # only when needed
  music: { file: auto }         # design / engineering episodes may want a quiet music bed
scenes:
  - id: s01
    narration: "One beat of the voiceover."
    characters: ["the bellhop"]          # names from `characters` (used as Flow Ingredients)
    shot: "0-2 s: ...; 2-4 s: ..."       # very specific: who does what, which object, how it moves, beat by beat
    camera: "smooth slow push-in from a medium shot to a macro close-up on his hands"
    setting: "only if different from the episode setting"
    sfx: "every sound the action makes"  # Flow generates these; no music, no voices
    must: ["facts that must be visible"]  # e.g. "all three engines are at the tail"
    never: ["wrong versions to rule out"] # e.g. "a door in the side of the fuselage"
    start_frame: "s08@4.04"              # optional: Frames to Video from an approved clip's frame
    popups:                              # numbers / key words, added by the build
      - { text: "$30", at_word: "thirty" }
  - id: s02
    narration: "The next beat, same shot continuing."
    clip: clips/s01.mp4                  # shares s01's clip
    clip_start: 4
  - id: s13                              # the last scene loops back to the first frame
    end_frame: "s01@0"
    clip_start: 4.18                     # 8 − this scene's seconds
```

## Writing a great `shot` (this decides the video's quality)
- Name the subject, its exact action, and how it moves, beat by beat: "0-2 s: the bellhop counts five one-dollar bills
  onto his palm; 2-4 s: he slips two into his vest pocket and glances left".
- One clear idea per shot; physical, readable motion (hands, objects moving, doors opening, things falling).
- For how-it-works beats: cutaway, see-through shells, cross-sections, atoms as coloured spheres, or the hidden part
  (or a thin fast thing like a wire or fishing line) traced with a glowing green, yellow or cyan outline.
- Big moment, shake or reveal: ask for a deep sub-bass thud in `sfx`; the lime pop-up adds the build's impact sound.
- Bright: say where the light comes from ("sunlit lobby", "bright lab lights"). Night, space or underground scenes:
  the subject brightly rim-lit with glowing accents (moonlit blue, floodlights, glowing magma).
- Never ask for text, numbers, labels, timers, signs or logos in the picture (the build adds pop-ups).
- Real people: generic stylised look only; unidentified people from behind or in shadow.
- Keep the bottom quarter calm (captions) and the top-right corner clear (logo).
