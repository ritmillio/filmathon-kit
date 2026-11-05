# Stage specs: stages 2-8, one 6-second clip each (look B, silent)

Stage 1 is done: `exports/first6_B2_silent.mp4` (start `stills/B2_start.jpg`, end `stills/B2_end.jpg`, prompts `docs/prompts/B2_start.txt`, `B2_end.txt`, `clip_B2.txt`). **Every other stage copies how that one was made.** Team verdict on it: "we really like this one".

## Common rules (all stages)
- **Look B:** hand-made marker, wax crayon and torn paper: wobbly marker outlines, crayon grain, torn-paper walls with small scribbled doodles, limited palette (ultramarine, navy, cream, orange, yellow ochre, brown). Imperfect and human; never glossy, airbrushed or "rendered".
- **Same room, same camera in every stage:** a four-pane window centred on the back wall with a wide sill; wooden plank floor; one-point perspective; a striped rug in front of the window; **the bed slot is the centre of the rug**; the tall floor lamp stands at the **left**; a wooden **door is on the right wall and is always visible** (closed, ajar or open, never missing); the room outline matches `stills/B2_start.jpg` exactly.
- **Continuity inside a shot (the team's rule):** nothing appears, disappears, teleports or changes place within the 6 seconds. Everything that exists in the shot is in **both** the start frame and the end frame. Only states change (light, door, weather, poses, small movements). Changes between stages happen by **hard cut** (stage N and stage N+1 do not need to match; each stage is a fresh state of the room).
- **Cast designs** come from the first stage frames (`stills/B2_end.jpg`): the lamp (cream trapezoid shade with two dot eyes and a smile, a pull chain with beads, a thin dark pole, round base; hops in place on its base), the teddy bear (brown, button eyes; from stage 6 the **worn** bear with a stitched seam and a patch on the belly). Faces only on the Lamp, the Bear, the Mug and the Cushion. No people, no text, no hands of people.
- **Silent.** Never generate audio. No sound design.
- **ElevenLabs only.** Use only `scripts/el_do.py` (below). Never use another generator, never print or paste the API key, never open `.env.local`.
- **Prompts must not name any studio, film or artist.**

## How each stage is made (the recipe that worked)
1. **Start still**: edit `stills/B2_end.jpg` (reference image: the style and the lamp and bear designs) into this stage's start state. Prompt starts with "Edit the attached picture into ..." and says what to keep, what to change, "same hand-made marker, wax-crayon and torn-paper style, same framing". See `docs/prompts/B2_start.txt` and `B2_end.txt` as the model.
   `python3 scripts/el_do.py still sN_start --prompt-file docs/prompts/sN_start.txt --ref stills/B2_end.jpg`
2. **Look at it** (Read the .jpg). Reject and redo once if: the room outline drifted, the door is missing, the bed is not at the centre, anything people-like, text, glossy or airbrushed look, wrong cast.
3. **End still**: edit the **start still** (`--ref stills/sN_start.jpg`) into the end state (same objects, same places, only the states change). Look at it.
4. **Clip**: `python3 scripts/el_do.py clip sN_B_fast --prompt-file docs/prompts/sN_clip.txt --start stills/sN_start.jpg --end stills/sN_end.jpg --secs 6`. The clip prompt follows `docs/prompts/clip_B2.txt`: the look sentence, a STRICT CONTINUITY paragraph listing where each object stays, then a timed script (0 s, 1 s, 2 s ...). Each character acts with its own tempo: Lamp quick and bouncy, Bear slow and small, Mug a swaying groove.
5. **Check the clip**: `ffmpeg -v error -y -i shots/sN_B_fast.mp4 -vf "select='not(mod(n,18))',scale=480:-1,tile=4x2" -frames:v 1 stills/sN_check.png` and Read it. Does anything pop in, vanish or jump? Is the bed still at the centre? The door still visible? If it fails, adjust the prompt and **re-run the clip once** (never more).
6. **Credit budget:** two stills (about 800 credits each) plus one Fast clip (about 2,400) is about 4,000 per stage. **Hard cap: 9,000 credits for your whole stage** (so at most 2 extra stills and 1 extra clip). Do not use the standard Veo model.
7. **Files** (use these exact names): `stills/sN_start.jpg|png`, `stills/sN_end.jpg|png`, `shots/sN_B_fast.mp4`, `exports/sN_B_silent.mp4`, `docs/prompts/sN_start.txt`, `sN_end.txt`, `sN_clip.txt`. **Do not touch git. Do not edit any existing file.**
8. **Report back** (short): the files made, a one-line verdict per check, what is wrong with the clip (if anything), and how many stills and clips you generated.

---

## S2 Childhood (film 6-14 s): playful, warm
- **State:** a **small wooden child's bed** at the centre of the rug with a patchy blanket. **Crayon scribbles on the walls** (a sun, a house, an animal) among the torn-paper walls. **A column of pencil height marks on the door frame.** A few toys on the floor: a ball and three wooden blocks. The lamp at left is ON, warm. The clean bear sits on the sill. The door on the right wall stands ajar with a warm line of light. Window: warm dusk sky, one star.
- **Start:** as above, with the lamp on and happy. **End:** same, door open wider with warm light, lamp mid-bounce glow brighter.
- **Motion script:** 0 s the lamp bounces on its base in time, excited; 1.5 s the ball rolls slowly across the floor from the left toward the rug and stops against the bed leg (the ball is in the start frame, at the left); 3 s a block wobbles and hops once in place; 4 s the bear tilts its head to watch the ball; 5 s the door swings wider and warm light brightens; blanket ruffles gently throughout.

## S3 Teens (14-22 s): rebellious, dim, rain
- **State:** a **messy teen bed** (tangled dark blanket, a pillow) at the centre of the rug. **Posters** pinned over the wall doodles (simple scribbled band-poster shapes, no text). A **guitar** leaning against the bed. A **toy box** with toys stuffed in at the left floor. Rain streaks on the window glass, blue-grey dim sky. The lamp at left on, dim, eyes half rolled. The bear on the **far end of the sill**, small and ignored. **Door on the right wall: ajar at the start, SLAMMED shut at the end** (always visible).
- **Start:** door ajar with a thin line of light, lamp dim and sulky (eyes rolled up). **End:** door shut, room darker, posters crooked.
- **Motion script:** 0 s rain runs down the glass; 1 s the lamp rolls its eyes slowly up and round; 2.5 s the door **slams shut** hard; 2.7 s the whole room shakes: posters flutter, the guitar wobbles, the lamp trembles, the bear bounces slightly; 4 s everything settles, light dimmer; the lamp's eyes droop.

## S4 Away (22-28 s): empty, cold, lonely
- **State:** the room is nearly **empty**: the rug is bare (**the bed slot is empty**), a **few cardboard boxes** stacked at the left and right floor, **faded rectangles** on the walls where posters were, one scrap of crayon drawing remaining. Snow falls outside the window, pale cold blue-white light. The lamp at left is **off**, shade drooped, eyes closed or half shut. The bear sits on the sill facing the door, alone. **Door on the right wall: closed at the start.**
- **Start:** door closed, no warm light, lamp off and slumped. **End:** door closed again, same, bear slumped lower.
- **Motion script:** 0 s snow drifts outside, dust in cold light; 1.5 s the door opens a crack and a thin beam of warm light falls across the floor; 2 s the bear lifts its head and leans toward the door with hope; 3.5 s the door swings closed again, the beam vanishes; 4 s the bear slowly slumps and turns its head to the window; the lamp's eyes stay shut.

## S5 Family (28-38 s): the biggest warm light
- **State:** warm amber evening. A **double bed** at the centre of the rug with floral bedding. A **wooden crib** on the rug at the right of the bed with a mobile of three stars above it, **the clean bear sitting inside the crib**. Floral wallpaper feel on the torn-paper walls, **a wedding picture** in a frame and two small potted plants on the floor/sill. A face-free **armchair** at the right front, and a **round side table with the Mug** (cream mug with a small smiling face) beside it. The lamp at left glows big and warm, leaning toward the crib. The door on the right wall is **open** with golden light. Window: warm amber evening sky. (Sill is bare.)
- **Start/End:** same room; the end has the lamp glow a touch brighter and the mobile at a different angle.
- **Motion script:** 0 s the mobile turns slowly; 1 s the Mug sways side to side in a funky groove, coffee sloshing, the side table steadies itself; 2 s the lamp leans in over the crib and its glow pulses softly; 3 s the bear in the crib tilts its head, following the mobile; 4 s the blanket on the double bed rises and falls gently; 5 s everything settles, warm and happy.

## S6 Quiet years (38-46 s): soft autumn dusk
- **State:** only the **double bed** on the rug (the crib is gone). The armchair, **worn** now (a patch, a sag), at the right front, with the **worn bear** (stitched seam, belly patch) sitting on it facing the window. **Many framed pictures** on the walls. Faded floral colours, softer palette. A tall tree outside with autumn leaves, a long beam of low gold afternoon light across the floor with dust motes. The Mug on its side table (face, calm). The lamp at left, glow dimmer. Door on the right wall closed.
- **Start:** bright gold beam. **End:** the beam shorter and dimmer, a longer shadow.
- **Motion script:** 0 s leaves drift past the window; 1.5 s the lamp sways very slowly and tries a little hop, landing awkwardly (a small wobble); 3 s the Mug sways slowly; 4 s the light slowly dims and the beam slides across the floor; the worn bear slowly turns its head toward the old height marks by the door.

## S7 Old age (46-54 s): pale blue dawn, fragile
- **State:** a **narrow single bed with side rails** at the centre of the rug, a blanket and a pillow; the **worn bear** lies on the pillow. The armchair has been **moved right beside the bed** (slid from the right). **Round side table** by the bed with a glass, a pill bottle and the Mug (still, no groove). A **cane** leaning against the wall by the door. A huge bare tree outside, pale blue dawn. The lamp is near the bed, **leaning over it**, small trembling dim glow. Faded walls. Door on the right wall closed.
- **Start:** pale dim light, everything held. **End:** the glow slightly weaker.
- **Motion script:** 0 s the blanket rises and falls very slowly (someone breathing, never shown); 1.5 s the lamp's glow trembles and flickers once; the shade tilts slightly closer to the bed; 3 s the whole room gives a slight tremor, a picture frame on the wall tilts; the armchair rocks once and stops; 4.5 s the bear on the pillow turns its head toward the lamp; the glow weakens.

## S8 End (54-60 s): stillness, then dark
- **State:** the same old-age room as S7 (single bed with rails, armchair beside it, side table, cane, worn bear on the pillow, lamp leaning over the bed). The window is **white** (a pale blank dawn). Door closed. Everything is still.
- **Start:** still room, lamp glowing weakly, eyes open, smile. **End:** the room **dark**, only the white window lightly visible; the lamp's glow out, its eyes closed, its smile still there.
- **Motion script:** 0 s total stillness (only crayon grain boils); 1 s the lamp looks around slowly one last time; 2 s its light gently flickers; 3 s a second flicker; 4 s the glow slowly dims; 5 s one final flicker and the light goes out, the eyes closing, the room in darkness; everything else stays perfectly still.
