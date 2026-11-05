#!/usr/bin/env python3
"""Scratch soundtrack for the first 6 seconds. Placeholder tones for timing only.
The real sounds come from ElevenLabs (see ../SOUND.md). The first cry is NOT included here."""
import wave, numpy as np
SR = 48000; N = int(6.0 * SR)
t = np.arange(N) / SR
mix = np.zeros(N, dtype=np.float64)
rng = np.random.default_rng(3)

def add(start, sig, gain=1.0):
    i = int(start * SR); j = min(N, i + len(sig))
    if i < N: mix[i:j] += gain * sig[:j - i]

def env(n, attack, decay):
    x = np.arange(n) / SR
    return np.minimum(x / max(attack, 1e-4), 1) * np.exp(-x / decay)

def tone(f, dur, attack=0.005, decay=0.08, f_end=None):
    n = int(dur * SR); x = np.arange(n) / SR
    ff = f if f_end is None else f + (f_end - f) * x / dur
    return np.sin(2 * np.pi * np.cumsum(ff) / SR) * env(n, attack, decay)

def noise(dur, lp=0.2):
    n = int(dur * SR); x = rng.normal(0, 1, n)
    y = np.zeros(n); a = lp
    for i in range(1, n): y[i] = y[i - 1] * (1 - a) + x[i] * a
    return y

# heartbeat, 60 bpm: lub-dub every second, from 0.5 s, fading out over the last second
for k in range(6):
    s = 0.5 + k
    if s >= 6: break
    fade = 1.0 if s < 5.0 else max(0.0, 1 - (s - 5.0))
    add(s, tone(58, 0.22, 0.004, 0.07), 0.55 * fade)
    add(s + 0.30, tone(48, 0.2, 0.004, 0.06), 0.40 * fade)
# door flung open: air whoosh plus a short hinge creak
w = noise(0.7, 0.08) * np.sin(np.linspace(0, np.pi, int(0.7 * SR))) ** 2
add(1.4, w, 0.35)
add(1.4, tone(210, 0.45, 0.02, 0.2, f_end=140) * 0.12)
# pops: cradle, mobile, blanket
for s, f in ((2.2, 520), (2.6, 640), (2.9, 760)):
    add(s, tone(f, 0.09, 0.002, 0.03, f_end=f * 0.45), 0.35)
# (first cry at 3.0 s goes here: use baby_cry.wav from ElevenLabs)
# teddy bear set down: soft cloth plop
add(3.7, tone(130, 0.18, 0.004, 0.05, f_end=70), 0.5)
add(3.7, noise(0.12, 0.05) * env(int(0.12 * SR), 0.002, 0.03), 0.25)
# lamp switch click
c = noise(0.02, 0.9) * env(int(0.02 * SR), 0.0005, 0.004)
add(4.0, c, 0.45)
add(4.0, tone(2200, 0.03, 0.0005, 0.006), 0.15)
# music-box motif: first four notes
for s, f in ((4.2, 659.3), (4.7, 784.0), (5.2, 1046.5), (5.7, 784.0)):
    n = int(1.4 * SR); x = np.arange(n) / SR
    bell = (np.sin(2 * np.pi * f * x) + 0.35 * np.sin(2 * np.pi * f * 2.76 * x) + 0.15 * np.sin(2 * np.pi * f * 5.4 * x)) * env(n, 0.002, 0.45)
    add(s, bell, 0.16)
# very quiet room tone
mix += noise(6.0, 0.02)[:N] * 0.03 * np.minimum(t / 1.0, 1)
mix = np.tanh(mix * 1.1)
mix *= 0.8 / max(1e-9, np.abs(mix).max())
st = np.stack([mix, mix], axis=1)
with wave.open('scratch_audio.wav', 'wb') as f:
    f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR)
    f.writeframes((st * 32767).astype('<i2').tobytes())
print('wrote scratch_audio.wav')
