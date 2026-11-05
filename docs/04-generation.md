# 04 · Generation

Order matters. **Sound first, picture second**, because voice and music fix your timing.

## 1. Voice-over (ElevenLabs)

1. Pick one voice and stick with it for the whole film.
2. Generate the narration in one or two takes, not line by line, so the delivery stays consistent.
3. Save to `voice/vo01.mp3`. Measure it: `ffprobe -v error -show_entries format=duration -of csv=p=0 voice/vo01.mp3`.
4. If it runs over your target runtime, trim the script rather than speeding up the voice.

Ask the agent: *"Generate `voice/vo01.mp3` from this text with voice X, calm and slightly slow."*

## 2. Music

Describe mood, tempo, instruments and the shape: *"60 seconds, sparse piano, slow build, a held breath at 0:45, resolves warm at the end."* Save as `music/theme.mp3`. Generate 2–3 variants and pick one by listening, not by prompt.

## 3. Sound effects

Three to six well-placed sfx (a door, a wind-up, a whoosh on a cut) lift a film more than extra shots. Save in `sfx/` and place them by timestamp in `film.json`.

## 4. Shots

Prompt formula that works for most image-to-video and text-to-video models:

```
[subject + action], [setting], [camera move], [lighting], [style line]
```

Example: *"An old lighthouse keeper climbs a spiral staircase, lantern swinging, slow push-in, warm amber light against cold blue windows, 35mm film, soft grain."*

### Consistency tricks

- **Same style line, word for word, in every prompt.**
- **Generate a still first**, approve it, then animate it (image-to-video). It is cheaper to reject a still than a clip.
- **Reuse the same character/reference image** for every shot with that character.
- **One camera move per shot.** "Slow push-in", "static", "pan left". Never combine.
- **Ask for 4–5 seconds.** Longer clips drift.
- **Keep native clip audio off** (default). You will add your own sound.

### Budget

Every attempt costs credits. Plan 2 variants per shot, regenerate only the shots that are truly unusable, and watch your balance. Don't spend the last 20% of credits on a shot that could be cut instead.

## File naming

`shots/s01.mp4`, `shots/s02.mp4`, … Keep alternates as `s01_b.mp4` so `film.json` stays readable.
