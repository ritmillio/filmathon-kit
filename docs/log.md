# Project log

Newest entries at the bottom. Times are CET on Nov 5, 2026. Each entry says what was decided or changed, and what was verified.

## Where things stand (update this block)

- **Film:** "A Life in One Room", 60 s, 15 shots (`docs/shotlist.md`).
- **Deadline:** submit by 22:30 (aim 22:15). Working export by 21:45.
- **Done:** story, design rules, sound plan and cue sheet, room layout sketch, shot list, a code-rendered 6-second animatic (timing only).
- **Not done:** ElevenLabs connection check, stills, clips, sound generation, the edit.
- **Open questions:** see the list at the bottom.

## Log

### ~17:30-19:00 · Story and sound decided (before this repo)
- Chosen story: **A Life in One Room**. One fixed room, no people, a life from birth to death told by living objects. The loop ending: a heartbeat stops, one second of silence, a faster heartbeat begins.
- Sound idea: **60 BPM**, one beat a second. Music-box motif that grows up and grows old. Silence at 22-27 s and 56.3-57.3 s.
- Sound tools: ElevenLabs SFX v3 and Eleven Music v2.5. About 24,000 credits planned (4% of the 600,000). The per-generation sound-effect rate was not confirmed; one test generation is needed.

### ~19:05 · Room layout from the designer's sketch
- `assets/sketches/room_layout_sketch.jpg`: one-point perspective, four-pane window on the back wall, plank floor, striped rug. This replaces the earlier flat side-on layout.
- Mapping: the window sill is `shelf_low`, the rug is the `bed` slot.

### ~19:08 · First 6 seconds, as a code-rendered test
- `preview/first6.py` renders the Birth stage on the sketch layout (24 fps on twos, 1920x1080). `preview/scratch_audio.py` makes a placeholder soundtrack.
- **Verified:** looked at key frames from every beat. Not watched in real time by the assistant.
- **This is an animatic only and is not eligible for the film.** The final visuals must be AI-generated.

### ~19:10 · Teddy Bear replaces the Toy Bird
- The team edited `STORY.md`: the first object is now a **Teddy Bear** (button eyes), set on the shelf at 3.7 s "with a soft plop".
- Updated `DESIGN.md`, `SOUND.md` and `audio/sound_cues.csv`. New effect `plush_plop.wav` (31 effects in total).

### ~19:13 · RULES CORRECTION (important)
- Read the official kit (`README.md`, `docs/`). **Visuals must be 100% AI-generated, and image, video, audio and music must come only from the ElevenLabs Pro package** to be prize-eligible. Team rule: ElevenLabs is the only generation tool.
- `DESIGN.md` previously said the brief rules out AI video. **That was wrong** (it was copied from the style board). Corrected.
- Consequence: the sketch-to-image-to-video pipeline is right, and the code-rendered approach is only an animatic.
- Consequence: the room cannot be locked pixel-exactly. The sketch overlay check (`scripts/overlay_check.py`) and cutting between room states replace the earlier code-based lock.

### ~19:15 · Shot list drafted
- `docs/shotlist.md`: 15 shots, 3-6 s each, each a different state of the same room. The change is made by cutting, not by AI morphing. Sound leads picture at the first cut.

### ~19:20 · Reference rule for Disney (or any studio) material
- The team plans to build the design around Disney examples from a Figma file.
- The kit excludes real brands and characters. Added a rule to `DESIGN.md`: take the **craft** (colour, line, shape language, staging, animation principles) in our own words, never the **content** (characters, props, logos, titles, frames). No studio names in prompts. No upload of their frames as references.
- Not yet received: the Figma file.

### ~19:22 · Repo set up for regular pushes
- Added `CLAUDE.md` (standing rules, including push regularly and log everything), `scripts/save.sh` (commit and push with a secret and size check) and this log.
- The team's local `.gitignore` change (`/.env.local`, written by `elevenlabs onboard`) was included.

### ~19:30 · First push to `main`
- Pushed commit `206d516` to the private repo `ritmillio/filmathon-kit` (no branches, straight to `main`, as the team asked). Verified on GitHub: the new files are there, and no `.env`, `.mcp.json`, media or key files are in the tree.
- A bug in `scripts/save.sh` made the first run exit silently without committing (a size check returned a false status under `set -e`). Fixed, then pushed.
- From now on: `scripts/save.sh "message"` after every meaningful change, plus a dated entry in this log.

### ~19:45 · Assets folder, the designer's item sketches, and the Figma reference structure
- Added `assets/items/` (seven item sketches, cropped square on white), `assets/sketches/items_original/`, `assets/sketches/contact_sheet.png`, the registry `assets/items.md`, and `assets/README.md`.
- The sketches add things the story did not have. Updated `STORY.md`, `DESIGN.md`, `docs/shotlist.md` and `SOUND.md` to match: a **worn, stitched bear** next to the clean bear (read as the same bear, new and old), **one tall floor lamp with a pull chain** instead of three lamps, and **four things with faces** (Bear, Lamp, Mug, Cushion). Also an armchair and a round side table (replaces the nightstand). These are marked **proposed** in `assets/items.md` and need the team's yes.
- Figma structure: `assets/references/figma/` with a README (how to add a board), an index, and a per-board template. Third-party exports are not committed (`assets/references/.gitignore`).
- The kit's own docs and the style board were reworded so that no other generation tool is named. **Team rule recorded in `CLAUDE.md`, `DESIGN.md` and `README.md`: ElevenLabs is the only generation tool.** Earlier commits in git history still contain the old wording; history was not rewritten.

### ~19:46 · ElevenLabs connected
- The key saved by `elevenlabs onboard` in `.env.local` was verified against ElevenLabs: plan **Pro, active**, 0 of 610,000 credits used.
- Created `.mcp.json` (git-ignored, mode 600) from the kit's example, using that key. It loads when Claude Code is restarted in this folder and the project server is approved.
- **Not yet checked:** whether the MCP exposes image and video generation, or only audio.

### ~19:47 · Skills search
- A background search for filmmaking agent skills is running. Candidates will be vetted (read, licence, security notes) before anything is added to the repo.

## Open questions

1. **ElevenLabs:** key verified (Pro, 610,000 credits). After a restart, does the MCP expose image and video, or only audio? If not, generate stills and clips in the web app.
2. **The door.** The sketch has none. The shot list treats it as off-frame right.
3. **The "high shelf"** for the Bear in S3/S4. The sketch only has the sill.
4. **Team name** for the file name `teamname_filmtitle.mp4`.
5. **Disney Figma file:** to be sent. Convert to our own style notes only.
6. **Credits:** what do image and video generations cost on the Pro package? Check the balance every 30 minutes.
7. **The Vercel pages** (`change-film-plan.vercel.app`) describe the earlier code-rendered plan. These Markdown files are now the source of truth.
