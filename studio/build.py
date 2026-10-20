"""Render an episode folder into finished, branded videos (one per export profile).

  python -m studio.build episodes/microwave-heating                  HowZit Reel + Lowkey Genius Short
  python -m studio.build episodes/microwave-heating --draft          fast half-size preview
  python -m studio.build episodes/microwave-heating --profile howzit just one export
  python -m studio.build episodes/microwave-heating --offline        no voice (silent), estimated timings
  python -m studio.build episodes/microwave-heating --only s03        one scene, quick check
"""
from __future__ import annotations

import argparse
import shutil
import time
from pathlib import Path

from .audio import pick_music, sfx_track
from .captions import AssWriter
from .config import ROOT, color, load_episode, resolve
from .media import end_card, placeholder_card, prepare_picture, render_scene, run, scene_fx
from .post import write_post
from .prompts import write_prompts
from .voice import pad_audio, scene_voice, voiceover_scenes

IMAGE_EXT = (".png", ".jpg", ".jpeg", ".webp")
CLIP_EXT = (".mp4", ".mov", ".webm", ".mkv")


def find_visual(scene: dict, episode_dir: Path) -> tuple[Path | None, str]:
    """scene.clip / scene.image, or a file named after the scene id in clips/ or images/."""
    for key, kind in (("clip", "clip"), ("image", "image")):
        if scene.get(key):
            p = resolve(scene[key], episode_dir)
            if p:
                return p, kind
            print(f"  ! scene {scene['id']}: {key} '{scene[key]}' not found, using placeholder")
    for folder, exts, kind in (("clips", CLIP_EXT, "clip"), ("images", IMAGE_EXT, "image")):
        for ext in exts:
            p = episode_dir / folder / f"{scene['id']}{ext}"
            if p.exists():
                return p, kind
    return None, "placeholder"


def build(episode_dir: Path, draft: bool, offline: bool, only: str | None, profiles: list[str] | None) -> list[Path]:
    t0 = time.time()
    episode, cfg = load_episode(episode_dir)
    brand = cfg["brand"]
    profiles = profiles or brand.get("default_profiles") or list(brand["profiles"])
    for name in profiles:
        if name not in brand["profiles"]:
            raise SystemExit(f"Unknown profile '{name}'. Profiles in brand/brand.yaml: {', '.join(brand['profiles'])}")

    scenes = episode["scenes"]
    for i, s in enumerate(scenes, 1):
        s.setdefault("id", f"s{i:02d}")
        s["_number"] = i
    if only:
        scenes = [s for s in scenes if s["id"] == only]
        if not scenes:
            raise SystemExit(f"No scene with id '{only}'")

    v = cfg["video"]
    fps = v["fps"]
    W, H = (v["width"] // 2, v["height"] // 2) if draft else (v["width"], v["height"])
    W, H = W - W % 2, H - H % 2
    colors = cfg["tokens"]["color"]
    work = episode_dir / ".cache" / ("draft" if draft else "full")
    (work / "fonts").mkdir(parents=True, exist_ok=True)
    voice_cache = episode_dir / ".cache" / "voice"
    fonts_dir = resolve(brand.get("fonts_dir", "brand/fonts"), episode_dir) or ROOT / "brand" / "fonts"
    for ttf in list(fonts_dir.glob("*.ttf")) + list(fonts_dir.glob("*.otf")):
        shutil.copy(ttf, work / "fonts" / ttf.name)  # libass reads fonts from a relative folder (safe on Windows)
    font_file = _font_file(fonts_dir, cfg["captions"]["font"])

    base = AssWriter(cfg, font_file)
    if (episode.get("hook") and (brand.get("hook_box") or {}).get("enabled", True)
            and (not only or only == episode["scenes"][0]["id"])):
        base.add_hook(str(episode["hook"]))

    vo = {}
    if episode.get("voiceover") and not offline:
        vo_file = resolve(episode["voiceover"], episode_dir)
        if not vo_file:
            raise SystemExit(f"voiceover file not found: {episode['voiceover']}")
        vo = voiceover_scenes(vo_file, episode["scenes"], voice_cache)
    upscale = (cfg.get("quality") or {}).get("upscale", "auto")
    cuts = []

    clips, audios, fxs, t = [], [], [], 0.0
    print(f"Building '{episode.get('title', episode_dir.name)}' — {len(scenes)} scenes, {W}x{H}")
    for scene in scenes:
        if scene["id"] in vo:
            wav, words, speech = vo[scene["id"]]
            pad = 0.0  # the recording's own pauses are kept
        else:
            wav, words, speech = scene_voice(scene, cfg, episode_dir, voice_cache, offline)
            pad = float(scene.get("pad", cfg["scene"]["pad_after"]))
        seconds = max(speech + pad, float(scene.get("min_seconds", 0)))
        seconds = round(seconds * fps) / fps

        src, kind = find_visual(scene, episode_dir)
        label = src.name if src else "(placeholder)"
        if kind == "placeholder":
            src = work / f"{scene['id']}_placeholder.png"
            placeholder_card(scene, scene["_number"], W, H, src, font_file, colors)
            kind = "image"
        elif kind == "image" and not draft:
            src = prepare_picture(src, W, H, float(scene.get("zoom", cfg["scene"]["zoom"])),
                                  episode_dir / ".cache" / "upscaled", upscale)
        clip = work / f"{scene['id']}.mp4"
        fit = render_scene(src, kind, seconds, scene.get("motion", cfg["scene"]["default_motion"]),
                           float(scene.get("zoom", cfg["scene"]["zoom"])), W, H, fps, clip, fast=draft,
                           clip_start=float(scene.get("clip_start", 0)), loop_in=scene.get("loop_in"),
                           clip_end=scene.get("clip_end"))
        padded = work / f"{scene['id']}_voice.wav"
        pad_audio(wav, padded, seconds)
        fx = work / f"{scene['id']}_fx.wav"
        keep_fx = (cfg.get("clip_audio") or {}).get("enabled", True) and scene.get("clip_audio", True)
        scene_fx(src if kind == "clip" and keep_fx else None, fit, seconds, fx)
        if fit and (fit["speed"] != 1.0 or fit["hold"] > 0):
            label += f"  (clip {'slowed to ' + format(fit['speed'], '.2f') + 'x' if fit['speed'] != 1.0 else ''}"
            label += f"{', last frame held ' + format(fit['hold'], '.1f') + 's' if fit['hold'] > 0 else ''})"

        for popup in scene.get("popups") or []:  # pop-ups first: they decide where lime is busy
            base.add_popup(popup, words, t, t + seconds, scene["id"])
        base.add_captions(words, t, t + seconds)
        clips.append(clip)
        audios.append(padded)
        fxs.append(fx)
        print(f"  {scene['id']}  {seconds:5.2f}s  {label}")
        if t > 0:
            cuts.append(t)
        t += seconds

    _concat(work, clips, audios, "body")
    (work / "body_fx_a.txt").write_text("".join(f"file '{p.name}'\n" for p in fxs))
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", "body_fx_a.txt", "-c", "pcm_s16le", "body_fx.wav"], cwd=work)
    body_seconds = t

    out_dir = episode_dir / "output"
    out_dir.mkdir(exist_ok=True)
    slug = episode_dir.name + (f"_{only}" if only else "")
    outputs = []
    for name in profiles:
        prof = brand["profiles"][name]
        writer = base.clone()
        seg_v, seg_a, seg_fx, total = [work / "body.mp4"], [work / "body.wav"], [work / "body_fx.wav"], body_seconds
        ec = prof.get("end_card")
        if ec and not only:
            ec_scene = {"id": f"end_{name}", "narration": ec.get("line") or " "}
            speak = ec.get("line") and not vo  # with a voiceover file the end card stays silent (music only)
            wav, words, speech = scene_voice(ec_scene, cfg, episode_dir, voice_cache, offline) if speak else (None, [], 0)
            secs = round(max(speech + 0.5, float(ec.get("min_seconds", 2.5))) * fps) / fps
            logo = resolve(ec["file"], episode_dir)
            png = work / f"end_{name}.png"
            end_card(W, H, logo, float(ec.get("width", 0.8)), png, colors)
            render_scene(png, "image", secs, "zoom_in", 0.03, W, H, fps, work / f"end_{name}.mp4", fast=draft)
            ea = work / f"end_{name}_voice.wav"
            if wav:
                pad_audio(wav, ea, secs)
            else:
                run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", f"{secs:.3f}", str(ea)])
            writer.lime_busy.append((total, total + secs))  # the logo is lime: no lime word highlight
            writer.add_captions(words, total, total + secs)
            seg_v.append(work / f"end_{name}.mp4")
            seg_a.append(ea)
            efx = work / f"end_{name}_fx.wav"
            scene_fx(None, None, secs, efx)
            seg_fx.append(efx)
            prof_cuts = cuts + [total]
            total += secs
        else:
            prof_cuts = list(cuts)
        writer.add_text_watermark(total)
        writer.write(work / f"captions_{name}.ass", work / f"captions_{name}.srt")
        _concat(work, seg_v, seg_a, f"joined_{name}")
        (work / f"joined_{name}_fx_a.txt").write_text("".join(f"file '{p.name}'\n" for p in seg_fx))
        run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"joined_{name}_fx_a.txt",
             "-c", "pcm_s16le", f"joined_{name}_fx.wav"], cwd=work)

        stem = f"{slug}_{prof.get('suffix', name)}" + ("_draft" if draft else "")
        out = out_dir / f"{stem}.mp4"
        sfx = sfx_track(total, prof_cuts, writer.popup_times, cfg, episode_dir, work / f"sfx_{name}.wav")
        _final_mix(cfg, prof, name, episode_dir, work, W, H, total, out, draft, sfx)
        shutil.copy(work / f"captions_{name}.srt", out_dir / f"{stem}.srt")
        outputs.append(out)
        print(f"  → {_show(out)}  ({total:.1f}s)")

    if not only and episode.get("preset", "explainer") != "kids":
        post = write_post(episode, cfg, profiles, out_dir / f"{episode_dir.name}_post.md")
        print(f"  → {_show(post)}")
    if not only:
        gp = write_prompts(episode, out_dir / f"{episode_dir.name}_gemini_prompts.md")
        print(f"  → {_show(gp)}")
    print(f"Done in {time.time() - t0:.0f}s")
    return outputs


def _concat(work: Path, videos: list[Path], audios: list[Path], name: str) -> None:
    (work / f"{name}_v.txt").write_text("".join(f"file '{p.name}'\n" for p in videos))
    (work / f"{name}_a.txt").write_text("".join(f"file '{p.name}'\n" for p in audios))
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"{name}_v.txt", "-c", "copy", f"{name}.mp4"], cwd=work)
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"{name}_a.txt", "-c", "pcm_s16le", f"{name}.wav"], cwd=work)


def _font_file(fonts_dir: Path, font_name: str) -> Path | None:
    """The .ttf for a font name like 'Open Sans ExtraBold' (file OpenSans-ExtraBold.ttf)."""
    want = font_name.replace(" ", "").lower()
    for p in sorted(fonts_dir.glob("*.ttf")):
        if p.stem.replace("-", "").lower() == want:
            return p
    return next(iter(sorted(fonts_dir.glob("*.ttf"))), None)


def _final_mix(cfg, prof, name, episode_dir, work, W, H, total, out, draft, sfx=None):
    k = W / cfg["video"]["width"]  # 1.0 full size, 0.5 draft
    inputs = ["-i", f"joined_{name}.mp4", "-i", f"joined_{name}.wav"]
    fc = [f"[0:v]ass=captions_{name}.ass:fontsdir=fonts[v0]"]
    vlabel, n = "v0", 2

    wm = prof.get("watermark") or {}
    wm_file = resolve(wm.get("file"), episode_dir)
    if wm_file:
        inputs += ["-i", str(wm_file)]
        size = max(int(wm.get("size", 110) * k), 2)
        fc.append(f"[{n}:v]scale={size}:{size},format=rgba,colorchannelmixer=aa={wm.get('opacity', 0.95)}[wm]")
        fc.append(f"[{vlabel}][wm]overlay={int(wm.get('x', 834) * k)}:{int(wm.get('y', 236) * k)}:format=auto[v1]")
        vlabel, n = "v1", n + 1
    elif wm.get("file"):
        print(f"  ! watermark file not found: {wm['file']}")

    if cfg["brand"].get("progress_bar"):
        bar = max(int(8 * k), 2)
        lime = color(cfg, "lime").lstrip("#")
        fc.append(f"color=c=0x{lime}:s={W}x{bar}:r={cfg['video']['fps']}[bar]")
        fc.append(f"[{vlabel}][bar]overlay=x='-W+W*t/{total:.3f}':y=H-{bar}:shortest=1[v2]")
        vlabel = "v2"

    music = pick_music(cfg, episode_dir)
    m = cfg.get("music") or {}
    ca = cfg.get("clip_audio") or {}
    beds = []  # (input label, volume, duck under the voice?)
    if music:
        inputs += ["-stream_loop", "-1", "-i", str(music)]
        fc.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,volume={m.get('volume', 0.2)},"
                  f"afade=t=in:d=0.4,afade=t=out:st={max(total - 1.5, 0):.2f}:d=1.5[m0]")
        beds.append(("m0", m.get("duck", True), 6))
        n += 1
    if ca.get("enabled", True):
        inputs += ["-i", f"joined_{name}_fx.wav"]
        fc.append(f"[{n}:a]volume={ca.get('volume', 0.9)}[c0]")
        beds.append(("c0", ca.get("duck", True), 3))
        n += 1
    ducked = [b for b in beds if b[1]]
    voice = "[1:a]"
    if ducked:
        fc.append(f"[1:a]asplit={len(ducked) + 1}[vo]" + "".join(f"[sc{i}]" for i in range(len(ducked))))
        voice = "[vo]"
    mix, k = [], 0
    for label, duck, ratio in beds:
        if duck:
            fc.append(f"[{label}][sc{k}]sidechaincompress=threshold=0.02:ratio={ratio}:attack=15:release=350:makeup=1[{label}d]")
            mix.append(f"[{label}d]")
            k += 1
        else:
            mix.append(f"[{label}]")
    if sfx:
        inputs += ["-i", sfx.name]
        mix.append(f"[{n}:a]")
        n += 1
    if mix:
        fc.append(f"{voice}{''.join(mix)}amix=inputs={1 + len(mix)}:duration=first:normalize=0[mix]")
        a = "[mix]"
    else:
        a = voice
    fc.append(f"{a}loudnorm=I={cfg.get('loudness', -14)}:TP=-1.5:LRA=11,aresample=48000[aout]")

    q = cfg.get("quality") or {}
    video_q = (["-preset", "veryfast", "-crf", "22"] if draft else
               ["-preset", str(q.get("preset", "slow")), "-crf", str(q.get("crf", 16)),
                "-maxrate", "16M", "-bufsize", "32M", "-profile:v", "high", "-level", "4.2"])
    run(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", ";".join(fc),
         "-map", f"[{vlabel}]", "-map", "[aout]", "-t", f"{total:.3f}",
         "-c:v", "libx264", *video_q, "-pix_fmt", "yuv420p", "-r", str(cfg["video"]["fps"]),
         "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-movflags", "+faststart", str(out.resolve())], cwd=work)


def _show(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def main():
    ap = argparse.ArgumentParser(description="Render an episode into branded videos.")
    ap.add_argument("episode", type=Path, help="episode folder containing script.yaml")
    ap.add_argument("--draft", action="store_true", help="fast half-resolution preview")
    ap.add_argument("--offline", action="store_true", help="skip text-to-speech (silent, estimated timings)")
    ap.add_argument("--only", help="render a single scene id, e.g. s03")
    ap.add_argument("--profile", action="append", help="export profile from brand/brand.yaml (repeatable)")
    a = ap.parse_args()
    build(a.episode.resolve(), a.draft, a.offline, a.only, a.profile)


if __name__ == "__main__":
    main()
