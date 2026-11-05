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
Measured today (balance counter lags a little): one 1K still about 3,000; one 6 s Fast clip about 2,400; one 4 s standard clip about 4,800 (a 6 s standard clip about 7,000).
Process, in this order, and stop at any failed gate:
1. Style test on **one still** (done: characters).
2. Base room still in style v3, check against the sketch overlay.
3. End-state still with the new characters.
4. **One Fast 6 s clip** as the motion test. Only if it passes, one standard clip for the final.
Never run two paid generations in parallel on an unapproved look.
