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

### ~21:30 · Real sound generated (replaces placeholder beeps)
- Team feedback: placeholder sound is garbage; build it like classic hand-drawn animated-feature scores.
- Measured the four reference tracks (loudness, brightness, dynamics; the tempo estimate was unreliable and is ignored). The favourite (A04) is the darkest and opens quietest, then grows. No audio was listened to by the assistant.
- Music: `music_v2_5` with a stage-by-stage composition plan (`audio/music_plan.json`, `scripts/el_music.py`). Take 1 kept, take 2 rejected (flat arc). Final note generated separately.
- Effects: 31 files via SFX v3 (`scripts/el_sfx.py`), one take each. **Not yet listened to by a person.**
- Mix: `mix_real.wav`, 84 cues, 60.000 s, silence at 56.5-57.2 s is digital silence. Video: `exports/animatic_60s_real_sound.mp4` (cards + real sound).
- Credits: balance 18,855 -> 19,825 after two music takes, the note and 32 effects. This is much cheaper than planned, but the counter may lag. Re-check.
- Open: first listen by the team; per-effect retakes; add accents on each pop (cue sheet); try video-to-music on real clips.

### ~21:45 · Team character notes split into per-character files
- The team sent `karakterek.md` (Hungarian: Lamp, Bear, Mug). Kept unchanged as `docs/characters/_source_karakterek_hu.md`. Created one English file per character in `docs/characters/` with an index and the team's five headings; added the gaps (a life-long arc for each, shots, prompt blocks, sound and a musical voice per character) and the characters the notes did not cover (Cushion, Armchair, Side Table, Bed, Door and Window). *(added)* parts are proposals.
- **New facts from the team that change earlier assumptions:** the Lamp hops on one leg and walks around (earlier: stationary, "heart of the room"); the Bear climbs and sits on the armchair (earlier: carried only, the armchair appears at 28 s); the Mug grooves constantly with coffee sloshing (earlier: a quiet side-table presence).
- **Not yet applied:** `STORY.md`, `docs/shotlist.md` and the music plan still use the earlier behaviour. Four open decisions are listed in `docs/characters/README.md`. Change the story files only after the team answers.

### ~22:05 · First 6 seconds with Veo 3.1 and real sound
- Models: ElevenLabs hosts only Veo 3.1 (standard and Fast) as usable video models; Seedance (2.0, Fast, Mini, 2.5) returns `model_access_denied` for our key (checked all four). Creatify Aurora is for talking avatars, not for us.
- **Shot 1** (0-3 s): the Fast clip `shots/s01_raw.mp4` is clean (room locked, moonlight shimmers, dust). The **standard** Veo 3.1 run (`shots/s01_veo_std.mp4`) is **rejected**: the moonlight streaks became huge glowing squiggles streaming from the window. Lesson: the standard model overreads "shimmer"; use calmer wording ("the pale streaks slowly brighten").
- **Shot 2** (3-6 s): standard Veo 3.1 `shots/s02_veo_std.mp4` approved: the mobile stays above the cradle, the lamp blinks, the room holds.
- **Cut:** `exports/first6_veo31_with_sound.mp4`, 1920x1080, 24 fps, 6.000 s, with the first 6 s of the real mix (placeholder gone). Not yet reviewed by a person in real time.
- **Credits:** balance 32,781 of 610,000 after the standard shot 1 run and the shot 2 clip. A standard 1080p 4 s clip costs about 4,800.

### 20:10 · Redo of the first 6 s: why v1 failed, and v2 (continuous, on-style)
- **Time correction:** the real clock at this point is about 20:00 CET. Earlier log times ("21:30", "22:05") were the assistant's estimates and were wrong. Deadline 22:30 stands.
- **Why v1 failed (team feedback):** a visible cut between the two clips; characters lifeless; style far from `DESIGN.md`. **Causes found:** (1) the stills used a shorter style line than the DESIGN prefix, with no "palette only" and no ban on gradients, so they came out glossy with glow, bloom, purple and pink; (2) clips used "one small motion", which reads as dead; (3) two separate clips joined by a hard cut, per the old "change by cutting" rule.
- **Decision (team):** for the opening, the change happens **inside one continuous clip**. The old rule "change by cutting, one small motion" is relaxed for S1. Other stages to be decided after this test.
- **v2 method:** full DESIGN style prefix word for word plus "no gradients, no glow, no bloom, no purple, no pink"; stills `stills/g1v2.jpg` (base room, approved) and `stills/s2v2.jpg` (end state, approved), 1K; one Veo 3.1 clip, **start frame + end frame**, 6 s, with a timed acting script from the character files (squash and stretch, anticipation, hop). Post: held on twos (12 fps to 24) as `DESIGN.md` requires.
- **Result (Fast model test):** much closer to the design (flat, in palette). Characters now act: the lamp hops, the cradle pops in, the bear drops onto the sill. Problems: the "door light" became a big amber slab, the cradle morphs messily when it first appears (about 2-3 s), the bear flops over mid-clip, the lamp grew thin spring legs. `shots/first6_fast.mp4`, cut `exports/first6_v2_continuous_fast.mp4` with the real sound mix.
- **Credits:** counter 41,289 of 610,000 after two stills and one 6 s Fast clip (the counter lags; costs per item not measured).
- **Open:** the team's "extended story line" message arrived with no file attached; waiting for the path.

### 20:25 · Expanded storyboard received
- Team file `expanded_storyboard.md` saved unchanged as `docs/storyboard_expanded.md`. `docs/storyboard_reconciliation.md` lists what it adds and nine conflicts with the older files. Biggest: the Bird (we use the Teddy Bear), camera moves (our rule is locked), the ending (click-and-darkness vs the loop), and Scene 1 (the Lamp waking in the dark, no cradle).
- Nothing in `STORY.md`, the shot list or the sound plan was changed yet. Waiting for the team's decisions.

### 20:40 · Style v3 (Disney-craft) replaces the flat look; sound paused
- Team feedback: sound is garbage and the reference tracks were not used; characters too close to the sketches; the look must follow the Figma references (feature-animation craft, "somewhat realistic but fluid"). **Sound is paused**: silent tests only; the team will do sound later (the assistant cannot listen to audio and only measured loudness of the reference tracks).
- Processed `room design figma.svg` (6 images, no scripts or links) and re-checked the character board. Findings in `docs/style_v3.md`: faces with eyebrows and open mouths, real arms and feet, appealing rounded shapes, varied-weight dark-brown ink, soft two-tone shading, rich painterly rooms with texture and one strong warm light. These replace "flat cel, almost no shading".
- Team: sketches are only for what each character is; redesign freely with the craft elements. Test sheet `stills/chars_v3.png` (Lamp, Bear, Mug), one 1K still, 3,045 credits (41,289 -> 44,334). Reads as the sketch idea with much more appeal. Not yet approved by the team.
- `DESIGN.md` Style DNA and `SOUND.md` marked superseded and paused with pointers. Credit costs measured: still about 3,000; Fast 6 s about 2,400; standard 4 s about 4,800.
- Open: team approval of the character look (button eyes on the Bear or soulful eyes?), curtains on the window (the references frame the window with cloth).

### 20:13 · Style v3 working: GPT image 2.5 inside ElevenLabs
- Team feedback: the first v3 test was "not close to Disney style"; generate images first; use GPT image 2.5, with a key from an AI gateway in another project. **Declined the outside key** (eligibility: only the ElevenLabs package counts; the assistant did not open the other project). GPT image 2.5 exists inside ElevenLabs (`gpt-image-2.5-flare`, `-sunburst`, `gpt-image-2`) and works with our key.
- Reviewed the character images at full size again: faces and arms are sculpted from the object itself; rendered gloss; ornament. Rewrote the prompt object-first.
- Results (silent, stills only): `stills/chars_v4.png` (Lamp, Bear, Mug), `stills/room_v4.jpg` (empty room on the sketch layout, curtains added), `stills/end_v4.jpg` (room with lamp, bear, cradle, warm light from the right). Much closer to the references. **Awaiting team approval.**
- Cost: character sheet about 920, room 2K about 520, end frame about 500. Balance 45770 of 610,000 used.
- Next (after approval): one Fast 6 s clip from `room_v4` to `end_v4` (start and end frame), then standard only if it passes. No sound.

### 20:17 · Clean-cel look found (v5); painterly v4 rejected
- Team feedback with two screenshots of the references: v4 was "really far from the Disney style". Re-analysed: the references are clean graphic cel animation (bold even outline, flat saturated fills, one hard shadow tone, white-oval eyes with pupils, big mouths, mitten hands), not painterly or textured.
- Rewrote the prompts accordingly (`docs/prompts/chars_v5.txt`, `room_v5.txt`, `end_v5.txt`) and generated with `gpt-image-2.5-sunburst` and `-flare` via ElevenLabs. Held the line of **not uploading the team's reference images** to the generator.
- Result: much closer. `stills/chars_v5_sunburst.png` chosen over the flare sheet; `room_v5.jpg` matches the sketch layout; `end_v5.jpg` has lamp, bear and cradle in one clean style with a lit-lamp glow. Awaiting team approval.
- Cost: about 3,100 credits for four stills (45,770 to 48,884; counter lags). No video made yet, no sound.
- Next after approval: one Fast 6 s clip from `room_v5` to `end_v5` (start and end frame), about 2,400 credits.

### 20:20 · Direction change: hand-made look, not studio style
- Team: "Forget the Disney style. Make it feel drawn by a man or a woman, original, not AI slop." Switched to a hand-drawn look based on the designer's own sketches. Two variants generated: A (gouache and pastel) and B (marker, crayon, torn paper, doodles). Both use the designer's sketches as references; prompts in `docs/prompts/hand_A.txt`, `hand_B.txt`. Documented in `docs/style_v3.md`.
- The clean-cel images (`chars_v5`, `room_v5`, `end_v5`) are set aside. Balance 51480 of 610,000.
- Awaiting the team's choice of A or B (or notes). Next: character sheet and room in the chosen look, then one Fast 6 s clip (start and end frame).

### 20:25 · Look B chosen; first 6 s made, silent
- Team: "Now we are getting it. Let's go with hand B... Do not put any sound under it." **Look B** (marker, crayon, torn paper) is the film's look. No sound on this cut or any test until the team does the sound.
- Start frame `stills/hand_B_empty.jpg` (edited from `hand_B`, same room, cold and empty, one still about 780 credits). End frame `stills/hand_B.jpg`.
- One continuous Veo 3.1 **Fast** clip, 6 s, start and end frame, no audio (`shots/first6_B_fast.mp4`, prompt `docs/prompts/clip_B_first6.txt`). Cut on twos (12 to 24 fps), 1920x1080, silent: `exports/first6_B_silent.mp4`.
- Result (checked from 8 frames, not yet watched in real time by the assistant): continuous, no cut; moonlight shimmers; an orange bar of door light slides in; the cradle tumbles in and settles; the bear appears on the sill; the lamp pops in on a springy coil, blinks, smiles and lights up with a yellow crayon glow. Crayon grain re-draws each frame. **Flaws:** the cradle first arrives tilted and fast; at the very end the bear tips forward on the sill; the lamp's legs are a coil (design drift from the sketch).
- Cost: balance 55549 of 610,000 used (about 3,200 for the empty still and the Fast clip, counter lags).

### 20:31 · First 6 s v2 in look B: continuity fixed
- Team feedback on the first B cut: "not bad", but the bed jumped into the centre and things appeared and vanished; wants the bed at the centre, the door not to disappear, and lights consistent. Drawings are "kind of okay".
- **Decisions:** nothing pops in, vanishes or teleports within a shot; the cradle stays at the centre of the rug from frame 1; the **door is a real object on the right wall** (closed, then open, always visible); the lamp turns on and stays lit; the bear stays seated. Recorded in `docs/storyboard_reconciliation.md`. This also settles the old "door off-frame" question.
- Method: both frames contain every object. `stills/B2_start.jpg` (cold, lamp asleep, door closed) edited from `hand_B`; `stills/B2_end.jpg` (door open, warm light, lamp lit) edited from the start frame. One Veo 3.1 Fast clip, 6 s, start and end frame, no audio, with a strict-continuity prompt (`docs/prompts/clip_B2.txt`). Cut on twos, silent: `exports/first6_B2_silent.mp4`.
- Result (8 frames checked): cradle fixed at centre, bear seated, door visible throughout and opening, lamp asleep to awake to hop to glow, glow stays. Minor: the lamp briefly shows thin coil legs while hopping; the door surface turns orange from the light.
- Cost: balance 60051 of 610,000 used (counter lags; about 4,000 for two stills and one Fast clip).
