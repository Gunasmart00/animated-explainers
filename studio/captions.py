"""Burned-in text, written as one .ass subtitle file per export:
captions (with the spoken word lit up), pop-up callouts, the hook box and an optional text watermark.

Times are absolute seconds from the start of the video. The .ass canvas is always the full preset
size (1080x1920), so half-size drafts scale everything down automatically.

Brand rule: lime is for one thing per frame. While the hook box or a lime pop-up is on screen,
the caption highlight is switched off.
"""
from __future__ import annotations

import copy
import re
from pathlib import Path

from .config import color

BREAK_AFTER = (".", "!", "?", ";", ":", ",", "—")


def ass_color(hex_color: str, opacity: float = 1.0) -> str:
    h = hex_color.lstrip("#")
    alpha = int(round((1 - opacity) * 255))
    return f"&H{alpha:02X}{h[4:6]}{h[2:4]}{h[0:2]}".upper()


def _tag_color(hex_color: str) -> str:
    """Colour for an inline override tag (\\1c etc.): &HBBGGRR&, alpha goes in separate \\1a tags."""
    h = hex_color.lstrip("#")
    return f"&H{h[4:6]}{h[2:4]}{h[0:2]}&".upper()


def ts(seconds: float) -> str:
    cs = max(int(round(seconds * 100)), 0)
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def srt_ts(seconds: float) -> str:
    ms = max(int(round(seconds * 1000)), 0)
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def esc(text: str) -> str:
    return text.replace("\\", "").replace("{", "(").replace("}", ")").replace("\n", "\\N")


def group_words(words: list[dict], per_line: int) -> list[list[dict]]:
    groups, cur = [], []
    for i, w in enumerate(words):
        if cur and (w["start"] - cur[-1]["end"] > 0.6):
            groups.append(cur)
            cur = []
        cur.append(w)
        nxt = words[i + 1] if i + 1 < len(words) else None
        # Don't strand the last word of a sentence on its own ("hot.") — let the line run one long.
        dangling = (nxt is not None and len(cur) == per_line and not w["text"].endswith(BREAK_AFTER)
                    and nxt["text"].endswith((".", "!", "?")))
        if (len(cur) >= per_line and not dangling) or w["text"].endswith(BREAK_AFTER) or nxt is None:
            groups.append(cur)
            cur = []
    return groups


def _norm(s: str) -> str:
    return re.sub(r"[^\w$%₹]", "", s.lower())


def find_word(words: list[dict], target: str, nth: int = 1) -> dict | None:
    """Exact text first ("One," beats "one"), then case-insensitive, then partial. nth picks a repeat."""
    t = _norm(target)
    tests = (lambda w: w["text"].strip() == target.strip(),
             lambda w: _norm(w["text"]) == t,
             lambda w: bool(t) and t in _norm(w["text"]))
    for test in tests:
        hits = [w for w in words if test(w)]
        if len(hits) >= nth:
            return hits[nth - 1]
    return None


def _em_ratio(font_file: Path | None) -> float:
    try:
        from fontTools.ttLib import TTFont
        f = TTFont(str(font_file))
        return f["head"].unitsPerEm / (f["OS/2"].usWinAscent + f["OS/2"].usWinDescent)
    except Exception:
        return 0.65


class AssWriter:
    def __init__(self, cfg: dict, font_file: Path | None):
        self.cfg = cfg
        self.font_file = font_file
        self.W, self.H = cfg["video"]["width"], cfg["video"]["height"]
        self.events: list[str] = []
        self.srt: list[tuple[float, float, str]] = []
        self.lime_busy: list[tuple[float, float]] = []
        self.popup_times: list[tuple[float, str | None]] = []  # (start, sfx name) for sound effects

    def clone(self) -> "AssWriter":
        return copy.deepcopy(self)

    def _c(self, value, default="white", opacity=1.0) -> str:
        return ass_color(color(self.cfg, value, default), opacity)

    def _lime_free(self, start: float, end: float) -> bool:
        return all(end <= a or start >= b for a, b in self.lime_busy)

    # ---------- hook box ----------
    def add_hook(self, text: str) -> None:
        hb = self.cfg["brand"]["hook_box"]
        x, y, w, h, r = hb["x"], hb["y"], hb["w"], hb["h"], hb.get("radius", 24)
        end = float(hb.get("seconds", 3.0))
        size, lines = self._fit(text, w - 64, h - 24, int(hb.get("size", 84)))
        box = (f"m {r} 0 l {w - r} 0 b {w} 0 {w} 0 {w} {r} l {w} {h - r} b {w} {h} {w} {h} {w - r} {h} "
               f"l {r} {h} b 0 {h} 0 {h} 0 {h - r} l 0 {r} b 0 0 0 0 {r} 0")
        anim = "\\fad(120,180)\\fscx92\\fscy92\\t(0,160,\\fscx100\\fscy100)"
        self.events.append(f"Dialogue: 4,{ts(0)},{ts(end)},Box,,0,0,0,,"
                           f"{{\\an7\\pos({x},{y})\\p1\\bord0\\shad0\\1c{self._c(hb.get('fill'), 'lime')}{anim}}}{box}{{\\p0}}")
        body = "\\N".join(esc(line) for line in lines)
        self.events.append(f"Dialogue: 5,{ts(0)},{ts(end)},Hook,,0,0,0,,"
                           f"{{\\an5\\pos({x + w // 2},{y + h // 2})\\fs{size}\\1c{self._c(hb.get('text'), 'ground')}{anim}}}"
                           f"{body}")
        self.lime_busy.append((0.0, end))

    def _fit(self, text: str, max_w: int, max_h: int, size: int) -> tuple[int, list[str]]:
        """Largest font size (down to 44) where the hook fits the box in at most 2 lines."""
        try:
            from PIL import ImageFont
        except ImportError:
            ImageFont = None
        em = _em_ratio(self.font_file)  # libass sizes text by ascent+descent, not by the em square
        for s in range(size, 43, -2):
            if ImageFont and self.font_file:
                font = ImageFont.truetype(str(self.font_file), max(int(s * em), 1))
                width = lambda t: font.getlength(t)
            else:
                width = lambda t: len(t) * s * em * 0.56
            lines, cur = [], ""
            for word in text.split():
                trial = f"{cur} {word}".strip()
                if width(trial) <= max_w or not cur:
                    cur = trial
                else:
                    lines.append(cur)
                    cur = word
            lines.append(cur)
            if len(lines) <= 2 and all(width(l) <= max_w for l in lines) and len(lines) * s <= max_h:
                return s, lines
        print(f"  ! hook text is long for the hook box: '{text}'. Aim for 3-7 words.")
        return 44, lines

    # ---------- captions ----------
    def add_captions(self, words: list[dict], offset: float, scene_end: float) -> None:
        c = self.cfg["captions"]
        groups = group_words(words, int(c.get("words_per_line", 3)))
        x, y = self.W // 2, int(self.H * c["position_y"])
        hi = self._c(c["highlight_color"]) if c.get("highlight_color") else None
        base = self._c(c.get("color"), "white")
        for gi, g in enumerate(groups):
            start = offset + g[0]["start"]
            nxt = groups[gi + 1][0]["start"] + offset if gi + 1 < len(groups) else None
            end = nxt if nxt is not None and nxt - (offset + g[-1]["end"]) < 0.6 else offset + g[-1]["end"] + 0.25
            end = min(end, scene_end)
            texts = [self._caption_text(w["text"]) for w in g]
            self.srt.append((start, end, " ".join(w["text"].strip() for w in g)))
            blur = f"\\blur{c['blur']}" if c.get("blur") else ""
            # bottom-anchored so a 2-line caption grows upward, away from Instagram's buttons;
            # a 1-line caption is still centred on position_y
            pos = f"{{\\an2\\pos({x},{y + int(c['size']) // 2}){blur}}}"
            if not hi:
                self.events.append(f"Dialogue: 1,{ts(start)},{ts(end)},Caption,,0,0,0,,{pos}{esc(' '.join(texts))}")
                continue
            # One event per spoken word, that word lit up (unless lime is already on screen).
            for wi, w in enumerate(g):
                ws = offset + w["start"] if wi else start
                we = offset + g[wi + 1]["start"] if wi + 1 < len(g) else end
                if we <= ws:
                    continue
                lit = wi if self._lime_free(ws, we) else -1
                parts = [(f"{{\\1c{hi}}}{esc(t)}{{\\1c{base}}}" if k == lit else esc(t)) for k, t in enumerate(texts)]
                self.events.append(f"Dialogue: 1,{ts(ws)},{ts(we)},Caption,,0,0,0,,{pos}{' '.join(parts)}")

    def _caption_text(self, t: str) -> str:
        t = t.strip()
        return t.upper() if self.cfg["captions"].get("uppercase") else t

    # ---------- pop-ups ----------
    def add_popup(self, popup: dict, words: list[dict], offset: float, scene_end: float, scene_id: str) -> None:
        p = self.cfg["popups"]
        if "at_word" in popup:
            w = find_word(words, str(popup["at_word"]), int(popup.get("nth", 1)))
            if w is None:
                print(f"  ! scene {scene_id}: pop-up word '{popup['at_word']}' not found in narration; showing at scene start")
                start = offset + 0.2
            else:
                start = offset + w["start"]
        else:
            start = offset + float(popup.get("at", 0.2))
        end = min(start + float(popup.get("hold", p["hold"])), scene_end)
        col_name = popup.get("color", p.get("default_color", "white"))
        col = self._c(col_name)
        y = popup.get("y", p["position_y"])
        if isinstance(y, str):
            y = {"top": 0.30, "center": 0.45, "bottom": 0.55}.get(y, p["position_y"])
        x = popup.get("x", 0.5)
        size = int(popup.get("size", p["size"]))
        pos = f"\\an5\\pos({int(self.W * x)},{int(self.H * y)})\\fs{size}"
        pop = "\\fscx30\\fscy30\\t(0,160,\\fscx112\\fscy112)\\t(160,280,\\fscx100\\fscy100)\\fad(60,180)"
        text = esc(str(popup["text"]))
        if popup.get("glow", p.get("glow", False)):
            lime = _tag_color(color(self.cfg, "lime"))
            self.events.append(f"Dialogue: 2,{ts(start)},{ts(end)},Popup,,0,0,0,,"
                               f"{{{pos}{pop}\\bord10\\blur16\\1c{lime}\\3c{lime}\\1a&H70&\\3a&H90&\\shad0}}{text}")
        self.events.append(f"Dialogue: 3,{ts(start)},{ts(end)},Popup,,0,0,0,,"
                           f"{{{pos}{pop}\\bord{p.get('outline', 2)}\\3c&H000000&\\3a&H80&\\shad3\\4c&H000000&\\4a&H90&"
                           f"\\1c{_tag_color(color(self.cfg, col_name))}}}{text}")
        is_lime = color(self.cfg, col_name) == color(self.cfg, "lime")
        self.popup_times.append((start, popup.get("sfx", "reveal" if is_lime else "default")))
        if color(self.cfg, col_name) == color(self.cfg, "lime"):
            self.lime_busy.append((start, end))

    # ---------- text watermark ----------
    def add_text_watermark(self, total: float) -> None:
        wm = self.cfg["brand"].get("text_watermark") or {}
        if not wm.get("text"):
            return
        vert, horiz = wm.get("position", "bottom-center").split("-")
        an = {"top": {"left": 7, "center": 8, "right": 9}, "bottom": {"left": 1, "center": 2, "right": 3}}[vert][horiz]
        mx, my = int(self.W * 0.04), int(self.H * 0.035)
        x = {"left": mx, "center": self.W // 2, "right": self.W - mx}[horiz]
        y = self.H - my if vert == "bottom" else my
        op = wm.get("opacity", 0.55)
        tag = (f"{{\\an{an}\\pos({x},{y})\\fs{wm.get('size', 40)}\\1c{_tag_color(color(self.cfg, wm.get('color'), 'ink'))}\\1a&H{int((1 - op) * 255):02X}&"
               f"\\3c{ass_color('#000000', op * 0.6)}}}")
        self.events.append(f"Dialogue: 0,{ts(0)},{ts(total)},Watermark,,0,0,0,,{tag}{esc(wm['text'])}")

    # ---------- output ----------
    def write(self, path, srt_path=None) -> None:
        c, p = self.cfg["captions"], self.cfg["popups"]
        bold = "-1" if c.get("bold", True) else "0"
        pbold = "-1" if p.get("bold", c.get("bold", True)) else "0"
        hb = self.cfg["brand"]["hook_box"]
        header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {self.W}
PlayResY: {self.H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Caption,{c['font']},{c['size']},{self._c(c.get('color'))},{self._c(c.get('color'))},{self._c(c.get('outline_color'), '#000000')},{self._c(c.get('shadow_color'), '#000000', c.get('shadow_opacity', 0.5))},{bold},0,0,0,100,100,0,0,1,{c['outline']},{c.get('shadow', 0)},5,120,120,0,1
Style: Popup,{p['font']},{p['size']},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,{pbold},0,0,0,100,100,0,0,1,{p.get('outline', 6)},0,5,0,0,0,1
Style: Box,{c['font']},20,{self._c(hb.get('fill'), 'lime')},&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: Hook,{c['font']},{hb.get('size', 70)},{self._c(hb.get('text'), 'ground')},&H00FFFFFF,&H00000000,&H00000000,{bold},0,0,0,100,100,0,0,1,0,0,5,0,0,0,1
Style: Watermark,{c['font']},40,&H70FFFFFF,&H70FFFFFF,&HA0000000,&H00000000,{bold},0,0,0,100,100,0,0,1,1.5,0,2,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
        with open(path, "w", encoding="utf-8") as f:
            f.write(header + "\n".join(self.events) + "\n")
        if srt_path:
            with open(srt_path, "w", encoding="utf-8") as f:
                for i, (s, e, t) in enumerate(self.srt, 1):
                    f.write(f"{i}\n{srt_ts(s)} --> {srt_ts(e)}\n{t}\n\n")
