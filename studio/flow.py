"""Time every scene to the narration and fill the Google Flow prompts for it.

  python -m studio.flow episodes/why-pen-caps-have-a-hole            uses audio/voiceover.* if script.yaml names it
  python -m studio.flow episodes/why-pen-caps-have-a-hole --offline  estimated timings, no voice

Writes:
  output/<episode>_flow_prompts.md   narration to paste into ElevenLabs, F0 reference prompts, and one F1 prompt per
                                     Flow clip with its length and the file name to save it as
  output/<episode>_timing.json       start and length of every scene
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from .config import ROOT, load_episode, resolve
from .voice import scene_voice, voiceover_scenes

LENGTHS = (4, 6, 8)  # Veo 3.1 Fast clip lengths in Flow


def flow_blocks() -> dict[str, str]:
    text = (ROOT / "prompts" / "flow.md").read_text(encoding="utf-8")
    out = {}
    for sec in re.split(r"^## ", text, flags=re.M)[1:]:
        title = sec.splitlines()[0]
        m = re.search(r"\((F[-\w]+)\)", title)
        code = re.findall(r"```\n(.*?)\n```", sec, flags=re.S)
        if m and code:
            out[m.group(1)] = code[0].strip()
    return out


def scene_timings(episode: dict, cfg: dict, episode_dir: Path, offline: bool) -> dict[str, float]:
    scenes = episode["scenes"]
    cache = episode_dir / ".cache" / "voice"
    if episode.get("voiceover") and not offline:
        vo = resolve(episode["voiceover"], episode_dir)
        if not vo:
            raise SystemExit(f"voiceover file not found: {episode['voiceover']}")
        parts = voiceover_scenes(vo, scenes, cache)
        return {s["id"]: parts[s["id"]][2] for s in scenes}
    out = {}
    for s in scenes:
        _, _, speech = scene_voice(s, cfg, episode_dir, cache, offline)
        out[s["id"]] = speech + float(s.get("pad", cfg["scene"]["pad_after"]))
    return out


def clip_owner(scene: dict) -> str:
    """Which scene's Flow clip this scene uses (its own, or another's via `clip: clips/s03.mp4`)."""
    c = str(scene.get("clip") or "")
    m = re.search(r"(s\d+)\.\w+$", c.replace("\\", "/"))
    return m.group(1) if m else scene["id"]


def _objects(episode: dict, scene: dict, shot: str) -> str:
    """Fixed looks for recurring objects (e.g. the airliner): `objects:` in script.yaml, used when the scene names one
    in `objects:` or its shot/setting mentions the object's name."""
    text = " ".join(str(scene.get(k) or "") for k in ("shot", "setting", "camera")) + " " + shot
    out = []
    for o in episode.get("objects") or []:
        name = str(o.get("name", "")).strip()
        key = name.lower().removeprefix("the ").strip()  # "the water bottle" also matches "her water bottle"
        if name and (name in (scene.get("objects") or []) or key in text.lower()):
            out.append(f"{name}: {str(o.get('look', '')).strip()}")
    return "; ".join(out)


def _sizes(episode: dict, char_names: list[str], objects_text: str) -> list[str]:
    """Real-world sizes (`size:` on characters and objects) of everything in the shot, for the Scale line."""
    out = []
    for c in episode.get("characters") or []:
        if c.get("name") in char_names:
            out.append(f"{c['name']}: {c['size']}" if c.get("size") else f"{c['name']}: (no size given!)")
    for o in episode.get("objects") or []:
        if o.get("name") and str(o["name"]) + ":" in objects_text:
            out.append(f"{o['name']}: {o['size']}" if o.get("size") else f"{o['name']}: (no size given!)")
    return out


def _frame(spec) -> tuple[str, float] | None:
    """'s08@4.04' -> ('s08', 4.04): a frame of an already approved clip, used as a Frames to Video start/end frame."""
    if not spec:
        return None
    clip, _, at = str(spec).partition("@")
    return clip.strip(), float(at or 0)


def _timing(members: list[dict], timing: dict, action: int) -> str:
    """How long each scene's part of the clip is on screen, from the voiceover timing."""
    parts = []
    for m in members:
        a = float(m.get("clip_start", 0))
        parts.append(f"{a:.1f}-{a + timing[m['id']]['seconds']:.1f} s of this clip is used on screen")
    return ("; ".join(parts) + ". The key action must be complete and clearly readable inside that window; "
            "start moving from the very first frame (no slow fade-in, no static start).")


def build_prompts(episode: dict, cfg: dict, timings: dict[str, float]) -> tuple[str, dict]:
    b = flow_blocks()
    style = (episode.get("flow_style") or b["F-STYLE"]).strip()  # an episode can set its own look (owner picks from samples)
    chars = {str(c.get("name", "")).strip(): str(c.get("look", "")).strip() for c in episode.get("characters") or []}
    scenes = episode["scenes"]

    start, timing = 0.0, {}
    for s in scenes:
        timing[s["id"]] = {"start": round(start, 2), "seconds": round(timings[s["id"]], 2)}
        start += timings[s["id"]]

    # clip groups: owner scene -> scenes that use its clip
    groups: dict[str, list[dict]] = {}
    for s in scenes:
        groups.setdefault(clip_owner(s), []).append(s)

    lines = [f"# {episode.get('title', '')} — Flow prompts", "",
             f"Total length {start:.1f} s · {len(scenes)} scenes · {len(groups)} Flow clips "
             f"(about {20 * len(groups)} credits on Veo 3.1 Fast).",
             "Settings: Portrait 9:16 · Veo 3.1 Fast · sound on · download Upscaled 1080p (see prompts/flow.md).", ""]

    narration = "\n".join(s["narration"].strip() for s in scenes)
    lines += ["## Narration for ElevenLabs (paste as is)", "```", narration, "```",
              f"{len(narration)} characters.", ""]

    # Ingredients (reference images) keep a character consistent but force 8 s clips. Turn them off with
    # `flow_ingredients: false` when characters appear once or only from behind: every clip is then Text to Video
    # with the character's look written into the prompt, and its length follows the narration.
    ingredients = episode.get("flow_ingredients", True) is not False
    used = sorted({n for s in scenes for n in (s.get("characters") or []) if n in chars}) if ingredients else []
    if used:
        lines += ["## F0 — Reference images (make first, then use them as Ingredients)", ""]
        for n in used:
            p = b["F0"].replace("[NAME]", n).replace("[LOOK]", chars[n]).replace("[F-STYLE]", style)
            lines += [f"### {n}", "```", p, "```", ""]

    if episode.get("loop", True):  # owner 2026-10-18: every Reel loops (last frame = first frame) so people watch twice
        last, first = scenes[-1], scenes[0]
        ef = _frame(last.get("end_frame"))
        if not ef or ef[0] != clip_owner(first) or ef[1] > 0.05:
            print(f"  ! loop: the last scene ({last['id']}) should have end_frame: \"{clip_owner(first)}@0\" "
                  "so the video ends on its own first frame")
    lines += ["## F1 — Scene clips", ""]
    for owner, members in groups.items():
        lead = next(s for s in scenes if s["id"] == owner) if any(s["id"] == owner for s in scenes) else members[0]
        if lead.get("graded_from"):  # made from another clip in editing, no Flow prompt
            continue
        need = max(float(m.get("clip_start", 0)) + timings[m["id"]] for m in members)
        lengths = tuple(episode.get("flow_lengths") or LENGTHS)  # Veo 3.1 Fast on Google AI Pro: only 8 s (2026-10-18)
        length = next((n for n in lengths if n >= need), max(lengths))
        action = min(length, max(2, int(need + 0.99)))  # whole seconds of the clip the scene really uses
        names = [n for n in (lead.get("characters") or []) if n in chars]
        mode = f"Ingredients to Video with: {', '.join(names)} (8 s)" if names and ingredients else "Text to Video"
        if names and ingredients:
            length = 8
        shot = (lead.get("shot") or lead.get("visual") or "").strip()
        start_f, end_f = _frame(lead.get("start_frame")), _frame(members[-1].get("end_frame") or lead.get("end_frame"))
        if start_f or end_f:  # Frames to Video: a neighbour's real frame fixes geometry, look and the cut
            mode = "Frames to Video" + (f" · START frame = {start_f[0]} at {start_f[1]} s" if start_f else "") \
                   + (f" · END frame = {end_f[0]} at {end_f[1]} s" if end_f else "")
            length = 8
        if end_f:
            # the clip must finish on the end frame, so the scene uses the LAST seconds of the clip
            used = sum(timings[m["id"]] for m in members)
            want = round(length - used, 2)
            if abs(float(lead.get("clip_start", 0)) - want) > 0.05:
                print(f"  ! {owner}: has end_frame, so set clip_start: {want} (the scene uses the last {used:.2f} s)")
        elif action < length:
            shot += (f" All of this happens in the first {action} seconds; for the remaining {length - action} seconds,"
                     " hold the final moment with a slow, gentle camera drift and no new action.")
        if len(members) > 1:
            shot += " " + " ".join(f"Then: {(m.get('shot') or m.get('visual') or '').strip()}" for m in members[1:]
                                   if (m.get("shot") or m.get("visual")))
        p = (b["F1"].replace("[F-STYLE]", style)
             .replace("[NAME: LOOK, for each character in the shot, or \"none\"]",
                      "; ".join(f"{n}: {chars[n]}" for n in names) or "none")
             .replace("[N]", str(length))
             .replace("[WHAT HAPPENS, beat by beat with rough timings, e.g. \"0-2 s: ...; 2-4 s: ...\"]", shot or "[describe the shot]")
             .replace("[CAMERA: lens and movement, e.g. \"smooth slow push-in from a medium shot to a close-up on his hands\"]",
                      (lead.get("camera") or "smooth slow push-in").strip())
             .replace("[SETTING]", (lead.get("setting") or episode.get("setting") or "a clean, bright modern interior").strip())
             .replace("[SFX: every audible action, e.g. \"paper rustle, cash register ding, soft footsteps on wood\"]",
                      (lead.get("sfx") or "soft natural sounds of the action").strip())
             .replace("[OBJECTS]", _objects(episode, lead, shot) or "none")
             .replace("[TIMING]", _timing(members, timing, action))
             .replace("[OPEN]", (lead.get("opens") or "continues naturally from the previous shot").strip())
             .replace("[END]", (members[-1].get("ends") or lead.get("ends") or "a clean, steady frame that cuts naturally to the next shot").strip()))
        if start_f:
            p = (f"Animate starting EXACTLY from the attached start frame: same art style, same characters and objects, same "
                 f"camera position and same light as that picture.\n") + p
        if end_f:
            p += ("\nThe clip ENDS EXACTLY on the attached end frame: in the last second the camera settles precisely into that "
                  "picture and holds it.")
        sizes = _sizes(episode, names, _objects(episode, lead, shot)) + [str(s) for s in (lead.get("sizes") or [])]
        if sizes:
            missing = [s.split(":")[0] for s in sizes if "no size given" in s]
            if missing:
                print(f"  ! {owner}: add `size:` (real-world size) for {', '.join(missing)}")
            p += ("\nReal-world scale (owner rule): " + "; ".join(s for s in sizes if "no size given" not in s) +
                  ". Every person, animal, vehicle and object keeps its true real-world size relative to the others in "
                  "every frame; never enlarge or shrink anything to fit the frame or to look cute; show size with camera "
                  "distance and framing instead.")
        if lead.get("must"):
            p += "\nMust be true in every frame: " + "; ".join(lead["must"]) + "."
        if lead.get("never"):
            p += "\nNever show: " + "; ".join(lead["never"]) + "."
        frames = [f for f in (start_f, end_f) if f]
        cut = [f"ffmpeg -v error -y -ss {t} -i clips\\{c}.mp4 -frames:v 1 frames\\{c}_at{t}.png" for c, t in frames]
        warn = f"  ⚠ narration needs {need:.1f} s: the build will slow the clip slightly or hold its last frame. Consider splitting the scene." if need > 8 * 1.25 else ""
        ids = ", ".join(f"{m['id']} ({timing[m['id']]['seconds']:.1f} s{', from ' + str(m.get('clip_start')) + ' s' if m.get('clip_start') else ''})" for m in members)
        lines += [f"### {owner} → save as `clips\\{owner}.mp4` · {length} s · {mode}",
                  f"Used by: {ids}{warn}", ""]
        if cut:
            lines += ["Cut the frame(s) first (in the episode folder):", "```", *cut, "```", ""]
        for m in members:
            lines.append(f"> {m['id']}: {m['narration'].strip()}")
        lines += ["", "```", p, "```", ""]
    return "\n".join(lines), timing


def main():
    ap = argparse.ArgumentParser(description="Time scenes to the narration and write the Flow prompts.")
    ap.add_argument("episode", type=Path)
    ap.add_argument("--offline", action="store_true", help="estimated timings (no voice, no internet)")
    a = ap.parse_args()
    d = a.episode.resolve()
    episode, cfg = load_episode(d)
    for i, s in enumerate(episode["scenes"], 1):
        s.setdefault("id", f"s{i:02d}")
    timings = scene_timings(episode, cfg, d, a.offline)
    text, timing = build_prompts(episode, cfg, timings)
    out = d / "output"
    out.mkdir(exist_ok=True)
    (out / f"{d.name}_flow_prompts.md").write_text(text, encoding="utf-8")
    (out / f"{d.name}_timing.json").write_text(json.dumps(timing, indent=1), encoding="utf-8")
    total = sum(v["seconds"] for v in timing.values())
    print(f"{len(timing)} scenes, {total:.1f} s -> {out / (d.name + '_flow_prompts.md')}")


if __name__ == "__main__":
    main()
