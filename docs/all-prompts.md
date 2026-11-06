# All prompts used for "A Life in One Room"

Compiled 2026-11-06. Part 1 is every generation prompt sent to ElevenLabs (verbatim from `docs/prompts/`, ordered by stage, then version). Part 2 is every prompt typed to Claude Code in the three working sessions (chronological; session-continuation summaries and a few prompts that mention other tools or real brands are left out to match the competition rules; very long pasted text is cut at 3,000 characters; any key-like strings are redacted).

## Part 1 - Generation prompts (114 files)

### `s01_v2_clip.txt`

```text
A hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft muted dark blue-brown outlines (never black), gentle crayon grain, warm tender mood, limited palette of ultramarine, navy, cream, orange, ochre and brown. Locked camera, no camera movement, no zoom. One continuous 6-second shot: a cold night room wakes up, told through the characters' acting. Silent.
STRICT CONTINUITY: nothing appears, disappears, teleports or changes place. The cradle stays at the centre of the rug and never moves. The teddy bear stays seated on the window sill the whole time. The floor lamp stays at the left on its round base. The door stays on the right wall, always visible. The window, walls, rug and floor never change. No people, no text.
The lamp is one rigid piece: its pole stays straight and upright, never bending or stretching, with no legs or arms. It moves only by tilting or hopping as a whole on its round base, the shade bobbing slightly. Its eyes are always two small plain black dots (no pupils, no highlights), when asleep two short soft curved dashes.
TIGHTENED RULES: the lamp has NO legs, NO feet, NO arms and NO small creature or object beside its base: only the straight pole on its round base; the pole never leans or bends, the lamp only does a small hop straight up and down in place. The door hinges at the right edge of the wall and swings open only about 60 degrees, staying inside the right wall area, never crossing over the window, and then stays open and still to the end; it never swings back. The warm light and dust are a thin soft glow with a few small sparkles along the floor, not a big cloud or stream. The bear only gently moves its head and ears: its body, arms and legs stay in place on the sill, no flailing, no waving.
Motion script, smooth and continuous, on twos, with gentle anticipation before every action, an arc, a soft landing and follow-through:
0 to 1 s: cold, quiet, still. The sleeping lamp's shade nods slightly with a slow breath. The bear shivers once. Moonlight softly brightens on the floor.
At 1 s the door swings slowly open on its hinges, always visible, and warm orange light with sparkling dust gently spreads across the floor.
At 2 s the warm light reaches the cradle: its blanket flutters and the cradle rocks gently in place. The bear's ears perk up, it sits up a little straighter and turns its head toward the cradle, staying seated on the sill.
At 3.3 s the lamp wakes: its two black dot eyes open, it blinks, looks around, spots the cradle, crouches slightly in anticipation, then hops once in place as one rigid piece, landing softly on its base, the shade glowing brighter and the pull chain swinging.
At 5 s everything settles into the final picture: door open with warm light, lamp glowing, bear watching over the cradle.
```

### `s01_v2_clip_run1.txt`

```text
A hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft muted dark blue-brown outlines (never black), gentle crayon grain, warm tender mood, limited palette of ultramarine, navy, cream, orange, ochre and brown. Locked camera, no camera movement, no zoom. One continuous 6-second shot: a cold night room wakes up, told through the characters' acting. Silent.
STRICT CONTINUITY: nothing appears, disappears, teleports or changes place. The cradle stays at the centre of the rug and never moves. The teddy bear stays seated on the window sill the whole time. The floor lamp stays at the left on its round base. The door stays on the right wall, always visible. The window, walls, rug and floor never change. No people, no text.
The lamp is one rigid piece: its pole stays straight and upright, never bending or stretching, with no legs or arms. It moves only by tilting or hopping as a whole on its round base, the shade bobbing slightly. Its eyes are always two small plain black dots (no pupils, no highlights), when asleep two short soft curved dashes.
Motion script, smooth and continuous, on twos, with gentle anticipation before every action, an arc, a soft landing and follow-through:
0 to 1 s: cold, quiet, still. The sleeping lamp's shade nods slightly with a slow breath. The bear shivers once. Moonlight softly brightens on the floor.
At 1 s the door swings slowly open on its hinges, always visible, and warm orange light with sparkling dust gently spreads across the floor.
At 2 s the warm light reaches the cradle: its blanket flutters and the cradle rocks gently in place. The bear's ears perk up, it sits up a little straighter and turns its head toward the cradle, staying seated on the sill.
At 3.3 s the lamp wakes: its two black dot eyes open, it blinks, looks around, spots the cradle, crouches slightly in anticipation, then hops once in place as one rigid piece, landing softly on its base, the shade glowing brighter and the pull chain swinging.
At 5 s everything settles into the final picture: door open with warm light, lamp glowing, bear watching over the cradle.
```

### `s01_v2_end.txt`

```text
Redraw this exact picture with only these changes, keeping every object and position the same (window, sill, bear seated on the sill, cradle at the centre of the rug, lamp at the left on its base, door on the right wall): the door is now swung open on its hinges, still on the right wall and fully visible, with warm orange-gold light streaming through the doorway and spreading across the plank floor, the rug and the cradle, warm golden patches on the floor. The lamp is awake and glowing warmly: its eyes are two small plain black dots, hand-drawn with a slight imperfection, no pupils, no highlights, no outlines, no lashes, and a small smile, with a soft warm glow on the wall around it. The bear is seated on the sill, head turned slightly toward the cradle. Same soft look: hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Thin, soft outlines in a muted dark blue-brown, never black, slightly broken and feathered, not dominant. Gentle crayon grain, softly blended warm light, subtle torn-paper wall patches. Not vector, not polished, not glossy. Limited palette: ultramarine, navy, cream, orange, ochre, brown. Locked camera framing identical to the reference. No people, no text.
```

### `s01_v2_start.txt`

```text
Redraw this exact picture as a hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Keep every object and every position exactly the same: the four-pane night window with stars and moon, the wide sill, the teddy bear seated on the right end of the sill, the wooden cradle at the centre of the striped rug, the tall floor lamp at the left on its round base with a pull chain, the closed brown door on the right wall with its round knob, the plank floor, the torn-paper wall patches, the small star and house and tree doodles on the walls. Cold night room, moonlight streaks on the floor, the lamp asleep with its eyes as two short soft curved dashes and a small smile, the door closed. Thin, soft outlines in a muted dark blue-brown, never black, about half as thick as before, slightly broken and feathered, not dominant. Gentle crayon grain, softly blended light, subtle torn-paper wall patches. Not vector, not polished, not glossy, not digitally rendered. Warm, tender mood. Limited palette: ultramarine, navy, cream, orange, ochre, brown. Locked camera framing identical to the reference. No people, no text.
```

### `s01_v3_clip.txt`

```text
A hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft muted dark blue-brown outlines (never black), gentle crayon grain, warm tender mood, limited palette of ultramarine, navy, cream, orange, ochre and brown. Locked camera, no camera movement, no zoom. One continuous 8-second shot: a cold night room wakes up and the little teddy bear climbs down from the window sill to look into the cradle. Silent.
STRICT CONTINUITY: nothing falls, drops, appears, disappears or teleports. The cradle stays at the centre of the rug and never moves (it only rocks very slightly at the end). The floor lamp stays fixed at the left on its round base: it is one rigid piece with a straight upright pole, no legs, no arms, it never hops, bends or leans; it only wakes (eyes open) and glows. The door on the right wall hinges at its right edge, swings slowly open about 60 degrees and then stays open and still; it never swings back and never crosses the window. The window, walls, rug and floor never change. No people, no text, no objects falling into the room.
Motion script, smooth, continuous, on twos, physically connected, the bear always in contact with the wall, sill or floor:
0 to 1.2 s: cold, quiet, still. The sleeping lamp breathes slowly. The bear sits on the sill and shivers once.
At 1.2 s the door swings slowly open; warm light and a few small dust sparkles spread across the floor.
At 2 s the lamp wakes: its two small plain black dot eyes open and it smiles, glowing warmly, standing still and rigid.
2.2 to 5.5 s the bear climbs down carefully from the sill in ONE continuous visible movement: it turns round, lowers its legs over the sill edge, grips the wall and the sill with its paws, climbs down paw over paw and steps onto the floor. It never falls, never drops, never flails.
5.5 to 7 s the bear walks slowly across the floor to the cradle, one calm step after another.
7 to 8 s the bear stands beside the cradle at its right front, leans forward with both paws on the rim, head over the rim, and looks down into the cradle, head slightly tilted, curious and attentive; the cradle rocks very slightly. The window sill is empty at the end.
```

### `s01_v3_end.txt`

```text
Redraw this exact picture with only these changes, keeping the room, window, rug, cradle with its orange blanket, lamp position and door position the same: the door on the right wall is now swung open on its hinges, fully visible, with warm orange-gold light streaming through the doorway across the plank floor and the rug. The lamp is awake and glowing warmly: two small plain black dot eyes, hand-drawn with a slight imperfection, no pupils, no highlights, no outlines, no lashes, and a small smile. The window sill is now completely EMPTY: no bear on the sill. The teddy bear (brown, button eyes, same design) now stands on the floor on the rug right beside the cradle at its right front side, leaning forward with both paws on the cradle's rim, its head over the rim looking down into the cradle, curious and attentive. Same soft look: hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Thin, soft outlines in a muted dark blue-brown, never black, slightly broken and feathered. Gentle crayon grain, softly blended warm light, subtle torn-paper wall patches. Not vector, not polished, not glossy. Limited palette: ultramarine, navy, cream, orange, ochre, brown. Locked camera framing identical to the reference. No people, no text.
```

### `s01_v4_clip.txt`

```text
A hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft muted dark blue-brown outlines (never black), gentle crayon grain, warm tender mood, limited palette of ultramarine, navy, cream, orange, ochre and brown. Locked camera, no camera movement, no zoom. One continuous 8-second shot: a cold night room wakes up and the little teddy bear climbs down from the window sill, goes straight to the cradle and peeks in. Silent. The first and last frames of the clip equal the supplied start and end stills exactly.
STRICT CONTINUITY: nothing falls, drops, appears, disappears or teleports. NO dust, NO sparkles, NO confetti, NO floating particles, NO glow dots anywhere; the warm light is only a soft plain patch of light on the floor. The cradle stays at the centre of the rug and never moves (it only rocks very slightly at the end). The rust-orange armchair with its cushion and striped throw stays in the right front corner, completely still, the same size and place all the time. The floor lamp stays fixed at the left: one rigid piece with a straight upright pole, no legs, no arms, it never hops, bends or leans; it only wakes (its two plain black dot eyes open) and glows. The door on the right wall hinges at its right edge, swings slowly open as in the end still and then stays open and still. The window, walls, rug and floor never change. The bear keeps the same size throughout. No people, no text.
Motion script, smooth, continuous, on twos, the bear always in contact with the wall, sill or floor:
0 to 1.2 s: cold, quiet, still. The sleeping lamp breathes slowly. The bear sits on the sill and shivers once.
At 1.2 s the door swings slowly open and warm light spreads across the floor.
At 2 s the lamp wakes, smiling, glowing warmly, standing still and rigid.
2.2 to 5 s the bear climbs down carefully from the sill in one continuous visible movement: turns round, lowers its legs, grips the wall and sill with its paws, climbs down paw over paw and steps onto the floor. Never falls or flails.
5 to 7 s the bear walks straight to the cradle by the shortest path, one calm step after another, not wandering and not going near the armchair.
7 to 8 s the bear stands at the cradle's right side, leans forward with both paws on the rim and peeks inside, head tilted, curious. Then it holds completely still until the end. Nothing happens after that. The sill is empty at the end.
```

### `s01_v4_end.txt`

```text
Redraw the first image exactly (door open with warm light, awake glowing lamp with two black dot eyes and small smile, empty window sill, the teddy bear leaning with its paws on the cradle rim peeking in, cradle unchanged), keeping the bear the same size. Only change: add the warm rust-orange rounded armchair with small cushion and striped throw in the right front corner of the room, exactly the same design, size and place as in the second image (the armchair there), angled toward the window, between the rug's right edge and the door wall, lit by the warm light from the door. Same hand-made look: soft wax crayon and coloured pencil on textured paper, gentle, delicate, slightly dreamy; thin soft muted dark blue-brown outlines, never black; gentle crayon grain; limited palette of ultramarine, navy, cream, orange, ochre, brown. Locked camera framing identical to the reference. No people, no text, no confetti, no sparkles, no dust specks, no floating particles.
```

### `s01_v4_start.txt`

```text
Redraw this exact picture, keeping every object, position, the cold night lighting, the sleeping lamp with its soft curved dash eyes, the closed door, the teddy bear seated on the window sill and the cradle at the centre of the rug exactly the same. Only change: add one warm rust-orange rounded armchair with a small cushion and a throw, same as the reference armchair design (rounded arms, small blue-grey cushion, striped throw), standing at the right front corner of the room, angled toward the window, between the rug's right edge and the door wall. It stays low and clear of the door and the rug, in cold night colours matching the room. Same hand-made look: soft wax crayon and coloured pencil on textured paper, gentle, delicate, slightly dreamy; thin soft muted dark blue-brown outlines, never black; gentle crayon grain; limited palette of ultramarine, navy, cream, orange, ochre, brown. Locked camera framing identical to the reference. No people, no text, no confetti, no sparkles, no dust specks, no floating particles.
```

### `s02_clip.txt`

```text
A hand-made animation of marker, wax crayon and torn paper, like a sketchbook come to life: wobbly marker outlines and crayon grain that gently shimmer and re-draw themselves every frame, animated on twos. Locked camera, no camera movement, no zoom. One continuous 6-second shot of a happy childhood room at warm dusk.
STRICT CONTINUITY: nothing appears, disappears, teleports or changes place. The small wooden child's bed stays at the centre of the rug the whole time. The teddy bear stays seated on the window sill. The floor lamp stays at the left, standing on its round base. The door stays on the right wall, always visible. The three wooden blocks, the crayon wall scribbles, the height marks on the door frame, the window, walls, rug and floor never change. The ball is on the floor at the left from the first frame.
0 seconds: the lamp bounces on its round base in time, quick and excited, its shade glowing warm.
At 1.5 seconds the ball rolls slowly across the floor from the left toward the rug and stops against the leg of the child's bed.
At 3 seconds one wooden block wobbles and hops once in place, landing in the same spot.
At 4 seconds the bear slowly tilts its head to watch the ball, staying seated.
At 5 seconds the door swings slowly wider and the warm light through it brightens.
The patchy blanket on the bed ruffles gently throughout. The lamp keeps bouncing happily. No people, no text, no sound.
```

### `s02_end.txt`

```text
Edit the attached picture into the next moment of the very same room, same hand-made marker, wax-crayon and torn-paper style, same framing, everything in exactly the same place: the small wooden child's bed with its patchy blanket at the centre of the rug, the teddy bear on the sill, the lamp at the left, the window with its dusk sky and one star, the crayon scribbles, the height marks on the door frame, the three wooden blocks and the walls. Changes: the red-orange ball has rolled from the left across the floor and now rests against the front leg of the child's bed at the rug. The lamp is mid-bounce, slightly squashed or stretched on its base, its glow brighter, warmer and bigger on the wall, eyes wide, happy open smile. The bear stays seated, its head tilted slightly toward the ball. The door on the right wall is now open wider, swung inward, still clearly visible as a wooden door, with more warm orange light spilling across the floor toward the rug. The blanket slightly ruffled. Same wobbly marker outlines, crayon grain, imperfect hand-made feel. No people, no text.
```

### `s02_start.txt`

```text
Edit the attached picture into the CHILDHOOD version of the very same room, in exactly the same hand-made marker, wax-crayon and torn-paper style, same framing, same four-pane window, walls, floor, striped rug and door position. Keep in place exactly where they are: the tall floor lamp at the left (same cream trapezoid shade, two dot eyes, smile, pull chain with beads, thin dark pole, round base), the teddy bear sitting on the window sill (same brown bear with button eyes), the wooden door on the right wall. Changes: replace the cradle with a SMALL WOODEN CHILD'S BED at the centre of the rug with a patchy patchwork blanket (orange, cream and ultramarine patches). The lamp is switched ON: warm yellow glowing shade, happy wide-open dot eyes and a big smile, a warm yellow crayon glow on the wall. The window shows a warm dusk sky (ultramarine fading to orange near the bottom) with ONE small star. The door on the right wall is slightly AJAR, still clearly visible as a wooden door, with a warm narrow line of orange light spilling through the gap onto the floor; a column of short pencil height marks climbs up the door frame. Add simple crayon scribbles drawn on the torn-paper walls: a yellow sun, a little house, and an animal like a cat. On the floor at the left, in front of the lamp, a red-orange ball; on the floor on the left of the rug, three small wooden blocks (yellow, blue, orange) stacked loosely in a row. The room is warm and playful, the moonlight streaks are gone. Same wobbly marker outlines, crayon grain, imperfect hand-made feel, limited palette. No people, no text, no letters on the blocks.
```

### `s02_v2_clip.txt`

```text
A hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft blue-brown outlines, never black, gentle crayon grain, warm tender mood, brought to life with smooth hand-drawn animation on twos: gentle anticipation before every action, arcs, soft squash on landing, settle and follow-through. Locked camera, no camera movement, no zoom. One continuous 8-second shot, silent. No people, no text.
CRITICAL, the lamp is a rigid tall floor lamp at ALL times: it ALWAYS keeps its long straight thin pole, the round base and the pull chain; the shade never separates from the pole; it NEVER grows legs, feet, arms or a body, never walks or runs, never turns into a blob; it only hops on its round base, the whole tall lamp lifting off the floor together and landing, pole always straight and vertical (tilting only a few degrees in the air). The lamp hops along the floor in FRONT of the rug, staying on the front part of the floor below the rug and bed, never overlapping or crossing the bed. The bear climbs down only along the wall and the bed's headboard behind the bed.
STRICT CONTINUITY: nothing appears, disappears or teleports; anything that changes place travels there in view along a continuous path. The window, walls, rug, floor and the open door never change. The child's bed stays at the centre of the rug and its patchwork blanket and sheets never move or lift except where the bear slides in. The ball and the three blocks stay put (the ball may only roll gently to the rug). The lamp is one rigid piece: its pole stays straight and upright, never bending or stretching, no legs or limbs appear; it moves only by hopping or tilting as a whole on its round base, the shade bobbing slightly and the pull chain swinging. The lamp's eyes are always two small plain black dots with a small smile. The bear keeps its button eyes and brown fur, and never leaves the picture.
0 to 1 second: the lamp at the left crouches slightly, squashing down on its base (anticipation), the chain swinging. The teddy bear on the window sill shifts its weight toward the edge of the sill and looks down at the bed.
1 to 3.5 seconds: the lamp hops in two or three smooth, playful arcs along the floor from the left, past the front of the rug, to the right, upright as one piece, each hop with a soft squash on landing, the shade bobbing and the chain swinging. Meanwhile from 1.5 to 6 seconds the bear turns around on the sill, lowers its legs over the edge, and climbs down slowly, in view, holding on to the wall and the bed's headboard, arm over arm, then slides carefully down into the bed, always visibly connected to the sill, the headboard and the bed.
3.5 to 6 seconds: the lamp lands in front of the open door at the right front of the floor and settles upright. The bear finishes lowering itself into the bed.
6 to 8 seconds: the bear settles against the pillow, the blanket tucked over its legs, content; the lamp bounces gently once and then stands still, lit. Warm door light throughout. The sill is empty at the end.
```

### `s02_v2_clip_run1.txt`

```text
A hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft blue-brown outlines, never black, gentle crayon grain, warm tender mood, brought to life with smooth hand-drawn animation on twos: gentle anticipation before every action, arcs, soft squash on landing, settle and follow-through. Locked camera, no camera movement, no zoom. One continuous 8-second shot, silent. No people, no text.
STRICT CONTINUITY: nothing appears, disappears or teleports; anything that changes place travels there in view along a continuous path. The window, walls, rug, floor and the open door never change. The child's bed stays at the centre of the rug and its patchwork blanket and sheets never move or lift except where the bear slides in. The ball and the three blocks stay put (the ball may only roll gently to the rug). The lamp is one rigid piece: its pole stays straight and upright, never bending or stretching, no legs or limbs appear; it moves only by hopping or tilting as a whole on its round base, the shade bobbing slightly and the pull chain swinging. The lamp's eyes are always two small plain black dots with a small smile. The bear keeps its button eyes and brown fur, and never leaves the picture.
0 to 1 second: the lamp at the left crouches slightly, squashing down on its base (anticipation), the chain swinging. The teddy bear on the window sill shifts its weight toward the edge of the sill and looks down at the bed.
1 to 3.5 seconds: the lamp hops in two or three smooth, playful arcs along the floor from the left, past the front of the rug, to the right, upright as one piece, each hop with a soft squash on landing, the shade bobbing and the chain swinging. Meanwhile from 1.5 to 6 seconds the bear turns around on the sill, lowers its legs over the edge, and climbs down slowly, in view, holding on to the wall and the bed's headboard, arm over arm, then slides carefully down into the bed, always visibly connected to the sill, the headboard and the bed.
3.5 to 6 seconds: the lamp lands in front of the open door at the right front of the floor and settles upright. The bear finishes lowering itself into the bed.
6 to 8 seconds: the bear settles against the pillow, the blanket tucked over its legs, content; the lamp bounces gently once and then stands still, lit. Warm door light throughout. The sill is empty at the end.
```

### `s02_v2_end.txt`

```text
Redraw this exact picture with the same room, same soft hand-made crayon look, same thin soft blue-brown outlines, same layout, window, rug, door and wall drawings, with only these changes: the floor lamp is no longer at the left; it now stands upright on the right side of the floor, in front of the open door, at the right front of the rug, still lit and glowing, same lamp (straight upright pole, trapezoid shade, pull chain, two small plain black dot eyes, no pupils, no highlights, small smile). The left wall area where the lamp stood is now empty (sun and house and cat drawings stay). The teddy bear is no longer on the window sill (the sill is empty); the bear now sits in the child's bed, propped against the pillow, with the patchwork blanket tucked over its legs, content, same button eyes. The ball has rolled to rest on the rug near the bed's foot; the three blocks stay at lower left. Everything else unchanged. No people, no text.
```

### `s02_v2_start.txt`

```text
Redraw this exact picture with the same room, layout, objects and positions: window centred with a sill, plank floor, striped rug, the child's bed with the patchwork blanket at the centre of the rug, the lamp at the left on its round base, lit, the clean teddy bear seated on the sill at the right, the open door on the right wall with warm light and height marks, the ball and three blocks at the lower left, crayon drawings on the walls (sun, house, cat, star, tree). Keep every object and its position the same. The lamp is straight and upright with a straight pole, and its eyes are two small plain black dots, hand-drawn with a slight imperfection, no pupils, no highlights, no outlines around them, no lashes, no whites, plus a small smile.
Style: Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Thin, soft outlines in a muted dark blue-brown, never black, about half as thick as before, slightly broken and feathered, not dominant. Gentle crayon grain, softly blended warm light, subtle torn-paper wall patches. Not vector, not polished, not glossy, not digitally rendered. Warm, tender mood. Limited palette: ultramarine, navy, cream, orange, ochre, brown. No people, no text.
```

### `s02_v3_clip.txt`

```text
A hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft blue-brown outlines, never black, gentle crayon grain, warm tender mood, brought to life with smooth hand-drawn animation on twos: gentle anticipation before every action, arcs, soft squash on landing, settle and follow-through. Locked camera, no camera movement, no zoom. One continuous 8-second shot, silent. No people, no text.
CRITICAL, the lamp is a rigid tall floor lamp at ALL times: it ALWAYS keeps its long straight thin pole, the round base and the pull chain; the shade never separates from the pole; it NEVER grows legs, feet, arms or a body, never walks, never turns into a blob; it only hops on its round base, the whole tall lamp lifting off the floor together as ONE rigid piece and landing, pole always straight and vertical (tilting only a few degrees in the air). The lamp hops along the front part of the floor below the rug, never crossing the bed.
THE BALL: the red ball with the white stripe lies at the left floor at the start. It rolls steadily and naturally along the floor from the left, in front of the bed, to the right, reaches the open doorway on the right wall, rolls through the doorway and out of sight, getting smaller and farther away until it is completely gone. Once it has left through the door it NEVER comes back: at the end of the shot there is no ball anywhere in the room, on the rug or at the door.
THE BEAR: the teddy bear never winks and never blinks in an exaggerated way; both button eyes stay normal, round, black and open at all times.
STRICT CONTINUITY: nothing appears, disappears or teleports; anything that changes place travels there in view along a continuous path. The window, walls, rug, floor and the open door never change. The child's bed stays at the centre of the rug and its patchwork blanket never moves except where the bear slides in. The three blocks stay put at the lower left. The lamp's eyes are always two small plain black dots with a small smile. The bear keeps its brown fur and never leaves the picture.
0 to 1 second: the lamp at the left crouches slightly, squashing down on its base (anticipation), the chain swinging. The bear on the window sill shifts its weight toward the edge of the sill and looks down at the bed. The ball starts to roll.
1 to 3.5 seconds: the lamp hops in two or three smooth arcs along the floor from the left to the right, upright as one rigid piece, each hop with a soft squash on landing. Meanwhile the ball rolls steadily from the left across the floor in front of the bed toward the open doorway on the right wall, passes through the doorway and rolls out of sight, getting smaller. From 1.5 to 6 seconds the bear turns around on the sill, lowers its legs over the edge, and climbs down slowly, in view, holding on to the wall and the bed's headboard, paw over paw, then slides carefully into the bed, never falling.
3.5 to 6 seconds: the lamp lands at the right front of the floor near the door and settles upright. The ball is gone for good. The bear finishes lowering itself into the bed.
6 to 8 seconds: the bear settles against the pillow, blanket over its legs, calm, both eyes normal; the lamp stands still and glows. Warm door light throughout. The sill is empty and there is no ball in the room.

TIGHTENED RULES: the lamp's pole is a stiff straight wooden rod and NEVER bends, curves, sways like a stem or stretches at any moment, not even in the air; it stays perfectly straight and the same length, like a solid toy; the lamp hops by moving as one solid unchanged object, with only a few degrees of tilt. The lamp's eyes stay two plain black open dots at all times, never closed arcs. The open door stays at exactly the same open angle and position all the time and does not swing wider or narrower. The ball rolls along the floor only at floor level, never in the air.
```

### `s02_v3_clip_run1.txt`

```text
A hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft blue-brown outlines, never black, gentle crayon grain, warm tender mood, brought to life with smooth hand-drawn animation on twos: gentle anticipation before every action, arcs, soft squash on landing, settle and follow-through. Locked camera, no camera movement, no zoom. One continuous 8-second shot, silent. No people, no text.
CRITICAL, the lamp is a rigid tall floor lamp at ALL times: it ALWAYS keeps its long straight thin pole, the round base and the pull chain; the shade never separates from the pole; it NEVER grows legs, feet, arms or a body, never walks, never turns into a blob; it only hops on its round base, the whole tall lamp lifting off the floor together as ONE rigid piece and landing, pole always straight and vertical (tilting only a few degrees in the air). The lamp hops along the front part of the floor below the rug, never crossing the bed.
THE BALL: the red ball with the white stripe lies at the left floor at the start. It rolls steadily and naturally along the floor from the left, in front of the bed, to the right, reaches the open doorway on the right wall, rolls through the doorway and out of sight, getting smaller and farther away until it is completely gone. Once it has left through the door it NEVER comes back: at the end of the shot there is no ball anywhere in the room, on the rug or at the door.
THE BEAR: the teddy bear never winks and never blinks in an exaggerated way; both button eyes stay normal, round, black and open at all times.
STRICT CONTINUITY: nothing appears, disappears or teleports; anything that changes place travels there in view along a continuous path. The window, walls, rug, floor and the open door never change. The child's bed stays at the centre of the rug and its patchwork blanket never moves except where the bear slides in. The three blocks stay put at the lower left. The lamp's eyes are always two small plain black dots with a small smile. The bear keeps its brown fur and never leaves the picture.
0 to 1 second: the lamp at the left crouches slightly, squashing down on its base (anticipation), the chain swinging. The bear on the window sill shifts its weight toward the edge of the sill and looks down at the bed. The ball starts to roll.
1 to 3.5 seconds: the lamp hops in two or three smooth arcs along the floor from the left to the right, upright as one rigid piece, each hop with a soft squash on landing. Meanwhile the ball rolls steadily from the left across the floor in front of the bed toward the open doorway on the right wall, passes through the doorway and rolls out of sight, getting smaller. From 1.5 to 6 seconds the bear turns around on the sill, lowers its legs over the edge, and climbs down slowly, in view, holding on to the wall and the bed's headboard, paw over paw, then slides carefully into the bed, never falling.
3.5 to 6 seconds: the lamp lands at the right front of the floor near the door and settles upright. The ball is gone for good. The bear finishes lowering itself into the bed.
6 to 8 seconds: the bear settles against the pillow, blanket over its legs, calm, both eyes normal; the lamp stands still and glows. Warm door light throughout. The sill is empty and there is no ball in the room.
```

### `s02_v3_end.txt`

```text
Redraw this exact picture with the same room, same soft hand-made crayon look, same thin soft blue-brown outlines, same layout, window, rug, door and wall drawings, with only these changes: the floor lamp is no longer at the left; it now stands upright on the right side of the floor, near the open door, at the right front of the rug, still lit and glowing, same lamp (straight upright pole, trapezoid shade, pull chain, two small plain black dot eyes, no pupils, no highlights, small smile). The left wall area where the lamp stood is now empty (sun, house and cat drawings stay). The teddy bear is no longer on the window sill (the sill is empty); the bear now sits in the child's bed, propped against the pillow, with the patchwork blanket over its legs, calm, with BOTH button eyes normal, round, black and open. THERE IS NO BALL ANYWHERE: remove the red ball completely; the floor, the rug and the doorway show no ball, no round toy of any kind. The three small blocks stay at the lower left floor. The open doorway shows a strip of warm outdoor light. Everything else unchanged. No people, no text.
```

### `s02_v4_clip.txt`

```text
A hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft blue-brown outlines, never black, gentle crayon grain, warm tender mood, brought to life with smooth hand-drawn animation on twos: gentle anticipation before every action, arcs, soft squash on landing, settle and follow-through. Locked camera, no camera movement, no zoom. One continuous 8-second shot, silent. No people, no text.
CRITICAL, the lamp is a rigid tall floor lamp at ALL times: it ALWAYS keeps its long straight thin pole, the round base and the pull chain; the shade never separates from the pole; it NEVER grows legs, feet, arms or a body, never walks, never turns into a blob; it only hops on its round base, the whole tall lamp lifting off the floor together as ONE rigid piece and landing, pole always straight and vertical (tilting only a few degrees in the air). The lamp hops along the floor in front of the bed, below the rug, never crossing the bed, and lands on the right side near the door, beside the armchair.
THE BALL: the red ball with the white stripe lies at the left floor at the start. It rolls steadily and naturally along the floor from the left, in front of the bed, to the right, reaches the open doorway on the right wall, rolls through the doorway and out of sight, getting smaller and farther away until it is completely gone. Once it has left through the door it NEVER comes back: at the end of the shot there is no ball anywhere in the room, on the rug or at the door.
THE ARMCHAIR: the rust-orange armchair with its small cushion and throw stays completely still in the right front corner for the whole clip, never moves, tips or changes. The ball rolls along the floor behind the armchair and out through the open doorway, never touching it.
THE BEAR: the teddy bear never winks and never blinks in an exaggerated way; both button eyes stay normal, round, black and open at all times.
STRICT CONTINUITY: nothing appears, disappears or teleports; anything that changes place travels there in view along a continuous path. The window, walls, rug, floor and the open door never change. The child's bed stays at the centre of the rug and its patchwork blanket never moves except where the bear slides in. The three blocks stay put at the lower left. The lamp's eyes are always two small plain black dots with a small smile. The bear keeps its brown fur and never leaves the picture.
0 to 1 second: the lamp at the left crouches slightly, squashing down on its base (anticipation), the chain swinging. The bear on the window sill shifts its weight toward the edge of the sill and looks down at the bed. The ball starts to roll.
1 to 3.5 seconds: the lamp hops in two or three smooth arcs along the floor from the left to the right, upright as one rigid piece, each hop with a soft squash on landing. Meanwhile the ball rolls steadily from the left across the floor in front of the bed toward the open doorway on the right wall, passes through the doorway and rolls out of sight, getting smaller. From 1.5 to 6 seconds the bear turns around on the sill, lowers its legs over the edge, and climbs down slowly, in view, holding on to the wall and the bed's headboard, paw over paw, then eases over the bed rail and sinks gently into the mattress in ONE continuous soft movement with no jumps, no pauses and no cuts, with a little weight, the blanket draping softly over its legs.
3.5 to 6 seconds: the lamp lands at the right front of the floor near the door and settles upright. The ball is gone for good. The bear's soft continuous descent into the bed ends settled against the pillow.
6 to 8 seconds: the bear settles against the pillow, blanket over its legs, calm, both eyes normal; the lamp stands still and glows. Warm door light throughout. The sill is empty and there is no ball in the room.

TIGHTENED RULES: the lamp's pole is a stiff straight wooden rod and NEVER bends, curves, sways like a stem or stretches at any moment, not even in the air; it stays perfectly straight and the same length, like a solid toy; the lamp hops by moving as one solid unchanged object, with only a few degrees of tilt. The lamp's eyes stay two plain black open dots at all times, never closed arcs. The open door stays at exactly the same open angle and position all the time and does not swing wider or narrower. The ball rolls along the floor only at floor level, never in the air.

The first frame equals the start still and the last frame equals the end still, both with the same armchair.
TIGHTENED (second run): the lamp hops LOW and small: each hop lifts the base only a hand's width off the floor, the pole stays within 5 degrees of vertical at all times (never leaning over, never swinging high up), the shade stays below the window sill line and never rises in front of the window. The bear's descent is SLOW and gentle: it takes the whole time from 1.5 to 6.5 seconds, paw over paw along the headboard, easing over the rail and sinking into the mattress without any jump or fall; it is never airborne.
```

### `s02_v4_clip_run1.txt`

```text
A hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft blue-brown outlines, never black, gentle crayon grain, warm tender mood, brought to life with smooth hand-drawn animation on twos: gentle anticipation before every action, arcs, soft squash on landing, settle and follow-through. Locked camera, no camera movement, no zoom. One continuous 8-second shot, silent. No people, no text.
CRITICAL, the lamp is a rigid tall floor lamp at ALL times: it ALWAYS keeps its long straight thin pole, the round base and the pull chain; the shade never separates from the pole; it NEVER grows legs, feet, arms or a body, never walks, never turns into a blob; it only hops on its round base, the whole tall lamp lifting off the floor together as ONE rigid piece and landing, pole always straight and vertical (tilting only a few degrees in the air). The lamp hops along the floor in front of the bed, below the rug, never crossing the bed, and lands on the right side near the door, beside the armchair.
THE BALL: the red ball with the white stripe lies at the left floor at the start. It rolls steadily and naturally along the floor from the left, in front of the bed, to the right, reaches the open doorway on the right wall, rolls through the doorway and out of sight, getting smaller and farther away until it is completely gone. Once it has left through the door it NEVER comes back: at the end of the shot there is no ball anywhere in the room, on the rug or at the door.
THE ARMCHAIR: the rust-orange armchair with its small cushion and throw stays completely still in the right front corner for the whole clip, never moves, tips or changes. The ball rolls along the floor behind the armchair and out through the open doorway, never touching it.
THE BEAR: the teddy bear never winks and never blinks in an exaggerated way; both button eyes stay normal, round, black and open at all times.
STRICT CONTINUITY: nothing appears, disappears or teleports; anything that changes place travels there in view along a continuous path. The window, walls, rug, floor and the open door never change. The child's bed stays at the centre of the rug and its patchwork blanket never moves except where the bear slides in. The three blocks stay put at the lower left. The lamp's eyes are always two small plain black dots with a small smile. The bear keeps its brown fur and never leaves the picture.
0 to 1 second: the lamp at the left crouches slightly, squashing down on its base (anticipation), the chain swinging. The bear on the window sill shifts its weight toward the edge of the sill and looks down at the bed. The ball starts to roll.
1 to 3.5 seconds: the lamp hops in two or three smooth arcs along the floor from the left to the right, upright as one rigid piece, each hop with a soft squash on landing. Meanwhile the ball rolls steadily from the left across the floor in front of the bed toward the open doorway on the right wall, passes through the doorway and rolls out of sight, getting smaller. From 1.5 to 6 seconds the bear turns around on the sill, lowers its legs over the edge, and climbs down slowly, in view, holding on to the wall and the bed's headboard, paw over paw, then eases over the bed rail and sinks gently into the mattress in ONE continuous soft movement with no jumps, no pauses and no cuts, with a little weight, the blanket draping softly over its legs.
3.5 to 6 seconds: the lamp lands at the right front of the floor near the door and settles upright. The ball is gone for good. The bear's soft continuous descent into the bed ends settled against the pillow.
6 to 8 seconds: the bear settles against the pillow, blanket over its legs, calm, both eyes normal; the lamp stands still and glows. Warm door light throughout. The sill is empty and there is no ball in the room.

TIGHTENED RULES: the lamp's pole is a stiff straight wooden rod and NEVER bends, curves, sways like a stem or stretches at any moment, not even in the air; it stays perfectly straight and the same length, like a solid toy; the lamp hops by moving as one solid unchanged object, with only a few degrees of tilt. The lamp's eyes stay two plain black open dots at all times, never closed arcs. The open door stays at exactly the same open angle and position all the time and does not swing wider or narrower. The ball rolls along the floor only at floor level, never in the air.

The first frame equals the start still and the last frame equals the end still, both with the same armchair.
```

### `s02_v4_end.txt`

```text
Redraw the FIRST reference image exactly (same room, same soft hand-made crayon look, same thin soft blue-brown outlines, window, rug, door, bed with the teddy bear sitting in it propped against the pillow under the patchwork blanket with both button eyes normal, lamp on the right near the door, three blocks at the lower left), with ONE change: add the armchair exactly as it appears in the SECOND reference image: the same rust-orange rounded armchair with a small blue cushion and a striped throw, in the same size and the same position, in the right front corner at the bottom right edge of the picture, partly cut off by the right and bottom frame edges, angled toward the window. Do not make the chair smaller or move it inward. The lamp stays where it is in the first reference (it may be partly hidden behind the chair's back is not wanted: keep the lamp fully visible in front of the door wall, the chair lower and in front of it). NO BALL anywhere, the window sill empty. Everything else unchanged. No people, no text.
```

### `s02_v4_start.txt`

```text
Redraw this exact picture with the same room, same soft hand-made crayon look, same thin soft blue-brown outlines, same layout, window, rug, door, bed, wall drawings, lamp, ball, three blocks and teddy bear on the sill, with ONE change: add the armchair from the second reference image (same as the reference: a warm rust-orange rounded armchair with a small cushion and a throw), standing in the right front corner of the room, angled toward the window, between the rug's right edge and the door wall, at the same design, size and place as in the reference, drawn in the same soft crayon look. Keep the clear floor path from the ball at the left, across the floor in front of the bed, to the open doorway free: the armchair stays tucked in the lower right corner and does not cover the doorway, the door or the floor in front of the door. Everything else unchanged. No people, no text.
```

### `s03_clip.txt`

```text
A hand-made animation of marker, wax crayon and torn paper, like a sketchbook come to life: wobbly marker outlines and crayon grain that gently shimmer and re-draw themselves every frame, animated on twos. Locked camera, no camera movement, no zoom. One continuous 6-second shot of a teenager's room on a rainy evening, a door slamming.
STRICT CONTINUITY: nothing appears, disappears, teleports or changes place. The messy teen bed with its dark blanket and pillow stays at the centre of the rug the whole time. The guitar leans against the bed the whole time. The toy box stays on the floor at the left. The floor lamp stays at the left on its round base. The teddy bear stays seated at the far right end of the window sill. The posters stay on the walls. The wooden door stays on the right wall, always visible. The window, walls, rug and floor never change.
0 to 1 second: rain streaks run down the window glass; the door on the right wall stands ajar with a thin line of orange light; the lamp is dim and sulky, eyes rolled up.
At 1 second the lamp slowly rolls its eyes up and around, in a slow bored circle.
At 2.5 seconds the door SLAMS shut hard and fast, still visible as a wooden door, and the thin orange light vanishes at once.
At 2.7 seconds the whole room shakes: the posters flutter and tilt crooked, the guitar wobbles against the bed, the lamp trembles on its base, the bear bounces slightly on the sill.
From 4 seconds everything settles; the room is darker and dimmer, the posters hang crooked, the door stays shut, the lamp's eyes droop half-closed. Rain keeps running down the glass. No people, no text, no sound.
```

### `s03_end.txt`

```text
Edit the attached picture into the next moment of the very same room, same hand-made marker, wax-crayon and torn-paper style, same framing, everything in exactly the same place: the messy teen bed with the guitar leaning against it at the centre of the rug, the toy box at the left, the lamp at the left, the bear at the far right end of the sill, the window with rain, the walls and the wooden door on the right wall. Changes: the door on the right wall is now SLAMMED SHUT, completely closed, still clearly visible as a wooden door with its round doorknob, no gap and no orange light at all. The room is darker and dimmer, cold blue-grey, the warm light on the floor and walls is gone, only a faint weak glow around the lamp. The posters on the walls are now CROOKED, tilted at different angles, one hanging by a corner. The lamp's eyes droop, half-closed, a flat tired mouth. The bear sits slightly tilted. The guitar leans at a slightly different angle. Same wobbly marker outlines, crayon grain, imperfect hand-made feel. No people, no text.
```

### `s03_start.txt`

```text
Edit the attached picture into a TEENAGER'S ROOM on a rainy dim evening, the very same room in exactly the same hand-made marker, wax-crayon and torn-paper style, same framing, same four-pane window, back wall, side walls, plank floor and striped rug. Keep in place exactly: the tall floor lamp at the left, the wooden door on the right wall, the window, the rug. Changes: remove the cradle. At the centre of the rug stands a MESSY TEEN BED with a tangled dark navy blanket and one crumpled pillow, centred on the rug. A wooden GUITAR leans against the side of the bed. A TOY BOX with toys stuffed in stands on the floor at the left. On the walls, scribbled band-poster shapes (simple crayon-drawn rectangles with abstract shapes, no words) are pinned over the wall doodles, straight and neat. The window shows blue-grey dim rainy sky with rain streaks running down the glass, no moon, no stars. The lamp is ON but dim, its shade a weak dull yellow, its two eyes rolled up to the top of the shade, a sulky flat mouth. The teddy bear sits small on the FAR RIGHT end of the window sill, ignored, head slightly down. The door on the right wall is AJAR, open a small gap, with a thin line of warm orange light in the gap and a thin strip of light on the floor. The room is dim, cool blue-grey with only a faint warm touch. Palette: ultramarine, navy, cream, orange, yellow ochre, brown. Same wobbly marker outlines, crayon grain, imperfect hand-made feel. No people, no text.
```

### `s03_v2_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated smoothly on twos. Thin, soft outlines in a muted dark blue-brown, never black, slightly broken and feathered. Gentle crayon grain, softly blended warm light. Not vector, not polished, not glossy. Locked camera, no camera movement, no zoom. One continuous 6-second shot of a teenager's room on a rainy night, told only through the acting of the objects.
STRICT CONTINUITY: nothing appears, disappears or teleports. The bed stays at the centre of the rug, the guitar leans against it, the toy box stays at the left, the small teddy bear stays seated at the far right end of the window sill, the window and walls never change. The door stays on the right wall, always visible, and is never opened wider than its starting ajar position: it only ever moves toward closed. The posters only tilt a little and stay on the wall. The bear only bounces a little in place and stays seated. The floor lamp stays at the left on its round base. The lamp is one rigid piece: its pole stays perfectly straight and upright, never bending, stretching or growing legs; during the shake it rocks only a few degrees as a whole on its round base, the pole always staying a straight vertical line, never leaning far, never bent, never curved. The lamp's eyes are always exactly two small plain black dots: no whites, no pupils, no highlights, no outlines around them, no lashes. They only move position inside the shade.
0 to 1 second: rain runs steadily down the window glass. The door stands slightly ajar with a thin line of warm light. The lamp is dim and sulky, its two dot eyes high in the shade.
At 1 second the lamp's two dot eyes drift slowly up and around in a slow, bored eye-roll, then settle.
At 2 seconds the door, which stays about as far open as in the first frame, begins to swing shut, gathering speed, and at 2.5 seconds it slams firmly shut against the wall; the warm line of light vanishes.
At 2.7 seconds a short gentle shake runs through the room: the posters flutter and tilt crooked, the guitar wobbles slightly against the bed, the lamp tilts as one rigid piece on its base and rights itself, the bear on the sill bounces slightly and settles.
From 4 seconds everything settles; the room is dimmer and cooler, the posters hang crooked, the lamp's dot eyes droop low. Rain keeps running. No people, no text, silent.
```

### `s03_v2_end.txt`

```text
Redraw this exact picture with every object and position kept the same (same room, same framing, bed centred on the rug with the guitar leaning on it, toy box at the left, teddy bear at the far right end of the sill, window with rain), changing only this: the wooden door on the right wall is now firmly SHUT, closed flat against the wall, with no line of light at all; the room is darker and dimmer, the warm glow of the lamp weaker, cold blue night over everything; the posters on both walls hang slightly crooked and tilted; the lamp's two plain black dot eyes have drooped low in the shade, sulky, with the same small flat mouth. The lamp pole stays perfectly straight and upright on its round base.
Style: Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Thin, soft outlines in a muted dark blue-brown, never black, about half as thick as before, slightly broken and feathered, not dominant. Gentle crayon grain, softly blended warm light, subtle torn-paper wall patches. Not vector, not polished, not glossy, not digitally rendered. Warm, tender mood. Limited palette: ultramarine, navy, cream, orange, ochre, brown.
The lamp's eyes are exactly two small plain black dots, hand-drawn with a slight imperfection: no whites, no pupils, no highlights, no outlines around them, no lashes, no eyebrows. No people, no text.
```

### `s03_v2_start.txt`

```text
Redraw this exact picture with every object and position kept the same: the teen room at night with rain on the four-pane window, the messy dark-blue bed centred on the striped rug with the guitar leaning against it, the toy box at the left with ball, robot and dinosaur, posters on both walls, the small teddy bear at the far right end of the window sill, the wooden door on the right wall slightly ajar with a thin line of warm light, and the floor lamp at the left, dim, with a straight upright pole, a round base and a pull chain. Same layout, same framing, same camera.
Style: Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Thin, soft outlines in a muted dark blue-brown, never black, about half as thick as before, slightly broken and feathered, not dominant. Gentle crayon grain, softly blended warm light, subtle torn-paper wall patches. Not vector, not polished, not glossy, not digitally rendered. Warm, tender mood. Limited palette: ultramarine, navy, cream, orange, ochre, brown.
The lamp's face: exactly two small plain black dots for eyes, hand-drawn with a slight imperfection, placed high up in the shade as if rolling its eyes upward, and a small flat mouth. No whites around the eyes, no pupils, no highlights, no outlines around the dots, no lashes, no eyebrows. The lamp pole is perfectly straight.
No people, no text.
```

### `s03_v3_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos. Thin, soft muted blue-brown outlines, never black. Locked camera, no camera movement, no zoom. One continuous 6-second shot of a teenager's messy room on a rainy night. Silent.
Everything stays exactly where it is: the messy bed with the guitar leaning on it at the centre, the toy box at the left, the posters, the small bear on the sill, the lamp at the left standing upright and straight, and the wooden door on the right wall, which stands slightly ajar with a thin line of warm light and STAYS EXACTLY THAT AJAR, not moving at all until 2.5 seconds.
The lamp's face is ONLY a small smile-line mouth and TWO TINY PLAIN BLACK INK DOTS for eyes, like two dots made with a pen: no whites, no pupils, no outlines, no highlights, no lashes, at all times. During the sulky eye-roll just those two black dots slowly slide up and round the shade and back.
Motion: rain runs down the window glass the whole time. From 0 to 2.5 seconds the lamp sulks and its two dots slide in a slow eye-roll. At 2.5 seconds the door SLAMS SHUT quickly and firmly from the ajar position (it only closes, never opens wider), and the warm thin light vanishes. At 2.7 seconds a short, gentle shake runs through the room: the posters flutter, the guitar wobbles slightly, the small bear bounces a little on the sill, and the lamp only jiggles its shade a tiny bit while its pole stays straight and its base stays planted. From 4 seconds everything settles, the room dimmer and bluer, the lamp's two dots drooping low. No people, no text.
```

### `s03_v4_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos. Thin, soft muted blue-brown outlines, never black. Locked camera, no camera movement, no zoom. One continuous 6-second shot of a teenager's messy room on a rainy night. Silent. The first frame equals the start still and the last frame equals the end still.

STRICT CONTINUITY: everything stays exactly where it is: the messy bed with the guitar leaning on it at the centre, the toy box at the left, the posters, the small bear on the sill, the warm rust-orange armchair with cushion and throw in the right front corner (it never moves, never tips, never changes), the lamp at the left standing upright with a perfectly straight rigid pole on its round base, and the wooden door on the right wall, which stands slightly ajar with a thin line of warm light and stays exactly that ajar, not moving at all until 2.5 seconds.

THE LAMP IS SIMPLE AND SMOOTH. Its face is only a small mouth line and TWO TINY PLAIN BLACK INK DOTS for eyes: no whites, no pupils, no outlines, no highlights, no lashes, ever. It never tilts, bends, hops, stretches or distorts; the pole is straight and the base stays planted; the shade stays still. No floating dots, no sparkles, no glow particles, no extra effects around the lamp.

Motion: rain runs down the window glass the whole time. From 0 to 2.5 seconds the lamp sulks: its two black dots slowly slide up and round inside the shade and back in a sulky eye-roll (only the dots move). At 2.5 seconds the door SLAMS SHUT quickly and firmly from the ajar position (it only closes, never opens wider), and the thin warm light vanishes. At 2.7 seconds a short gentle shake runs through the room: the posters flutter, the guitar wobbles slightly, the small bear bounces a little on the sill; the lamp stays upright and still. From 3.5 seconds everything settles, the room dimmer and bluer. The lamp's two dots droop low, and then two soft muted-blue teardrops form under the shade and roll straight down the front of the lamp's shade, one beside each dot, and fade away softly; nothing else. No people, no text.

TIGHTENED RULES (a previous attempt failed on these): (1) The door is FROZEN in the exact slightly-ajar position of the first frame, a narrow gap only about a hand wide, for the first 2.5 seconds. It must NOT swing open wider at any time; its only movement in the whole clip is one fast closing slam at 2.5 s. (2) The lamp's eyes are always two open round black dots; never closed eyes, never curved lines, never eyebrows, never anything drawn above the shade (nothing floats above or around the lamp). (3) The lamp pole is vertical and straight in every frame, the lamp never leans or bends, the shade stays level. (4) The two blue teardrops stay attached to the shade face: they start just under the dots and slide straight down the face of the shade, fading before the bottom rim, no drips outside the shade. (5) The posters and room do not move except the short flutter after the slam.
```

### `s03_v4_clip_run1.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos. Thin, soft muted blue-brown outlines, never black. Locked camera, no camera movement, no zoom. One continuous 6-second shot of a teenager's messy room on a rainy night. Silent. The first frame equals the start still and the last frame equals the end still.

STRICT CONTINUITY: everything stays exactly where it is: the messy bed with the guitar leaning on it at the centre, the toy box at the left, the posters, the small bear on the sill, the warm rust-orange armchair with cushion and throw in the right front corner (it never moves, never tips, never changes), the lamp at the left standing upright with a perfectly straight rigid pole on its round base, and the wooden door on the right wall, which stands slightly ajar with a thin line of warm light and stays exactly that ajar, not moving at all until 2.5 seconds.

THE LAMP IS SIMPLE AND SMOOTH. Its face is only a small mouth line and TWO TINY PLAIN BLACK INK DOTS for eyes: no whites, no pupils, no outlines, no highlights, no lashes, ever. It never tilts, bends, hops, stretches or distorts; the pole is straight and the base stays planted; the shade stays still. No floating dots, no sparkles, no glow particles, no extra effects around the lamp.

Motion: rain runs down the window glass the whole time. From 0 to 2.5 seconds the lamp sulks: its two black dots slowly slide up and round inside the shade and back in a sulky eye-roll (only the dots move). At 2.5 seconds the door SLAMS SHUT quickly and firmly from the ajar position (it only closes, never opens wider), and the thin warm light vanishes. At 2.7 seconds a short gentle shake runs through the room: the posters flutter, the guitar wobbles slightly, the small bear bounces a little on the sill; the lamp stays upright and still. From 3.5 seconds everything settles, the room dimmer and bluer. The lamp's two dots droop low, and then two soft muted-blue teardrops form under the shade and roll straight down the front of the lamp's shade, one beside each dot, and fade away softly; nothing else. No people, no text.
```

### `s03_v4_end.txt`

```text
Redraw this exact picture with every object and position kept exactly the same (door firmly shut, darker room, crooked posters, lamp with two plain black dot eyes drooped low, straight upright pole, bear on the sill, bed with guitar, toy box), changing only this: ADD one warm rust-orange rounded armchair with a small cushion and a throw blanket at the RIGHT FRONT CORNER of the room, angled toward the window, between the rug's right edge and the door wall, same design as the reference chair (second reference image), dimmer in the night light. Do not add anything else.
Style: Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Thin, soft outlines in a muted dark blue-brown, never black. Limited palette: ultramarine, navy, cream, orange, ochre, brown. No people, no text, no sparkles, no floating dots.
```

### `s03_v4_start.txt`

```text
Redraw this exact picture with every object and position kept exactly the same (same room, framing, camera; messy bed with guitar at the centre, toy box at the left, posters, small teddy bear on the sill, floor lamp at the left with a straight upright pole and two plain black dot eyes, door on the right wall slightly ajar with a thin line of warm light), changing only this: ADD one warm rust-orange rounded armchair with a small cushion and a throw blanket at the RIGHT FRONT CORNER of the room, angled toward the window, between the rug's right edge and the door wall, same as the reference chair design (second reference image), partly in the dim night light. Keep the door ajar and the lamp unchanged. Do not add anything else.
Style: Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Thin, soft outlines in a muted dark blue-brown, never black. Gentle crayon grain. Limited palette: ultramarine, navy, cream, orange, ochre, brown. No people, no text, no sparkles, no floating dots.
```

### `s04_clip.txt`

```text
A hand-made animation of marker, wax crayon and torn paper, like a sketchbook come to life: wobbly marker outlines and crayon grain that gently shimmer and re-draw themselves every frame, animated on twos. Locked camera, no camera movement, no zoom. One continuous 6-second shot of an empty, cold, lonely room in winter.
STRICT CONTINUITY: nothing appears, disappears, teleports or changes place. The rug at the centre of the floor stays bare and empty the whole time. The cardboard boxes stay stacked at the left and right floor. The faded rectangles and the crayon scrap stay on the walls. The teddy bear stays seated at the same spot on the window sill the whole time: it never leaves the sill, never moves toward the door, never falls, never tumbles; only its head and upper body tilt a little while its seat stays fixed. The floor lamp stays at the left on its round base, switched off. The door stays on the right wall, always visible. The window, walls, rug and floor never change.
0 to 1.5 seconds: the room is cold, pale and still; snow drifts down outside the window, a few specks of dust float in the cold light, the crayon grain boils. The lamp is off, slumped, eyes closed.
At 1.5 seconds the door on the right wall opens only a narrow crack, a few degrees, the door staying the same size and in the same place on the wall, and a thin narrow beam of warm light falls across the floor from the crack. The door never opens wide.
At 2 seconds the bear, still seated on the sill, slowly lifts its head and tilts its head a little toward the door with hope.
At 3.5 seconds the door gently closes again to its original shut position, the beam of light fades and the room is cold and pale again.
At 4 seconds the bear, still seated at the same spot, slowly lets its head and shoulders droop and turns its head toward the snowy window. The lamp's eyes stay shut.
From 5 seconds everything is still, door closed, snow falling, cold and lonely. No people, no text, no sound.
```

### `s04_end.txt`

```text
Edit the attached picture into the next moment of the very same room, same hand-made marker, wax-crayon and torn-paper style, same framing, everything in exactly the same place: the bare empty striped rug, the cardboard boxes at left and right, the faded rectangles and crayon scrap on the walls, the window with falling snow, the tall floor lamp at the left, the teddy bear on the window sill, and the wooden door on the right wall. Changes: the door is CLOSED again, no light at all through it, same cold blue-white pale light everywhere, no warm colour. The teddy bear is still on the sill in the same spot but now slumped lower: its shoulders and head sag down, its head turned away from the door toward the snowy window, looking sad and small. The lamp stays off with eyes closed, shade drooped. Same wobbly marker outlines, crayon grain, imperfect hand-made feel. No people, no text.
```

### `s04_start.txt`

```text
Edit the attached picture into a new, EMPTY, COLD WINTER version of the very same room, in exactly the same hand-made marker, wax-crayon and torn-paper style, same framing, same window, same walls, same plank floor, same striped rug, same perspective. Keep in place exactly where they are: the four-pane window centred on the back wall with its wide sill, the striped rug on the floor, the tall floor lamp at the left, the teddy bear seated on the window sill, the wooden door on the right wall. Changes: REMOVE the cradle completely so the centre of the striped rug is bare and empty. ADD a few brown cardboard boxes, stacked at the left floor and at the right floor, drawn in marker and crayon. On the walls, show a few pale faded rectangles where posters used to hang, and one small scrap of crayon drawing remaining. Outside the window it is snowing: pale snowflakes falling over a cold blue-white dusk sky, snowy ground. The light is pale, cold blue-white, no warm orange or yellow light anywhere. The lamp is switched OFF, its shade pale, dull and drooped slightly, its two eyes closed like sleeping arcs, slumped and sad. The bear sits alone on the sill, upright, facing toward the door on the right. The door on the right wall is CLOSED, clearly visible, with a round doorknob and a dark crack beneath it, no light through it. Same wobbly marker outlines, crayon grain, imperfect hand-made feel. No people, no text.
```

### `s04_v2_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft muted blue-brown outlines, never black, gentle crayon grain, not vector, not polished, not glossy. Warm, tender, melancholy mood. One continuous 8-second shot, locked camera, no camera movement, no zoom, silent.
STRICT CONTINUITY: nothing appears, disappears or teleports. The room, window, walls, boxes, striped rug and plank floor never change. The lamp stays at the left on its round base, off, shade drooped, eyes two short soft dashes, completely frozen and rigid as one solid piece: the pole stays perfectly straight and vertical, the shade never tilts, bends, leans or moves at all for the whole 8 seconds. The door stays on the right wall, always visible, and only swings closed. The same small teddy bear is always visible, from the first frame to the last, and travels in view along a continuous path from the centre of the rug to the window sill. No people in the room. Only one tiny distant silhouette far away outside on the snowy path, very small, no details.
Motion script. 0 to 2.5 s: the bear sits in the exact centre of the rug looking at the open door, perfectly still except its head slowly following the door. The door closes slowly and smoothly on its hinges, and the warm orange beam on the floor narrows and fades until the door is fully shut with a soft settle and the room turns cold blue. 2.5 to 3.5 s: a long quiet pause, the door shut, the bear's head slowly sinks and its small shoulders drop. 3.5 to 4.2 s: the bear slowly turns its head toward the window. 4.2 to 6.5 s: the bear gets up and moves across the floor to the window in one continuous movement, then climbs up the wall under the sill paw over paw, with weight and gentle momentum, and pulls itself up onto the window sill, never vanishing, never jumping. 6.5 to 8 s: the bear settles seated on the right side of the sill with its back to us, looking out of the window. Outside, snow falls gently, and the tiny dark silhouette of a person walks away along the snowy path, growing smaller and fainter.
The door is one rigid wooden slab turning on its hinges at the right wall, it never moves toward the middle of the room and it ends flat against the right wall frame. Smooth, physically connected motion on twos with gentle anticipation, arcs, soft landings and settles. Locked camera. Silent.
```

### `s04_v2_clip_run1.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft muted blue-brown outlines, never black, gentle crayon grain, not vector, not polished, not glossy. Warm, tender, melancholy mood. One continuous 8-second shot, locked camera, no camera movement, no zoom, silent.
STRICT CONTINUITY: nothing appears, disappears or teleports. The room, window, walls, boxes, striped rug and plank floor never change. The lamp stays at the left on its round base, off, shade drooped, eyes two short soft dashes, completely still, its pole straight. The door stays on the right wall, always visible, and only swings closed. The same small teddy bear is always visible, from the first frame to the last, and travels in view along a continuous path from the centre of the rug to the window sill. No people in the room. Only one tiny distant silhouette far away outside on the snowy path, very small, no details.
Motion script. 0 to 2.5 s: the bear sits in the exact centre of the rug looking at the open door, perfectly still except its head slowly following the door. The door closes slowly and smoothly on its hinges, and the warm orange beam on the floor narrows and fades until the door is fully shut with a soft settle and the room turns cold blue. 2.5 to 3.5 s: a long quiet pause, the door shut, the bear's head slowly sinks and its small shoulders drop. 3.5 to 4.2 s: the bear slowly turns its head toward the window. 4.2 to 6.5 s: the bear gets up and moves across the floor to the window in one continuous movement, then climbs up the wall under the sill paw over paw, with weight and gentle momentum, and pulls itself up onto the window sill, never vanishing, never jumping. 6.5 to 8 s: the bear settles seated on the right side of the sill with its back to us, looking out of the window. Outside, snow falls gently, and the tiny dark silhouette of a person walks away along the snowy path, growing smaller and fainter.
Smooth, physically connected motion on twos with gentle anticipation, arcs, soft landings and settles. Locked camera. Silent.
```

### `s04_v2_end.txt`

```text
Redraw this exact picture keeping the room, window, lamp, boxes, rug, floor and wall patches exactly the same. Changes: the bear is no longer on the rug (the rug is bare). The same small teddy bear now sits on the window sill at the right side of the sill, seen from behind and slightly from the side, its head turned toward the window, looking out. The door on the right wall is now fully closed, flat against the frame, and there is no warm orange light anywhere: the whole room is cold blue-white night light. Through the window the snowy night shows a pale snowy path winding away between the dark fir trees toward the far distance, and far away on that path a tiny, very small dark silhouette of a person walking away, only a few pixels tall, no details. The lamp stays off, drooped, eyes as two short soft curved dashes.
Look: Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Thin, soft outlines in a muted dark blue-brown, never black, about half as thick as before, slightly broken and feathered, not dominant. Gentle crayon grain, subtle torn-paper wall patches. Not vector, not polished, not glossy, not digitally rendered. Tender, melancholy mood. Limited palette: ultramarine, navy, cream, orange, ochre, brown. No text.
```

### `s04_v2_start.txt`

```text
Redraw this exact picture in a new, softer look, keeping every object and position the same: the same empty room, the same four-pane window with the wide sill and snowy night outside, the lamp at the left, cardboard boxes at both sides, faded poster rectangles on the walls, the striped rug on the plank floor, the wooden door on the right wall. Changes: the small clean teddy bear (button eyes, dark nose) is no longer on the window sill; the sill is empty. The bear now sits upright in the exact centre of the striped rug, seen from a three-quarter side view, its head turned to the right to look at the door. The door on the right wall is open, swung inward and still fully visible, with a warm orange beam of light lying across the plank floor from the doorway towards the rug and the bear. The lamp at the left is switched off, its shade drooped slightly, its eyes two short soft curved dashes (sleeping), nothing else on the face. Rest of the room is cold blue night light, only the door beam is warm.
Look: Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Thin, soft outlines in a muted dark blue-brown, never black, about half as thick as before, slightly broken and feathered, not dominant. Gentle crayon grain, softly blended warm light, subtle torn-paper wall patches. Not vector, not polished, not glossy, not digitally rendered. Warm, tender mood. Limited palette: ultramarine, navy, cream, orange, ochre, brown. No people, no text.
```

### `s04_v4_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft muted blue-brown outlines, never black, gentle crayon grain, not vector, not polished, not glossy. Warm, tender, melancholy mood. One continuous 8-second shot, locked camera, no camera movement, no zoom, silent.
STRICT CONTINUITY: nothing appears, disappears or teleports. The room, window, walls, boxes, striped rug and plank floor never change. The lamp stays at the left on its round base, off, shade drooped, eyes two short soft dashes, completely frozen and rigid as one solid piece: the pole stays perfectly straight and vertical, the shade never tilts, bends, leans or moves at all for the whole 8 seconds. The door stays on the right wall, always visible, and only swings closed. The same small teddy bear is always visible, from the first frame to the last, and travels in view along a continuous path from the centre of the rug to the window sill. No people in the room. Only one tiny distant silhouette of a person far away outside on the snowy path, very small, no details, visible from the very first frame and walking steadily farther away along the winding path for the whole 8 seconds.
Motion script. Throughout the whole clip, from 0 to 8 s, outside the window the tiny dark silhouette of a person is visible on the snowy path and keeps walking slowly away, growing smaller and fainter, never stopping and never disappearing. 0 to 2.5 s: the bear sits in the exact centre of the rug looking at the open door, perfectly still except its head slowly following the door. The door closes slowly and smoothly on its hinges, and the warm orange beam on the floor narrows and fades until the door is fully shut with a soft settle and the room turns cold blue. 2.5 to 3.5 s: a long quiet pause, the door shut, the bear's head slowly sinks and its small shoulders drop. 3.5 to 4.2 s: the bear slowly turns its head toward the window. 4.2 to 6.5 s: the bear gets up and moves across the floor to the window in one continuous movement, then climbs up the wall under the sill paw over paw, with weight and gentle momentum, and pulls itself up onto the window sill, never vanishing, never jumping. 6.5 to 8 s: the bear settles seated on the right side of the sill with its back to us, looking out of the window. Outside, snow falls gently.
The door is one rigid wooden slab turning on its hinges at the right wall, it never moves toward the middle of the room and it ends flat against the right wall frame. Smooth, physically connected motion on twos with gentle anticipation, arcs, soft landings and settles. Locked camera. Silent.
```

### `s04_v4_end.txt`

```text
Redraw this exact picture keeping the room, window, lamp, boxes, rug, floor and wall patches exactly the same. Changes: the bear is no longer on the rug (the rug is bare). The same small teddy bear now sits on the window sill at the right side of the sill, seen from behind and slightly from the side, its head turned toward the window, looking out. The door on the right wall is now fully closed, flat against the frame, and there is no warm orange light anywhere: the whole room is cold blue-white night light. Through the window the snowy night shows a pale snowy path winding away between the dark fir trees toward the far distance, and far away on that path a tiny, very small dark silhouette of a person walking away, only a few pixels tall, no details. The lamp stays off, drooped, eyes as two short soft curved dashes.
Look: Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Thin, soft outlines in a muted dark blue-brown, never black, about half as thick as before, slightly broken and feathered, not dominant. Gentle crayon grain, subtle torn-paper wall patches. Not vector, not polished, not glossy, not digitally rendered. Tender, melancholy mood. Limited palette: ultramarine, navy, cream, orange, ochre, brown. No text.
```

### `s04_v4_start.txt`

```text
Redraw this exact picture, keeping everything identical: the same room, the bear sitting in the centre of the striped rug looking at the open door, the open door with its warm orange beam, the lamp, boxes, wall patches, rug and floor, with no change of position, colour or line. The only change: through the window, in the lower left pane, a pale snowy path winds away between the dark fir trees toward the far distance, and far away on that path a tiny, very small dark silhouette of a person walks away, only a few pixels tall, no details. Nothing else changes.
Look: Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Thin, soft outlines in a muted dark blue-brown, never black, slightly broken and feathered. Gentle crayon grain. Not vector, not polished, not glossy. Limited palette: ultramarine, navy, cream, orange, ochre, brown. No text.
```

### `s05_clip.txt`

```text
A hand-made animation of marker, wax crayon and torn paper, like a sketchbook come to life: wobbly marker outlines and crayon grain that gently shimmer and re-draw themselves every frame, animated on twos. Locked camera, no camera movement, no zoom. One continuous 6-second shot of a warm, happy amber family evening in a bedroom.
STRICT CONTINUITY: nothing appears, disappears, teleports or changes place. The double bed with floral bedding stays at the centre of the striped rug the whole time. The wooden crib stays on the rug to the right of the bed, with the teddy bear inside it, and the three-star mobile hangs above it the whole time. The floor lamp stays at the left on its round base. The wooden door stays open on the right wall, always visible. The armchair and the round side table with the smiling mug stay at the right front. The wedding picture stays on the left wall in the same size and place the whole time (it never shrinks, moves or duplicates), and the two plants stay where they are. The lamp's pole stays straight and rigid and never bends. The window, walls, rug and floor never change.
0 to 1 second: the three stars of the mobile turn slowly above the crib; the crayon grain boils.
At 1 second the little mug on the side table sways side to side in a funky groove, its coffee sloshing, the side table steadying itself on its feet.
At 2 seconds the floor lamp, standing on its round base, tips its shade only slightly toward the crib with a small quick bounce, its pole staying straight, and its warm glow pulses softly.
At 3 seconds the teddy bear in the crib slowly tilts its head, following the turning mobile.
At 4 seconds the floral blanket on the double bed rises and falls very slightly, as if breathing, staying flat on the bed.
From 5 seconds everything settles, warm and happy, into the final image. No people, no text, no sound.
```

### `s05_end.txt`

```text
Edit the attached picture into the next moment of the very same room, same hand-made marker, wax-crayon and torn-paper style, same framing, everything in exactly the same place and the same objects: double bed at the centre of the rug, crib with the teddy bear inside to the right of the bed, three-star mobile above the crib, armchair, side table with the smiling mug, wedding picture, two plants, open door on the right wall, lamp at the left, window. Only states change: the lamp glow is a touch brighter and bigger, its shade leaning a little further over toward the crib; the three stars of the mobile have turned to a different angle; the bear's head is tilted slightly toward the mobile; the mug is tilted slightly to one side as if swaying; the bedding on the double bed is raised a little as if it just breathed in. Same wobbly marker outlines, crayon grain, imperfect hand-made feel. No people, no text.
```

### `s05_start.txt`

```text
Edit the attached picture into the FAMILY EVENING version of the very same room, in exactly the same hand-made marker, wax-crayon and torn-paper style, same framing, same four-pane window centred on the back wall with its wide sill, same plank floor, same striped rug, same room outline. Keep in place: the tall floor lamp at the left (cream trapezoid shade with two dot eyes and a smile, pull chain with beads, thin dark pole, round base), the wooden door on the right wall (it must stay clearly visible, now OPEN, swung inward, with golden light spilling through it across the floor). Replace the cradle: put a large DOUBLE BED with floral bedding (blanket with orange, cream and blue flowers, two pillows) at the exact centre of the rug, its foot toward the viewer. Remove the teddy bear from the window sill; the sill is bare. ADD to the right of the bed on the rug a small wooden CRIB with slatted sides, and above it a mobile of three yellow stars hanging from strings; the clean brown teddy bear with button eyes sits inside the crib. ADD at the right front floor a plain face-free armchair with a round side table beside it, and on the table a small cream mug with a tiny smiling face. ADD a framed wedding picture (simple scribbled two small figures, no faces, no text) on the back wall, and two small potted plants on the floor. Floral wallpaper feel on the torn-paper walls. Mood: warm amber evening, window sky glowing warm amber and orange with one star; the lamp glows big and warm yellow, leaning slightly toward the crib, with a golden pool of light on the wall; the rug and floor are golden. Same wobbly marker outlines, crayon grain, imperfect hand-made feel, limited palette of ultramarine, navy, cream, orange, yellow ochre, brown. No people, no text.
```

### `s05_v2_clip.txt`

```text
A hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, brought gently to life. Thin, soft outlines in a muted dark blue-brown, never black, slightly feathered. Gentle crayon grain re-drawing softly each frame, on twos. Warm, tender mood. Locked camera, no camera movement, no zoom. One continuous 6-second shot, silent, no people, no text.
STRICT CONTINUITY: nothing appears, disappears or teleports. The double bed stays at the centre of the rug and its floral quilt stays completely still, flat and smooth: it never lifts, balloons, billows or jumps. The crib stays on the right of the bed. The armchair stays still at the right front. The floor lamp stays at the left, upright and rigid, its pole straight, with two small plain black dot eyes. The door stays open on the right wall. The window, walls, rug and floor never change. The small round side table with curly legs, with the smiling mug on its top, starts at the right front beside the armchair and travels in view along the floor to the left front, in front of the foot of the bed, always visible.
0 to 1 second: the star mobile above the crib turns gently; the teddy bear in the crib, with bright button eyes and a small soft smile, relaxed and happy, bounces slightly with a little happy wiggle; the mug on the table sways a little; the table crouches slightly on its curly legs in anticipation.
1 to 5 seconds: the side table walks. Its curly legs step one after another in a rhythmic, slightly bouncy, whimsical walk, one curly foot lifting and landing at a time with a small bounce, carrying the mug on its top across the plank floor from the right front, passing in front of the rug, to the left front. The mug sways gently from side to side but stays firmly on the table top, smiling. The lamp stays upright and its shade bobs very gently.
5 to 6 seconds: the table stops at the left front in front of the foot of the bed and settles with a little bounce, the mug wobbling once and then still. The bear in the crib smiles contentedly.
Smooth, continuous, physically connected motion with anticipation, a soft arc, a soft settle and follow-through. Silent.
```

### `s05_v2_end.txt`

```text
Redraw this exact picture with one change: the small round side table with curly legs and the smiling mug on its top is no longer at the right front next to the armchair; it now stands on the plank floor at the left front of the room, in front of the foot of the bed, to the left of the rug, mid-stride with its curly legs, the mug still on top of it. The armchair at the right front now stands alone with its blanket, and the floor where the table was is plain planks. Everything else stays exactly the same: same framing, double bed with floral quilt unchanged and flat, crib with the happy smiling bear with bright button eyes, star mobile, the lamp at the left with two plain black dot eyes and a small smile, the open door with golden light, plants, wedding picture. Same soft hand-made wax crayon and coloured pencil look on textured paper, thin soft muted dark blue-brown outlines, never black, warm tender mood. No people, no text.
```

### `s05_v2_start.txt`

```text
Redraw this exact picture as a hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Keep every object and position exactly the same: same room, same framing, window centred with a sill, plank floor, striped rug, double bed with the floral quilt at the centre of the rug, the wooden crib on the right of the bed with the star mobile hanging over it, the floor lamp at the left with its two small plain black dot eyes and a small smile, the wedding picture on the left wall, plants, the open wooden door on the right wall with golden light, the armchair at the right front, and at its right front the small round side table with curly legs and the smiling mug on its top. The teddy bear sitting in the crib looks noticeably happier: bright round button eyes, a small soft smile, relaxed posture, the original bear design kept. Thin, soft outlines in a muted dark blue-brown, never black, about half as thick as before, slightly broken and feathered, not dominant. Gentle crayon grain, softly blended warm light, subtle torn-paper wall patches. Not vector, not polished, not glossy, not digitally rendered. Warm, tender mood. Limited palette: ultramarine, navy, cream, orange, ochre, brown. The lamp's eyes are two small plain black dots, no pupils, no highlights, no outlines, no lashes. No people, no text.
```

### `s06_clip.txt`

```text
A hand-made animation of marker, wax crayon and torn paper, like a sketchbook come to life: wobbly marker outlines and crayon grain that gently shimmer and re-draw themselves every frame, animated on twos. Locked camera, no camera movement, no zoom. One continuous 6-second shot of a quiet room in soft autumn dusk, the light slowly fading.
STRICT CONTINUITY: nothing appears, disappears, teleports or changes place. The double bed stays at the centre of the rug the whole time. The worn teddy bear stays sitting on the worn armchair at the right front, facing the window. The round side table with the smiling mug stays beside the armchair. The floor lamp stays at the left, standing on its round base. The framed pictures stay on the walls. The wooden door stays firmly CLOSED and shut on the right wall the whole time, it never opens. There is exactly ONE mug, and it stays on the small side table the whole time, it never moves to the bed or anywhere else. The bed stays plain, nothing sits on it. The window, tree, walls, rug and floor never change.
0 to 1.5 seconds: bright gold beam of low light across the floor with dust motes drifting in it; a few autumn leaves drift past the window outside.
At 1.5 seconds the lamp, staying upright on its round base at the left, sways very slightly and tries a tiny hop straight up and down in place, landing awkwardly with a small wobble, its pull chain swinging a little, then steadies. It never tips over or leans far.
At 3 seconds the mug sways slowly side to side while staying on the side table.
At 4 seconds the light slowly dims and the gold beam slowly slides shorter across the floor, shadows lengthening and turning blue; the worn bear on the armchair slowly turns its head a little toward the closed door.
From 5 seconds everything settles into the final image: dimmer shorter beam, long shadows, lamp glowing softly. No people, no text, no sound.
```

### `s06_end.txt`

```text
Edit the attached picture into the next moment of the very same room, same hand-made marker, wax-crayon and torn-paper style, same framing, everything in exactly the same place: the double bed at the centre of the rug, the worn bear on the worn armchair at the right front facing the window with its head turned a little towards the door, the round side table with the smiling mug, the lamp at the left, the framed pictures, the window with the tall autumn tree, the closed door on the right wall. Changes only in light: the sun has sunk lower, so the beam of gold light across the floor is now SHORTER, narrower and dimmer, with longer, deeper blue shadows across the floor and the wall; the sky in the window is deeper dusky orange and violet-blue with fewer leaves left drifting; the lamp's glow is a little dimmer, its eyes open, calm smile. Overall the room is a touch darker and cooler. Same wobbly marker outlines, crayon grain, imperfect hand-made feel. No people, no text.
```

### `s06_start.txt`

```text
Edit the attached picture into a soft AUTUMN DUSK version of the very same room, in exactly the same hand-made marker, wax-crayon and torn-paper style, same framing, same four-pane window with its wide sill, same walls, floor planks and striped rug, same tall floor lamp at the left, same wooden door on the right wall. Remove the wooden cradle and instead place a DOUBLE BED at the centre of the rug, with faded floral bedding (muted cream, dusty orange and blue), a headboard towards the back wall, standing on the middle of the rug. The wooden door on the right wall is CLOSED, clearly visible, with its round doorknob. The teddy bear is no longer on the sill (the sill is bare) and is now a WORN bear (stitched seam down its side, a round patch on its belly, button eyes, faded brown) sitting on a worn old ARMCHAIR (a patch and a sag in the seat, no face) at the right front of the room, turned to face the window. Next to the armchair a small round side table with a cream mug that has a small calm smiling face. Add many small framed pictures hanging on the back wall and side walls (simple scribbled frames, no text). Outside the window: a tall tree with autumn leaves in yellow ochre and orange against a soft dusk sky, a few leaves drifting. A long beam of low bright gold afternoon light falls from the window across the floor and rug with a few dust motes. The lamp at the left is on but its glow is dimmer, eyes open, calm smile. Softer, faded palette (ultramarine, navy, cream, orange, yellow ochre, brown). Same wobbly marker outlines, crayon grain, imperfect hand-made feel. No people, no text.
```

### `s06_v2_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft outlines in a muted dark blue-brown, never black, slightly broken and feathered. Gentle crayon grain re-drawing softly each frame. Warm, tender mood. Locked camera, no camera movement, no zoom. One continuous 6-second shot of a quiet autumn dusk in a bedroom. Silent.
STRICT CONTINUITY: nothing appears, disappears, teleports or changes place. The double bed stays at the centre of the rug and never moves; its quilt lies still. The armchair stays at the right front and never moves. The side table and the smiling mug stay beside the armchair. The floor lamp stays at the left on its round base. The framed pictures stay on the walls. The window, walls, rug and floor never change. THE DOOR ON THE RIGHT WALL IS FIRMLY SHUT FOR THE WHOLE CLIP AND IS A SOLID FLAT PANEL FIXED TO THE WALL, it does not swing, hinge, rotate, tilt or open at any moment: it is closed, never moving, never opening, not even a crack, no light coming through, the door frame and door panel stay exactly as in the first frame. Nobody enters. No people, no text.
Motion script: 0 to 6 seconds, outside the window a few orange autumn leaves drift slowly past and flutter down through the dusk air, and the setting sun sinks slightly lower. The floor lamp is one rigid piece: its pole stays perfectly straight and upright, it never bends, leans or hops; its base stays planted on the floor at the same spot and the whole lamp only rocks a tiny amount, at most two degrees, left and right, the shade bobbing gently; it never leans over, the pull chain swinging a little, its eyes two plain black dots and a small smile, never changing. The smiling mug on the side table sways slowly and slightly. From 1.5 to 4 seconds the worn teddy bear in the armchair slowly and gently turns only its head a little to its right, toward the framed pictures on the right wall, then holds still; its body stays seated in the armchair and the door beside it does not react or move. The long beam of gold light on the floor slowly shortens, thins and dims, and the room grows a little dimmer and bluer, settling into the final picture. Nothing else moves: the bed, the quilt, the armchair, the pictures and the door stay completely still.

REMINDER: the door is closed and motionless in every single frame, identical to the first frame. The lamp stays upright and in place in every frame.
```

### `s06_v2_end.txt`

```text
Redraw this exact picture, keeping every object and its position exactly the same, same soft crayon and coloured pencil look, thin soft blue-brown outlines, never black. Only these changes: the dusk is a little later, so the window sky is deeper orange and navy with the sun lower and a few leaves drifting at slightly different places; the long beam of gold light on the floor is shorter, thinner and dimmer, fading toward the right; the room is slightly dimmer and the lamp glow a little softer; the worn teddy bear in the armchair has its head turned slightly toward the wall on its right, toward the door frame. The door on the right wall stays firmly shut and closed, exactly as before. The lamp stays upright and straight, its eyes two small plain black dots with a small smile. The armchair, bed, mug, pictures and rug do not move. No people, no text.
```

### `s06_v2_start.txt`

```text
Redraw this exact picture, keeping every object and its position exactly the same: the double bed with the floral quilt centred on the striped rug, the four-pane window with the autumn tree and sunset above it, the lamp at the left on its round base, the worn armchair at the right front with the worn teddy bear in it, the small side table with the smiling mug beside the armchair, the framed pictures on both walls, the plank floor with the long beam of gold light, and the wooden door on the right wall, firmly closed. Same framing, same layout.
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Thin, soft outlines in a muted dark blue-brown, never black, about half as thick as before, slightly broken and feathered, not dominant. Gentle crayon grain, softly blended warm light, subtle torn-paper wall patches. Not vector, not polished, not glossy, not digitally rendered. Warm, tender mood. Limited palette: ultramarine, navy, cream, orange, ochre, brown. Autumn dusk. The lamp's eyes are two small plain black dots, hand-drawn with a slight imperfection, no pupils, no highlights, no outlines around them, no lashes, no whites, plus a small smile. No people, no text.
```

### `s06_v3_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Warm, tender mood. Locked camera, no camera movement, no zoom. One continuous 6-second shot of a quiet autumn dusk in a bedroom. Silent.
Everything in the room stays exactly where it is: the double bed with its quilt at the centre of the rug, the armchair with the worn teddy bear at the right front, the side table with the smiling mug, the framed pictures, the floor lamp at the left, and the wooden door on the right wall, which stands half open and stays exactly as half open as in the first frame the whole time.
Only these small things move: outside the window a few orange autumn leaves drift slowly past and flutter down; the setting sun sinks a little lower; the smiling mug sways very slightly; the lamp's warm glow gently breathes, softly brighter and dimmer, while the lamp itself stands perfectly still, upright and straight; from 1.5 to 4 seconds the worn teddy bear slowly turns only its head a little toward the framed pictures, then holds still; the long beam of golden light on the floor slowly shortens and dims, and the room grows a little dimmer and bluer. No people, no text.
```

### `s06_v3_end.txt`

```text
Redraw this exact picture with everything in exactly the same place and the same soft crayon look. Changes only: the golden beam of light on the floor is a little shorter and dimmer, the dusk sky outside is a little deeper orange and blue, and the room is slightly dimmer. The half-open door on the right wall is exactly as it is, in the same position. No people, no text.
```

### `s06_v3_start.txt`

```text
Redraw this exact picture, keeping every object, position and the soft hand-made wax-crayon and coloured-pencil look exactly the same (thin soft muted blue-brown outlines, never black, gentle crayon grain, warm dusk light, same lamp with two plain black dot eyes). Only one change: the wooden door on the right wall is now HALF OPEN, swung inward about 40 degrees and clearly visible as a wooden door, with a soft warm golden light coming through the gap and lying across the floor. Everything else identical. No people, no text.
```

### `s06_v4_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Warm, tender mood. Locked camera, no camera movement, no zoom. One continuous 8-second shot of a quiet autumn dusk in a bedroom. Silent.

STRICT CONTINUITY: everything in the room stays exactly where it is and rigid: the double bed with its quilt at the centre of the rug, the armchair at the right front (it never moves, never tips, never rocks), the side table with the smiling mug, the framed pictures, the floor lamp at the left standing perfectly still, upright and straight with its pole never bending (only its warm glow gently breathes), and the wooden door on the right wall, which stays HALF OPEN exactly as in the first frame the whole time (it does not swing, open wider or close). Orange autumn leaves exist ONLY outside the window behind the glass: they drift and flutter down slowly out there and never enter the room, never appear on the floor, bed, armchair or in the air inside the room. No people, no text, nothing else appears.

The only character who moves is the OLD worn teddy bear (faded fur, stitched seam on the head, stitched cross over one eye, patches on belly and arm, one drooping ear). It is very old, stiff and tired, and moves slowly and carefully, always in contact with the armchair or the floor, never playful, never fast, never falling:
0-1.5 s: it sits upright on the armchair seat, tired, its chest rising and falling slowly.
1.5-3 s: it pauses, slowly shifts its weight from side to side, and puts its paws on the armrest.
3-5 s: it pushes itself up slowly, its arms trembling slightly, and stands on the seat swaying a little, resting for a moment.
5-7.5 s: it climbs down over the armrest to the floor carefully, one limb at a time, one paw, then a leg, pausing to rest between steps.
7.5-8 s: it stands hunched on the floor beside the armchair, one paw resting on the armrest, catching its breath.

TIGHTENED RULES (important): the bear NEVER climbs onto the top or back of the armchair and NEVER stands higher than the seat. It stays right at the armchair the whole time: it stands on the seat cushion, then lowers itself over the FRONT-RIGHT armrest (the side nearest the viewer and the door) straight down to the floor right next to the armchair, and ends standing UPRIGHT on its feet, hunched, in front of the armchair's right side with one paw on the armrest, exactly like the last frame. It never walks toward the bed or the lamp, never goes behind or past the side table, never lies down, never tumbles, never collapses: at every moment it is upright on its feet or its paws and in contact with the armchair. The side table and the mug stay still in the same place, never hidden or moved. The bear is always the same size, in the same plane as the armchair.
```

### `s06_v4_clip_run1.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Warm, tender mood. Locked camera, no camera movement, no zoom. One continuous 8-second shot of a quiet autumn dusk in a bedroom. Silent.

STRICT CONTINUITY: everything in the room stays exactly where it is and rigid: the double bed with its quilt at the centre of the rug, the armchair at the right front (it never moves, never tips, never rocks), the side table with the smiling mug, the framed pictures, the floor lamp at the left standing perfectly still, upright and straight with its pole never bending (only its warm glow gently breathes), and the wooden door on the right wall, which stays HALF OPEN exactly as in the first frame the whole time (it does not swing, open wider or close). Orange autumn leaves exist ONLY outside the window behind the glass: they drift and flutter down slowly out there and never enter the room, never appear on the floor, bed, armchair or in the air inside the room. No people, no text, nothing else appears.

The only character who moves is the OLD worn teddy bear (faded fur, stitched seam on the head, stitched cross over one eye, patches on belly and arm, one drooping ear). It is very old, stiff and tired, and moves slowly and carefully, always in contact with the armchair or the floor, never playful, never fast, never falling:
0-1.5 s: it sits upright on the armchair seat, tired, its chest rising and falling slowly.
1.5-3 s: it pauses, slowly shifts its weight from side to side, and puts its paws on the armrest.
3-5 s: it pushes itself up slowly, its arms trembling slightly, and stands on the seat swaying a little, resting for a moment.
5-7.5 s: it climbs down over the armrest to the floor carefully, one limb at a time, one paw, then a leg, pausing to rest between steps.
7.5-8 s: it stands hunched on the floor beside the armchair, one paw resting on the armrest, catching its breath.
```

### `s06_v4_end.txt`

```text
Redraw this exact picture with everything in exactly the same place and the same soft crayon look. Only change: the old worn teddy bear is no longer on the armchair seat; it now stands on the plank floor right beside the armchair, hunched and tired, one paw resting on the armrest, the other arm hanging, knees slightly bent, head low, the whole body visible with its faded fur, stitched seam on the head, belly patch and arm patch. The armchair seat is empty. The armchair, door (half open, same position), lamp, bed, side table with mug and window are unchanged. Orange leaves only outside the window behind the glass, none in the room. No people, no text.
```

### `s06_v4_start.txt`

```text
Redraw this exact picture, keeping the room, the double bed, the lamp with two plain black dot eyes, the framed pictures, the window with the autumn tree and sunset, the small side table with the smiling mug, the rug, the floor and the half-open wooden door on the right wall (swung inward about 40 degrees, warm gold light through the gap) exactly the same, in the same soft hand-made wax-crayon and coloured-pencil look on textured paper (thin soft muted blue-brown outlines, never black, gentle crayon grain, warm dusk light). Only change: the armchair at the right front is now turned a little toward the viewer and the room, so the seat and the front of the armchair are clearly visible, and the OLD worn teddy bear sits upright on the seat in front of the backrest with its whole body visible: head, both arms, belly and both legs. The bear is visibly aged: faded pale-brown fur, a stitched seam across the head, a stitched cross over one eye, a patch on the belly and a patch on one arm, loose threads, one slightly drooping ear, a tired sagging slouched posture, paws resting in its lap; gentle, never frightening. Orange autumn leaves are visible ONLY outside the window behind the glass; there are NO leaves anywhere inside the room, on the floor, the bed or the armchair. No people, no text.
```

### `s06_v5_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Warm, tender mood. Locked camera, no camera movement, no zoom. One continuous 8-second shot of a quiet autumn dusk in a bedroom. Silent. The first and last frames equal the start and end stills exactly.

STRICT CONTINUITY: everything in the room stays exactly where it is and rigid: the double bed with its quilt at the centre of the rug, the armchair at the right front (it never moves, never tips, never rocks), the side table with the smiling mug, the framed pictures, the floor lamp at the left standing perfectly still, upright and straight with its pole never bending (only its warm glow gently breathes), and the wooden door on the right wall, which stays HALF OPEN exactly as in the first frame the whole time. Orange autumn leaves exist ONLY outside the window behind the glass and never enter the room. No people, no text, no sparkles, nothing else appears.

The only character who moves is the OLD worn teddy bear (faded fur, stitched seam on the head, stitched cross over one eye, patches on belly and arm). It always keeps the same small size, never grows or shrinks, and moves in ONE continuous slow, tired, careful movement, always in contact with the chair, floor, bed or sill, never fast, never teleporting:
0-1.5 s: it sits tired on the armchair seat, chest rising and falling slowly.
1.5-3 s: it slowly stands up on the seat, swaying a little, and rests a moment.
3-4.5 s: it climbs down carefully from the chair over the front armrest to the floor, one limb at a time.
4.5-6.5 s: it walks slowly across the floor, past the foot of the bed, toward the wall under the window, always on the floor, passing in front of the bed's foot.
6.5-7.5 s: at the wall it climbs up the bed's headboard onto the window sill, paw over paw.
7.5-8 s: it stands on the sill with its back to us, looking out at the autumn sunset, exactly like the last frame. The armchair is now empty.
```

### `s06_v5_end.txt`

```text
Redraw this exact picture, identical framing, same hand-made soft wax crayon and coloured pencil look on textured paper, thin soft muted blue-brown outlines, never black, same palette. Keep every object and position exactly the same: the double bed with its quilt at the centre of the rug, the floor lamp at the left with two plain black dot eyes and a small smile, the side table with the smiling mug, the framed pictures, the half-open wooden door on the right wall, the window with the autumn sunset and the tree. Same as the reference: the rust-orange armchair at the right front corner stays exactly the same, but is now EMPTY (only the seat cushion visible). The old patched teddy bear, exactly the same bear with the same size, patches, stitched seam and faded fur, now stands on the wide window sill under the window, seen from behind or in profile, looking out of the window at the autumn sunset, tiny against the window. The bear is the same small size as before relative to the bed and the armchair. Orange leaves only outside the glass. No other changes, no people, no text, no sparkles.
```

### `s06_v6_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Warm, tender mood. Locked camera, no camera movement, no zoom. One continuous 8-second shot of a quiet autumn dusk in a bedroom. Silent. The first and last frames equal the start and end stills exactly.

STRICT CONTINUITY: everything in the room stays exactly where it is and rigid: the double bed with its quilt at the centre of the rug, the armchair at the right front (it never moves, never tips, never rocks), the side table with the smiling mug, the framed pictures, the floor lamp at the left standing perfectly still, upright and straight with its pole never bending (only its warm glow gently breathes), and the wooden door on the right wall, which stays HALF OPEN exactly as in the first frame the whole time. Orange autumn leaves exist ONLY outside the window behind the glass and never enter the room. No people, no text, no sparkles, nothing else appears.

The only character who moves is the OLD worn teddy bear (faded fur, stitched seam on the head, stitched cross over one eye, patches on belly and arm). It always keeps the same small size, never grows or shrinks, and moves in ONE continuous slow, tired, careful movement, always in contact with the chair, floor, bed or sill, never fast, never teleporting:
0-1.5 s: it sits tired on the armchair seat, chest rising and falling slowly.
1.5-3 s: it slowly stands up on the seat, swaying a little, and rests a moment.
3-4.5 s: it climbs down carefully from the chair over the front armrest to the floor, one limb at a time.
4.5-6.5 s: it walks slowly across the floor, past the foot of the bed, toward the wall under the window, always on the floor, passing in front of the bed's foot.
6.5-7.5 s: at the wall it climbs up the bed's headboard onto the window sill, paw over paw.
7.5-8 s: it stands on the sill with its back to us, looking out at the autumn sunset, exactly like the last frame. The armchair is now empty.

The old bear is slim with thin limbs and a small flat belly, exactly as in the first frame, in every frame; it never looks plump or round-bodied.
```

### `s06_v6_end.txt`

```text
Edit the first reference image (the bedroom with the old bear standing on the window sill, seen from behind, armchair empty). Keep EVERYTHING exactly the same: identical framing, bed, quilt, rug, lamp, side table, pictures, half-open door, window, armchair, soft wax crayon look, thin muted blue-brown outlines. Change ONLY the old bear on the sill: redraw it slim. The old teddy bear must be SLIM like the young bear in the second reference: a small slim torso, thin arms and thin legs, a small flat belly, a small body relative to its head, same head size, faded fur, a few patches, a stitched seam on the head and a stitched cross over one eye. Clearly NOT plump, NOT round-bodied, NOT fat. Same pose and place, tiny against the window.
```

### `s06_v6_start.txt`

```text
Edit the first reference image (the bedroom with the old bear seated in the rust-orange armchair). Keep EVERYTHING exactly the same: identical framing, bed, quilt, rug, lamp, side table with mug, pictures, half-open door, window, autumn sunset, armchair, hand-made soft wax crayon and coloured pencil look, thin soft muted blue-brown outlines. Change ONLY the old bear sitting in the armchair: redraw it much slimmer. The old teddy bear must be SLIM like the young bear in the second reference: a small slim torso, thin arms and thin legs, a small flat belly, a small body relative to its head, same head size, faded fur, a few patches, a stitched seam on the head and a stitched cross over one eye. Clearly NOT plump, NOT round-bodied, NOT fat. Same seated pose, same place, no larger than before.
```

### `s07_clip.txt`

```text
A hand-made animation of marker, wax crayon and torn paper, like a sketchbook come to life: wobbly marker outlines and crayon grain that gently shimmer and re-draw themselves every frame, animated on twos. Locked camera, no camera movement, no zoom. One continuous 6-second shot of a fragile quiet room at pale blue dawn.
STRICT CONTINUITY: nothing appears, disappears, teleports or changes place. The narrow single bed with side rails stays at the centre of the rug the whole time. The worn teddy bear stays lying on the pillow. The armchair stays right beside the bed. The round side table with the glass, pill bottle and mug stays by the bed. The cane stays leaning by the door. The floor lamp stays standing near the bed, leaning over it. The door stays closed on the right wall, always visible. The window with the huge bare tree, the walls and the floor never change.
0 to 1.5 seconds: everything is held and still; only the crayon grain boils. The blanket on the bed rises and falls only a tiny amount, a few pixels, very slowly, like quiet breathing; the blanket never grows bigger than the bed and never hangs over its edges.
At 1.5 seconds the lamp's dim glow trembles and flickers once, and its shade tilts slightly closer to the bed.
At 3 seconds the whole room gives a slight tremor: a picture frame on the wall tilts a little, and the armchair gives one very small rock, only a degree or two, and stays flat on the floor beside the bed.
At 4.5 seconds the worn bear on the pillow slowly turns its head toward the lamp, and the lamp's glow weakens.
From 5 seconds everything settles into the final image: pale, dim, fragile. No people, no text, no sound.
```

### `s07_end.txt`

```text
Edit the attached picture into the next moment of the very same room, same hand-made marker, wax-crayon and torn-paper style, same framing, everything in exactly the same place: the narrow single bed with rails at the centre of the rug, the worn teddy bear on the pillow, the armchair beside the bed, the round side table with glass, pill bottle and mug, the cane by the door, the closed door on the right wall, the window with the huge bare tree, the lamp leaning over the bed, the faded framed pictures. Changes: the lamp's glow is slightly weaker and dimmer, its shade tilted a little closer to the bed; the bear's head is turned slightly toward the lamp; one wall picture hangs slightly tilted; the light in the room is a touch paler and dimmer. Same wobbly marker outlines, crayon grain, imperfect hand-made feel. No people, no text.
```

### `s07_start.txt`

```text
Edit the attached picture into the OLD-AGE, PALE BLUE DAWN version of the very same room, in exactly the same hand-made marker, wax-crayon and torn-paper style, same framing, same window, back wall, floor planks and striped rug, same wobbly marker outlines and crayon grain. Keep exactly in place: the four-pane window centred on the back wall with its wide sill, the wooden door on the right wall (CLOSED, with round doorknob, clearly visible), the rug in front of the window. Changes: REMOVE the cradle. At the centre of the rug stand a narrow single wooden bed with side rails, a pale blanket and a pillow; the small worn teddy bear (stitched seam, patch on its belly, button eyes) lies on the pillow. A worn armchair (no face) stands right beside the bed on its right side, on the rug edge. A small round side table with curly legs stands on the left of the bed holding a drinking glass, a small pill bottle and a small cream mug with a tiny calm smiling face. A wooden cane leans against the right wall beside the door. The tall floor lamp (cream trapezoid shade, two dot eyes, small smile, pull chain with beads, thin dark pole, round base) now stands close to the bed at the left, its shade leaning over the bed, with a small dim weak pale glow. Outside the window: a huge bare tree with many branches against a pale blue dawn sky, no stars, no moon. Faded, pale walls with a couple of small faded framed pictures. The room is lit by pale dim blue-grey dawn light, no strong warm light. No people, no text.
```

### `s07_v2_clip.txt`

```text
A hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, like a sketchbook come to life. Thin, soft outlines in a muted dark blue-brown, never black, slightly broken and feathered. Crayon grain re-draws itself gently each frame. Locked camera, no camera movement, no zoom. One continuous 6-second shot, pale blue dawn in an old person's room, silent. Very calm, small, slow movements only.
STRICT CONTINUITY: nothing appears, disappears or teleports, and nothing changes shape. The narrow bed with rails stays at the centre of the rug. The armchair is fixed to the floor and never moves: it does not rock, tip, slide or lean, it stays upright in exactly the same place for the whole clip. The side table with the glass, pills and mug, the cane by the door, the closed door, the window with the bare tree and the rug never move. The worn teddy bear stays lying on the pillow. The lamp stays at the left, standing on its round base, for the whole clip. The lamp is one rigid, stiff piece made of a straight upright pole, a round base and a cream shade fixed on top: the pole is always perfectly straight and vertical, it never bends, curves, droops, stretches, falls or detaches, the shade is always attached to the top of the pole and always visible, the base never leaves the floor. The only lamp movement is a very slight tilt of the whole lamp, a few degrees, toward the bed, and back. The lamp's eyes stay two small plain black dots with a small smile.
0 to 1.5 seconds: calm and still. The blanket rises and falls very slowly with a sleeper's breath. The lamp glows steadily.
1.5 to 3 seconds: the lamp's glow trembles and flickers once, softly, and the whole lamp tilts a few degrees toward the bed, pole straight.
3 to 4.5 seconds: the bear on the pillow slowly turns its head toward the lamp. The picture on the left wall tilts slightly on its nail.
4.5 to 6 seconds: the glow weakens slowly, the lamp stays standing upright with its shade on top, everything settles into the final picture. The blanket keeps breathing slowly. The armchair has not moved at all. No people, no text, no sound.
```

### `s07_v2_clip_try1.txt`

```text
A hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, like a sketchbook come to life. Thin, soft outlines in a muted dark blue-brown, never black, slightly broken and feathered. Crayon grain re-draws itself gently each frame. Locked camera, no camera movement, no zoom. One continuous 6-second shot, pale blue dawn in an old person's room, silent.
STRICT CONTINUITY: nothing appears, disappears or teleports. The narrow bed with rails stays at the centre of the rug. The armchair is fixed to the floor and never moves: it does not rock, tip, slide or lean, it stays upright in exactly the same place for the whole clip. The side table with the glass, pills and mug, the cane by the door, the closed door, the window with the bare tree and the rug never move. The worn teddy bear stays lying on the pillow. The lamp stays at the left on its round base. The lamp is one rigid piece: the pole stays straight and upright, it never bends or stretches, only the shade tilts slightly toward the bed as a whole. The lamp's eyes stay two small plain black dots with a small smile, never changing shape.
0 to 1 second: calm and still. The blanket rises and falls very slowly with a sleeper's breath. The lamp glows steadily.
1 to 2.5 seconds: the lamp's glow trembles and flickers once, softly. The shade tilts slightly toward the bed, a small gentle lean, the pole staying straight.
2.5 to 4 seconds: the bear on the pillow slowly turns its head toward the lamp. The picture on the left wall tilts slightly on its nail.
4 to 6 seconds: the glow weakens slowly, everything settles into the final picture. The blanket keeps breathing slowly. The armchair has not moved at all. No people, no text, no sound.
```

### `s07_v2_end.txt`

```text
Redraw this exact picture with only these changes, keeping the same soft wax crayon and coloured pencil look, thin soft muted dark blue-brown outlines, never black: the lamp's shade is tilted slightly toward the bed (the whole lamp as one rigid piece, the pole stays straight and upright, only a slight lean of the top), the lamp's glow is weaker and dimmer, the worn bear on the pillow has turned its head toward the lamp, the picture on the left wall hangs slightly tilted, the blanket is the same. The armchair, bed, side table, cane, door, window and rug are exactly where they were, the armchair completely unchanged and upright. The lamp's eyes are two small plain black dots, no pupils, no highlights, no outlines, plus a small smile. No people, no text.
```

### `s07_v2_start.txt`

```text
Redraw this exact picture as a hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Keep every object and every position exactly the same: the narrow bed with rails centred on the striped rug, the worn teddy bear on the pillow, the armchair beside the bed on the right, the round side table with the glass, the pill bottle and the smiling mug, the lamp at the left with its pull chain, the cane leaning by the door, the closed door on the right wall, the bare tree in the window, the two framed pictures, the plank floor and the torn-paper wall patches. Thin, soft outlines in a muted dark blue-brown, never black, about half as thick as before, slightly broken and feathered, not dominant. Gentle crayon grain, softly blended warm light, subtle torn-paper wall patches. Not vector, not polished, not glossy, not digitally rendered. Warm, tender mood, pale blue dawn. Limited palette: ultramarine, navy, cream, orange, ochre, brown. The lamp's eyes are two small plain black dots, hand-drawn with a slight imperfection: no pupils, no highlights, no outlines around them, no lashes, no whites, plus a small smile. No people, no text.
```

### `s78_v3_E.txt`

```text
Redraw this exact picture with the same framing and every object in the same position (narrow bed with rails centred, armchair beside it, side table with glass, pills and smiling mug, the cane by the door, the bare tree in the pale blue dawn window, the lamp at the left with its weak warm glow and two small plain black dot eyes and small smile, closed door), same soft hand-made wax crayon and coloured pencil look, thin soft muted blue-brown outlines, never black. Change only the bear: the very old teddy bear now LIES on its back-and-side on the pillow, its head resting on the pillow turned toward the lamp on the left, its body under the pale blanket which is tucked up to its chest so only its head and one paw show on top of the blanket. It is clearly very old: faded fur, a stitched seam across the top of the head, a stitched cross over one eye, one slightly drooping ear, loose threads. Its eyes are open, tired and gentle, a quiet reflective look. Nothing else changes. No sparkles, no text, no people.
```

### `s78_v3_S.txt`

```text
Redraw this exact picture with the same framing and every object in the same position (narrow bed with rails centred, armchair beside it, side table with glass, pills and smiling mug, the cane by the door, the bare tree in the pale blue dawn window, the lamp at the left with its weak warm glow and two small plain black dot eyes and small smile, closed door), same soft hand-made wax crayon and coloured pencil look, thin soft muted blue-brown outlines, never black. Change only the bear and the bed: the pillow is now EMPTY and the blanket is smooth and flat on the bed, with no bear on it. The very old teddy bear now STANDS on the plank floor on the rug at the foot of the bed, in front of the bed's footboard, seen from the front, hunched, shoulders sagging, head slightly bowed, arms hanging down, tired and gentle. It is clearly very old: faded fur, a stitched seam across the top of the head, a stitched cross over one eye, a patch on the belly, a patch on the arm, one slightly drooping ear, loose threads. It is about the size it was on the pillow. Nothing else changes. No sparkles, no text, no people.
```

### `s78_v3_a_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Warm, tender mood. Locked camera, no camera movement, no zoom. One continuous 8-second shot in a quiet old-age bedroom at pale blue dawn. Silent.
STRICT CONTINUITY: everything in the room stays exactly where it is and fixed and rigid: the narrow bed with rails at the centre, the armchair beside it (completely still, never rocking or tipping), the side table with glass, pills and smiling mug, the cane, the pictures, the tree in the window, and the closed wooden door on the right wall, which stays closed. The lamp at the left is a fixed, rigid, solid object like a statue: its pole and shade stay exactly as in the first frame, perfectly straight and upright, it never tilts, bends, leans, bows or moves at all; only its warm glow may softly brighten and dim. Only the old bear, the blanket and the lamp's glow move.
The first frame shows the very old teddy bear (faded fur, stitched seam on its head, stitched cross over one eye, patches on belly and arm) standing hunched on the floor at the foot of the bed, the pillow empty. The last frame shows it lying on the pillow under the blanket, head turned toward the lamp, eyes open. The bear is very old and must clearly read as old throughout: faded dull fur, a visible stitched seam across its head, a stitched cross over one eye, a patch on its belly, a patch on its arm, a drooping ear, a stooped hunched back, stiff slow limbs. It is slow and tired, every movement deliberate with pauses, a gentle reflective expression, nothing theatrical, never playful.
Timing: 0-1.5 s the old bear stands for a moment, breathing slowly, and takes in the room: it slowly turns its head to the window (its whole body stays still, no stepping), then to the pictures, then to the lamp. 1.5-3.5 s it shuffles very slowly and unsteadily, tiny small steps, long pauses along the side of the bed, pausing to rest, swaying a little. 3.5-5.5 s it climbs up the side rails carefully one limb at a time with pauses, always holding on. 5.5-7 s it crawls onto the mattress and slowly lies back onto the pillow in one long slow settle, the blanket coming over it. 7-8 s it lies still, head turned toward the lamp, eyes open, tired and gentle; the blanket rises and falls gently; the lamp's glow trembles slightly (the lamp itself does not move or tilt at all). No people, no text, no sparkles.
```

### `s78_v3_a_clip_run1.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Warm, tender mood. Locked camera, no camera movement, no zoom. One continuous 8-second shot in a quiet old-age bedroom at pale blue dawn. Silent.
STRICT CONTINUITY: everything in the room stays exactly where it is and fixed and rigid: the narrow bed with rails at the centre, the armchair beside it (completely still, never rocking or tipping), the side table with glass, pills and smiling mug, the cane, the pictures, the tree in the window, and the closed wooden door on the right wall, which stays closed. The lamp at the left is one rigid piece: its pole stays straight and upright, it never bends or moves its base. Only the old bear, the blanket and the lamp's glow move.
The first frame shows the very old teddy bear (faded fur, stitched seam on its head, stitched cross over one eye, patches on belly and arm) standing hunched on the floor at the foot of the bed, the pillow empty. The last frame shows it lying on the pillow under the blanket, head turned toward the lamp, eyes open. The bear is very old, slow and tired, every movement deliberate with pauses, a gentle reflective expression, nothing theatrical, never playful.
Timing: 0-1.5 s the old bear stands for a moment, breathing slowly, and takes in the room: it slowly turns its head to the window, then to the pictures, then to the lamp. 1.5-3.5 s it walks slowly and unsteadily along the side of the bed, pausing to rest, swaying a little. 3.5-5.5 s it climbs up the side rails carefully one limb at a time with pauses, always holding on. 5.5-7 s it crawls onto the mattress and slowly lies back onto the pillow in one long slow settle, the blanket coming over it. 7-8 s it lies still, head turned toward the lamp, eyes open, tired and gentle; the blanket rises and falls gently; the lamp's glow trembles slightly and its shade tilts a few degrees toward the bed (the pole stays straight). No people, no text, no sparkles.
```

### `s78_v3_b_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Quiet, tender, reflective mood. Locked camera, no camera movement, no zoom. One continuous 8-second shot in a quiet old-age bedroom. Silent.
STRICT CONTINUITY: everything stays exactly where it is, fixed and rigid: the narrow bed, the armchair (completely still), the side table, the cane, the pictures, the window and tree, and the closed door. The lamp is one rigid piece: its pole stays straight and upright. The very old teddy bear (faded, stitched seam, stitched cross over one eye) lies on the pillow under the blanket the whole time; it never leaves the bed and NEVER sits up or rises: it stays lying down flat on the pillow with its head resting on the pillow and its body under the blanket, always the same small size as in the first frame, never growing larger, never moving closer to the camera. The blanket stays smooth and lying over its body. The lamp is a fixed rigid object that never tilts or moves; only its glow dims.
Timing: 0-1.5 s the old bear lies still, breathing slowly, the blanket rising and falling. 1.5-3.5 s it slowly turns only its head on the pillow a little toward the window and looks for a long moment at the pale light, its body not moving. 3.5-5 s it lifts one small paw only a few centimetres off the blanket toward the lamp and lets it rest on the blanket; its breathing slows, the blanket rising less each time; the lamp's glow flickers once and dims. 5-6.5 s its eyes slowly close; one last slow breath; stillness. 6.5-8 s the room darkens smoothly to a dark blue-grey night (a clean fade, not black), the lamp goes out with its eyes as two soft curved dashes and its smile, the bear lies still with eyes closed. Gentle, quiet, nothing theatrical. No sparkles, no yellow dots, no cable, no wire, no people, no text.
```

### `s78_v3_b_clip_run1.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Quiet, tender, reflective mood. Locked camera, no camera movement, no zoom. One continuous 8-second shot in a quiet old-age bedroom. Silent.
STRICT CONTINUITY: everything stays exactly where it is, fixed and rigid: the narrow bed, the armchair (completely still), the side table, the cane, the pictures, the window and tree, and the closed door. The lamp is one rigid piece: its pole stays straight and upright. The very old teddy bear (faded, stitched seam, stitched cross over one eye) lies on the pillow under the blanket the whole time; it never leaves the bed.
Timing: 0-1.5 s the old bear lies still, breathing slowly, the blanket rising and falling. 1.5-3.5 s it slowly turns its head to the window and looks for a long moment at the pale light. 3.5-5 s it lifts one paw a little toward the lamp and lets it rest on the blanket; its breathing slows, the blanket rising less each time; the lamp's glow flickers once and dims. 5-6.5 s its eyes slowly close; one last slow breath; stillness. 6.5-8 s the room darkens smoothly to a dark blue-grey night (a clean fade, not black), the lamp goes out with its eyes as two soft curved dashes and its smile, the bear lies still with eyes closed. Gentle, quiet, nothing theatrical. No sparkles, no yellow dots, no cable, no wire, no people, no text.
```

### `s78_v3_dark.txt`

```text
Redraw this exact picture with the same framing and every object in the same position, same soft hand-made wax crayon and coloured pencil look, thin soft muted blue-brown outlines, never black. Change only the light: the night has come. The room is now dark blue-grey, softly and evenly darkened (not black, everything still faintly readable), the window faintly pale grey-blue with the tree a dark silhouette. The lamp is switched off: no glow at all, its shade a dull muted cream-grey, its eyes are two short soft curved dashes (closed, sleeping) and its small smile is still there. The old bear still lies on the pillow under the blanket, perfectly still, its eyes now CLOSED, peaceful. Everything else is unchanged and still. No sparkles, no dots of light, no cable, no wire, no people, no text.
```

### `s7_v4_E.txt`

```text
Redraw the first reference image with the same framing, same soft hand-made wax crayon and coloured pencil look on textured paper, thin soft muted blue-brown outlines, never black. Keep the room exactly as in the first reference image: narrow wooden bed with rails centred on the striped rug, side table with glass, pills and smiling mug, the lamp at the left (two small plain black dot eyes, small smile, weak warm glow), cane by the door, closed door, pictures, the bare tree in the pale blue dawn window. ARMCHAIR CHANGE: remove the brown armchair that stands beside the bed. Instead draw the armchair exactly as in the second reference image (a warm rust-orange rounded armchair with a small cushion and a throw blanket), at the right FRONT corner of the room, in the foreground, angled toward the window, between the rug's right edge and the door wall, same design, same size and same place as in the second reference. The space beside the bed is now empty floor and rug. THE BEAR: the same very old teddy bear as in the first reference (faded fur, stitched seam across the head, stitched cross over one eye, patch on belly, patch on arm, one drooping ear), about 200 pixels tall when standing, small relative to the bed: it must stay the same size in every frame. Pose: the old bear LIES flat on its back on the pillow, head resting on the pillow turned toward the lamp at the left, its body lying under the pale blanket which drapes softly and naturally over it, only head and one paw visible; its whole body length is about the same as its standing height (about 200 pixels), so it fills the upper half of the mattress and is NOT enlarged. Eyes open, tired and gentle. No sparkles, no text, no people.
```

### `s7_v4_S.txt`

```text
Redraw the first reference image with the same framing, same soft hand-made wax crayon and coloured pencil look on textured paper, thin soft muted blue-brown outlines, never black. Keep the room exactly as in the first reference image: narrow wooden bed with rails centred on the striped rug, side table with glass, pills and smiling mug, the lamp at the left (two small plain black dot eyes, small smile, weak warm glow), cane by the door, closed door, pictures, the bare tree in the pale blue dawn window. ARMCHAIR CHANGE: remove the brown armchair that stands beside the bed. Instead draw the armchair exactly as in the second reference image (a warm rust-orange rounded armchair with a small cushion and a throw blanket), at the right FRONT corner of the room, in the foreground, angled toward the window, between the rug's right edge and the door wall, same design, same size and same place as in the second reference. The space beside the bed is now empty floor and rug. THE BEAR: the same very old teddy bear as in the first reference (faded fur, stitched seam across the head, stitched cross over one eye, patch on belly, patch on arm, one drooping ear), about 200 pixels tall when standing, small relative to the bed: it must stay the same size in every frame. Pose: the old bear STANDS on the plank floor on the rug at the foot of the bed, in front of the footboard, seen from the front, hunched, head slightly bowed, arms hanging, tired and gentle, standing about as tall as the footboard rail height. The pillow is EMPTY, the blanket smooth and flat. No sparkles, no text, no people.
```

### `s7_v4_a_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Locked camera, no camera movement, no zoom. One continuous 8-second shot in a quiet old-age bedroom. Silent. The first and last frames of the clip equal the supplied start and end stills.
STRICT CONTINUITY: everything stays exactly where it is, fixed and rigid: the narrow bed with rails at the centre, the rust-orange armchair in the right front corner with its cushion, throw and little side table (completely still, never rocking or tipping), the side table with glass, pills and smiling mug, the cane, the pictures, the window and tree, the closed door. The lamp is one rigid piece with a straight upright pole; only its warm glow may breathe. Only the old bear and the blanket move. The bear keeps the SAME small size throughout, it never grows, never nears the camera.
The very old teddy bear (faded fur, stitched seam on its head, stitched cross over one eye, patches on belly and arm, drooping ear) starts standing hunched on the rug at the foot of the bed, the pillow empty, and ends lying on the pillow under the blanket, head turned toward the lamp, eyes open.
Timing: 0-2 s it stands, breathing slowly, turns its head slowly toward the lamp. 2-5 s it walks slowly and stiffly to the side of the bed and climbs UP THE BED RAIL slowly, one limb at a time, always holding on, with pauses. 5-6.5 s it eases onto the mattress. 6.5-8 s it turns and settles down onto the pillow in ONE soft, weighty, slow movement, like a heavy tired body sinking into the pillow; the blanket simply drapes and shifts naturally with its body, resting on it by its own weight; the bear does not pull the blanket mechanically and the blanket never lifts or floats. It ends lying still, eyes open, the blanket rising and falling gently. Slow, tired, gentle, never playful. No sparkles, no people, no text.
IMPORTANT BLANKET RULE (the previous attempt failed here): the blanket is a flat, heavy, tucked-in bedspread that lies on the mattress the whole time, fixed at the foot and sides like a made bed. It does NOT billow, balloon, flap, rise like a sail, lift off the bed, hang over the rail or cover the bear's head. It stays smooth and lies flat on the mattress; the bear crawls on top of it, then slides in under only the top edge near the pillow as it lies down, so that at the end the blanket is drawn up only to the bear's chest exactly as in the end still. The bed looks the same size and shape in every frame.
```

### `s7_v4_a_clip_run1.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Locked camera, no camera movement, no zoom. One continuous 8-second shot in a quiet old-age bedroom. Silent. The first and last frames of the clip equal the supplied start and end stills.
STRICT CONTINUITY: everything stays exactly where it is, fixed and rigid: the narrow bed with rails at the centre, the rust-orange armchair in the right front corner with its cushion, throw and little side table (completely still, never rocking or tipping), the side table with glass, pills and smiling mug, the cane, the pictures, the window and tree, the closed door. The lamp is one rigid piece with a straight upright pole; only its warm glow may breathe. Only the old bear and the blanket move. The bear keeps the SAME small size throughout, it never grows, never nears the camera.
The very old teddy bear (faded fur, stitched seam on its head, stitched cross over one eye, patches on belly and arm, drooping ear) starts standing hunched on the rug at the foot of the bed, the pillow empty, and ends lying on the pillow under the blanket, head turned toward the lamp, eyes open.
Timing: 0-2 s it stands, breathing slowly, turns its head slowly toward the lamp. 2-5 s it walks slowly and stiffly to the side of the bed and climbs UP THE BED RAIL slowly, one limb at a time, always holding on, with pauses. 5-6.5 s it eases onto the mattress. 6.5-8 s it turns and settles down onto the pillow in ONE soft, weighty, slow movement, like a heavy tired body sinking into the pillow; the blanket simply drapes and shifts naturally with its body, resting on it by its own weight; the bear does not pull the blanket mechanically and the blanket never lifts or floats. It ends lying still, eyes open, the blanket rising and falling gently. Slow, tired, gentle, never playful. No sparkles, no people, no text.
```

### `s7_v4_b_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Locked camera, no camera movement, no zoom. One continuous 8-second shot in a quiet old-age bedroom. Silent. The first and last frames of the clip equal the supplied start and end stills.
THE BEAR STAYS LYING DOWN THE WHOLE TIME. The very old teddy bear (faded fur, stitched seam on its head, stitched cross over one eye) lies on the pillow under the blanket from the first frame to the last. It does NOT sit up. It does NOT rise. It does NOT lean up off the pillow. Its back and head stay resting on the pillow and mattress for all 8 seconds. It does NOT grow: it stays exactly the same small size as in the first frame, never larger, never closer to the camera, never taller than the pillow.
STRICT CONTINUITY: the bed, the rust-orange armchair in the right front corner with its cushion, throw and little side table (completely still), the side table with glass, pills and mug, the cane, the pictures, the window and tree, the closed door all stay fixed and rigid. The lamp is a rigid object with a straight upright pole that never moves or tilts; only its glow dims.
Timing: 0-1.5 s the bear lies still, breathing slowly, the blanket rising and falling softly. 1.5-3 s lying down, it gently stretches ONE arm only a little toward the lamp at the left, a small affectionate goodnight, its head and body staying on the pillow. 3-4 s it holds the arm out for a moment. 4-5 s it slowly lowers the arm back onto the blanket. 5-6 s its eyes slowly close, the blanket rising and falling more slowly, it falls asleep. 5-8 s the lamp's glow dims out and goes out (its eyes become two soft curved dashes with its smile), and the whole room fades smoothly to a dark blue-grey night (not black), ending as the last still: lamp off, bear lying asleep with eyes closed. Gentle, quiet, nothing theatrical. No sparkles, no dots, no cable, no people, no text.
CORRECTION (the previous attempt failed here): the bear's head and shoulders stay resting flat on the pillow; its head stays the same small size and never lifts up or forward. Only the forearm and paw move: the forearm lifts a little off the blanket toward the lamp, with the elbow staying on the blanket and the head still on the pillow, then lowers back. The bear is a small bear: its head is smaller than the pillow's width at every moment, and its shoulders never rise above the headboard rail. No sitting, no propping up, no growth.
```

### `s7_v4_b_clip_run1.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Locked camera, no camera movement, no zoom. One continuous 8-second shot in a quiet old-age bedroom. Silent. The first and last frames of the clip equal the supplied start and end stills.
THE BEAR STAYS LYING DOWN THE WHOLE TIME. The very old teddy bear (faded fur, stitched seam on its head, stitched cross over one eye) lies on the pillow under the blanket from the first frame to the last. It does NOT sit up. It does NOT rise. It does NOT lean up off the pillow. Its back and head stay resting on the pillow and mattress for all 8 seconds. It does NOT grow: it stays exactly the same small size as in the first frame, never larger, never closer to the camera, never taller than the pillow.
STRICT CONTINUITY: the bed, the rust-orange armchair in the right front corner with its cushion, throw and little side table (completely still), the side table with glass, pills and mug, the cane, the pictures, the window and tree, the closed door all stay fixed and rigid. The lamp is a rigid object with a straight upright pole that never moves or tilts; only its glow dims.
Timing: 0-1.5 s the bear lies still, breathing slowly, the blanket rising and falling softly. 1.5-3 s lying down, it gently stretches ONE arm only a little toward the lamp at the left, a small affectionate goodnight, its head and body staying on the pillow. 3-4 s it holds the arm out for a moment. 4-5 s it slowly lowers the arm back onto the blanket. 5-6 s its eyes slowly close, the blanket rising and falling more slowly, it falls asleep. 5-8 s the lamp's glow dims out and goes out (its eyes become two soft curved dashes with its smile), and the whole room fades smoothly to a dark blue-grey night (not black), ending as the last still: lamp off, bear lying asleep with eyes closed. Gentle, quiet, nothing theatrical. No sparkles, no dots, no cable, no people, no text.
```

### `s7_v4_dark.txt`

```text
Redraw the first reference image with the same framing and every object in the same position (including the rust-orange armchair at the right front corner exactly as in the second reference), same soft hand-made wax crayon and coloured pencil look, thin soft muted blue-brown outlines, never black. Change only the light: the night has come. The room is dark blue-grey, softly and evenly darkened (not black, everything faintly readable), the window faintly pale grey-blue with the tree a dark silhouette. The lamp is off: no glow, shade a dull muted cream-grey, its eyes two short soft curved dashes (closed) and its small smile still there. The old bear lies on the pillow under the blanket, same small size, perfectly still, eyes CLOSED, peaceful. No sparkles, no dots of light, no cable, no people, no text.
```

### `s7_v6_E.txt`

```text
Redraw the first reference image exactly: same framing, same soft hand-made wax crayon and coloured pencil look, thin soft muted blue-brown outlines. Keep everything identical: the narrow wooden bed with rails, the rust-orange armchair at the right front corner with its side table and mug, the side table with glass, pills and mug, the lamp at the left, the cane, the door, pictures, the bare tree window. Change ONLY the bear's body. THE BEAR MUST BE SLIM: the old bear is the same very old teddy bear (faded fur, stitched seam across the head, stitched cross over one eye, a few patches, one drooping ear), but with a SLIM body like the young bear in the second reference image: slim torso, thin arms and thin legs, a small flat belly, NOT plump, NOT round, NOT fat, small body relative to its head, same head size as before. Pose unchanged: lying on the pillow, head turned toward the lamp, blanket draped softly over a thin small body (the blanket lies low and flat over the slim body), one thin arm visible. Same small overall size. No sparkles, no text, no people.
```

### `s7_v6_S.txt`

```text
Redraw the first reference image exactly: same framing, same soft hand-made wax crayon and coloured pencil look, thin soft muted blue-brown outlines. Keep everything identical: the bed with rails and empty pillow, the rust-orange armchair at the right front corner, side table, lamp, cane, door, window. Change ONLY the bear's body. THE BEAR MUST BE SLIM: the old bear is the same very old teddy bear (faded fur, stitched seam across the head, stitched cross over one eye, a few patches, one drooping ear), but with a SLIM body like the young bear in the second reference image: slim torso, thin arms and thin legs, a small flat belly, NOT plump, NOT round, NOT fat, small body relative to its head, same head size, same standing height. Pose unchanged: standing at the foot of the bed on the rug, hunched, head slightly bowed, arms hanging. No sparkles, no text, no people.
```

### `s7_v6_a_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Locked camera, no camera movement, no zoom. One continuous 8-second shot in a quiet old-age bedroom. Silent. The first and last frames of the clip equal the supplied start and end stills.
STRICT CONTINUITY: everything stays exactly where it is, fixed and rigid: the narrow bed with rails at the centre, the rust-orange armchair in the right front corner with its cushion, throw and little side table (completely still, never rocking or tipping), the side table with glass, pills and smiling mug, the cane, the pictures, the window and tree, the closed door. The lamp is one rigid piece with a straight upright pole; only its warm glow may breathe. Only the old bear and the blanket move. The bear keeps the SAME small size throughout, it never grows, never nears the camera.
The very old SLIM teddy bear with thin limbs and a small body (faded fur, stitched seam on its head, stitched cross over one eye, patches on belly and arm, drooping ear) starts standing hunched on the rug at the foot of the bed, the pillow empty, and ends lying on the pillow under the blanket, head turned toward the lamp, eyes open.
Timing: 0-2 s it stands, breathing slowly, turns its head slowly toward the lamp. 2-5 s it walks slowly and stiffly to the side of the bed and climbs UP THE BED RAIL slowly, one limb at a time, always holding on, with pauses. 5-6.5 s it eases onto the mattress. 6.5-8 s it turns and settles down onto the pillow in ONE soft, weighty, slow movement, like a heavy tired body sinking into the pillow; the blanket simply drapes and shifts naturally with its body, resting on it by its own weight; the bear does not pull the blanket mechanically and the blanket never lifts or floats. It ends lying still, eyes open, the blanket rising and falling gently. Slow, tired, gentle, never playful. No sparkles, no people, no text.
IMPORTANT BLANKET RULE (the previous attempt failed here): the blanket is a flat, heavy, tucked-in bedspread that lies on the mattress the whole time, fixed at the foot and sides like a made bed. It does NOT billow, balloon, flap, rise like a sail, lift off the bed, hang over the rail or cover the bear's head. It stays smooth and lies flat on the mattress; the bear crawls on top of it, then slides in under only the top edge near the pillow as it lies down, so that at the end the blanket is drawn up only to the bear's chest exactly as in the end still. The bed looks the same size and shape in every frame.
```

### `s7_v6_b_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Locked camera, no camera movement, no zoom. One continuous 8-second shot in a quiet old-age bedroom. Silent. The first and last frames of the clip equal the supplied start and end stills.
THE BEAR STAYS LYING DOWN THE WHOLE TIME. The very old SLIM teddy bear with thin limbs and a small body (faded fur, stitched seam on its head, stitched cross over one eye) lies on the pillow under the blanket from the first frame to the last. It does NOT sit up. It does NOT rise. It does NOT lean up off the pillow. Its back and head stay resting on the pillow and mattress for all 8 seconds. It does NOT grow: it stays exactly the same small size as in the first frame, never larger, never closer to the camera, never taller than the pillow.
STRICT CONTINUITY: the bed, the rust-orange armchair in the right front corner with its cushion, throw and little side table (completely still), the side table with glass, pills and mug, the cane, the pictures, the window and tree, the closed door all stay fixed and rigid. The lamp is a rigid object with a straight upright pole that never moves or tilts; only its glow dims.
Timing: 0-1.5 s the bear lies still, breathing slowly, the blanket rising and falling softly. 1.5-3 s lying down, it gently stretches ONE arm only a little toward the lamp at the left, a small affectionate goodnight, its head and body staying on the pillow. 3-4 s it holds the arm out for a moment. 4-5 s it slowly lowers the arm back onto the blanket. 5-6 s its eyes slowly close, the blanket rising and falling more slowly, it falls asleep. 5-8 s the lamp's glow dims out and goes out (its eyes become two soft curved dashes with its smile), and the whole room fades smoothly to a dark blue-grey night (not black), ending as the last still: lamp off, bear lying asleep with eyes closed. Gentle, quiet, nothing theatrical. No sparkles, no dots, no cable, no people, no text.
CORRECTION (the previous attempt failed here): the bear's head and shoulders stay resting flat on the pillow; its head stays the same small size and never lifts up or forward. Only the forearm and paw move: the forearm lifts a little off the blanket toward the lamp, with the elbow staying on the blanket and the head still on the pillow, then lowers back. The bear is a small bear: its head is smaller than the pillow's width at every moment, and its shoulders never rise above the headboard rail. No sitting, no propping up, no growth.
```

### `s7_v6_dark.txt`

```text
Redraw the first reference image exactly with every object in the same position, same soft wax crayon look. Change only the light: the night has come. Room dark blue-grey, softly evenly darkened (not black, everything faintly readable), window faintly pale grey-blue with the tree a dark silhouette. The lamp is off: no glow, dull cream-grey shade, eyes two short soft curved dashes, small smile. The slim old bear lies on the pillow under the blanket exactly as in the reference, slim and small, perfectly still, eyes CLOSED, peaceful. No sparkles, no dots of light, no cable, no people, no text.
```

### `s7_v7_b_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, animated on twos with a slow, tender, quiet feel. Thin, soft muted blue-brown outlines, never black. Locked camera, no camera movement, no zoom. One continuous 8-second shot in a quiet old-age bedroom. Silent. The first and last frames of the clip equal the supplied start and end stills.
THE BEAR STAYS LYING DOWN THE WHOLE TIME. The very old SLIM teddy bear with thin limbs and a small body (faded fur, stitched seam on its head, stitched cross over one eye) lies on the pillow under the blanket from the first frame to the last. It does NOT sit up. It does NOT rise. It does NOT lean up off the pillow. Its back and head stay resting on the pillow and mattress for all 8 seconds. It does NOT grow: it stays exactly the same small size as in the first frame, never larger, never closer to the camera, never taller than the pillow.
STRICT CONTINUITY: the bed, the rust-orange armchair in the right front corner with its cushion, throw and little side table (completely still), the side table with glass, pills and mug, the cane, the pictures, the window and tree, the closed door all stay fixed and rigid. The lamp is a rigid object with a straight upright pole that never moves or tilts; only its glow dims.
Timing: 0-1.5 s the bear lies still, breathing slowly, the blanket rising and falling softly. 1.5-3 s lying down, it lifts ONE short forearm a little toward the lamp at the left, bending at the elbow, a tiny affectionate goodnight wave, its head and body staying on the pillow. 3-4 s it holds the arm out for a moment. 4-5 s it slowly lowers the arm back onto the blanket. 5-6 s its eyes slowly close, the blanket rising and falling more slowly, it falls asleep. 5-8 s the lamp's glow dims out and goes out (its eyes become two soft curved dashes with its smile), and the whole room fades smoothly to a dark blue-grey night (not black), ending as the last still: lamp off, bear lying asleep with eyes closed. Gentle, quiet, nothing theatrical. No sparkles, no dots, no cable, no people, no text.
CORRECTION (the previous attempt failed here): the bear's head and shoulders stay resting flat on the pillow; its head stays the same small size and never lifts up or forward. Only the forearm and paw move: the forearm lifts a little off the blanket toward the lamp, with the elbow staying on the blanket and the head still on the pillow, then lowers back. The bear is a small bear: its head is smaller than the pillow's width at every moment, and its shoulders never rise above the headboard rail. No sitting, no propping up, no growth.

ARM LENGTH (the previous attempt failed here: the arm stretched to about three times its length): the bear's arms are SHORT, STUBBY plush arms, each only about as long as the bear's head, exactly the same length as in the first frame and as in all earlier scenes. The arm NEVER stretches, lengthens, extends or reaches across the room. The goodnight gesture is made only by bending the elbow and raising the short forearm and paw a few centimetres off the blanket, the paw staying close to the bear, nowhere near the lamp, then lowering it again. Both arms keep the same short length in every single frame.
```

### `s08_clip.txt`

```text
A hand-made animation of marker, wax crayon and torn paper, like a sketchbook come to life: wobbly marker outlines and crayon grain that gently shimmer and re-draw themselves every frame, animated on twos. Locked camera, no camera movement, no zoom. One continuous 6-second shot of a quiet old-age room at the very end, a pale white dawn window, the room slowly falling into darkness.
STRICT CONTINUITY: nothing appears, disappears, teleports or changes place. The narrow single bed with side rails stays at the centre of the rug the whole time, the worn teddy bear lies on its pillow the whole time. The armchair stays beside the bed, the side table with the glass, pill bottle and mug stays next to it, the cane stays leaning by the door. The floor lamp stays at the left, leaning over the bed, standing on its round base. The closed wooden door stays on the right wall, always visible and closed. The lamp has NO electrical cable, NO wire and NO cord anywhere: only its straight pole, its pull chain with beads and its round base, and nothing ever grows out of it or trails from it. The lamp's pole stays still and does not bend; only its eyes and its glow change. The window, walls, rug and floor never change.
0 to 1 second: total stillness; only the crayon grain boils. The lamp glows weakly, eyes open, smiling.
At 1 second the lamp slowly looks around, its eyes drifting left then right, one last time.
At 2 seconds its light gently flickers once.
At 3 seconds a second gentle flicker.
At 4 seconds the glow slowly dims.
At 5 seconds one final flicker, the light goes out, the lamp's eyes close into sleeping arcs with the smile remaining, and the room is in darkness, only the white window lightly visible.
Everything else stays perfectly still the whole time. No people, no text, no sound.
```

### `s08_end.txt`

```text
Edit the attached picture into the next moment of the very same room, same hand-made marker, wax-crayon and torn-paper style, same framing, everything in exactly the same place: the single bed with rails at the centre of the rug with the worn bear on the pillow, the armchair beside it, the side table with the glass, pill bottle and mug, the cane by the door, the tall floor lamp at the left leaning over the bed, the closed door on the right wall, the window and walls. Changes: the room is now DARK, deep dim blue-grey shadow over everything, no warm light anywhere. The lamp's glow is completely out: its shade is dull grey-cream, its two eyes are now CLOSED like sleeping arcs, and its small smile is still there. The window is still pale white and is the only lightly lit thing, casting a faint pale glow on the sill and a little on the floor. Same wobbly marker outlines, crayon grain, imperfect hand-made feel. No people, no text.
```

### `s08_start.txt`

```text
Edit the attached picture into the quiet final moment of an old-age version of the very same room, in exactly the same hand-made marker, wax-crayon and torn-paper style, same framing, same four-pane window, back wall, side walls, plank floor and striped rug, same wobbly marker outlines and crayon grain. Remove the cradle. In its place, at the exact centre of the rug, stands a narrow single bed with wooden side rails, a plain faded blanket and a pillow; a small WORN teddy bear (brown, button eyes, a stitched seam and a round patch on its belly) lies on the pillow. A worn, sagging armchair stands right beside the bed on its right side, on the rug edge. A small round side table with curly legs stands next to the armchair with a glass of water and a small pill bottle on it, and a small cream mug with a tiny smiling face. A wooden cane leans against the right wall beside the door. The tall floor lamp stays at the left of the picture, its pole leaning over towards the bed, cream trapezoid shade with a pull chain with beads, its two dot eyes open and a small smile, glowing only very weakly, a faint pale yellow glow. The window is filled with pale blank white dawn light, no tree, no stars, no moon. The wooden door on the right wall is CLOSED and clearly visible, with its round doorknob. Faded, pale, quiet colours: soft blue-grey walls, cream, a little ochre, no strong orange anywhere. Everything is still. No people, no text.
```

### `s08_v2_clip.txt`

```text
Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy, thin soft muted blue-brown outlines, never black, gentle crayon grain, warm tender mood. One continuous 6-second shot, locked camera, no camera movement, no zoom, silent.
STRICT CONTINUITY: nothing appears, disappears, teleports or changes place. The narrow bed with the worn bear on the pillow stays at the centre of the rug. The armchair, side table with glass, pills and mug, the cane and the closed door on the right wall stay exactly where they are and completely still. The window, walls, rug and floor never change. The floor lamp stays at the left on its round base. The lamp is one rigid piece: its pole stays straight and upright and never bends; it does not hop or move, only its two eyes and its glow change. No sparkles, no dots of light, no specks, no cable, no wire, no cord, no extra objects, no people, no text.
Motion script. 0 to 1 second: total stillness, the lamp glows weakly and softly, its eyes are two plain small black dots with a small smile. 1 to 2.2 seconds: the two dot eyes slowly glance to the left, then to the right, looking around the room one last time. 2.2 seconds: the glow gives one gentle flicker, dimming a little and returning. 2.2 to 3.8 seconds: the glow slowly and steadily dims. 3.8 seconds: one last small flicker. 4 to 5.2 seconds: the lamp goes out, its glow fades away and the whole room darkens smoothly and evenly in one clean fade to a dark blue-grey, never black, everything still faintly visible, the window staying faintly pale. At 5 seconds the two dot eyes softly close into two short soft curved dashes, the small smile remains. 5.2 to 6 seconds: held still in the dark blue-grey room. Everything else in the room stays perfectly still the whole time.
```

### `s08_v2_end.txt`

```text
Redraw this exact picture with the same framing and every object in the same position, same soft hand-made wax crayon and coloured pencil look, thin soft muted blue-brown outlines, never black. Change only the light: the night has come. The room is now dark blue-grey, softly and evenly darkened (not black, everything still faintly readable), the window faintly pale grey-blue. The lamp is switched off: no glow at all, its shade a dull muted cream-grey, its eyes are two short soft curved dashes (closed, sleeping) and its small smile is still there. Everything else is unchanged and still. No sparkles, no dots of light, no cable, no wire, no people, no text.
```

### `s08_v2_start.txt`

```text
Redraw this exact picture: keep every object and every position exactly the same (window centred with a sill, plank floor, striped rug, narrow bed with rails and the worn bear on the pillow, armchair, side table with glass, pills and the small smiling mug, cane by the door, door on the right wall closed, floor lamp at the left with a pull chain, the framed drawings on the left wall). Same framing, no zoom. Hand-made drawing in soft wax crayon and coloured pencil on textured paper, gentle, delicate and slightly dreamy. Thin, soft outlines in a muted dark blue-brown, never black, about half as thick as before, slightly broken and feathered, not dominant. Gentle crayon grain, softly blended warm light, subtle torn-paper wall patches. Not vector, not polished, not glossy, not digitally rendered. Warm, tender mood. Limited palette: ultramarine, navy, cream, orange, ochre, brown. The lamp is glowing weakly and softly, its eyes are two small plain black dots, hand-drawn with a slight imperfection, no pupils, no highlights, no outlines around them, no lashes, plus a small smile. Window pale white-blue. No sparkles, no dots of light, no cable, no wire, no people, no text.
```

### `B2_end.txt`

```text
Edit the attached picture into the next moment of the very same room, same hand-made marker, wax-crayon and torn-paper style, same framing, everything in exactly the same place: the cradle at the centre of the rug, the bear on the sill, the lamp at the left, the window, the walls and the door on the right wall. Changes: the door on the right wall is now OPEN, swung inward, still clearly visible as a wooden door, and warm orange crayon light spills through it across the floor and onto the rug; the moonlight streaks on the rug turn golden. The lamp is now switched ON: its shade glows warm yellow with a pool of yellow crayon light on the wall, its two eyes are wide open and smiling. The bear stays seated, its head tilted slightly toward the cradle. Same wobbly marker outlines, crayon grain, imperfect hand-made feel. No people, no text.
```

### `B2_start.txt`

```text
Edit the attached picture into the NIGHT, LAMP-OFF version of the very same room, in exactly the same hand-made marker, wax-crayon and torn-paper style, same framing, same window, walls, doodles, floor and striped rug. Keep in place, exactly where they are: the wooden cradle at the centre of the rug, the teddy bear sitting on the window sill, the tall floor lamp at the left. Changes: the lamp is switched OFF (shade pale and dull, no glow, its two eyes closed like sleeping arcs, a calm sleeping smile); no warm orange or yellow light anywhere; the room is cold and dark blue lit only by pale blue moonlight with a few pale moonlight streaks on the rug and floor; the bear sits upright with its head level. ADD a tall wooden door on the right wall, drawn in the same marker and crayon style in perspective, CLOSED, with a round doorknob, a dark crack of shadow beneath it. Same wobbly marker outlines, crayon grain, imperfect hand-made feel. No people, no text.
```

### `chars_v5.txt`

```text
Original character design sheet in the style of classic hand-drawn feature animation cels: clean, graphic, bright and vector-clean. Three living household objects side by side on a plain white background, full body, dynamic acting poses.
RENDERING RULES (very important): a bold, continuous, even-weight dark-brown ink outline around every shape, like clean cel ink. Flat saturated local colours with exactly one hard-edged shadow tone and one crisp highlight tone per shape. Glossy metal and glaze shown as simple clean white highlight shapes. NO texture, NO paper grain, NO brush strokes, NO fur strands, NO soft gradients, NO airbrush, NO painterly rendering, NO photoreal lighting. High-key bright saturated colours.
FACES: big white oval eyes with black pupils and a tiny white glint, a heavy upper eyelid line, thick expressive eyebrows, a very large mouth with dark red inside, a pink tongue and a few teeth, set into the object's form. Arms are thin tubular parts of the object ending in small simple mitten hands.
LEFT, a cheerful floor lamp: a cream conical lampshade is the head with the face built into it, a golden brass pole in a springy S-curve, a golden collar that makes an elbow, one thin brass arm with a small mitten hand, the other hand holding a beaded pull chain, an ornate round golden foot, mid-hop with squash and stretch, the shade glowing warm lemon yellow.
MIDDLE, a gentle sad teddy bear: a round plush bear in flat warm brown with a lighter tan belly and muzzle, a stitched seam and a square patch on the belly, big sad white eyes with heavy lids, brows raised in the middle, small mouth turned down, sitting slumped with its head tilted.
RIGHT, a funky coffee mug: a cream ceramic mug with the face on the front and a huge grin, the handle forms one arm resting on its hip, two thin legs with round shoes, brown coffee sloshing over the rim, a curl of steam, hips swaying.
Appealing, exaggerated, caricatured, simple strong silhouettes. Original characters. No text, no people, no 3D render.
```

### `clip_B2.txt`

```text
A hand-made animation of marker, wax crayon and torn paper, like a sketchbook come to life: wobbly marker outlines and crayon grain that gently shimmer and re-draw themselves every frame, animated on twos. Locked camera, no camera movement, no zoom. One continuous 6-second shot of a quiet night room waking up.
STRICT CONTINUITY: nothing appears, disappears, teleports or changes place. The cradle stays at the centre of the rug the whole time. The teddy bear stays seated on the window sill the whole time. The floor lamp stays at the left, standing on its round base. The door stays on the right wall, always visible. The window, walls, rug and floor never change.
0 to 1 second: the room is cold, dark and still; only the crayon grain boils and the moonlight streaks shimmer. The lamp is asleep, eyes closed.
At 1 second the door on the right wall slowly swings open on its hinges, the door staying visible, and warm orange light spills in across the floor and rug, turning the moonlight streaks golden.
At 2 seconds the cradle rocks gently a couple of times and its blanket stirs.
At 2.8 seconds the bear slowly turns its head toward the cradle with a quiet, loving, slightly wistful look, and stays seated.
At 3.5 seconds the lamp wakes: its eyes open, it blinks, then it crouches slightly and hops once in place on its round base with a springy bounce, bobbing happily, its pull chain swinging, its shade lighting up warm yellow with a glow on the wall, and it smiles.
From 5 seconds everything settles into the final image: door open with warm light, lamp glowing, bear watching the cradle. No people, no text, no sound.
```

### `clip_B2_creative.txt`

```text
A hand-made animation of marker, wax crayon and torn paper, like a sketchbook come to life, animated with exaggerated, expressive hand-drawn animation principles: strong anticipation before every action, squash and stretch, overshoot and settle, secondary motion that follows through (swinging chain, flapping blanket, bouncing ears), held poses and snappy timing, on twos. Marker lines and crayon grain re-draw themselves every frame. Locked camera, no camera movement, no zoom. One continuous 6-second shot: a cold night room wakes up, told through the characters' acting.
STRICT CONTINUITY: nothing appears, disappears, teleports or changes place. The cradle stays at the centre of the rug. The teddy bear stays seated on the window sill. The floor lamp stays at the left on its round base. The door stays on the right wall, always visible. The window, walls, rug and floor never change.
0 to 1 second: cold, silent and still. The sleeping lamp's shade nods slowly up and down with each sleeping breath, eyes closed. The bear gives a tiny shiver in the cold, its ears twitching. Moonlight shimmers on the rug.
At 1 second the door gives a nervous little shake, creaks, and swings open slowly on its hinges, always visible. A warm orange beam spreads across the floor in a ripple, dust sparkling in the light.
At 1.8 seconds the warm light slides over each thing in turn like a gentle hand: the rug turns golden, the cradle's blanket flutters and the cradle rocks twice, the bear's ears perk straight up and its eyes go wide, and it sits up straighter.
At 2.8 seconds the bear leans forward and tilts its head with a tender, wondering look at the cradle, then glances at the lamp.
At 3.3 seconds the lamp wakes in a big comic stretch: the shade rises and stretches up with a yawn, the pole stretches tall, the eyes pop open, it blinks twice, looks around, confused, spots the cradle, and its mouth opens in delight. It crouches low in anticipation, squashing down, then springs up in one joyful hop with the shade glowing brighter, landing with a squash and a bounce, the pull chain swinging in follow-through.
At 5 seconds the lamp winks at the bear, the bear gives a small happy nod, and everything settles into the final picture: door open with warm light, lamp glowing, bear watching over the cradle. No people, no text, no sound.
```

### `clip_B_first6.txt`

```text
A hand-made animation of marker, wax crayon and torn paper, like a sketchbook come to life: wobbly marker outlines and crayon grain that gently shimmer and re-draw themselves every frame (hand-drawn line boil), animated on twos, slightly jerky and charming, like cut-out and stop-motion paper. Locked camera, no camera movement, no zoom. One continuous 6-second shot in which a cold, empty night room comes alive.
0 to 1.2 seconds: the cold room is still, the pale moonlight streaks shimmer faintly on the rug, the crayon grain boils.
At 1.2 seconds a warm orange bar of light slides in from the right edge, as if a door has opened off-screen, and the moonlight streaks on the rug turn golden.
At 1.8 seconds a small wooden cradle pops onto the rug with a squashy bounce, rocks twice and settles; its blanket flutters.
At 3.0 seconds a teddy bear drops onto the window sill with a small soft bounce, then slowly tilts its head down toward the cradle, a quiet, loving, slightly wistful look.
At 3.8 seconds the tall floor lamp at the left pops in, crouches in anticipation, then hops once on its round base with a springy bounce, its two dot eyes and smile appear, it blinks, bobs happily, its pull chain swinging, and its shade lights up warm yellow, painting a pool of yellow crayon light on the wall.
Everything moves with squash and stretch, anticipation and follow-through. Each character has its own tempo: the lamp quick and bouncy, the bear slow and small, the cradle gentle. The window, walls, sill, rug and floor never change position. The final frame matches the end image. No people, no text, no sound.
```

### `end_v5.txt`

```text
Clean graphic cel-animation frame in the style of classic hand-drawn feature animation. Use the FIRST reference image (the empty night room) as the exact background: keep the window, curtains, sill, walls, floor and rug in the same positions, same framing, same clean flat style. Use the SECOND reference image only for the designs of the lamp and the teddy bear: keep their designs, faces, outlines and rendering exactly, in the same clean cel style as the room.
Add to the room: the cheerful golden floor lamp with the cream conical shade and big expressive face, standing at the far left of the room, mid-hop with a happy bounce, one hand waving, the shade glowing warm lemon yellow and casting a flat warm yellow pool of light on the wall and floor; the sad teddy bear sitting on the right end of the wide window sill, head tilted toward the room with a longing look; a small wooden cradle with a hood and a golden-yellow blanket standing on the rug, with a mobile of three small yellow stars above it. A flat warm orange shaft of light enters from the right edge across the floor, turning the moonbeams on the rug golden.
Same rendering rules everywhere: bold even dark outlines, flat saturated colours with hard-edged two-tone shading, no texture, no grain, no gradients, no painterly look. No people, no text, no other furniture, no 3D render, no photoreal, no purple, no pink.
```

### `hand_A.txt`

```text
A frame from a hand-illustrated animated picture book, made by a real illustrator, not a machine. Painted by hand in opaque gouache with a loose brush and drawn with a dip pen and brown-black ink on slightly rough, warm paper. Use the first attached sketch for the room layout (keep it: one-point perspective, a four-pane window centred on the back wall with a wide sill, a plank floor, a striped rug) and the other attached sketches only for the shapes of the characters: a tall floor lamp with a trapezoid shade, a smiling face and a pull chain; a teddy bear with button eyes sitting on the sill.
THE HAND-MADE FEEL (very important): uneven, wobbly ink lines that vary in thickness and sometimes overshoot or break; colour fills that do not quite reach the lines, with small gaps of bare paper and visible brush marks; slightly crooked window frame and floorboards, nothing perfectly straight or symmetric; a few pencil construction lines left visible; some areas deliberately left loose and unfinished, with detail only where the eye should go; flat patches of colour, only a limited palette of six or seven colours: deep ultramarine, navy, warm cream, ochre yellow, burnt orange, brown and a little brick red. Naive, charming, personal, a little imperfect. NOT glossy, NOT airbrushed, NOT rendered, NOT symmetrical, NOT over-detailed, no gradients, no sparkles, no lens effects.
Scene: a cold blue night room, the window with simple white star dots and a crescent moon, a small wooden cradle on the striped rug, the lamp at the left glowing warm yellow with a simple painted pool of light, the bear on the sill, a stripe of orange light from the right. No people, no text.
```

### `hand_B.txt`

```text
A frame drawn by an illustrator on paper with thick felt marker, wax crayon and torn paper collage, like the roughs in a designer's sketchbook: the sketchbook feel of a personal short film, not a finished studio picture. Use the first attached sketch for the room layout (keep it: one-point perspective, a four-pane window centred on the back wall with a wide sill, a plank floor, a striped rug) and the other attached sketches for the shapes of the characters: a tall floor lamp with a trapezoid shade, a smiling face and a pull chain; a teddy bear with button eyes sitting on the sill.
THE HAND-MADE FEEL (very important): thick confident marker outlines that wobble, with the ink pooling at corners; crayon colour scribbled over paper texture with the grain showing through; big simple shapes with patches that miss the edge; torn-paper textures for the walls; small scribbled doodles and marks; a loose, spontaneous, imperfect, human line. Limited palette: ultramarine, navy, cream, bright orange, yellow ochre, brown. NOT clean vector, NOT glossy, NOT airbrushed, NOT rendered, NOT symmetric, no gradients, no sparkles, no glow filters.
Scene: a cold blue night room, a four-pane window with scribbled stars, a small cradle on the striped rug, the lamp at the left lit warm yellow, the bear on the sill, a bar of orange light from the right. No people, no text.
```

### `hand_B_empty.txt`

```text
Edit the attached picture into the EMPTY, COLD, DARK version of the very same room, in exactly the same hand-made marker, wax-crayon and torn-paper style. Keep everything about the room identical: the same window, sill, torn-paper walls, scribbled doodles, wooden floor, striped rug, framing and line quality. REMOVE: the floor lamp, the teddy bear, the cradle and its blanket, all the warm orange and yellow light, the orange bar of light on the right and the glowing wall. In their place: the same wall and floor in cold dark blue crayon, a quiet empty room lit only by pale blue moonlight, with four pale blue-white crayon streaks of moonlight lying across the rug and floor. The rug stripes become dull cream and muted orange. Stars and moon stay in the window. Same wobbly marker outlines, same crayon grain, same imperfect hand-made feel. No people, no text, no new objects.
```

### `room_v5.txt`

```text
Background plate for classic hand-drawn feature animation: clean, graphic, bright cel-animation background, redrawn from the attached rough sketch of an EMPTY cosy room at night. KEEP THE SKETCH LAYOUT EXACTLY: one-point perspective, a large four-pane window centred on the back wall with a wide wooden sill, a plank floor, a striped rug, same positions and sizes.
RENDERING RULES: clean coloured ink linework (dark blue-brown lines, not black) around every shape, flat saturated colour fills with simple hard-edged shadow shapes and soft gentle watercolour variation only inside large areas. NO oil-paint texture, NO grain, NO photoreal lighting, NO heavy gradients. Bold, graphic, readable shapes like a storybook cartoon background.
Colours: walls in rich saturated ultramarine and deep navy blue, wooden window frame and plank floor in warm orange-brown wood with simple plank lines, a woven rug with golden-yellow and brick-red stripes and little fringe, blue floral-patterned curtains tied back with a sash on both sides of the window, a night sky with a big round pale moon and simple white stars and a few simple tree silhouettes, four pale snow-blue vertical moonbeams lying on the floor and rug as flat hard-edged shapes. Warm and inviting despite the night.
Nothing else in the room: no furniture, no people, no text, no 3D render, no photoreal, no purple, no pink.
```

### `title_card.txt`

```text
A black chalkboard background, deep matte black, with the words "lifetime in one little room" hand-written in white chalk across the middle: loose, slightly uneven, childlike but careful handwriting, soft dusty chalk strokes with the grain of the board showing through, a tiny hand-drawn chalk underline beneath the words. Only these words, in lower case, exactly spelled: lifetime in one little room. Nothing else on the picture: no other text, no border, no pictures, no people. Centered, wide cinematic frame, lots of empty black space.
```

### `title_card_a.txt`

```text
A black chalkboard background, deep matte black, with the words "a lifetime in one little room" hand-written in white chalk across the middle: loose, slightly uneven, childlike but careful handwriting, soft dusty chalk strokes with the grain of the board showing through, a tiny hand-drawn chalk underline beneath the words. Only these words, in lower case, exactly spelled: a lifetime in one little room. Nothing else on the picture: no other text, no border, no pictures, no people. Centered, wide cinematic frame, lots of empty black space.
```

## Part 2 - Prompts typed to Claude

### 1. 2026-11-05 12:12 UTC (planning session)

> so lets say we build the movie in 1080P then we could upscale it to 4K at the end ?

### 2. 2026-11-05 12:13 UTC (planning session)

> alright and for editing ? what should we do ?

### 3. 2026-11-05 12:20 UTC (planning session)

> [Image #1] connect to this

### 4. 2026-11-05 13:02 UTC (planning session)

> everything is prepared to win ? cutting software etc ?

### 5. 2026-11-05 13:02 UTC (planning session)

> install everything that we might need

### 6. 2026-11-05 13:20 UTC (planning session)

> give me link

### 7. 2026-11-05 13:22 UTC (planning session)

> no the link where and what i still need to install

### 8. 2026-11-05 13:30 UTC (planning session)

> Add ElevenLabs to my project: run `npx -y @elevenlabs/cli@latest onboard init` and follow what it prints.

### 9. 2026-11-05 13:30 UTC (planning session)

> u have access to everything now right ?

### 10. 2026-11-05 17:04 UTC (build session)

> a tema a versenyen valtozas , animaciot szeretnenk , keress nekunk erdekes topicokat . amire fel tudunk epiteni 60 masodperces kisfilmet

### 11. 2026-11-05 17:06 UTC (build session)

> Please analyze further the fifth and the eighth items, and please try to come up with three different storylines. In one of the storylines, please try to mix up the fifth and the eighth one.

### 12. 2026-11-05 17:06 UTC (build session)

> This ain't good. Please try to loop on it for, I don't know, a couple of minutes, 5 minutes, please, at least. Try to back the stories and see what is possible and how we could make this animation within a 4-hour frame.

### 13. 2026-11-05 17:10 UTC (build session)

> please create artifact we could read

### 14. 2026-11-05 17:11 UTC (idea session)

> https://www.youtube.com/watch?v=G3kIas8ooUQ -> Could you analyze this YouTube video? Could you find out what the style of that is and how we could recreate the style of this video and this animation?

### 15. 2026-11-05 17:13 UTC (build session)

> Still, I'm unable to open it.

### 16. 2026-11-05 17:13 UTC (idea session)

> No, this is not enough. Please, would you be able to go in depth and try to figure it out? Maybe Google it and try to figure it out. What's the style of this, and how could we prompt to recreate something similar?

### 17. 2026-11-05 17:18 UTC (build session)

> We have decided that we would like to go with the room, and we want to build. I want you to figure out at least five different variations of what we could do. What we imagine is that we have the room that is fixed, but the storyline is changing within that room. I want you to create five different ideas that we could animate.

### 18. 2026-11-05 17:18 UTC (idea session)

> Are you able to create an artifact so we could check the design elements and the prompts and all that?

### 19. 2026-11-05 17:19 UTC (build session)

> Be able to put it into an artifact so it's much easier to read.

### 20. 2026-11-05 17:21 UTC (build session)

> I have an issue with opening the artifacts, please. Is it okay if we create them so that they do not ask us to log in?

### 21. 2026-11-05 17:25 UTC (build session)

> We are kind of sure about the room, but I think we are finding all the ideas too generic. We need some unique way that probably is not going to be presented by any of the competitors, and we would like to come up with a storyline for 60 seconds. We kind of want to tell a story within 60 seconds.

### 22. 2026-11-05 17:26 UTC (idea session)

> Unable to open the link. Please make it publishable so that we don't need to log in.

### 23. 2026-11-05 17:29 UTC (build session)

> Would you be able to come up with ideas where we are changing the room itself, but with the room and the background? We want to build up a story where we are not focusing on the people, but we are focusing on the room itself: how the room is changing, what is changing in the room, and build up a story around it.

### 24. 2026-11-05 17:37 UTC (build session)

> We have figured out the story. The story is that the room is fixed, and we don't put any people in it. We just go from birth to death. We are representing, with the change of the room, that one person was born here. We follow throughout his/her life, and we change the room around it based on the years of his living. We want to build up a story around it.
> 
> The room is fixed, and the things in the room are changing. The things in the room are alive, and we are going to draw the things in the room.

### 25. 2026-11-05 17:41 UTC (build session)

> We are a two-person team. One of my teammates is a designer who will create the items. What would she need to do? Please create a task list. I'm a programmer, and I will be prompting the video. What do I need to do?

### 26. 2026-11-05 17:47 UTC (build session)

> We don't have infinite time. Could you help us in terms of what items we should draw, what items we shouldn't, and what items we should just prompt? We have decided on the design. 
> 
> The design is here. The design is here. /Users/zoltanfodor/Developer/change-short/style-board.html

### 27. 2026-11-05 17:51 UTC (build session)

> Could you tell me if there's a better model than Sedans 2.5 now for putting together videos?

### 28. 2026-11-05 17:52 UTC (build session)

> Could you pull the ElevenLabs prices in terms of token usage and see how we should build up and which model we should use for what? How are we going to connect these dots so the AI is not going to change the room layout, just the items within it, and we'll know that we are putting together one project?

### 29. 2026-11-05 17:55 UTC (build session)

> And we haven't decided on the music under it, or I don't know what we should do with that. Could you figure out the sound effect for this animation for the entire 6th second?

### 30. 2026-11-05 18:02 UTC (build session)

> [Image #6]Here's the sketch for the layout for the room. We want to have something like that. Could we maybe, for trying out, start putting together the first 6 seconds of the video? See if the direction that we want is the correct one.

### 31. 2026-11-05 18:04 UTC (idea session)

> You got the updated storyline. ? One simple change: instead of a toy bird, we want to use a toy teddy bear. Please change that in the storyline.md file.

### 32. 2026-11-05 18:06 UTC (idea session)

> §It's still missing for you to put together the first 6 seconds of the video. Could you tell me also: did you get the layout?

### 33. 2026-11-05 18:11 UTC (build session)

> Pushing everything to the repository, right?

### 34. 2026-11-05 18:19 UTC (build session)

> [Image #8] [Image #9] [Image #10] [Image #11] [Image #12] [Image #13] [Image #14] [Image #15]There are some assets. please create an assets folder and we gonna put here the items we kinda wanna build around and make it live , also we gonna sSoon, we're going to send some Figma files where we are compiling all the assets that we found interesting, and we want to use those assets as examples. Put together the structure that we're going to use those Figma file references.

### 35. 2026-11-05 18:26 UTC (build session)

> /Users/zoltanfodor/Downloads/characters\ figma.svg Here's the first file for Figma where we found some examples for characters.

### 36. 2026-11-05 18:28 UTC (build session)

> So, you need character notes, or should we compile that, or are you going to compile that? Also, give me the setup or the situation on ElevenLabs, and also, how can I compact?

### 37. 2026-11-05 18:29 UTC (idea session)

> is elevenlabs mcp working ? can u connect to it ?

### 38. 2026-11-05 18:30 UTC (build session)

> /compact

### 39. 2026-11-05 18:30 UTC (build session)

> <command-name>/compact</command-name>
>             <command-message>compact</command-message>
>             <command-args></command-args>

### 40. 2026-11-05 18:35 UTC (build session)

> [Request interrupted by user for tool use]

### 41. 2026-11-05 18:41 UTC (build session)

> Could we enable ByteDance models? Should we do it?

### 42. 2026-11-05 18:42 UTC (build session)

> Should we do it on the ElevenLabs platform? Also, how much credit did we use for this snippet?

### 43. 2026-11-05 18:43 UTC (build session)

> okay so basically we have to use the 600K credits otherwise we gonna be outsde of the competiton -> so basically i want you to first put together here without using any credits somehow then when we have it we will use the tokens from elevenlabs

### 44. 2026-11-05 18:49 UTC (build session)

> /Users/zoltanfodor/Downloads/karakterek.md Here are some of the characteristics of the characters within our movie. Please split them into separate characters, and if you find any gaps, feel free to add additional things.

### 45. 2026-11-05 18:51 UTC (build session)

> Seedance is not available for some reason. Could you help mewhy? 
> 
> <pasted_content id="3013">
> Seedance models are available via the ElevenLabs API, but they are disabled by default and require explicit approval to use.
> 
> According to ElevenLabs documentation, ByteDance models (including Seedance 2.0, 2.0 Fast, 2.0 Mini, and 2.5) are disabled for API users by default due to regional and regulatory constraints. To enable them:
> 
> You must contact ElevenLabs support to request access. 
> Enterprise customers can specifically contact support to request access. 
> Some models (like Seedance 2.0 Fast and 2.0 Mini) are not available in the United States. 
> The API endpoints for these models include:
> 
> bytedance-seedance-v2 (Seedance 2.0)
> bytedance-seedance-v2-fast (Seedance 2.0 Fast)
> bytedance-seedance-v2-mini (Seedance 2.0 Mini)
> bytedance-seedance-v2.5 (Seedance 2.5)
> Video generation via API requires a Pro plan or above. 
> </pasted_content id="3013">
> 
>  I found these, but this is not good for us, to be honest, because we don't have the time to contact support.

### 46. 2026-11-05 18:52 UTC (build session)

> Any other model that is equivalent to Seedance and we could use it, like Google Neo, Veo 3.1, or any other models

### 47. 2026-11-05 18:54 UTC (build session)

> Okay, that's going to be good for us, right? What I want you to do is, on all the Markdown files, put together the first 6 seconds with the Veo 3.1. This is going to be the first entry point for us to see if the direction is correct. Please generate the first 6 seconds, and we will see.

### 48. 2026-11-05 18:58 UTC (build session)

> To be honest, this is not truly good because there was a cut in between the two snips. We need to make it fluid in terms of how we are doing the animations within the 6-second frames. We need to make the animated items live. I haven't noticed any characteristics, and the style is far from the style that we have designed in the Markdown files. Please revisit all the Markdown files and how you are generating the first snippet, the 6-second video. When you are making sure that everything's aligning, please redo the first 6 seconds. It just takes so much credit.

### 49. 2026-11-05 19:03 UTC (build session)

> /Users/zoltanfodor/Downloads/expanded_storyboard.md add this

### 50. 2026-11-05 19:21 UTC (build session)

> Now we are getting it. Let's go with hand B, and based on that, let's create the first 6 seconds. Do not put any sound under it, please.

### 51. 2026-11-05 19:26 UTC (build session)

> Okay, this is not bad, but please be more consistent in terms of realistic stuff. For example, the bed just jumped into the center, so please don't do that. Let's have the bed at the center. Let's have the door not disappear, and the lights and stuff like that. The drawings are kind of okay, I believe.

### 52. 2026-11-05 19:33 UTC (build session)

> [Image #19] We really like this one. Please, based upon this, spin up subagents to create all the 6-second videos separately, so you can try and recreate, based on this, all the 6 seconds. So that would mean That would mean 7 more videos, so 7 subagents, please.

### 53. 2026-11-05 19:46 UTC (build session)

> lets try to join all 8 into one video

### 54. 2026-11-05 19:48 UTC (build session)

> please open it for me in finder

### 55. 2026-11-05 19:52 UTC (build session)

> Could you just once recreate the first knit with different AI models? I want to see one 6-second video with Kling, and maybe you select one or two others. I just want to compare it. The drawings are kind of okay, but the animation is not, so make it more creative.

### 56. 2026-11-05 19:57 UTC (build session)

> <pasted_content id="3013">
> ## Overall Visual Direction and Animation Quality
> 
> Please refine the animation while preserving the original artistic concept, atmosphere, character designs, storytelling, and overall visual identity.
> 
> The main objective is to achieve a smoother, softer, more organic animation with more natural character movements and transitions. All movements should feel intentional, fluid, and physically connected, avoiding sudden jumps, unnatural transitions, or movements that appear disconnected from the characters' actions.
> 
> *Visual style refinement:*
> - Soften the overall appearance of the illustrations.
> - Make the outlines less sharp, less thick, and less dominant.
> - Avoid overly dark, heavy, or rigid contours.
> - Introduce a subtle softness to the linework, creating a more delicate, gentle, hand-drawn appearance.
> - Preserve the original hand-drawn aesthetic rather than making the animation look overly polished, digitally rendered, or vector-based.
> - Maintain consistency in line thickness, texture, shading, and facial features across all scenes.
> - The animation should have a warm, gentle, slightly dreamy quality.
> 
> The goal is to make the entire animation feel more fluid and cohesive without losing the charm and personality of the original illustrations.
> 
> ---
> 
> ## Scene 2 – Smoother Movement and Character Actions
> 
> The movement in this scene should be noticeably smoother and more fluid.
> 
> *Lamp movement:*
> - The lamp should make a playful jump across the room.
> - Its movement should follow a natural, visible jumping trajectory, including a gentle anticipation before takeoff, a smooth arc through the air, and a soft landing.
> - Avoid sudden position changes or teleportation-like movements.
> - The lamp should feel lively and animated, with a slight sense of weight and personality.
> - Its movement should be playful but still consistent with the gentle atmosphere of the animation.
> 
> *Teddy bear movement:*
> - The teddy bear should climb down from the window in a natural and continuous motion.
> - It should visibly move from the window ledge, carefully climb down, and make its way into the bed.
> - The transition from the window to the bed should happen as one connected sequence rather than through sudden repositioning.
> - The bear's body should move organically, with small, natural movements of its arms, legs, and body as it climbs.
> - Once it reaches the bed, it should settle into a comfortable position naturally.
> 
> Make sure both the lamp's jump and the teddy bear's climbing movement are clearly animated, smooth, and easy to follow.
> 
> ---
> 
> ## Scene 3 – Consistent Lamp Facial Design
> 
> Please correct the lamp's eyes to ensure complete visual consistency with its original character design.
> 
> - The lamp must not have eyes that look like they belong to a different illustration style.
> - Its eyes should remain exactly in the same simple, hand-drawn style as the original design.
> - Use two small, simple black dots as eyes.
> - The eyes should look like they were dr

### 57. 2026-11-05 20:01 UTC (idea session)

> do you see the design references ?

### 58. 2026-11-05 20:02 UTC (idea session)

> do you see the sound references ?

### 59. 2026-11-05 20:13 UTC (idea session)

> lets try music v2.5

### 60. 2026-11-05 20:21 UTC (idea session)

> open it in finder

### 61. 2026-11-05 20:22 UTC (build session)

> <pasted_content id="3013">
> # Animation Refinement Instructions – Second Revision
> 
> ## Overall Direction
> 
> Please refine the animation according to the following scene-specific instructions while preserving the existing illustration style, character designs, atmosphere, and visual quality.
> 
> The current artistic direction is working well, so the focus should be on correcting specific movements, improving storytelling clarity, and making the final stages of the animation more emotionally meaningful.
> 
> Do not unnecessarily redesign scenes that are already working well. Preserve their existing composition, timing, and visual identity unless a specific change is requested below.
> 
> ---
> 
> ## Scene 1 – Teddy Bear Climbing Down from the Window
> 
> *Correct the entrance and movement of the character.*
> 
> - The coffee pot must not fall or drop into the room. Its entrance should be natural and controlled, without any sudden falling motion.
> - The teddy bear should climb down from the window in a continuous, clearly visible movement.
> - Show the bear carefully descending from the windowsill rather than suddenly appearing somewhere else in the room.
> - After climbing down, the teddy bear should approach the baby crib.
> - The bear should lean forward and look inside the crib, as if curiously checking what is inside.
> - Make sure the bear's gaze is clearly directed into the crib.
> - The transition between climbing down, approaching the crib, and looking inside should feel smooth and connected.
> 
> The scene should communicate a gentle sense of curiosity and attentiveness.
> 
> ---
> 
> ## Scene 2 – Ball Movement and Teddy Bear Expression
> 
> ### Ball movement
> 
> - The ball should roll naturally out of the room through the open doorway.
> - Its movement should be continuous and clearly follow the direction of the door.
> - The ball should gradually move farther away until it completely exits the room.
> - Once the ball has left, it must not reappear anywhere in the scene.
> - In particular, the ball must not suddenly reappear in the middle of the room at the end of the sequence.
> - Preserve the direction and continuity of the ball's movement throughout the entire shot.
> 
> The ball should have a clear beginning and end to its movement: it starts inside the room, rolls through the doorway, and remains outside the room.
> 
> ### Teddy bear expression
> 
> - The teddy bear must not wink at the end of the scene.
> - Keep both eyes in their normal original appearance throughout the entire sequence.
> - Avoid any blinking or exaggerated facial gesture that could be interpreted as a wink.
> - Preserve the bear's established facial design and natural expression.
> 
> ---
> 
> ## Scene 3 – Lamp with Blue Tears
> 
> The scene is already working well overall, so please preserve its current composition, animation, and atmosphere.
> 
> *One specific adjustment:*
> 
> - Change the lamp's tears to a soft blue color.
> - The tears should be clearly recognizable as tears while remaining consistent with the original hand-drawn illustration style.
> - Use a gentl

### 62. 2026-11-05 20:25 UTC (idea session)

> /Users/zoltanfodor/Developer/filmathon-kit/exports/film_v2_silent.mp4 check out this -> this is the entire video -> we need every section different style based on the storyline - the style of the music is good but there should be more changing in sound based on the current section somehow and at the end it should be like a jazz music when people die ..

### 63. 2026-11-05 20:34 UTC (build session)

> status ?

### 64. 2026-11-05 20:35 UTC (idea session)

> u are working on these ?

### 65. 2026-11-05 20:35 UTC (build session)

> pls open in finder

### 66. 2026-11-05 20:37 UTC (idea session)

> open finder

### 67. 2026-11-05 20:37 UTC (build session)

> open in finder please

### 68. 2026-11-05 20:38 UTC (build session)

> create a link to this please that i can send to a friend quickly

### 69. 2026-11-05 20:40 UTC (idea session)

> which one changes in tune the most based on the scenes ?

### 70. 2026-11-05 20:42 UTC (idea session)

> Maybe the fourth one is the best one, but there is an issue. I don't feel like it's changing the tune enough. We need to check the script once again, and we need to try to come up with the song that basically aligns with every 6-second snip. Please recheck that, please read the script, and try to tune it in a way that it's more this thing.

### 71. 2026-11-05 20:45 UTC (idea session)

> I don't think it's distinct enough. I think you need to read the script once again and try to make it more distinct between the sections.

### 72. 2026-11-05 20:48 UTC (idea session)

> This is much better, especially the second one, but the mix in between the sections is kind of bad. Please try to connect the sections somehow.

### 73. 2026-11-05 20:55 UTC (build session)

> <pasted_content id="3013">
> ### Overall Creative Direction
> 
> Please refine the animation according to the following instructions while preserving the existing artistic style, atmosphere, character designs, and storytelling.
> 
> One of the most important objectives of this revision is to make the entire animation feel like one continuous, evolving story rather than a collection of separate, disconnected scenes.
> 
> *1. Smoother scene transitions*
> 
> - Make the transitions between individual shots significantly smoother and more organic.
> - Avoid abrupt cuts, sudden changes in composition, or transitions that make the scenes feel isolated from one another.
> - Whenever possible, use natural visual transitions that maintain continuity between the characters, objects, lighting, and room environment.
> - Preserve the spatial relationship between objects when moving from one scene to another.
> - The animation should feel as though time is continuously passing within the same room.
> - Avoid sudden changes in the room's layout, character positions, or object appearances.
> 
> *2. Consistent teddy bear character – extremely important*
> 
> Throughout the entire animation, use exactly the same teddy bear character.
> 
> The teddy bear represents one individual whose life and aging process we follow throughout the story.
> 
> - Never replace the teddy bear with a different-looking version.
> - Maintain exactly the same original character design, proportions, facial features, body shape, and recognizable details.
> - Do not randomly increase or decrease the teddy bear's size.
> - Do not change its proportions, head-to-body ratio, limb length, or overall silhouette.
> - The teddy bear must remain visually recognizable in every single scene.
> - Its appearance should only evolve when an explicit aging modification is requested.
> - Aging should be represented through subtle changes in the condition of its fabric, patches, fading, and general wear — NOT through changes in its original size or body proportions.
> 
> *The teddy bear must remain the same character throughout its entire life journey.*
> 
> *3. Consistent armchair – environmental continuity*
> 
> Introduce one specific armchair that becomes a recurring element throughout the animation.
> 
> - This armchair should be placed in the corner of the room.
> - It must be the exact same armchair whenever it appears.
> - It should remain in the same general position and maintain consistent proportions, design, and recognizable details.
> - The armchair should be present in every scene except Scene 4.
> - It should naturally become part of the room's environment, rather than appearing as a newly introduced object in every shot.
> - Its presence should help establish continuity between the scenes and reinforce the impression that we are watching the same room evolve over time.
> 
> The armchair should feel like a permanent part of the teddy bear's world.
> 
> ---
> 
> ## Scene 1 – Introducing the Armchair and Simplifying the Teddy Bear's Movement
> 
> ### Add the armchair
> 
> - Introduce an armchai

### 74. 2026-11-05 20:57 UTC (idea session)

> Could you make the ending more feral? Change the ending to align more with passing life.

### 75. 2026-11-05 20:58 UTC (build session)

> we need to compact as well since we are at 42%

### 76. 2026-11-05 20:58 UTC (idea session)

> open finder

### 77. 2026-11-05 21:01 UTC (idea session)

> idk ... any other suggestions for the ending ?

### 78. 2026-11-05 21:03 UTC (idea session)

> open finder

### 79. 2026-11-05 21:03 UTC (idea session)

> did u change anything ?

### 80. 2026-11-05 21:03 UTC (idea session)

> we dont like the ending tbh

### 81. 2026-11-05 21:07 UTC (idea session)

> This is much better. The only thing we should change is in this part: it's the teenager part.  [Image #3] - Make it as fast as it is now, but make it smoother, since currently it's too outside of everything else in the video.

### 82. 2026-11-05 21:07 UTC (build session)

> open finder w the video

### 83. 2026-11-05 21:13 UTC (idea session)

> open in finder

### 84. 2026-11-05 21:16 UTC (build session)

> in the 6 7 8 sections make the teddy bear the same but little bit older ... do not enlarge it etc. also add this music under it this is the final music /Users/zoltanfodor/Developer/filmathon-kit/exports/film_v2_teen_smooth1.mp4
> 
> also we need a final snitt black image with white chalk writing style : lifetime in one little room

### 85. 2026-11-05 21:19 UTC (build session)

> /compact

### 86. 2026-11-05 21:20 UTC (build session)

> alright we have few more shots ->   [Image #28] here make the background full black the writing is good 
> 
> [Image #29]  [Image #30]  in the last scenes the teddy bear is still fat... fix it ...

### 87. 2026-11-05 21:24 UTC (build session)

> status

### 88. 2026-11-05 21:24 UTC (build session)

> continue the stage 6 clips ... and lets see

### 89. 2026-11-05 21:25 UTC (build session)

> we have a few minutes of wiggle room

### 90. 2026-11-05 21:29 UTC (build session)

> open in finder

### 91. 2026-11-05 21:33 UTC (build session)

> everzthing is perfect, keep everything as it is just in the last scene when the teddy reaches towards the lamp please shorten its arms as it is in the previous scenes
> 
> [Image #31] [Image #32] wtf

### 92. 2026-11-05 21:38 UTC (build session)

> a lifetime or lifetime here ? [Image #33] which would make sense ?

### 93. 2026-11-05 21:38 UTC (build session)

> could u fix the ending ?

### 94. 2026-11-05 21:41 UTC (build session)

> /Users/zoltanfodor/Developer/filmathon-kit/exports/final/teamname_alifetimeinonelittleroom.mp4 perfgect this is the final -> i want you to push everything to github as well please

### 95. 2026-11-05 21:44 UTC (build session)

> ai models we used for generating the video ? exact

### 96. 2026-11-05 21:44 UTC (idea session)

> ai model we used for the sound 
> exact model name

### 97. 2026-11-05 22:40 UTC (build session)

> stop all theae
