# Script writer (for Claude)

The rules and the exact YAML format live in **`prompts/gemini.md` → G1**, so Gemini and Claude write
scripts the same way. When asked to write a script, Claude follows G1, then G2 (fact check) and G3
(retention check) itself, and saves the result as `episodes/<name>/script.yaml`.

Extra checks Claude runs before saving:
- 140–160 narration words in total (count them).
- Every `at_word` appears verbatim in its scene's narration; `nth: 2` for a repeated word.
- Lime pop-up at most once. Hook 3–7 words.
- `structure: reveal` → the answer is not said before the last scene.
- Exactly 5 hashtags, none of reels / viral / explore / fyp.
- `facts` sources only when sure they exist; otherwise `[]` and tell the owner which claims need checking.
- Then run `python -m studio.build episodes/<name> --draft` and fix any warnings.

## Fields the renderer uses
`preset`, `hook`, `voice` (optional), `overrides` (optional) and per scene `id`, `narration`, `motion`,
`zoom`, `popups` (`text`, `at_word`, `nth`, `color`, `x`, `y`, `size`, `hold`, `glow`), `image`, `clip`, `audio`.

## Fields for posting and pictures
`title`, `structure`, `caption`, `hashtags`, `cover_text`, `alt_text`, `characters`, `facts`, scene `visual`.
