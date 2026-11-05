#!/usr/bin/env python3
"""Assemble a film from film.json using ffmpeg. Standard library only.

    python3 scripts/rough_cut.py film.json            # build
    python3 scripts/rough_cut.py film.json --dry-run  # print the ffmpeg command

What it does:
  * normalises every shot to the target size / fps (crop-to-fill, no black bars)
  * joins shots with optional crossfades
  * places voice-over / sfx at absolute times, lays music underneath
  * ducks the music under the voice, then loudness-normalises the mix
  * exports H.264 + AAC MP4 (the festival delivery format)
"""
import argparse
import json
import shlex
import subprocess
import sys
from pathlib import Path


def probe_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return float(out)


def fnum(x: float) -> str:
    return f"{x:.3f}"


def build(cfg: dict, base: Path):
    W = cfg.get("width", 1920)
    H = cfg.get("height", 1080)
    fps = cfg.get("fps", 24)
    xf = float(cfg.get("crossfade", 0.0))
    shots = cfg["shots"]
    if not shots:
        sys.exit("film.json has no shots")

    inputs, fc = [], []

    # ---- video ---------------------------------------------------------
    durs = []
    for i, s in enumerate(shots):
        path = base / s["file"]
        if not path.exists():
            sys.exit(f"missing shot file: {path}")
        start = float(s.get("start", 0))
        avail = probe_duration(path) - start
        d = min(float(s["duration"]), avail) if "duration" in s else avail
        if d <= xf * 2 and xf > 0:
            sys.exit(f"shot {s['file']} is {d:.2f}s, too short for a {xf}s crossfade")
        durs.append(d)
        inputs += ["-i", str(path)]
        fc.append(
            f"[{i}:v]trim=start={fnum(start)}:duration={fnum(d)},setpts=PTS-STARTPTS,"
            f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
            f"fps={fps},setsar=1,format=yuv420p[v{i}]"
        )

    if len(shots) == 1:
        fc.append("[v0]null[vout]")
        total = durs[0]
    elif xf > 0:
        prev, acc = "v0", durs[0]
        for k in range(1, len(shots)):
            offset = acc - xf
            out = "vout" if k == len(shots) - 1 else f"x{k}"
            fc.append(
                f"[{prev}][v{k}]xfade=transition=fade:duration={fnum(xf)}:"
                f"offset={fnum(offset)}[{out}]"
            )
            prev, acc = out, acc + durs[k] - xf
        total = acc
    else:
        joined = "".join(f"[v{i}]" for i in range(len(shots)))
        fc.append(f"{joined}concat=n={len(shots)}:v=1:a=0[vout]")
        total = sum(durs)

    # ---- audio ---------------------------------------------------------
    n = len(shots)
    voice_labels, sfx_labels = [], []
    for v in cfg.get("voice", []):
        p = base / v["file"]
        if not p.exists():
            sys.exit(f"missing voice file: {p}")
        inputs += ["-i", str(p)]
        ms = int(float(v.get("start", 0)) * 1000)
        vol = v.get("volume", 1.0)
        lab = f"vo{n}"
        fc.append(f"[{n}:a]adelay={ms}|{ms},volume={vol}[{lab}]")
        voice_labels.append(lab)
        n += 1
    for s in cfg.get("sfx", []):
        p = base / s["file"]
        if not p.exists():
            sys.exit(f"missing sfx file: {p}")
        inputs += ["-i", str(p)]
        ms = int(float(s.get("start", 0)) * 1000)
        vol = s.get("volume", 0.8)
        lab = f"fx{n}"
        fc.append(f"[{n}:a]adelay={ms}|{ms},volume={vol}[{lab}]")
        sfx_labels.append(lab)
        n += 1

    music = cfg.get("music")
    music_label = None
    if music:
        p = base / music["file"]
        if not p.exists():
            sys.exit(f"missing music file: {p}")
        inputs += ["-i", str(p)]
        vol = music.get("volume", 0.35)
        fade = float(music.get("fade_out", 2.0))
        fade_at = max(total - fade, 0)
        fc.append(
            f"[{n}:a]atrim=duration={fnum(total)},asetpts=PTS-STARTPTS,volume={vol},"
            f"afade=t=in:d=1,afade=t=out:st={fnum(fade_at)}:d={fnum(fade)}[mus]"
        )
        music_label = "mus"
        n += 1

    mix_inputs = []
    if voice_labels:
        if len(voice_labels) == 1:
            fc.append(f"[{voice_labels[0]}]anull[voicebus]")
        else:
            ins = "".join(f"[{l}]" for l in voice_labels)
            fc.append(f"{ins}amix=inputs={len(voice_labels)}:normalize=0[voicebus]")
        if music_label:
            fc.append("[voicebus]asplit=2[voice_a][voice_b]")
            fc.append(
                f"[{music_label}][voice_b]sidechaincompress="
                "threshold=0.04:ratio=8:attack=20:release=500[mus_d]"
            )
            mix_inputs += ["voice_a", "mus_d"]
        else:
            mix_inputs += ["voicebus"]
    elif music_label:
        mix_inputs += [music_label]
    mix_inputs += sfx_labels

    if not mix_inputs:
        sys.exit("No audio: the festival requires sound in the file.")

    ins = "".join(f"[{l}]" for l in mix_inputs)
    fc.append(
        f"{ins}amix=inputs={len(mix_inputs)}:normalize=0:duration=longest,"
        f"atrim=duration={fnum(total)},"
        "loudnorm=I=-16:TP=-1.5:LRA=11[aout]"
    )

    out_path = base / cfg.get("output", "exports/rough_cut.mp4")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = (
        ["ffmpeg", "-y", "-hide_banner"] + inputs +
        ["-filter_complex", ";".join(fc),
         "-map", "[vout]", "-map", "[aout]",
         "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p",
         "-r", str(fps), "-c:a", "aac", "-b:a", "256k", "-ar", "48000",
         "-movflags", "+faststart", "-t", fnum(total), str(out_path)]
    )
    return cmd, total, out_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg_path = Path(a.config).resolve()
    cfg = json.loads(cfg_path.read_text())
    base = cfg_path.parent
    cmd, total, out = build(cfg, base)
    print(f"total runtime: {total:.1f}s -> {out}")
    if a.dry_run:
        print(" ".join(shlex.quote(c) for c in cmd))
        return
    subprocess.run(cmd, check=True)
    print(f"done: {out}")
    if not 30 <= total <= 90:
        print(f"WARNING: runtime {total:.1f}s is outside the 30-90s rule", file=sys.stderr)


if __name__ == "__main__":
    main()
