# Figma references

The team collects study material in Figma. This folder is where we keep what we learn from it, in our own words.

## The rule

**Learn the craft, never copy the content.** Take colour relationships, line quality, shape language, staging and animation principles. Do not take characters, props, logos, titles or recognisable scenes. Do not write a studio name or a film title into a prompt. Do not upload a reference frame to the generator. Full rule: `DESIGN.md`, "Using references".

## How to add a Figma board

1. **Export the frames you like** from Figma as PNG (2x) and save them in `boards/<board-slug>/exports/`. (The assistant cannot open Figma links, so exports or pasted images are how we share them.)
2. **Copy `_TEMPLATE.md`** to `boards/<board-slug>/notes.md` and fill it in: one entry per frame, with an ID (`R01`, `R02`, ...).
3. **Write what we take** from each frame in one line, in our own words, as *qualities* ("warm lamp glow against a cool blue night", "round soft furniture shapes").
4. **Add a row** to `_INDEX.md`.
5. **Promote what is approved.** Qualities the team agrees on are copied into the STYLE line in `docs/shotlist.md` and into `DESIGN.md`. Only then do they reach a prompt.
6. **Log it** in `docs/log.md` and run `scripts/save.sh "message"`.

## What is committed

- `_INDEX.md`, `_TEMPLATE.md`, every `notes.md`: yes.
- `boards/*/exports/*`: **no**. They are third-party frames and stay on the machine (see `../.gitignore`). Only `.gitkeep` is committed.

## Layout

```
assets/references/figma/
  README.md
  _INDEX.md           one row per reference frame
  _TEMPLATE.md        copy this for each board
  boards/
    <board-slug>/
      notes.md        our notes, in our own words
      exports/        PNG exports (not committed)
```
