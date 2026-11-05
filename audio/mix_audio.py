#!/usr/bin/env python3
"""Mix a cue sheet into one 60-second WAV with ffmpeg.

Usage:  python3 mix_audio.py --cues sound_cues.csv --audio-dir audio --out mix.wav

CSV columns: time_s, file, gain_db, fade_in_s, fade_out_s, dur_s, src_start_s, note
  time_s       when the sound starts in the film
  dur_s        how long it plays (blank = whole file). Longer than the file = loops.
  src_start_s  where in the file to start (blank = 0)
"""
import argparse, csv, os, subprocess, sys

def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(out.stdout.strip())

def num(v, default=0.0):
    v = (v or "").strip()
    return float(v) if v else default

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cues", default="sound_cues.csv")
    ap.add_argument("--audio-dir", default="audio")
    ap.add_argument("--out", default="mix.wav")
    ap.add_argument("--length", type=float, default=60.0)
    ap.add_argument("--strict", action="store_true", help="fail if a file is missing")
    a = ap.parse_args()

    rows = [r for r in csv.DictReader(open(a.cues, encoding="utf-8")) if r["file"].strip()]
    inputs, chains, missing = [], [], []
    for r in rows:
        path = os.path.join(a.audio_dir, r["file"].strip())
        if not os.path.exists(path):
            missing.append(r["file"].strip()); continue
        n = len(inputs)
        length = probe(path)
        t = num(r["time_s"]); gain = num(r["gain_db"]); fi = num(r["fade_in_s"]); fo = num(r["fade_out_s"])
        src = num(r["src_start_s"]); dur = num(r["dur_s"], length - src)
        f = [f"aresample=48000", "aformat=sample_fmts=fltp:channel_layouts=stereo"]
        if src > 0: f += [f"atrim=start={src}", "asetpts=PTS-STARTPTS"]
        if dur > length - src + 0.01: f += ["aloop=loop=-1:size=2147483647", "asetpts=PTS-STARTPTS"]
        f.append(f"atrim=duration={dur}")
        if fi > 0: f.append(f"afade=t=in:st=0:d={fi}")
        if fo > 0: f.append(f"afade=t=out:st={max(dur - fo, 0)}:d={fo}")
        f.append(f"volume={gain}dB")
        f.append(f"adelay={int(round(t * 1000))}:all=1")
        chains.append(f"[{n}:a]" + ",".join(f) + f"[a{n}]")
        inputs.append(path)
    if missing:
        msg = "Missing files: " + ", ".join(sorted(set(missing)))
        if a.strict: sys.exit(msg)
        print("Warning. " + msg + " (those cues are skipped)")
    if not inputs: sys.exit("No audio files found.")
    labels = "".join(f"[a{i}]" for i in range(len(inputs)))
    chains.append(f"{labels}amix=inputs={len(inputs)}:normalize=0:dropout_transition=0,"
                  f"alimiter=limit=0.95,apad=whole_dur={a.length},atrim=0:{a.length}[out]")
    graph = ";".join(chains)
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for p in inputs: cmd += ["-i", p]
    cmd += ["-filter_complex", graph, "-map", "[out]", "-ar", "48000", "-ac", "2", a.out]
    subprocess.run(cmd, check=True)
    print(f"Wrote {a.out}: {len(inputs)} cues, {probe(a.out):.3f} s")

if __name__ == "__main__":
    main()
