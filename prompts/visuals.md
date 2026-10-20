# Scene pictures and clips

The exact Gemini prompts are in `prompts/gemini.md` (G4 reference sheet, G5 scene pictures, G6 Veo clips).

## Where files go
```
episodes/<episode>/images/s01.png   ← still picture; the renderer adds the slow camera move
episodes/<episode>/clips/s03.mp4    ← moving clip, used instead of the picture for that scene
```
Any of .png .jpg .jpeg .webp / .mp4 .mov .webm work. Scenes without a file render as a labelled
placeholder card, so you can check timing first.

## Look: like the reference Reel (3D)
Decided 2026-10-17 and confirmed 2026-10-18 (a brief switch to 2D was reverted): polished, semi-realistic 3D
characters in bright, clean, pastel-blue interiors, soft lighting, shallow depth of field (the style block in
`prompts/gemini.md`), matching the owner's reference Reel. HowZit's brand stays in the overlays: watermark,
end card, lime glow on pop-ups. Characters look fairly real, so turn on Instagram's AI label when posting.

## Sharpness
- Ask Gemini for the largest image size it offers; download the full file, never a screenshot.
- Real-ESRGAN (optional, free) upscales small pictures before the camera move: put the Windows build in
  `tools\realesrgan\` (see the checklist). Without it the renderer uses high-quality Lanczos scaling.
- Veo clips: choose 1080p when offered.

## Layout rules the pictures must leave room for
| Area (1080×1920) | What goes there | Picture should be |
|---|---|---|
| Top-right, x 834 y 236 | HowZit watermark | nothing important |
| Middle, y 400–1200 | Main subject; pop-ups appear around y ≈ 690 | the action |
| Around y 1500 | Captions | calm, not too busy |
| Bottom 420 px, right 120 px | Instagram buttons and caption | nothing important |

## Consistency
- One Gemini chat per episode for all pictures; attach the reference sheet (G4) and name the character.
- If a character drifts: re-attach the sheet and say "same character as the reference, same clothes".
- Real historical people: generic look only, never a real face.
- Never Ben 10 names, symbols or characters (brand rule).
