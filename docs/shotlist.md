# Shot list: A Life in One Room

**Theme:** Change
**Logline:** A room with no people in it, where the things are alive, watches a whole life go by: a baby is born, grows, leaves, returns, grows old, and a new life begins in the same room.
**Target runtime:** 60.0 s, 15 shots, hard cuts landed on sound. Read with `STORY.md` (what happens), `DESIGN.md` (rules), `SOUND.md` (sound).

## Prompt parts (paste word for word into every visual prompt)

**STYLE:** Flat 2D hand-painted animation in the style of 1940s-50s European feature animation. Flat cel colours, one fill per shape, almost no shading. Thin slightly irregular warm-brown outlines, never black. Painted background with broad brush streaks and paper grain. Cold ultramarine and navy night with one warm gold light. Theatre staging, locked camera. Original design.

**ROOM:** The same room as the reference image: one-point perspective, a large four-pane window centred on the back wall with a wide wooden sill, a plank floor, a striped rug on the floor. The window, sill, rug, floor and wall lines do not change. No people.

**NEGATIVE:** people, hands, faces (except the teddy bear, the lamp, the mug and the cushion), text, letters, logos, 3D render, CGI, anime, photoreal, lens flare, black outlines, extra furniture, camera movement.

**Still prompt** = `STYLE` + `ROOM` + the shot's *State* + `NEGATIVE`. Approve it (and run `scripts/overlay_check.py`) before animating.
**Clip prompt** = `Animate this image. Locked camera, no camera movement. Only <Motion> moves. Everything else stays still. <seconds> seconds.` Native clip audio off.

**Reference images to make first (G1, G2):** (1) the empty room from the sketch; (2) the **Teddy Bear**: `assets/items/bear_new.png` (clean) and `assets/items/bear_worn.png` (stitched head, patched belly); (3) the **Lamp**: `assets/items/lamp_floor.png`, a tall floor lamp with a trapezoid shade, a pull chain and a smiling face; (4) `armchair.png`, `side_table.png`, `mug.png`, `cushion.png`. Attach the matching image as the reference in every shot where the item appears.

## Shots

| # | File | Time | Sec | State (what is in the room) | Motion (one small thing) | Sound anchors (see `SOUND.md`) |
|---|---|---|---|---|---|---|
| 1 | shots/s01.mp4 | 0-3 | 3 | S1. Cold dark empty room. Moonlight lies on the rug in four pale blue vertical streaks. Window shows stars. Nothing else. | moonlight shimmers, dust drifts | room tone, heartbeat 0.5, door flung open 1.4 (sound leads the picture), pops 2.2 / 2.6 / 2.9 |
| 2 | shots/s02.mp4 | 3-6 | 3 | S1. Warm gold light now fills the room from the right edge. The four patches on the rug are gold. A wooden cradle with a hood, a blanket and a mobile stands on the rug. A teddy bear sits on the sill. The tall floor lamp stands at front left, its eyes just opening. | mobile sways, the lamp blinks once | first cry 3.0, bear plop 3.7, lamp click 4.0, music starts 4.0 |
| 3 | shots/s03.mp4 | 6-10 | 4 | S2. Back wall has animal wallpaper. A crib on the rug. Blocks and a ball on the floor. Bear on the sill. Warm playful light. | the ball rolls a short way | bed creak 6.4 and 8.4, child steps 7.0, laugh 9.6 |
| 4 | shots/s04.mp4 | 10-14 | 4 | S2. A small bed on the rug. Crayon scribbles on the wall. A column of pencil height marks on the right edge of the back wall. Warm light from the right. | warm light from the right brightens | toys hop 10 / 11 / 12.2, door opens 11.4, pencil marks |
| 5 | shots/s05.mp4 | 14-18 | 4 | S3. Teen room. Posters on the wall. A messy bed on the rug. A guitar on the floor. Blue rain on the window. Dim light. | rain runs down the glass | wallpaper rips 14.4, posters pop, rain 15, guitar 16, slam 17.5 |
| 6 | shots/s06.mp4 | 18-22 | 4 | S3. A desk. The floor lamp at front left. A box of toys on the floor. The bear at the far end of the sill. Blue rain. | the lamp rolls its eyes once | lamp click 18.2, bear moved 20.2 |
| 7 | shots/s07.mp4 | 22-28 | 6 | S4. The room is empty. Boxes stacked. Only the bear on the sill, facing the room. Cold snow outside, pale light, almost no warmth. | snow falls outside, dust in the air | packing 22, steps 24, door closes 25.2, then near silence |
| 8 | shots/s08.mp4 | 28-33 | 5 | S5. Warm amber evening. A double bed on the rug, floral wallpaper, two plants, an armchair, a wedding picture on the wall. The bear on the sill. The floor lamp glows warm. A round side table with a smiling mug stands beside the armchair. | the lamp glow flickers softly | door opens warm 28.4, double bed slides 29.4, pops |
| 9 | shots/s09.mp4 | 33-38 | 5 | S5. A crib beside the double bed, the teddy bear now in the crib. A second column of height marks. Same warm room. | the mobile and the blanket stir | baby heartbeat 33, coo 34, bear plop 35.5, laugh 36 |
| 10 | shots/s10.mp4 | 38-42 | 4 | S6. A child's bed alone on the rug. Four frames on the wall. A tall tree outside the window. Autumn dusk, softer colours. | leaves drift past the window | bed creak 39, bed slides away 41, door closes 41.6 |
| 11 | shots/s11.mp4 | 42-46 | 4 | S6. Only the double bed on the rug. The armchair looks worn. Many pictures on the wall. The lamp glow is a little dimmer. | the light slowly dims | pictures pop 42 / 43 / 44, chair creak 45 |
| 12 | shots/s12.mp4 | 46-50 | 4 | S7. A narrow bed with side rails. The round side table with a glass, pills and the smiling mug. A cane against the wall. A huge tree outside, pale blue dawn. | the blanket rises and falls slowly | bed creak 46.6, cane 47.6, pills 48.4, breathing 49 |
| 13 | shots/s13.mp4 | 50-54 | 4 | S7. The armchair has moved right beside the bed. The lamp leans over the bed. The worn, stitched teddy bear lies on the cushion. Pale light. | the lamp trembles slightly | armchair slides 50, bear plop 51.6, clock loud, breathing |
| 14 | shots/s14.mp4 | 54-57 | 3 | S8. Everything is still. The window is white. The lamp has closed its eyes and its glow is out. | a white light fades up | heartbeat slows, lamp click off 56.0, **silence 56.3-57.3** |
| 15 | shots/s15.mp4 | 57-60 | 3 | S8. The empty room with a door open off-frame right: new gold light spills across the floor. The worn teddy bear sits on the floor, waiting. | the gold light spreads over the floor | door 57.3, fast newborn heartbeat 57.8, new cry 58.4, first music note 58.0 |

## Notes for generating

- Generate **2 variants** per shot, not more. Pick the cleaner one.
- Ask for 4-5 s clips and cut early. Shot 7 is 6 s: request 6 s, or hold the last frame for the extra second.
- If a still drifts from the sketch (window, sill, rug, floor), reject it. Do not fix it in the clip.
- Shots 1 and 15 matter most: the start and the end of the loop.
- **Open questions** that change shots: where is the door (shot 15 assumes off-frame right), and where is the high shelf (shot 6 uses the far end of the sill).

## Voice-over

None. The story is told by the room and the sound.

## Music brief

See `SOUND.md`: 60 BPM, a four-note music-box lullaby motif that grows up and grows old, silence at 22-27 s and 56.3-57.3 s, the first note again at 58 s.
