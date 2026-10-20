"""Posting copy for each episode (output/<episode>_post.md), filled from script.yaml.

Instagram allows at most 5 hashtags per post or Reel (since December 2025), so only the first 5 are used.
"""
from __future__ import annotations

from pathlib import Path

MAX_HASHTAGS = 5


def write_post(episode: dict, cfg: dict, profiles: list[str], path: Path) -> Path:
    title = episode.get("title", "")
    hook = episode.get("hook") or title
    tags = [f"#{str(t).lstrip('#')}" for t in (episode.get("hashtags") or [])]
    if len(tags) > MAX_HASHTAGS:
        print(f"  ! {len(tags)} hashtags in script.yaml; Instagram allows {MAX_HASHTAGS}. Using the first {MAX_HASHTAGS}.")
        tags = tags[:MAX_HASHTAGS]
    caption = (episode.get("caption") or "").strip() or (
        f"{hook}\n{episode.get('teaser', '[one line that teases the answer]')}\n\n"
        "Follow @howzit.explains for how things work in 60 seconds.")
    collab = (cfg["brand"].get("collab") or {}).get("instagram", "@lowkeygenius")
    if episode.get("voice_credit"):
        caption += "\n" + str(episode["voice_credit"]).strip()

    urls = []
    for fact in episode.get("facts") or []:
        for u in fact.get("sources") or []:
            if u not in urls:
                urls.append(u)
    facts_rows = "\n".join(
        f"| {f.get('claim', '')} | {' · '.join(f.get('sources') or []) or 'NEEDS 2 SOURCES'} |"
        for f in episode.get("facts") or []) or "| (no facts listed in script.yaml) | NEEDS SOURCES |"

    text = f"""# {title} — posting copy

## 1. Fact check (2 reliable sources per claim, before posting)
| Claim | Sources |
|---|---|
{facts_rows}

## 2. Instagram Reel on HowZit, Collab with {collab}
File: `output/*_howzit.mp4`

**Caption** (first line is the hook people see before "more")
```
{caption}

{' '.join(tags)}
```
**Cover**: {episode.get('cover_text') or 'pick the frame with the lime hook box'} (keep it in the centre: the grid crops to 3:4)
**Alt text**: {episode.get('alt_text') or '[one sentence describing what the video shows]'}

**Post it**
1. Instagram → + → Reel → choose the video → Next.
2. Paste the caption. Tap **Tag people → Invite collaborator** → `{collab}` → Done.
3. Edit cover → pick the hook frame. If Advanced settings shows Accessibility → Alt text, paste the alt text.
4. Share. Then on the {collab} account, open the invite in DMs and accept (the Reel then shows on both pages, with shared likes and comments).
5. Pin a comment with a question that makes people answer ("Did you know this? 👇").
6. Reply to comments in the first hour; save new questions as topic ideas.
"""
    if "youtube" in profiles:
        yt_title = episode.get("youtube_title") or f"{title} (in 60 seconds)"
        sources = ", ".join(urls) if urls else "[source 1], [source 2]"
        text += f"""
## 3. YouTube Short (Lowkey Genius)
File: `output/*_youtube.mp4` · Title ({len(yt_title)}/100): `{yt_title}`
```
{hook} Here's the 60-second version.

Sources: {sources}
More explainers: @howzit.explains on Instagram

#lowkeygenius #howitworks #explained
```
Settings: Not made for kids · Education · Playlist "How Things Work (Explained Lowkey)" · upload the `.srt` as English subtitles.
"""
    text += """
## Before you post
- Watch it once on your phone: captions readable, nothing hidden under the app buttons.
- Music or sound effects are licensed for Instagram (Instagram's own library is fine inside the app).
- Scenes made with Google Flow (Veo) → turn on Instagram's **AI label** (Advanced settings) before sharing.
"""
    path.write_text(text, encoding="utf-8")
    return path
