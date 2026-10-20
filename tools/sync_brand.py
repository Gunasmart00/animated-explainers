"""Copy the brand files from the youtube_clipping repo (the source of truth) into this repo.

Usage (from this folder):  python tools/sync_brand.py
                           python tools/sync_brand.py --source G:\\Apps\\youtube_clipping

Run it after changing anything in youtube_clipping/brand (colours, logos, watermark).
"""
import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = [
    "tokens.json", "brand-guide.md",
    "howzit/profile-1080.png", "howzit/profile-1080.svg",
    "howzit/wordmark-on-dark.png", "howzit/wordmark-on-dark.svg",
    "logo/lockup-on-dark.png", "logo/lockup-on-dark.svg",
    "logo/mark-on-dark.png", "logo/mark-on-dark.svg",
    "logo/mark-on-light.png", "logo/mark-on-light.svg",
    "youtube/watermark-150.png", "youtube/watermark-150.svg",
    "video/shorts-safe-zone-guide.png", "video/shorts-safe-zone-guide.svg",
]
# Made in this repo (not in youtube_clipping yet): howzit/watermark-150.svg/.png


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, default=ROOT.parent / "youtube_clipping")
    src = ap.parse_args().source / "brand"
    if not src.exists():
        raise SystemExit(f"Not found: {src}")
    for rel in FILES:
        s, d = src / rel, ROOT / "brand" / rel
        if not s.exists():
            print(f"  missing in source: {rel}")
            continue
        d.parent.mkdir(parents=True, exist_ok=True)
        if not d.exists() or s.read_bytes() != d.read_bytes():
            shutil.copy2(s, d)
            print(f"  updated {rel}")
    print("Brand files are in sync.")


if __name__ == "__main__":
    main()
