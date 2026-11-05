#!/usr/bin/env python3
"""Lay the room sketch over a generated still at 50% so you can see if the window, rug or floor moved.

    python3 scripts/overlay_check.py stills/s02.png          # writes stills/s02_overlay.png
    python3 scripts/overlay_check.py stills/s02.png --open   # and opens it (macOS)
"""
import subprocess, sys
from pathlib import Path
from PIL import Image, ImageChops, ImageOps

SKETCH = Path(__file__).resolve().parent.parent / "assets" / "sketches" / "room_layout_sketch.jpg"

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    img = Image.open(src).convert("RGB").resize((1920, 1080))
    sk = Image.open(SKETCH).convert("L").resize((1920, 1080))
    lines = ImageOps.invert(sk).point(lambda v: 255 if v > 90 else 0)       # dark sketch lines
    red = Image.new("RGB", img.size, (255, 40, 40))
    out = Image.composite(red, img, lines.point(lambda v: int(v * 0.85)))   # red lines on the image
    dst = src.with_name(src.stem + "_overlay.png")
    out.save(dst)
    print("wrote", dst, "-> window, sill, rug and floor lines should sit on the red lines")
    if "--open" in sys.argv:
        subprocess.run(["open", str(dst)])

if __name__ == "__main__":
    main()
