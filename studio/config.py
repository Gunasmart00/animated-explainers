"""Load and merge brand, preset and episode settings."""
from __future__ import annotations

import copy
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def deep_merge(base: dict, extra: dict | None) -> dict:
    out = copy.deepcopy(base)
    for key, value in (extra or {}).items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = deep_merge(out[key], value)
        else:
            out[key] = copy.deepcopy(value)
    return out


def read_yaml(path: Path) -> dict:
    # utf-8-sig: Notepad on Windows may add a byte-order mark
    with open(path, encoding="utf-8-sig") as f:
        text = f.read()
    text = text.replace("\t", "  ")
    if text.lstrip().startswith("```"):  # pasted with the code fence
        text = "\n".join(l for l in text.splitlines() if not l.strip().startswith("```"))
    try:
        return yaml.safe_load(text) or {}
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        where = f" near line {mark.line + 1}" if mark else ""
        raise SystemExit(f"{path.name} has a formatting problem{where}: {getattr(exc, 'problem', exc)}.\n"
                         "Tip: use the copy button on Gemini's code block, paste over the whole file, "
                         "and check that quotes inside a narration line are not unbalanced.")


def load_episode(episode_dir: Path) -> tuple[dict, dict]:
    """Return (episode, cfg). cfg = preset + brand + episode 'overrides'."""
    script_path = episode_dir / "script.yaml"
    if not script_path.exists():
        raise SystemExit(f"No script.yaml in {episode_dir}")
    episode = read_yaml(script_path)
    if not episode.get("scenes"):
        raise SystemExit(f"{script_path} has no scenes")

    preset_name = episode.get("preset", "explainer")
    preset_path = ROOT / "presets" / f"{preset_name}.yaml"
    if not preset_path.exists():
        raise SystemExit(f"Unknown preset '{preset_name}' (looked for {preset_path})")

    cfg = read_yaml(preset_path)
    cfg["brand"] = read_yaml(ROOT / "brand" / "brand.yaml")
    tokens_path = ROOT / cfg["brand"].get("tokens", "brand/tokens.json")
    cfg["tokens"] = json.loads(tokens_path.read_text(encoding="utf-8"))
    cfg = deep_merge(cfg, episode.get("overrides"))
    if episode.get("voice"):
        cfg["voice"] = deep_merge(cfg["voice"], {"name": episode["voice"]})
    return episode, cfg


def color(cfg: dict, value: str | None, default: str = "white") -> str:
    """A brand token name (lime, ground, ink, forest, surface, white) or a hex value -> hex."""
    value = value or default
    if str(value).startswith("#"):
        return str(value)
    palette = cfg["tokens"]["color"]
    if value not in palette:
        raise SystemExit(f"Unknown colour '{value}'. Brand colours: {', '.join(palette)} (from brand/tokens.json)")
    return palette[value]


def resolve(path: str | None, episode_dir: Path) -> Path | None:
    """Resolve a path from a config: episode folder first, then project root."""
    if not path:
        return None
    p = Path(path)
    if p.is_absolute():
        return p if p.exists() else None
    for base in (episode_dir, ROOT):
        if (base / p).exists():
            return (base / p).resolve()
    return None
