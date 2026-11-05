# assets/

Everything we draw, collect or study for the film.

| Folder | What it holds | Committed? |
|---|---|---|
| `items/` | The designer's item sketches, cropped to a square on white (PNG, 1024 px). These are the **reference images** we attach to the generator. | yes |
| `sketches/room_layout_sketch.jpg` | The room layout sketch. The base of every shot. Scripts point at this path. | yes |
| `sketches/items_original/` | The item sketches as they were sent (JPG). | yes |
| `sketches/contact_sheet.png` | One picture of every sketch, for a quick look. | yes |
| `references/figma/` | Study material collected in Figma. See its `README.md`. | notes yes, third-party exports no |
| `sponsors/` | Event logos from the kit. Not ours. | yes |

`items.md` is the registry: one row per item, with its role in the story, the stages it appears in and its status.

## Rules

- **One item per file, `lower_snake_case`.** Never overwrite an approved file. Add `_v2`.
- **Sketches are inputs, not final art.** The film's pictures are generated from them with ElevenLabs.
- **Reference exports from Figma are study material only.** They are never uploaded to the generator and never copied.
- When you add or change an item, update `items.md` and add a dated line to `docs/log.md`, then `scripts/save.sh "message"`.
