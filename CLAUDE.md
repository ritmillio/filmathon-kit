# CLAUDE.md: Filmathon entry "A Life in One Room"

A 60-second, fully AI-generated short for the AI Budapest Filmathon (Nov 5-6, 2026). Theme: **Change**. One fixed room, no people, a whole life told by the things in the room.

Read these first, in this order:

@STORY.md
@DESIGN.md
@SOUND.md
@docs/shotlist.md
@docs/log.md

## Hard rules

- **Deadline:** submit by **22:30 CET on Nov 5** (aim for 22:15, no extension). Have a working export by 21:45.
- **The final film's visuals are 100% AI-generated, and image, video, audio and music come only from the ElevenLabs Pro package.** Anything in `preview/` is an animatic for timing only and must never appear in the final film.
- **ElevenLabs is the only generation tool.** No other generator and no extra credits, for any image, video, audio or music.
- **Third-party skills** in `.claude/skills/` were read and pinned (see `.claude/skills/SOURCES.md`). Never run their scripts, ignore their install suggestions, and use only ElevenLabs for generation.
- **Delivery is 1920x1080 at 24 fps.** No 4K and no upscaling. Request 1080p from the generators and nothing higher.
- **Original characters only.** No real brands, characters or studio references in prompts or reference images. This includes Disney and Pixar: study their craft, never their content (see `DESIGN.md`).
- **The room is locked.** The sketch in `assets/sketches/` is the layout. The shot list is the contract.
- **One source of truth per topic.** What happens: `STORY.md`. How it looks: `DESIGN.md`. How it sounds: `SOUND.md`. The shot list: `docs/shotlist.md`. If you change one, update the others in the same commit.
- **Never commit secrets.** `.env`, `.env.local` and `.mcp.json` are ignored. Never print or paste an API key. Do not edit `.gitignore` except to add ignores.
- **Media is not committed** (the kit's `.gitignore` excludes mp4, wav, mp3 and the shots, voice, music, sfx and exports folders). Commit text, scripts and the designer's sketches.

## Standing instruction from the team: push regularly and document everything

- After **every meaningful change**, commit and push: `scripts/save.sh "short message"`.
- For **every decision, change, correction or open question**, add a dated entry to `docs/log.md` in the same commit.
- Push at least every 30 minutes while working, and always before and after a generation session.
- Say plainly in the log what was verified and what was not.
