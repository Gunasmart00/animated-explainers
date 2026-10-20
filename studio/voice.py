"""Narration audio plus word-level timings for each scene.

Engines:
  edge      Free Microsoft neural voices via the edge-tts package (needs internet).
            Word timings come straight from the voice engine, so captions are exact.
  recorded  Your own recording per scene (scene.audio). Word timings come from
            faster-whisper if installed, otherwise they are estimated.
  offline   No audio at all: silent track with estimated timings, for layout checks.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import re
from pathlib import Path

from .media import probe_duration, run

WORD_RE = re.compile(r"\S+")


def scene_voice(scene: dict, cfg: dict, episode_dir: Path, cache: Path, offline: bool) -> tuple[Path, list[dict], float]:
    """Return (wav_path, words, speech_seconds) for one scene."""
    text = scene["narration"].strip()
    cache.mkdir(parents=True, exist_ok=True)
    engine = "offline" if offline else cfg["voice"].get("engine", "edge")
    if scene.get("audio"):
        engine = "recorded"

    if engine == "recorded":
        from .config import resolve
        src = resolve(scene["audio"], episode_dir)
        if not src:
            raise SystemExit(f"Scene {scene['id']}: audio file not found: {scene['audio']}")
        wav = cache / f"{scene['id']}_rec.wav"
        to_wav(src, wav)
        dur = probe_duration(wav)
        words = whisper_words(wav) or estimate_words(text, dur, lead=0.05)
        return wav, words, dur

    if engine == "offline":
        words = estimate_words(text, None)
        dur = (words[-1]["end"] if words else 0) + 0.2
        wav = cache / f"{scene['id']}_silent.wav"
        run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
             "-t", f"{dur:.3f}", str(wav)])
        return wav, words, dur

    v = cfg["voice"]
    key = hashlib.sha1(json.dumps([text, v["name"], v.get("rate"), v.get("pitch")]).encode()).hexdigest()[:16]
    mp3, meta, wav = cache / f"{key}.mp3", cache / f"{key}.json", cache / f"{key}.wav"
    if not (mp3.exists() and meta.exists()):
        words = asyncio.run(_edge(text, v["name"], v.get("rate", "+0%"), v.get("pitch", "+0Hz"), mp3))
        meta.write_text(json.dumps(words, ensure_ascii=False, indent=1), encoding="utf-8")
    words = json.loads(meta.read_text(encoding="utf-8"))
    if not wav.exists():
        to_wav(mp3, wav)
    return wav, words, probe_duration(wav)


async def _edge(text: str, voice: str, rate: str, pitch: str, out: Path) -> list[dict]:
    import edge_tts

    comm = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch, boundary="WordBoundary")
    words: list[dict] = []
    try:
        with open(out, "wb") as f:
            async for chunk in comm.stream():
                if chunk["type"] == "audio":
                    f.write(chunk["data"])
                elif chunk["type"] == "WordBoundary":
                    start = chunk["offset"] / 1e7
                    words.append({"text": chunk["text"], "start": start,
                                  "end": start + chunk["duration"] / 1e7})
    except Exception as exc:  # network blocked, bad voice name, etc.
        out.unlink(missing_ok=True)
        raise SystemExit(f"Text-to-speech failed ({exc}). Check your internet connection and the "
                         f"voice name, or run with --offline to preview without audio.")
    return _attach_punctuation(text, words)


def _attach_punctuation(text: str, words: list[dict]) -> list[dict]:
    """The voice engine drops punctuation; put it back so captions break on sentences."""
    tokens = WORD_RE.findall(text)
    ti = 0
    for w in words:
        core = _norm(w["text"])
        for j in range(ti, min(ti + 4, len(tokens))):
            if _norm(tokens[j]).startswith(core) or core.startswith(_norm(tokens[j])):
                w["text"] = tokens[j]
                ti = j + 1
                break
    return words


def _norm(s: str) -> str:
    return re.sub(r"[^\w$%]", "", s.lower())


def estimate_words(text: str, total: float | None, lead: float = 0.1) -> list[dict]:
    """Spread words over the speech, weighted by length (about 2.7 words per second)."""
    tokens = WORD_RE.findall(text)
    weights = [len(_norm(t)) + 2.5 + (3 if t[-1] in ".!?" else 1 if t[-1] in ",;:" else 0) for t in tokens]
    span = (total - lead - 0.1) if total else len(tokens) / 2.7
    unit = span / max(sum(weights), 1)
    t, words = lead, []
    for tok, wt in zip(tokens, weights):
        words.append({"text": tok, "start": round(t, 3), "end": round(t + wt * unit * 0.85, 3)})
        t += wt * unit
    return words


def whisper_words(wav: Path) -> list[dict] | None:
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        return None
    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(str(wav), language="en", word_timestamps=True, vad_filter=False)
    return [{"text": w.word.strip(), "start": w.start, "end": w.end}
            for seg in segments for w in seg.words]


def to_wav(src: Path, dst: Path) -> None:
    run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-ar", "48000", "-ac", "2", str(dst)])


def pad_audio(src: Path, dst: Path, seconds: float) -> None:
    run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-af", f"apad=whole_dur={seconds:.3f}",
         "-t", f"{seconds:.3f}", "-ar", "48000", "-ac", "2", str(dst)])


# ---------- one voiceover file for the whole video ----------
def voiceover_scenes(path: Path, scenes: list[dict], cache: Path) -> dict[str, tuple[Path, list[dict], float]]:
    """Split one narration recording (AI Studio, ElevenLabs, your own voice) into the script's scenes.

    faster-whisper finds when each word is spoken; the script's words are matched to them in order,
    so captions keep the script's spelling while the timing follows the recording.
    """
    import difflib

    cache.mkdir(parents=True, exist_ok=True)
    wav = cache / "voiceover.wav"
    to_wav(path, wav)
    total = probe_duration(wav)
    stamp = cache / "voiceover_words.json"
    key = f"{path.stat().st_size}-{int(path.stat().st_mtime)}"
    heard = None
    if stamp.exists():
        saved = json.loads(stamp.read_text(encoding="utf-8"))
        if saved.get("key") == key:
            heard = saved["words"]
    if heard is None and all(s.get("vo_start") is not None for s in scenes[1:]):
        print("  using the scene start times written in script.yaml (vo_start)")
        return _split_by_pauses(wav, scenes, cache, total)
    if heard is None:
        try:
            print("  listening to the voiceover for word timings (first run downloads the speech model) …")
            heard = whisper_words(wav)
        except Exception as exc:  # no faster-whisper, model download blocked, …
            print(f"  ! speech model failed ({type(exc).__name__}: {exc})")
            heard = None
        if heard:
            stamp.write_text(json.dumps({"key": key, "words": heard}), encoding="utf-8")
    if not heard:
        print("  ! exact word timing unavailable (install faster-whisper for it); splitting scenes at the pauses instead")
        return _split_by_pauses(wav, scenes, cache, total)

    script = []  # (scene index, token)
    for si, s in enumerate(scenes):
        for tok in WORD_RE.findall(s["narration"]):
            script.append((si, tok))
    a = [_norm(t) for _, t in script]
    b = [_norm(w["text"]) for w in heard]
    times: list[tuple[float, float] | None] = [None] * len(script)
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            hw = heard[blk.b + k]
            times[blk.a + k] = (hw["start"], hw["end"])
    matched = sum(1 for t in times if t)
    if matched < len(script) * 0.6:
        print(f"  ! only {matched} of {len(script)} script words were found in the voiceover; "
              "check the recording follows script.yaml")
    # fill unmatched words by interpolating between matched neighbours
    known = [i for i, t in enumerate(times) if t]
    if not known:
        raise SystemExit("The voiceover doesn't match the script's words.")
    for i, t in enumerate(times):
        if t:
            continue
        prev = max((k for k in known if k < i), default=None)
        nxt = min((k for k in known if k > i), default=None)
        s0 = times[prev][1] if prev is not None else 0.0
        s1 = times[nxt][0] if nxt is not None else total
        gap = [j for j in range(prev + 1 if prev is not None else 0, nxt if nxt is not None else len(times))]
        pos = gap.index(i)
        step = (s1 - s0) / (len(gap) + 0.0001)
        times[i] = (s0 + pos * step, s0 + (pos + 0.85) * step)

    # scene boundaries: halfway through the pause between scenes
    first = {}
    last = {}
    for (si, _), t in zip(script, times):
        first.setdefault(si, t[0])
        last[si] = t[1]
    bounds = [0.0]
    for si in range(1, len(scenes)):
        bounds.append((last[si - 1] + first[si]) / 2 if si in first and si - 1 in last else bounds[-1])
    bounds.append(total)

    out = {}
    for si, s in enumerate(scenes):
        a0, a1 = bounds[si], bounds[si + 1]
        seg = cache / f"vo_{s['id']}.wav"
        run(["ffmpeg", "-y", "-v", "error", "-i", str(wav), "-ss", f"{a0:.3f}", "-to", f"{a1:.3f}",
             "-ar", "48000", "-ac", "2", str(seg)])
        words = [{"text": tok, "start": round(t[0] - a0, 3), "end": round(t[1] - a0, 3)}
                 for (sj, tok), t in zip(script, times) if sj == si]
        out[s["id"]] = (seg, words, a1 - a0)
    return out


def _split_by_pauses(wav: Path, scenes: list[dict], cache: Path, total: float) -> dict[str, tuple[Path, list[dict], float]]:
    """Without a speech model: cut the recording into scenes at the pauses nearest to where each scene should end
    (by its share of syllables), then spread each scene's words across its part."""
    import subprocess

    import numpy as np

    from .media import tool

    sr = 16000
    raw = subprocess.run([tool("ffmpeg"), "-v", "error", "-i", str(wav), "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"],
                         capture_output=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    hop = sr // 100
    fr = x[: len(x) // hop * hop].reshape(-1, hop)
    db = 20 * np.log10(np.sqrt((fr ** 2).mean(1)) + 1e-9)
    floor, peak = np.percentile(db, 5), np.percentile(db, 95)
    silent = db < floor + max(10.0, (peak - floor) * 0.3)
    voiced = np.where(~silent)[0]
    t0, t1 = (voiced[0] / 100, voiced[-1] / 100) if len(voiced) else (0.0, total)
    runs, i = [], 0
    while i < len(silent):
        if silent[i]:
            j = i
            while j < len(silent) and silent[j]:
                j += 1
            if (j - i) >= 12 and i / 100 > t0 and j / 100 < t1:
                runs.append(((i + j) / 200, (j - i) / 100))
            i = j
        else:
            i += 1
    weights = [sum(len(_norm(w)) + 2 for w in WORD_RE.findall(s["narration"])) for s in scenes]
    span, acc, bounds, last = t1 - t0, 0, [0.0], t0
    manual = all(s.get("vo_start") is not None for s in scenes[1:])
    for k in range(len(scenes) - 1):
        if manual:  # measured by hand from the pauses (`vo_start:` on every scene after the first)
            bounds.append(float(scenes[k + 1]["vo_start"]))
            continue
        acc += weights[k]
        expect = t0 + span * acc / sum(weights)
        window = span * weights[k] / sum(weights) * 0.45
        cands = [(c, length) for c, length in runs if last < c < expect + window and abs(c - expect) <= window]
        pick = max(cands, key=lambda r: r[1] - 0.3 * abs(r[0] - expect))[0] if cands else expect
        bounds.append(pick)
        last = pick
    bounds.append(total)
    out = {}
    for k, s in enumerate(scenes):
        a0, a1 = bounds[k], bounds[k + 1]
        seg = cache / f"vo_{s['id']}.wav"
        run(["ffmpeg", "-y", "-v", "error", "-i", str(wav), "-ss", f"{a0:.3f}", "-to", f"{a1:.3f}",
             "-ar", "48000", "-ac", "2", str(seg)])
        lead = (t0 - a0) if k == 0 else 0.08
        out[s["id"]] = (seg, estimate_words(s["narration"], (a1 - a0) - 0.1, lead=max(lead, 0.05)), a1 - a0)
    return out
