# D.B. Cooper: remake with the Flow + ElevenLabs process

The first version (dark, too realistic Gemini pictures) is kept in `_v1\`. `script.yaml` is now rewritten in the
new scene-by-scene format (16 scenes, 15 Flow clips, ~166 words) and its facts are already sourced.

Paste this into Claude Code (`claude --chrome` in G:\Apps\animated-explainers):

```
Make the D.B. Cooper video with the new process. Follow "Create New video" in CLAUDE.md, starting at step 5:
the research and script.yaml in episodes\db-cooper are done (keep the no-dates rule, the flap opening and the
name reveal in the last line). First move episodes\db-cooper\images\*.png into episodes\db-cooper\_v1\images\
(they're the old dark pictures), and install requirements.txt again (faster-whisper is new).
```
