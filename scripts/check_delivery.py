#!/usr/bin/env python3
"""Validate a film against the AI Budapest Filmathon 2026 delivery rules.

    python3 scripts/check_delivery.py exports/team_title.mp4
"""
import json
import re
import subprocess
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = Path(sys.argv[1])
    info = json.loads(subprocess.run(
        ["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(path)],
        capture_output=True, text=True, check=True).stdout)
    v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    dur = float(info["format"]["duration"])
    num, den = (v["avg_frame_rate"].split("/") + ["1"])[:2]
    fps = float(num) / float(den) if float(den) else 0

    checks = [
        ("container is MP4", path.suffix.lower() == ".mp4", path.suffix),
        ("file name csapatnev_filmcim.mp4",
         bool(re.fullmatch(r"[a-z0-9]+_[a-z0-9_]+\.mp4", path.name)), path.name),
        ("duration 30-90 s", 30 <= dur <= 90, f"{dur:.1f}s"),
        ("video stream is H.264", bool(v) and v["codec_name"] == "h264", v and v["codec_name"]),
        ("resolution >= 1280x720", bool(v) and v["width"] >= 1280 and v["height"] >= 720,
         v and f"{v['width']}x{v['height']}"),
        ("resolution is 1920x1080 (recommended)", bool(v) and (v["width"], v["height"]) == (1920, 1080),
         v and f"{v['width']}x{v['height']}"),
        ("16:9 landscape", bool(v) and abs(v["width"] / v["height"] - 16 / 9) < 0.01, ""),
        ("24 fps", abs(fps - 24) < 0.01, f"{fps:.3f}"),
        ("has audio track", a is not None, a and a["codec_name"]),
    ]
    bad = 0
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail or ''}")
        bad += not ok
    print("\nREADY TO SUBMIT" if not bad else f"\n{bad} check(s) failed")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
