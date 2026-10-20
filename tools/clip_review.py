"""One frame per scene from the review draft, for the owner's approval (CLAUDE.md step 8b).

  python tools/clip_review.py episodes\\db-cooper

Writes output/<name>_clips_review.jpg: the middle frame of every scene in output/<name>_howzit_draft.mp4, labelled
with the scene id, plus the LAST frame next to the FIRST frame so the loop seam can be checked.
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analyse_reference import ff  # noqa: E402


def main():
    ep = Path(sys.argv[1])
    name = ep.name
    draft = ep / "output" / f"{name}_howzit_draft.mp4"
    timing = json.loads((ep / "output" / f"{name}_timing.json").read_text())
    out = ep / "output" / f"{name}_clips_review.jpg"
    tmp = ep / "output" / "_review_tmp"
    tmp.mkdir(exist_ok=True)
    font = "C\\:/Windows/Fonts/arialbd.ttf" if sys.platform == "win32" else "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    shots = [(sid, ["-ss", f"{t['start'] + t['seconds'] / 2:.2f}"]) for sid, t in timing.items()]
    shots += [("LAST", ["-sseof", "-0.04"]), ("FIRST", ["-ss", "0"])]
    tiles = []
    for i, (label, seek) in enumerate(shots):
        f = tmp / f"{i:02d}.png"
        subprocess.run([ff("ffmpeg"), "-v", "error", "-y", *seek, "-i", str(draft), "-frames:v", "1", "-vf",
                        f"scale=240:-2,drawtext=fontfile='{font}':text='{label}':x=8:y=8:fontsize=24:fontcolor=yellow:"
                        "box=1:boxcolor=black@0.6", str(f)], check=True)
        tiles.append(f)
    cols = 8
    layout = "|".join(f"{'0' if i % cols == 0 else '+'.join(['w0'] * (i % cols))}_"
                      f"{'0' if i // cols == 0 else '+'.join(['h0'] * (i // cols))}" for i in range(len(tiles)))
    subprocess.run([ff("ffmpeg"), "-v", "error", "-y", *sum((["-i", str(f)] for f in tiles), []), "-filter_complex",
                    f"xstack=inputs={len(tiles)}:layout={layout}:fill=black", "-frames:v", "1", str(out)], check=True)
    for f in tiles:
        f.unlink()
    tmp.rmdir()
    print(f"-> {out}")


if __name__ == "__main__":
    main()
