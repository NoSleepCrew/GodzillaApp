#!/usr/bin/env python3
"""Copy and optimize kaiju images from images/ into assets/."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
INTAKE = ROOT / "images"

# Friendly drop names (case-insensitive) -> asset path relative to ROOT
IMPORT_MAP = {
    "burning godzilla.png": "assets/hero/godzilla-atomic.png",
    "burning godzilla.jpg": "assets/hero/godzilla-atomic.png",
    "godzilla.png": "assets/hero/godzilla-main.png",
    "godzilla.jpg": "assets/hero/godzilla-main.png",
    "godzilla-main.png": "assets/hero/godzilla-main.png",
    "king ghidorah.png": "assets/enemies/king-ghidorah.png",
    "king ghidorah.jpg": "assets/enemies/king-ghidorah.png",
    "king-ghidorah.png": "assets/enemies/king-ghidorah.png",
    "mechagodzilla.png": "assets/enemies/mechagodzilla.png",
    "rodan.png": "assets/enemies/rodan.png",
    "mothra.png": "assets/enemies/mothra.png",
    "gigan.png": "assets/enemies/gigan.png",
    "destoroyah.png": "assets/enemies/destoroyah.png",
    "anguirus.png": "assets/enemies/anguirus.png",
    "biollante.png": "assets/enemies/biollante.png",
    "spacegodzilla.png": "assets/enemies/spacegodzilla.png",
    "king caesar.png": "assets/enemies/king-caesar.png",
    "king-caesar.png": "assets/enemies/king-caesar.png",
    "hedorah.png": "assets/enemies/hedorah.png",
    "megaguirus.png": "assets/enemies/megaguirus.png",
    "city-battle-bg.png": "assets/city/city-battle-bg.png",
    "city-skyline.png": "assets/city/city-skyline.png",
    "kaiju-roster-reference.png": "assets/roster/kaiju-roster-reference.png",
}

MAX_HERO_WIDTH = 512
CROP_LOGO_RATIO = 0.93  # trim bottom logo bar on tall poster art


def prepare_image(im: Image.Image, dest: str) -> Image.Image:
    im = im.convert("RGBA") if "badge" in dest or "ui" in dest else im.convert("RGB")
    w, h = im.size

    if dest.endswith("godzilla-atomic.png") or dest.endswith("godzilla-main.png"):
        crop_h = int(h * CROP_LOGO_RATIO)
        im = im.crop((0, 0, w, crop_h))
        w, h = im.size
        if w > MAX_HERO_WIDTH:
            nh = int(h * MAX_HERO_WIDTH / w)
            im = im.resize((MAX_HERO_WIDTH, nh), Image.Resampling.LANCZOS)

    if dest.endswith("king-ghidorah.png") and max(w, h) > 640:
        scale = 640 / max(w, h)
        im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)

    return im


def import_file(src: Path, dest_rel: str) -> None:
    dest = ROOT / dest_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src)
    out = prepare_image(im, dest_rel)
    out.save(dest, "PNG", optimize=True, compress_level=9)
    print(f"  {src.name} -> {dest_rel} ({out.size[0]}x{out.size[1]}, {dest.stat().st_size // 1024} KB)")


def main() -> int:
    if not INTAKE.is_dir():
        print(f"Intake folder missing: {INTAKE}")
        return 1

    files = [f for f in INTAKE.iterdir() if f.is_file() and f.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}]
    if not files:
        print(f"No images in {INTAKE}")
        return 0

    print(f"Importing from {INTAKE}...")
    imported = 0
    for src in sorted(files):
        key = src.name.lower()
        dest_rel = IMPORT_MAP.get(key)
        if not dest_rel:
            print(f"  skip (unknown name): {src.name}")
            continue
        import_file(src, dest_rel)
        imported += 1

    if imported == 0:
        print("No recognized filenames. See images/README.md for naming.")
        return 1

    print(f"Done. Imported {imported} image(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
