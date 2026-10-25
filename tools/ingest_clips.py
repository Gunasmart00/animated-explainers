"""Copy the newest N videos from Downloads into an episode's clips folder as c01.mp4 ... (oldest first).

    python tools/ingest_clips.py episodes/<name> 6 [--dry-run] [--from "C:/Users/me/Downloads"] [--start 1]

Download the Flow clips in order (C1 first). --start 3 makes the first file c03.mp4 (for a redo of C3 only, use
N=1 --start 3). Existing clips are kept as clips/old/<name>_<time>.mp4 before being replaced.
"""
import argparse
import shutil
import time
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    ap.add_argument("count", type=int)
    ap.add_argument("--from", dest="src", default=str(Path.home() / "Downloads"))
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    vids = sorted(Path(a.src).glob("*.mp4"), key=lambda p: p.stat().st_mtime)[-a.count:]
    if len(vids) < a.count:
        raise SystemExit(f"Only {len(vids)} videos in {a.src}")
    clips = Path(a.episode) / "clips"
    clips.mkdir(parents=True, exist_ok=True)
    for i, v in enumerate(vids):
        dst = clips / f"c{a.start + i:02d}.mp4"
        print(f"{v.name}  ->  {dst}")
        if a.dry_run:
            continue
        if dst.exists():
            old = clips / "old"
            old.mkdir(exist_ok=True)
            shutil.move(str(dst), old / f"{dst.stem}_{time.strftime('%Y%m%d-%H%M%S')}.mp4")
        shutil.copy2(v, dst)
    if a.dry_run:
        print("(dry run: nothing copied)")


if __name__ == "__main__":
    main()
