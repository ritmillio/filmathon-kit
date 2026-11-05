# SOUND.md: sound for "A Life in One Room"

Read with `STORY.md` (timings, stage IDs S1-S8) and `DESIGN.md`. The full second-by-second list is in `audio/sound_cues.csv`; the mixer is `audio/mix_audio.py`. **If a timing in `STORY.md` changes, update the matching rows in `sound_cues.csv` and rebuild.**

## The idea

One pulse runs under everything: **60 beats per minute, one beat a second**, like a resting heart. The opening heartbeat, the music and the clock all keep it. At the end the old heart stops (56.2 s), there is **one second of true silence**, and a new heartbeat starts at **120 bpm** (a newborn). The music's very first note returns at 58 s. Sound and picture say the same thing: one life ends and the next begins.

- **Music:** one simple four-note music-box lullaby motif that grows up and grows old with the person. No second theme.
- **Effects:** everything that moves has a sound. The things are alive, so their small noises are the performance.
- **Silence:** two silences are made on purpose: 22-27 s (away) and 56.3-57.3 s (the end).
- **Voice:** none. There is no dialogue.

## Gate: check before you generate

- Confirm the competition rules on AI-generated audio, and whether a disclosure is needed (see `DESIGN.md`, Gate 0).
- Confirm your plan includes music and sound-effect generation, and read the licence if there is a prize. The pricing page lists a commercial licence for Starter and above; terms for sound effects are not stated.

## Models and cost (ElevenLabs Pro: $99 a month, 600,000 credits)

| Job | Model | Rate | Plan | Credits |
|---|---|---|---|---|
| Sound effects | **SFX v3** (`eleven_text_to_sound_v3`) | 200 per generation | 31 effects x 3 takes = 93 | 18,600 |
| Music | **Eleven Music v2.5** (`music_v2_5`) | 900 per minute | about 6 one-minute takes | 5,400 |
| Voice | none (optional: Eleven v4) | about 1 per character | none | 0 |
| **Total** | | | | **about 24,000 (4.0%)** |

Sources disagree on SFX billing (200 per generation vs a per-second rate). **Generate one effect and check your balance first.** SFX v2 and Music v1 are deprecated. Do not use them.

## Music

Generate the **whole arc once**. The silences are not asked of the generator. They are made by `sound_cues.csv`, which cuts the music into segments.

| Time | What the music does |
|---|---|
| 0-4 s | silence (heartbeat and room tone only) |
| 4-22 s | music box, then piano, then a muted guitar; lullaby, play, teenage irritation. The first note lands as the Lamp opens its eye (4.0 s). |
| 22-27 s | nearly silent (cut by the cue sheet) |
| 27-46 s | warm and full: piano and strings, motif in major, a higher second voice enters with the crib at 33 s |
| 46-54 s | slow, low, thin: the motif with long gaps, 4 dB quieter |
| 54-57 s | nothing |
| 58-60 s | one high music-box note: the first note of the piece again |

**Prompt (one 60-second piece, recommended):**

> Instrumental, no vocals, 60 seconds, tempo exactly 60 BPM in 4/4, one beat per second like a resting heartbeat, key of C major with touches of A minor. One simple four-note music-box lullaby motif that evolves through the piece. 0 to 4 seconds: silence. 4 to 22 seconds: the motif on music box, then playful on piano with soft pizzicato, then irritated and syncopated on a muted electric guitar with minor chords. 22 to 27 seconds: nearly silent, one low piano note. 27 to 46 seconds: warm and full, piano and strings, the motif in major, a higher second voice joins at about 33 seconds. 46 to 54 seconds: the motif slow and low on solo piano, soft tremulous strings, long gaps. 54 to 60 seconds: silence except one high music-box note at the very end.

**Fallback (two halves, same key and tempo, join at 28 s):**

> (first half, 28 s) Instrumental, no vocals, 28 seconds, tempo exactly 60 BPM in 4/4, key of C major with touches of A minor. A simple four-note music-box lullaby motif. 0 to 4 seconds silence. 4 to 14 seconds: music box lullaby, then playful piano with soft pizzicato. 14 to 22 seconds: the motif irritated and syncopated on a muted electric guitar with minor chords. 22 to 28 seconds: nearly silent, one low piano note.

> (second half, 32 s) Instrumental, no vocals, 32 seconds, tempo exactly 60 BPM in 4/4, key of C major with touches of A minor, continuing the same four-note music-box lullaby motif. 0 to 19 seconds: warm and full, piano and strings, the motif in major, a higher second voice joins at about 6 seconds. 19 to 27 seconds: the motif slow and low on solo piano, soft tremulous strings, long gaps. 27 to 32 seconds: silence except one high music-box note at the end.

Save the chosen take as `audio/music.wav`. If the first note is not at 4.1 s, change `src_start_s` on the last `music.wav` row of the cue sheet.

## Sound effects: 31 files to generate (SFX v3)

Save each as `audio/<name>.wav`. Make three takes, keep the best, and record the prompt in `audio/prompts.md`.

| File | Prompt |
|---|---|
| `baby_cry.wav` | Newborn baby first cry, close, a single cry, 3 seconds |
| `heart_slow.wav` | Steady slow adult heartbeat at 60 beats per minute, low soft thump, 12 seconds, seamless loop |
| `heart_fast.wav` | Fast small heartbeat of a newborn at 120 beats per minute, light and quick, 12 seconds, seamless loop |
| `door_open.wav` | Wooden bedroom door flung open with a hinge creak |
| `door_slam.wav` | Angry wooden door slam in a small room |
| `door_close.wav` | Wooden door closing softly, gentle latch click |
| `steps_child.wav` | Small child running on a wooden floor, 4 seconds |
| `laugh.wav` | Brief distant children laughing, 3 seconds |
| `rain.wav` | Steady rain on a window, indoor perspective, 12 seconds, seamless loop |
| `guitar_muffled.wav` | Muffled electric guitar practice heard through a wall, 6 seconds |
| `packing.wav` | Cardboard boxes being packed, tape ripping, 5 seconds |
| `slide.wav` | Soft wooden furniture sliding on a floor, short |
| `pop.wav` | Soft cartoon pop and squash for an object appearing, very short |
| `clock.wav` | Loud slow wall clock ticking in a silent room, 12 seconds, seamless loop |
| `breath_old.wav` | Gentle slow breathing of an elderly person asleep, 10 seconds |
| `room_tone.wav` | Quiet bedroom room tone at night, very faint air, no events, 20 seconds, seamless loop |
| `hop_thud.wav` | Soft small wooden toy hopping and landing on a wooden floor, single light thud, very short |
| `bed_creak.wav` | Short soft wooden bed frame creak as it shifts, single, 1 second |
| `puff.wav` | Small soft puff of dust, airy poof, very short |
| `lamp_click.wav` | Soft pull-chain click of a floor lamp, single |
| `lamp_hum.wav` | Very faint warm electric hum of a small lamp, steady, 20 seconds, seamless loop |
| `wood_tick.wav` | Small wooden toy tapping once on a wooden shelf, a dry hollow tock |
| `plush_plop.wav` | Soft stuffed teddy bear set down on a wooden shelf, a gentle cloth plop with a tiny settle, very short |
| `pencil_scratch.wav` | Pencil making a short quick scratch line on a wooden door frame, 1 second |
| `paper_rip.wav` | Wallpaper being torn off a wall in one long rip, 2 seconds |
| `chair_creak.wav` | Old upholstered armchair creaking softly as someone shifts, 1.5 seconds |
| `cane_tap.wav` | Wooden walking cane tapping twice on a wooden floor, slow |
| `pill_rattle.wav` | Plastic pill bottle shaken gently, a few pills rattling, 1 second |
| `baby_coo.wav` | Newborn baby gurgle and soft coo, content, 3 seconds |
| `wind_hush.wav` | Soft cold wind hush in an empty room with snow outside, 6 seconds, seamless loop |
| `steps_adult.wav` | Adult footsteps in shoes walking away across a wooden floor, 3 seconds |

## Cues by stage (summary; full list in `audio/sound_cues.csv`, 84 cues)

| Stage | Hero cues (time) | Beds |
|---|---|---|
| S1 Birth 0-6 | door flung open 1.4, pops 2.2/2.6/2.9, **first cry 3.0**, Teddy Bear set down 3.7, Lamp click 4.0 | room tone, heartbeat 0.5, lamp hum from 4.0, music from 4.0 |
| S2 Childhood 6-14 | bed creak 6.4 and 8.4, child footsteps 7.0, laugh 9.6, toy hops 10/11/12.2, pencil marks 7.8/10.2/12.6, door opens 11.4 | music-box lullaby |
| S3 Teens 14-22 | wallpaper rips 14.4, posters pop 15.6-16.4, **door slam 17.5**, Lamp eye-roll 18.2, Bear to high shelf 20.2 | rain 15, muffled guitar 16 |
| S4 Away 22-28 | packing 22.0, furniture slide 23, adult footsteps 24, **door closes 25.2**, dust 27 | clock 25, wind 25.5, silence |
| S5 Family 28-38 | door opens warm 28.4, double bed slides 29.4, plants pop, armchair 31, picture 31.8, crib 33, baby coo 34, Bear into crib 35.5, laugh 36, marks 36.6/37.6 | baby heartbeat 33 (quiet), full music |
| S6 Quiet 38-46 | bed creak 39, slide 41, door closes 41.6, pictures pop 42/43/44, chair creak 45 | slow quiet clock |
| S7 Old 46-54 | bed creak 46.6, rails click 46.8, cane 47.6, pills 48.4, armchair slides 50, Bear onto pillow 51.6 | loud clock 46, breathing 49, heartbeat 49.5, thin low music |
| S8 End 54-60 | armchair still 54.6, Bear still 55.3, **Lamp click off 56.0**, **silence 56.3-57.3**, door opens 57.3, **newborn heartbeat 57.8**, new cry 58.4 | first music note again 58.0 |

## Mix levels (dB, relative; 0 is the loudest)

| Layer | Level |
|---|---|
| Hero sounds (door, first cry, slam) | -4 to -8 |
| Music | -14 (-18 in old age) |
| Heartbeat | -14 to -16, then -10 at the end |
| Small foley (pops, ticks, creaks) | -12 to -20 |
| Beds (room tone, lamp hum, rain, clock) | -16 to -32 |

## Build

```
python3 audio/mix_audio.py --cues audio/sound_cues.csv --audio-dir audio --out mix.wav --strict
```

Produces a 60.000-second stereo file. Tested with placeholder tones: 84 cues, exactly 60.000 s, short files looped correctly, and the silence at 56.5-57.2 s measured as digital silence (-91 dB). Real files will differ, so listen. Cues near a silence have an explicit length so a long file cannot leak into it. Then mux `mix.wav` into the film with ffmpeg or lay it under the video in CapCut.

## Score approach v2 (real generation, 2026-11-05 ~21:30)

The first mix used beeps (placeholders). Replaced with real ElevenLabs sound:
- **Music:** `music_v2_5` driven by a **composition plan** (`audio/music_plan.json`, made with `scripts/el_music.py`): one chunk per story stage with exact durations (6, 8, 8, 6, 10, 8, 8, 6 s), the same four-note lullaby theme in every chunk, a warm storybook chamber orchestra (music box, celesta, harp, piano, pizzicato, clarinet, flute, soft horn, cello), no vocals or drums. **Plan format for v2.5 is `chunks` (text, duration_ms, positive_styles, negative_styles, context_adherence), not the v1 `sections` format.** The plan call (`/v1/music/plan`) is free.
- **Takes:** take 1 kept (quiet start, fade to silence, correct arc except S5 is not the loudest). Take 2 (seed 7, louder S5 and quieter S4 in the text) was worse: S4 was the loudest part. Prompt text does not control loudness reliably; the cue sheet does.
- **Final note:** the score fades to silence, so the last music-box note is generated separately (`music_note_first.wav`, SFX v3) and placed at 58.0 s.
- **Effects:** all 31 SOUND.md effects generated once with SFX v3 (`scripts/el_sfx.py`, `prompt_influence` 0.5, loops where the prompt says seamless loop). One take each; not yet listened to by anyone.
- **Craft from the reference tracks (measured, own words):** the favourite title opens very quiet and warm-dark and grows about 7 dB, which matches our story. Classic scores also hit the picture on every small action (stings, plucks, glissandos on each pop). We do that with the cue sheet: add a short plucked or glissando accent beside each hero pop and each object entrance.
- **Not yet used:** `/v1/music/video-to-music` (scores a video, can add synced effects, can return separate music and effects tracks). Best tried once the AI clips exist.

## Using the ElevenLabs MCP

1. Connect the MCP (see the project notes) and run `/mcp` to see the real tool list.
2. Generate **one file at a time** from the table above, using the exact prompt, and save it under the exact name in `audio/`.
3. Never regenerate a take that has been approved. Add the prompt to `audio/prompts.md` beside it.
4. After every new file, run the build command above and listen to the 56-58 s window first.
