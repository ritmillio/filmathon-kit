# 03 · Script and shot list

A 60-second AI film is roughly **10–14 shots of 3–6 seconds**. AI video clips tend to degrade after 5 seconds, so plan for short shots.

## Start from the judging criteria

Five things are judged: **story, visual world, film language, sound, AI use.** One idea that touches all five beats five ideas that touch one.

## The one-sentence test

Write: *"A [character] wants [thing] but [obstacle], and ends up [change]."*
If you cannot say it in one sentence, it is too big for 60 seconds.

## Structure for 60 seconds

| Seconds | Beat | Shots |
|---|---|---|
| 0–8 | Hook: an image or sound that makes us lean in | 2 |
| 8–25 | Set up the world and the want | 3–4 |
| 25–45 | Complication | 3–4 |
| 45–55 | Turn / payoff | 2 |
| 55–60 | Title card or last image | 1 |

## Use the template

Copy `templates/shotlist.md` to `docs/shotlist.md` and fill it in. Each row is one file you must generate, so the shot list is also your checklist.

## Make it makeable

- **One look.** Pick a single visual style sentence and paste it into every prompt. Consistency reads as "visual world".
- **Few characters, no talking faces.** Lip-sync across AI shots is the hardest thing to keep consistent. Voice-over avoids it entirely.
- **Sound carries the story.** Narration + music + two or three well-placed sfx make cheap visuals feel intentional.
- **Avoid text in shots.** AI text is often garbled. Add titles in the edit instead.
- **Stay non-political and non-infringing.** The rules exclude those films, so no real brands, characters or politics.

## Ask the agent

Good prompt for Claude Code:

> The theme is "X". Give me 5 one-sentence film ideas for a 60-second fully AI-generated film, each with a visual style line and why it suits AI generation. Then expand the one I pick into a shot list in `templates/shotlist.md` format.
