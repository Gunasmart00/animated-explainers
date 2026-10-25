"""Generate still images with the Gemini API (Nano Banana) from an episode's images.yaml: no copy-pasting.

    .venv\\Scripts\\python.exe tools\\gen_image.py episodes\\drive-through-378 --list
    .venv\\Scripts\\python.exe tools\\gen_image.py episodes\\drive-through-378 cast            (3 versions by default)
    .venv\\Scripts\\python.exe tools\\gen_image.py episodes\\drive-through-378 K0 -n 4
    .venv\\Scripts\\python.exe tools\\gen_image.py episodes\\drive-through-378 K0 --dry-run    (show the request, no cost)

images.yaml (in the episode folder; Claude writes it):

    model: gemini-nano-banana-2.1        # optional, this is the default
    size: 2K                             # 1K | 2K | 4K
    images:
      cast:
        aspect: "16:9"
        refs: ["~/Downloads/style_zack_1.jpg", "~/Downloads/style_zack_2.jpg"]
        prompt: |
          ...
      K0:
        aspect: "9:16"
        refs: ["images/cast.png", "~/Downloads/style_zack_1.jpg"]
        prompt: |
          ...

Style references (owner, 2026-10-24): every job automatically gets Zack style references from
refs/zack/curated/catalog.yaml (private, git-ignored). Default groups: `style: [people, sets]` at the top of
images.yaml; a job can set its own, e.g. `style: [animals/dog, people]` or `style: []` for none. A group name takes up
to `style_max` files (default 3); "animals/dog" picks the files whose name contains "dog". Style images are attached
AFTER the job's own refs, and the prompt automatically says they are for the rendering look only (never copy people).

Output: images/<name>_v1.png, _v2.png ... (never overwrites; numbering continues). Pick one and tell Claude, who
copies it to images/<name>.png. Every call is logged in images/gen_log.csv with the estimated cost.

Needs: pip install google-genai (once, in .venv) and the API key in the GEMINI_API_KEY environment variable or in a
.env file at the repo root (GEMINI_API_KEY=...). .env is git-ignored. Billing: the Gemini API has no free tier for
images (about $0.05 per 2K image, 2026-10). A Google AI Pro plan gives $10/month of Google Cloud credit that pays for
API calls (activate at the Google Developer Program site; the project needs a billing account linked). The tool stops
before this month's estimated spend passes $9 (HOWZIT_IMAGE_CAP_USD changes it).
"""
import argparse
import base64
import csv
import datetime
import mimetypes
import os
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = "gemini-nano-banana-2.1"
PRICE = {"1K": 0.0336, "2K": 0.0504, "4K": 0.113}  # USD per image, Nano Banana 2.1 standard (ai.google.dev, 2026-10)


def api_key():
    key = os.environ.get("GEMINI_API_KEY")
    env = ROOT / ".env"
    if not key and env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("GEMINI_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not key:
        sys.exit("No API key: put GEMINI_API_KEY=... in .env at the repo root (see docs/gemini-api-setup.md).")
    return key


def resolve(ep, p):
    p = Path(os.path.expanduser(p))
    if not p.is_absolute():
        p = ep / p if (ep / p).exists() else ROOT / p
    if not p.exists():
        sys.exit(f"Reference image not found: {p}")
    return p


def style_refs(groups, limit):
    cat_path = ROOT / "refs" / "zack" / "curated" / "catalog.yaml"
    if not groups:
        return []
    if not cat_path.exists():
        print(f"(no style catalog at {cat_path}; continuing without Zack style references)")
        return []
    cat = yaml.safe_load(cat_path.read_text(encoding="utf-8"))["groups"]
    out = []
    for g in groups:
        group, _, word = g.partition("/")
        files = [ROOT / x["file"] for x in cat.get(group, []) if not word or word in Path(x["file"]).stem]
        out += [f for f in files[:limit] if f.exists() and f not in out]
    return out


STYLE_NOTE = ("The last {m} attached image(s) are STYLE REFERENCES ONLY: copy only their 3D rendering look (real-time "
              "video-game engine render, skin and material quality, flat even lighting, plain painted sets). Never copy "
              "any person, face, hairstyle, outfit, animal design, place, text or logo from those style images.")


MONTHLY_CAP = float(os.environ.get("HOWZIT_IMAGE_CAP_USD", "9.0"))  # stay inside the $10/month AI Pro cloud credit


def month_spend():
    """Estimated USD spent this calendar month, from every episode's images/gen_log.csv."""
    month = datetime.date.today().strftime("%Y-%m")
    total = 0.0
    for log in ROOT.glob("episodes/*/images/gen_log.csv"):
        with log.open(encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("time", "").startswith(month):
                    total += float(row.get("usd_estimate") or 0)
    return total


def next_paths(ep, name, n):
    out = ep / "images"
    out.mkdir(exist_ok=True)
    i, paths = 1, []
    while len(paths) < n:
        p = out / f"{name}_v{i}.png"
        if not p.exists():
            paths.append(p)
        i += 1
    return paths


def generate(client, model, prompt, refs, aspect, size):
    """Returns PNG/JPEG bytes. Tries the Interactions API (current docs), then generate_content."""
    parts = [{"type": "text", "text": prompt}]
    for r in refs:
        parts.append({"type": "image", "data": base64.b64encode(r.read_bytes()).decode(),
                      "mime_type": mimetypes.guess_type(r.name)[0] or "image/jpeg"})
    try:
        it = client.interactions.create(model=model, input=parts,
                                        response_format={"type": "image", "aspect_ratio": aspect, "image_size": size})
        return base64.b64decode(it.output_image.data)
    except Exception as first:  # older SDK or model only on generate_content
        from google.genai import types
        contents = [types.Part.from_bytes(data=r.read_bytes(), mime_type=mimetypes.guess_type(r.name)[0] or "image/jpeg")
                    for r in refs] + [prompt]
        try:
            resp = client.models.generate_content(
                model=model, contents=contents,
                config=types.GenerateContentConfig(response_modalities=["IMAGE"],
                                                   image_config=types.ImageConfig(aspect_ratio=aspect, image_size=size)))
        except Exception as second:
            raise SystemExit(f"Generation failed.\n  interactions: {first}\n  generate_content: {second}")
        for part in resp.candidates[0].content.parts:
            if getattr(part, "inline_data", None) and part.inline_data.data:
                return part.inline_data.data
        raise SystemExit(f"No image in the reply (maybe refused): {resp.candidates[0].finish_reason} "
                         f"{getattr(resp, 'text', '')}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    ap.add_argument("name", nargs="?")
    ap.add_argument("-n", type=int, default=3, help="how many versions (default 3)")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    ep = (ROOT / a.episode) if not Path(a.episode).is_absolute() else Path(a.episode)
    spec = yaml.safe_load((ep / "images.yaml").read_text(encoding="utf-8"))
    jobs = spec["images"]
    if a.list or not a.name:
        for k, v in jobs.items():
            print(f"{k:12} {v.get('aspect', '9:16'):6} refs: {', '.join(v.get('refs', [])) or '-'}  "
                  f"style: {v.get('style', spec.get('style', ['people', 'sets']))}")
        return
    job = jobs[a.name]
    model = job.get("model", spec.get("model", DEFAULT_MODEL))
    size = str(job.get("size", spec.get("size", "2K")))
    aspect = str(job.get("aspect", "9:16"))
    refs = [resolve(ep, r) for r in job.get("refs", [])]
    styles = style_refs(job.get("style", spec.get("style", ["people", "sets"])), int(spec.get("style_max", 3)))
    refs = (refs + styles)[:14]  # the API takes up to 14 reference images
    prompt = job["prompt"].strip()
    if styles:
        prompt = STYLE_NOTE.format(m=len(styles)) + "\n\n" + prompt
    cost = PRICE.get(size, 0.05) * a.n
    print(f"{a.name}: {a.n} x {model} {size} {aspect}, {len(refs)} reference image(s) ({len(styles)} style), about ${cost:.2f}")
    spent = month_spend()
    print(f"this month so far: about ${spent:.2f} of the ${MONTHLY_CAP:.2f} cap")
    if spent + cost > MONTHLY_CAP and not a.dry_run:
        sys.exit("Stopped: this would go past the monthly cap (the $10 AI Pro cloud credit). Use -n 1, size 1K, "
                 "or wait for next month. Override for one run: set HOWZIT_IMAGE_CAP_USD=20")
    if a.dry_run:
        print("\n".join(str(r) for r in refs))
        print(prompt)
        return
    from google import genai
    client = genai.Client(api_key=api_key())
    log = ep / "images" / "gen_log.csv"
    new = not log.exists()
    for path in next_paths(ep, a.name, a.n):
        data = generate(client, model, prompt, refs, aspect, size)
        path.write_bytes(data)
        print("saved", path.relative_to(ROOT))
        with log.open("a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new:
                w.writerow(["time", "name", "file", "model", "size", "aspect", "refs", "usd_estimate"])
                new = False
            w.writerow([datetime.datetime.now().isoformat(timespec="seconds"), a.name, path.name, model, size, aspect,
                        ";".join(r.name for r in refs), PRICE.get(size, 0.05)])


if __name__ == "__main__":
    main()
