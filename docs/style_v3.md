# Style v3: feature-animation craft (replaces "Night Plate" flat cel)

**Team decision, 2026-11-05:** the look must follow the Figma references (a classic hand-drawn feature-animation world with living household objects), "somewhat realistic but fluid". The flat, minimal "Night Plate" in `DESIGN.md` (Style DNA, palette-only, no shading) is **superseded by this file**. The room layout, the locked room, the cast and the story rules stay.
Sketches stay as references for **what** each character is. The **design** is ours to redo with these craft elements.

## What the references show (own words; no names, no frames reused)
Seen in `room design figma.svg` (6 images) and `characters figma.svg` / `.pdf` (5 images). Third-party; stored locally, never committed, never sent to a generator.

**Characters (living objects)**
- A face built into the object: big round eyes with a white glossy highlight, clear thick eyebrows, a wide expressive mouth that opens and closes.
- Real limbs that belong to the object: slender arms and hands made from its own parts, small feet. Gesture and acting come from the arms and the whole body bending in an S-curve.
- Rounded, chunky "appealing" shapes; simple strong silhouettes; asymmetry and a lean in every pose.
- Confident dark-brown ink outline with varied line weight; clean cel colour with soft two-tone shading and a warm rim light.
- Squash and stretch, anticipation, follow-through, overlapping action: a hop has a crouch, a stretch and a settle.

**Rooms**
- Dense, painterly detail: wood grain, stone, plaster texture, visible ink hatching, many small props.
- Patterned curtains and cloth framing the window. Cosy clutter.
- One strong warm light (a lamp, a fire, a lit window) against a cold blue night window. Warm and cold contrast is the main drama.
- Painted backgrounds are softer and more textured than the characters, which are cleaner and brighter so they read.

## Style prefix v3 (paste word for word; no studio or film names)
> Hand-drawn 2D feature animation in a classic storybook style. Rounded appealing shapes, squash and stretch, a confident dark-brown ink outline with varied line weight, clean cel colour with soft two-tone shading and a warm rim light, glossy eye highlights. The room is a rich painted background with visible brush and ink texture, wood grain, and one strong warm light against a cold navy night window. Palette: night navy, ultramarine, snow blue, cream, star gold, lamp amber, wood brown. Locked camera, theatre staging. Original characters and design.

**Negative v3:** `people, hands of a person, text, letters, logos, watermark, 3D render, CGI, glossy plastic, anime, photoreal, lens flare, pure black outlines, existing film characters, extra furniture, purple, pink` (purple and pink are not in the film's palette).

## Character design v3 (from the test sheet `stills/chars_v3.png`)
Faces and arms are now allowed on the **Lamp, Bear and Mug** (and Cushion). The Armchair and Side Table stay face-free for now (decision pending, `docs/characters/README.md`).
| Character | Design v3 |
|---|---|
| Lamp | trapezoid cream shade is the head; big glossy eyes, eyebrows, wide open smile; springy S-curve pole; one slender cord arm; round base as a foot; pull chain with beads swinging from the shade |
| Bear | big round head, large soulful eyes with highlights, brows tilted up sadly, soft muzzle, plump belly with a lighter patch, small paws; slumped, longing posture (worn version: stitched head, patched belly) |
| Mug | round face on the body, big eyes and brows, wide grin, the handle is one arm on its hip, small round feet, coffee sloshing at the rim, a curl of steam |
The three still read as the sketches' idea (tall lamp with a pull chain and trapezoid shade, a teddy, a mug with a handle) but with feature-animation appeal.

## Animation rules for every clip prompt
- One clear acting beat per character, described as: anticipation, action, follow-through (for example: "crouches, springs up on its base, the shade bobs and settles").
- Each character keeps its own tempo: Lamp quick and bouncy, Mug a swaying groove, Bear slow and small.
- Hold animation on twos (12 drawings a second) in post: `fps=12,fps=24`.
- Write the prompt as a timed script (what happens at 0 s, 1.2 s, 3 s...).

## Reference rule (unchanged, from `DESIGN.md`)
Take **craft**, never **content**: no studio or film names in prompts, no character, prop or frame from the references, no uploading their images to the generator. We describe qualities in words.

## Credit discipline (the team asked not to burn credits)
Measured today (balance counter lags a little): one 1K Gemini still about 3,000 (use GPT image 2.5 instead, see the update at the end: about 520-920); one 6 s Fast clip about 2,400; one 4 s standard clip about 4,800 (a 6 s standard clip about 7,000).
Process, in this order, and stop at any failed gate:
1. Style test on **one still** (done: characters).
2. Base room still in style v3, check against the sketch overlay.
3. End-state still with the new characters.
4. **One Fast 6 s clip** as the motion test. Only if it passes, one standard clip for the final.
Never run two paid generations in parallel on an unapproved look.

## Update 20:13: what actually works (tested)
- **Model for stills: `gpt-image-2.5-flare`** (the GPT image model hosted **inside ElevenLabs**, same key, eligible). Much better than `gemini-3-pro-image` for this look, and cheaper: about 900 credits for a 1K character sheet and about 520 for a 2K room, against about 3,000 for a Gemini 1K still. Params: `quality` defaults to high, `resolution` 1K or 2K, up to 10 reference images.
- **Do not use outside generators** (for example an AI gateway key from another project): the competition counts only the ElevenLabs package. GPT image 2.5 is available through ElevenLabs, so nothing outside is needed.
- **The lesson from the references:** design the character **object first**. The face is sculpted into the object's form (shade pleats become brows and eyelids, a fabric fold is the nose, the mug's rim is the brow and its handle is an arm), arms come from the object's own parts (a brass neck, a cord, a handle) with a tiny hand-like finial, and surfaces are rendered (brass gloss, glaze highlights, fur and seams). A flat cartoon face stuck on an object looks like clip-art (that was the first test).
- **Approved candidates (awaiting team yes):** `stills/chars_v4.png` (character sheet), `stills/room_v4.jpg` (empty room, with floral curtains), `stills/end_v4.jpg` (room with lamp, bear and cradle). Order that works: room still from the sketch, character sheet, then the end-state still using the room and the sheet as references.

## Correction 20:17: clean cel, not painterly (supersedes the "rendered / painterly" parts above)
The team showed two reference screenshots again and said the painterly version was far from the target. Comparing: the references are **clean graphic cel animation**, not oil-painted or textured. The working recipe (tested, `docs/prompts/`):
- **Characters:** bold continuous even-weight dark-brown ink outline; flat saturated colours with exactly one hard-edged shadow tone and one crisp highlight shape; glossy metal and glaze as simple white highlight shapes; no texture, grain, strokes, fur strands, gradients or airbrush. Eyes are white ovals with black pupils and a tiny glint under a heavy lid and thick brows; a very large mouth with dark-red inside, pink tongue and a few teeth; arms are thin tubular object parts ending in small mitten hands; exaggerated poses with squash and stretch.
- **Rooms:** clean coloured linework (dark blue-brown, not black), flat saturated fills with simple hard-edged shadow shapes, bold graphic blues with one warm lamp glow, wood in warm orange-brown with plank lines, bright striped rug, patterned curtains, simple tree silhouettes and a round moon. No oil-paint texture, no grain, no heavy gradients.
- **Model:** `gpt-image-2.5-sunburst` (via ElevenLabs) gave the best characters; `-flare` is a rubber-hose variant, also usable. Costs about 780 credits per still (1K sheet or 2K room), balance counter lags a little.
- **Reference handling:** the team's reference images are **not** sent to the generator (the kit excludes real film characters and the output would copy them). We describe their qualities in words only.
- **Current candidates (awaiting team yes):** `stills/chars_v5_sunburst.png`, `stills/room_v5.jpg`, `stills/end_v5.jpg`. The earlier v3/v4 images (`chars_v3`, `chars_v4`, `room_v4`, `end_v4`) are rejected as too painterly.

## Direction change 20:20: "drawn by a person", no studio look (supersedes the clean-cel section)
**Team decision:** forget the studio style. The film should feel hand-made and original, not like polished AI output. The designer's own sketches (loose marker line, hand-filled colour) are the model.
What makes a picture read as human, used in the prompts (`docs/prompts/hand_A.txt`, `hand_B.txt`): wobbly lines of uneven thickness that overshoot or break; fills that miss the edge and show bare paper; visible brush, crayon or marker grain; crooked, not-quite-straight shapes and no symmetry; a few construction lines left in; some areas left loose and unfinished with detail only where the eye should go; a limited palette of about six colours; naive, slightly off perspective. Avoid: gloss, gradients, airbrush, sparkles, rendering, perfect symmetry, over-detail.
- **A, gouache and pastel** (`stills/hand_A.png`) and **B, marker, crayon and torn paper with doodles** (`stills/hand_B.png`), both `gpt-image-2.5-sunburst` 1K, with the designer's room sketch and her lamp and bear sketches as references. Both read as hand-made. Awaiting team choice.
- Bonus for animation: crayon and gouache grain shimmering between frames reads as hand-drawn line boil.
