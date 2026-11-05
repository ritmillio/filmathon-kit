# DESIGN.md: design rules for "A Life in One Room"

Read with `STORY.md` (what happens) and `SOUND.md` (how it sounds). The visual reference is `style-board.html` ("Night Plate"), a study of the look of 1940s-50s European feature animation. We copy the *technique and mood*, never characters, designs or marks from any existing film. **Original characters only.**

## Rules (from the AI Budapest Filmathon kit; the official event page wins)

- **Length** 30-90 s. Our film is exactly 60 s including the end card.
- **Visuals are 100% AI-generated.** No camera footage, no stock. Code-drawn or hand-drawn frames are **not** a substitute in the final film. Our sketches are references that the AI generates from.
- **Image, video, audio and music only from the ElevenLabs Pro package** to be prize-eligible.
- **Team rule: ElevenLabs is the only generation tool on this project.** No other generator, no extra credits.
- **File:** MP4, 16:9, 24 fps, 1920x1080 recommended (1280x720 minimum), audio in the file, named `teamname_filmtitle.mp4` (lowercase letters and digits).
- **Team rule on resolution: we deliver 1920x1080 at 24 fps. No 4K, and no upscaling to 4K.** Ask the generators for 1080p and nothing higher. (The kit's own advice is the same: upscaling is not worth the time or credits.)
- **Time:** submission 22:30 sharp (aim for 22:15). Working export by 21:45.
- **Judged on:** story, visual world, film language, sound, AI use.
- No real brands, characters or politics. Avoid text in shots (AI text garbles).

**Correction:** an earlier version of this file, copied from the style board, said the brief rules out AI video generation. That was wrong. AI generation is required, and it comes from ElevenLabs only.

`preview/first6.mp4` was rendered with code. It is an animatic for timing and mood only. **It must not appear in the final film.**

## Style DNA

- **Flat cel colour.** One fill per shape, almost no shading.
- **Tinted outlines.** A thin, slightly irregular line in a *darker tint of each fill* (brown on gold, navy on a blue). Never pure black. In code: stroke = fill darkened 45%, 1-2 px jitter re-seeded every drawing.
- **Painted plates.** The room and sky are painted-looking: broad visible brush streaks, paper grain, vignette. The ground is textured while the characters stay flat.
- **Caricature.** Dot eyes and a small smile on the Lamp, the Mug and the Cushion, button eyes on the Teddy Bear, chunky bodies, thin legs. French bande dessinee, not anime, not 3D.
- **Warm against cold.** Ultramarine and navy night, snow whites, one gold light.
- **Theatre staging.** Locked camera, long shot, small figures in a big space. Emotion comes from posture.
- **Frame rate.** 24 fps held on twos (12 unique drawings a second). Re-jitter outlines on every drawing ("line boil").

## Using references (Disney or any studio): learn the craft, never copy the content

The Filmathon rules exclude real brands and characters, and `DESIGN.md` already says original characters only. A Figma board of Disney examples is fine **as study material**, if we take the technique and leave the content.

**Take (abstract, and ours to reuse):**
- colour relationships: how warm light sits against cool shadow, how many colours per scene
- line quality: weight, taper, tinted outlines
- shape language: round and soft vs sharp, big heads and eyes, simple silhouettes
- staging: clear silhouettes, one focus per frame, a readable pose
- animation principles: squash and stretch, anticipation, follow-through, overlapping action
- lighting mood and painted-background texture

**Do not:**
- use any Disney (or Pixar, or other studio) **character, costume, prop, logo, title or recognisable scene**
- write "Disney", "Pixar", a film title or a character name into any prompt
- upload their frames as reference images to the generator (it will produce close copies)
- trace or redraw a recognisable design

**Where it goes:** `assets/references/figma/` (see its README). Exports of third-party frames stay on the machine and are never committed.

**How to use the Figma file:** for each example, write one line of what we take from it (for example "warm lamp glow against blue night" or "round, soft furniture shapes") and add it to this file in our own words. Prompts then describe the *qualities* ("soft rounded shapes, warm rim light, painted background"), never the source.

Our own characters stay: the Teddy Bear, the Lamp, the Bed, the Door, the Window.

## Palette (matched by eye from the board; tokens, not suggestions)

| Token | Hex | Use |
|---|---|---|
| night navy | `#0f1d44` | sky top, shadows |
| ultramarine | `#2a4a8f` | sky mid, brush body |
| snow blue | `#a9c1e6` | horizon, drifts |
| frost white | `#dce8f8` | snow highlights |
| star gold | `#e0a42b` | the one warm light |
| lamp amber | `#f3c98b` | window glow, bokeh |
| line brown | `#6b3f17` | tinted outlines |
| wood | `#c58a45` | Teddy Bear fur, furniture |

Do not introduce other hues. Stage looks are made by grading and by how much warm light there is.

## Light is life

One cold night plate for the whole film. Only the sky and the warm light change, stage by stage.

| Stage | Window and sky | Warm light |
|---|---|---|
| S1 Birth | cold night, small window | one small lamp |
| S2 Childhood | dusk with string-light bokeh | medium, playful |
| S3 Teens | ultramarine, blue rain | dim, a desk lamp |
| S4 Away | empty, cold snow, pale | almost none |
| S5 Family | warm amber evening | the biggest |
| S6 Quiet years | autumn dusk, soft | medium, steady |
| S7 Old age | pale blue dawn | small, trembling |
| S8 End | white, then quiet | out, then new gold from the door |

## Layout v2: the designer's room sketch (supersedes the slot table below where they differ)

Source: `assets/sketches/room_layout_sketch.jpg`. A one-point perspective room, locked camera, looking at the back wall.

| Part | Where (1920 x 1080) | Notes |
|---|---|---|
| back wall | x 515-1410, down to the base line at y about 714 | |
| side walls | left and right, meeting the floor along diagonals to the frame corners | |
| floor | planks fanning from a vanishing point near (960, 380) | |
| window | four panes. Frame x 566-1360. Cross rail at y about 270. Glass runs off the top of the frame. | the one big fixed element |
| window sill | x 557-1378, y 490-538 | **this is `shelf_low`**: the Teddy Bear sits here |
| rug | quad (640,835) (1245,830) (1370,992) (472,1003), vertical stripes | **this is the `bed` slot** (cradle, crib, beds stand on it) |
| warm light patches | four vertical shapes on the rug, from the sketch's orange | the first warm light of the film |

Open layout questions (the team must decide, then `locked/layout.json` is frozen):
1. **The door.** The sketch has none. The test render treats it as off-frame to the right: warm light spills in from the right edge. Keep that, or draw a door on a side wall?
2. **`shelf_high`.** STORY.md moves the Bear to a "high shelf" at 20.2 s. The sketch has only the window sill. Add a small wall shelf to the sketch, or move the Bear along the sill?
3. **Height marks** need a door frame. If the door is off-frame, put the marks on a wall edge or the window frame instead.
4. **`floor_1` to `floor_6`** keep their meaning but now sit on the perspective floor. The Lamp stands at the front left (about x 350, y 985).

First test render: `preview/first6.mp4` (0-6 s, Birth), built from this sketch.

## The locked room (the most important rule)

The room is fixed. Canvas 1920 x 1080, locked camera. Values below are approximate; the final numbers live in `locked/layout.json`.

| Slot | Position (x, y at the base) | Notes |
|---|---|---|
| floor line | y = 800 | where wall meets floor |
| window | rect (140,130)-(520,580) | fixed, left wall. Outside view is a separate layer behind it. |
| door | rect (1370,160)-(1630,800) | fixed, right wall |
| bed | centre (900, 880) | the one big slot. All bed forms stand on this baseline and footprint. |
| shelf_low | (820-1000, y 330) | fixed |
| shelf_high | (1100-1260, y 220) | fixed |
| floor_1 | (560, 900) | bedside, lamp side |
| floor_2 | (1250, 900) | armchair spot |
| floor_3 to floor_6 | (420,960) (700,980) (1100,980) (1450,940) | toys, boxes, plants, desk, cane. floor_6 is by the door. |
| wall_1 to wall_4 | (640,250) (880,160) (1100,380) (1250,200) | pictures, posters, frames |

**Locked, never changes:** window, door, shelves, floor line, bed slot position, camera, canvas, style rules.
**May change:** wallpaper, light, weather, sky, colour grade, and the items listed in the continuity ledger in `STORY.md`.

### How the lock is enforced
- The sketch is the layout. Every still must pass `scripts/overlay_check.py` against it.
- Items are placed by **slot name** ("bed", "shelf_low") in the shot list, never by a free description.
- Once approved, the base-room still is never regenerated.


## Items

### The designer's sketches (in `assets/items/`, tracked in `assets/items.md`)

| Item | File | Notes |
|---|---|---|
| Teddy Bear, new | `bear_new.png` | clean, button eyes |
| Teddy Bear, worn | `bear_worn.png` | stitched head, patched belly: the same bear, old |
| Floor lamp | `lamp_floor.png` | tall pole, trapezoid shade, pull chain, smiling face |
| Armchair | `armchair.png` | high back, front view |
| Side table | `side_table.png` | round top, curly legs ending in ball feet |
| Mug | `mug.png` | smiling, one handle |
| Cushion | `cushion.png` | sleepy face, four corner tassels |

**Still to sketch** (needed by the shot list): the bed forms (cradle with hood, crib, single bed, double bed, and the overlays blanket and rails) and the mobile. Everything else (door light, tree, wallpaper, posters, frames, plants, boxes, cane, toys) is generated from the style line.

### Made in code or from images (everything else)
Wall, floor, wallpapers (animals, teen, floral), window frame, door frame, shelves, height marks, props (blocks, ball, mobile, boxes, posters, frames, wedding picture, plants, nightstand, glass, pills, cane, desk, guitar, wall clock), eyes for the Lamp, light, weather, dust, bokeh.

### Not made
People. Hand-painted backgrounds per decade. A new room per stage. Animation in-betweens. Any text in the picture.

## The pipeline: sketch, image, video

1. **Sketch** (designer): the base room (`assets/sketches/room_layout_sketch.jpg`) and each item.
2. **Image** (ElevenLabs): generate one still per shot from the style line, the base-room reference and the shot's state. Approve the still before animating it.
3. **Video** (ElevenLabs): animate the approved still, image-to-video, 3-5 seconds, locked camera, one small motion, native clip audio off.
4. **Edit**: `scripts/rough_cut.py film.json` joins the clips and lays the sound. Hard cuts, landed on sound.

**The change is made by cutting, not by AI morphing.** Each shot is a different state of the same room (see the continuity ledger in `STORY.md`). The AI only has to hold one state for a few seconds and move one small thing. That is far more reliable than asking it to transform a room.

### Approval gates
- **G1** base look: one approved still of the empty room from the sketch. Every later still uses it as the reference.
- **G2** reference images for the Teddy Bear and the Lamp (the two characters with faces). Every shot with them reuses these.
- **G3** each shot's still is approved before it is animated.
- **G4** each clip passes the checks below, or is cut shorter, or is re-generated once.

### Keeping the room the same (AI cannot guarantee a pixel-exact room)
- Put the **base-room image and the style line, word for word,** into every still prompt: "the same room as the reference".
- Say what must **not** change: the window, the sill, the rug, the floor and the back-wall lines.
- Run `python3 scripts/overlay_check.py <image>` on every still. It lays your sketch over the image at 50% so you can see at once whether the window, rug or floor moved. Reject a still where they moved.
- Cut a shot **before** it drifts (usually after 3-4 s).

### Folder layout
```
assets/sketches/            designer sketches, incl. room_layout_sketch.jpg
shots/s01.mp4 ... s15.mp4   approved clips (kit convention; alternates as s01_b.mp4)
stills/                     approved stills, one per shot (not committed)
voice/ music/ sfx/          generated audio (not committed)
docs/shotlist.md            the 15-shot list with prompts
film.json                   edit list for scripts/rough_cut.py (not committed)
```

## Prompt templates

Always begin an image or video prompt with the **style prefix**:

> Flat 2D cel animation in the style of 1940s-50s European feature animation. Flat colours, one fill per shape, almost no shading. Thin slightly irregular warm-brown outline, a darker tint of each fill, never black. Painted background with broad brush streaks and paper grain. Palette only: night navy, ultramarine, snow blue, frost white, star gold, lamp amber, line brown, wood. Locked camera, theatre staging. Original design.

**Negative list** (append to every prompt): `people, hands, faces (except the Teddy Bear, the Lamp, the Mug and the Cushion), text, letters, logos, watermark, 3D render, CGI, glossy plastic, anime, photoreal lighting, lens flare, pure black outlines, camera movement, existing film characters, extra furniture`.

Item image: `<style prefix> Use the attached sketch as the exact shape and proportion. Subject: <item>. Plain flat pure-magenta #FF00FF background, no shadow, no floor. <negative list>`

Clip: `<style prefix> Start from the attached image. Locked camera, no camera movement. Only the <item> moves: <one clear action, one second>. Everything else stays still. Plain flat pure-magenta #FF00FF background. <negative list>`

## Acceptance checks for any generated image or clip

- [ ] Window, sill, rug and floor match the sketch in the overlay check.
- [ ] Only items in the continuity ledger for that stage appear.
- [ ] Palette tokens only. Outlines are brown, not black.
- [ ] No people, text or logos. Faces only on the Teddy Bear (buttons), the Lamp, the Mug and the Cushion.
- [ ] Locked camera, no drift or zoom.
- [ ] Same proportions as the approved item image.

## Tooling note: ElevenLabs

- Setup (from the kit): API key from your ElevenLabs profile in `.env`, then `claude mcp add elevenlabs -e ELEVENLABS_API_KEY=... -e ELEVENLABS_MCP_OUTPUT_MODE=files -- uvx elevenlabs-mcp`. Never paste the key into chat.
- The MCP server covers **audio** (speech, sound effects, music). Whether it also exposes **image and video** generation must be checked on the day. If it does not, generate stills and clips in the ElevenLabs web app and save them into `stills/` and `shots/`. ElevenLabs also exposes image and video generation through its API (Flows). See `docs/elevenlabs-generation.md`. The rule requires all generation to come from the Pro package either way.

## Forbidden

People or the shadow of a person. Text. Black outlines. 3D, photoreal or anime looks. Camera moves. Changing the room. Adding items not in the ledger. Regenerating an approved asset.
