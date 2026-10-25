"""Write a by-hand sheet of an episode's image jobs (for AI Studio / Gemini web, no API).

    .venv\\Scripts\\python.exe tools\\image_sheet.py episodes\\drive-through-378

-> episodes/<name>/output/<name>_image_prompts.md: for every job in images.yaml, the files to attach (full paths, in
order), the aspect ratio, the file name to save the result as, and the full prompt (with the style note), ready to
paste. Same jobs and style references as tools/gen_image.py, so either route gives the same request.
"""
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_image import ROOT, STYLE_NOTE, style_refs  # noqa: E402

WIN_ROOT = r"G:\Apps\animated-explainers"


def win(p: Path) -> str:
    try:
        return WIN_ROOT + "\\" + str(p.relative_to(ROOT)).replace("/", "\\")
    except ValueError:
        return str(p)


def main():
    ep = ROOT / sys.argv[1]
    spec = yaml.safe_load((ep / "images.yaml").read_text(encoding="utf-8"))
    out = [f"# {ep.name}: images by hand\n",
           "Where: aistudio.google.com → Create → Image (Nano Banana), or the Gemini app with the image tool. "
           "For each job: set the aspect ratio, attach the files in the order listed, paste the prompt, generate 2-3, "
           "download the best and save it with the name given (into the episode's `images` folder). "
           "Then tell Claude, who checks it before the next job uses it.\n"]
    for name, job in spec["images"].items():
        refs = [(ep / r) if (ep / r).exists() or r.startswith("images/") else Path(r) for r in job.get("refs", [])]
        styles = style_refs(job.get("style", spec.get("style", ["people", "sets"])), int(spec.get("style_max", 3)))
        prompt = job["prompt"].strip()
        if styles:
            prompt = STYLE_NOTE.format(m=len(styles)) + "\n\n" + prompt
        files = [win(ep / r) if not str(r).startswith("~") else str(r) for r in job.get("refs", [])] + [win(s) for s in styles]
        out.append(f"\n## {name}  ({job.get('aspect', '9:16')})\n")
        out.append(f"Save as: `{win(ep / 'images' / (name + '.png'))}`\n\n")
        out.append("Attach, in this order:\n" + ("".join(f"{i}. `{f}`\n" for i, f in enumerate(files, 1)) or "- nothing\n"))
        out.append(f"\n```\n{prompt}\n```\n")
    path = ep / "output" / f"{ep.name}_image_prompts.md"
    path.parent.mkdir(exist_ok=True)
    path.write_text("".join(out), encoding="utf-8")
    print("wrote", path)


if __name__ == "__main__":
    main()
