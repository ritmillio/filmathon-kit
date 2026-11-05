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

### ~20:00 · Skills vetted and added; ElevenLabs image and video confirmed
- A background search found ten skill candidates. Its report was based on summaries, so we fetched the raw files at pinned commits and read them ourselves.
- **Added** to `.claude/skills/`: `shot-list`, `color-script`, `scene-breakdown`, `cut-list` (MIT, text only) and `elevenlabs` (MIT; SKILL.md and references only). Sources, commits and rules are in `.claude/skills/SOURCES.md`. Scripts and agent config were not copied.
- **Not added:** `shot-planning` (its footage route breaks our rules), and two skills with no licence (reading only).
- **Confirmed against ElevenLabs' live API spec:** image and video generation exist (`/v1/flows/image`, `/v1/flows/video`) with several hosted models and a start-frame option. Written up in `docs/elevenlabs-generation.md`. This answers the earlier open question about image and video.
- **Not yet tested:** our key's Flows permission, credit cost per generation, and which model holds the room best. First test is described in that file.

### ~20:10 · ElevenLabs MCP status, and the resolution rule
- **MCP status:** configured in `.mcp.json` (git-ignored) with the verified key, and `claude mcp list` shows it as **Pending approval**. Nothing has been called through it yet. To activate: run `claude` in `~/Developer/filmathon-kit`, approve the project server, then check `/mcp`. The server package was downloaded once to warm the cache.
- **Resolution rule (team decision):** deliver **1920x1080 at 24 fps**, no 4K, no upscaling. Written into `DESIGN.md`, `CLAUDE.md` and `docs/elevenlabs-generation.md`. The kit recommends 1920x1080 (minimum 1280x720) and says 4K upscaling is not worth it. It does not state a hard maximum, so this is our rule, not a quoted competition limit.

### ~20:20 · First Figma board received: characters
- File `characters figma.svg` (a 485 x 485 board with five embedded images). Checked first: no scripts, no external links. Stored in `assets/references/figma/boards/characters/exports/` (**not committed**: third-party images). The five images were extracted to `char_01.png` to `char_05.png`.
- The board shows five classic feature-animation characters that are living household objects. Notes written in our own words with no names (`assets/references/figma/boards/characters/notes.md`), index rows R01 to R05.
- **Most useful for us:** R04, life without a face through posture, which is our own rule. Also: faces sit in the object's form, limbs are the object's own parts, relationships between objects.
- **Risk noted:** our idea (living household objects) is close to these characters. Added distance rules to the notes: keep our two-dot faces, no lashes or eyebrows, no hands or costumes, our own palette and scribbly outline, mostly passive objects, and never use these images as generator references.
- Nothing from this board has reached a prompt yet. Qualities become part of the STYLE line only after the team approves them.

### ~20:30 · Character notes compiled; ElevenLabs status re-checked
- **`docs/characters.md`** (continuity bible) compiled by the assistant from the story, design rules, item registry and sketches: one block per character with look, acting, key moments, sound and a **prompt block** to paste verbatim into every prompt. Five questions for the team are at the bottom. Draft, needs approval.
- **ElevenLabs status:** key verified (Pro, active, 0 of 610,000 credits). The key can reach the image and video generation endpoints (list calls returned HTTP 200, no credits used). The MCP is still **Pending approval** until `claude` is run in this folder and the server is approved.

## Open questions

1. **ElevenLabs:** key verified (Pro, 610,000 credits). Image and video exist in the API (see `docs/elevenlabs-generation.md`). After a restart, does the MCP expose them? If not, call the API or use the web app.
2. **The door.** The sketch has none. The shot list treats it as off-frame right.
3. **The "high shelf"** for the Bear in S3/S4. The sketch only has the sill.
4. **Team name** for the file name `teamname_filmtitle.mp4`.
5. **Disney Figma file:** to be sent. Convert to our own style notes only.
6. **Credits:** what do image and video generations cost on the Pro package? Check the balance every 30 minutes.
7. **The Vercel pages** (`change-film-plan.vercel.app`) describe the earlier code-rendered plan. These Markdown files are now the source of truth.

### ~20:50 · First 6 seconds generated with ElevenLabs (sketch -> still -> clip)
- **Seedance 2.5 is not usable:** the API returns `model_access_denied` ("ByteDance models are disabled by default and require explicit approval"). Seedream is the same. Used **Veo 3.1 Fast** (`veo-3.1-fast-generate-001`), hosted inside ElevenLabs, 1080p, 4 s, native audio off. Veo cannot turn prompt enhancement off.
- **G1 base room still:** `gemini-3-pro-image`, 2K, sketch as reference. Window, sill, back-wall line and rug within about 2% of the sketch. Approved.
- **Shot 1 clip:** room locked, moonlight shimmers, dust drifts. Passed.
- **Shot 2 still:** first try failed (zoomed, lamp and bear kept raw black marker lines). Fixed by saying "same painted style, no black outlines, identical framing" and giving the base still first. Variant B approved.
- **Shot 2 clip:** layout locked, lamp blinks well; **the mobile drifted** off the cradle in front of the window. Known issue.
- **Cost:** about 4,250 credits after the still and the first clip (0.7% of 610,000). Shot 2 still and clip not yet measured.
- Cut file: `exports/first6_ai_silent.mp4` (3 s + 3 s, hard cut, no sound yet). `scripts/el_gen.py` is the generation client.
- **Audio references** (four Disney tracks) saved locally in `assets/references/audio/` (not committed).

### ~21:05 · Free 60 s animatic (no credits)
- Team plan: lock timing first without credits, then spend ElevenLabs credits on the final shots. (Clarified: the rule is ElevenLabs-only, not "spend all 600K".)
- `preview/animatic.py` builds `exports/animatic_60s_placeholder.mp4`: 15 shot cards (from `docs/shotlist.md`) over the base room, with the 84-cue placeholder sound mix (beeps and noise, not real sound). Exactly 60.000 s. **Timing only; never in the final film.** Verified: duration, one frame checked. Not watched in real time.
