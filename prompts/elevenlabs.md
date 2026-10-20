# ElevenLabs narration

Page: https://elevenlabs.io/app/speech-synthesis/text-to-speech (signed in with the owner's account).
The owner has already **selected the voice** to use there: never change the voice.

## Steps (Claude in Chrome)
1. Open the page. Read the selected voice name and model at the bottom and note them in the episode's `story.md`.
2. Paste the narration: every scene's `narration` from `script.yaml`, in order, one scene per line, nothing else
   (no scene ids, no stage directions). `python -m studio.flow` also prints it ready to paste.
3. Settings, aiming for a natural, lively storyteller:
   - **Eleven v3**: Stability **Natural**. Don't add audio tags unless the owner asks.
   - **Multilingual v2 / other models**: Stability ~45 %, Similarity ~75 %, Style ~10 %, Speaker boost on,
     Speed 1.10–1.15 (the reference narrator speaks 4.3–5.1 syllables a second, pausing only at sentence ends).
4. Check the character count against the remaining credits shown on the page **before** generating.
   - Enough credits → **Generate**, then download the newest generation as MP3 (or WAV if offered).
   - Not enough credits → don't generate. Tell the owner and use the built-in voice instead (Brian, see below).
5. Save it as `episodes\<name>\audio\voiceover.mp3` (keep the real extension) and add to `script.yaml`:
   `voiceover: audio/voiceover.mp3`
6. Run `python -m studio.flow episodes\<name>`: it listens to the file (faster-whisper), times every scene to the
   recording, and warns if words are missing.

## Fallback voice (no credits, or ElevenLabs is down)
Leave `voiceover:` out of `script.yaml`. The build uses the free built-in voice from `presets/explainer.yaml`
(`en-US-BrianMultilingualNeural`, the owner's pick, at +14% since the 8-video analysis; +10% if it sounds rushed).

## Licence
ElevenLabs' **free plan has no commercial licence** and requires crediting ElevenLabs ("elevenlabs.io") in the
title when content is published. If the owner's account is on the free plan, set
`voice_credit: "Voice: elevenlabs.io"` in `script.yaml` (it's added to the caption) and tell the owner. Paid plans
(Starter and up) include a commercial licence and need no credit.
Never clone or imitate a real creator's voice.
