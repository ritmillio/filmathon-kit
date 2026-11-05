# 05 · Editing

You have three options, from fastest to most control. For a 30–90 second film in one evening, **start with option 1** and only move on if you need to.

## Option 1: `film.json` + `rough_cut.py` (recommended)

Edit the numbers, re-run, watch. A rebuild takes seconds.

```bash
python3 scripts/rough_cut.py film.json
open exports/rough_cut.mp4
```

What you can control in `film.json`:

| Field | Effect |
|---|---|
| `shots[].start` / `duration` | Trim a shot. Cut earlier than feels natural |
| `crossfade` | `0` = hard cuts, `0.3` = soft. Hard cuts feel more cinematic for action |
| `voice[].start` | When narration begins (seconds) |
| `sfx[].start` | Place a sound on a cut or an action |
| `music.volume` / `fade_out` | Music level and tail |

Music is automatically ducked under the voice and the whole mix is normalised to -16 LUFS, so you don't need to balance levels by hand.

Ask the agent for notes-style changes: *"Shorten shot 4 to 2.5 seconds and move the whoosh to land on the cut."*

## Option 2: a GUI editor for hand-tuning

| Editor | Cost | Good for |
|---|---|---|
| **iMovie** (preinstalled on Mac) | Free | Simplest. Fine for trimming and titles |
| **CapCut Desktop** | Free tier | Fast, templates, auto-captions |
| **DaVinci Resolve** | Free | Best colour grading and audio; steeper learning curve (budget an hour) |

Workflow: build the rough cut with Option 1, then import the **individual files** plus `exports/rough_cut.mp4` as a reference into your editor and adjust. Only do this if you already know the editor, since learning it during a five-hour event is a risk.

## Option 3: let the agent do all of it

Describe changes in plain language and have the agent edit `film.json`. This is the intended workflow for people with no editing experience.

## Editing principles for AI footage

- **Cut early.** Leave a shot before the AI glitches appear (hands, faces, text).
- **Cut on sound.** Land a cut on a beat, a whoosh or a word.
- **Contrast beats consistency.** Alternate wide/close, still/moving.
- **Let one shot breathe** at the emotional turn.
- **Add a title card and credits** inside the 90 seconds, and count them.
- **Listen on headphones and on a speaker**, because cinema sound is unforgiving. Voice should be clear and music must never fight it.
