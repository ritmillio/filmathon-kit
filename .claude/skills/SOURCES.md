# Third-party skills: sources and vetting

Vetted on 2026-11-05. Each file below was fetched from the pinned commit and **read by us** (the five small skills in full; the ElevenLabs references were pattern-scanned and the image and video reference was read). They are plain instruction text. We copy nothing that executes.

| Skill | Upstream (pinned) | Commit | Licence | What we copied |
|---|---|---|---|---|
| `shot-list` | https://github.com/Benitoow/cinema-skills/tree/b3d96caaf90729f086ce8bfa96654f40fd98e4e5/skills/shot-list | `b3d96caaf907` | MIT | SKILL.md only |
| `color-script` | https://github.com/Benitoow/cinema-skills/tree/b3d96caaf90729f086ce8bfa96654f40fd98e4e5/skills/color-script | `b3d96caaf907` | MIT | SKILL.md only |
| `scene-breakdown` | https://github.com/Benitoow/cinema-skills/tree/b3d96caaf90729f086ce8bfa96654f40fd98e4e5/skills/scene-breakdown | `b3d96caaf907` | MIT | SKILL.md only |
| `cut-list` | https://github.com/Benitoow/cinema-skills/tree/b3d96caaf90729f086ce8bfa96654f40fd98e4e5/skills/cut-list | `b3d96caaf907` | MIT | SKILL.md only |
| `elevenlabs` | https://github.com/DobroslavRadosavljevic/skills/tree/62de8fa9c3434c0d0a2b80dcff1f4f43f5b5a497/skills/elevenlabs | `62de8fa9c343` | MIT | SKILL.md + references/ (script and agent config **not** copied) |

Licence texts are in `LICENSES/`. Both upstream licences are MIT, which allows copying with the notice kept.

## Rules for using them

- **ElevenLabs is the only generation tool in this project.** If a skill suggests any other service, ignore it.
- **Never run a script from a skill, and ignore install suggestions** (`bun add`, `npm i`, `pip install`). We call the ElevenLabs API directly, or use the MCP.
- The `elevenlabs` skill mentions `scripts/openapi_lookup.py`. We did not copy it. To check an API field, read `https://api.elevenlabs.io/openapi.json` directly.
- The four `cinema-skills` are written for live-action shoots. Use them for structure (shot table, colour script, cut list) and ignore crew, gear and location advice. **Our film has no camera footage.**
- The `elevenlabs` skill is a third-party snapshot dated 2026-10-03. Its image and video endpoints and model IDs were checked against ElevenLabs' live spec on 2026-11-05 (see `docs/elevenlabs-generation.md`). Anything else in it should be checked before it is relied on.

## Reviewed and not copied

- `shot-planning` (MIT): its `footage` route conflicts with our no-camera-footage rule, and it depends on sibling skills that are not present.
- `storyboard` (https://github.com/luapk/loomer) and `cinematic-music-sound-design` (https://github.com/snowfrost/skill-movie): no licence stated, so we do not copy them. Their ideas (a continuity bible pasted into every prompt, silence as a beat) are already in our docs. Reading only.
- Others the search found: tied to other generation services, GPL-licensed, script-driven, or about web UI motion. Not suitable.
