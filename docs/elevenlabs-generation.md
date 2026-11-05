# Generating pictures and video with ElevenLabs

Checked on 2026-11-05 against ElevenLabs' live API spec (`https://api.elevenlabs.io/openapi.json`) and the detail in `.claude/skills/elevenlabs/references/image-video-flows.md` (a third-party snapshot, read by us).

## What exists (confirmed in the live spec)

| Job | Endpoint | Notes |
|---|---|---|
| Image | `POST /v1/flows/image`, `GET /v1/flows/image/{generation_id}` | asynchronous |
| Video | `POST /v1/flows/video`, `GET /v1/flows/video/{generation_id}` | asynchronous |
| Stored media | `/v1/assets` | reuse a reference image across shots |
| Templates | `/v1/flows/templates` | published Flows, optional |

**Image models in the spec:** `gemini-3-pro-image`, `gemini-3.1-flash-image`, `gemini-3.1-flash-lite-image`, `gemini-2.5-flash-image`, `gpt-image-2`, `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-1`, `gpt-image-1.5`, `bytedance-seedream-5-lite`, `bytedance-seedream-5-pro`.
**Video models in the spec:** `veo-3.1-generate-001`, `veo-3.1-fast-generate-001`, `bytedance-seedance-v2` (and `-fast`, `-mini`), `bytedance-seedance-v2.5`, `creatify-aurora`.
All of these are hosted inside ElevenLabs, so using them keeps us on the one-tool rule. Model lists change often: re-check the spec before hard-coding.

## How we would use it (from the skill reference, to confirm with a first test)

- **Stills:** an image model, 16:9, with the room sketch and the item sketches as references (several references are allowed per image). Send a reference inline (base64) or store it as an asset.
- **Clips:** a video model with `startFrame` set to the approved still, 4 to 8 seconds, 16:9, 1080p, and a negative prompt. **Native clip audio off** (our sound is made separately).
- **Chaining:** a video request can point at a still that is still pending, so we do not have to wait.
- **Polling:** images every 2 s or more, video every 10 s or more. Output links expire after about an hour, so download the file straight away into `stills/` or `shots/`.
- Failed generations are not charged.

## Not verified yet (check before relying on it)

1. **Our key may lack Flows permission.** The plan is Pro, which the endpoints require, but the key's permissions were not tested.
2. **Credit cost** per image and per clip is not known. Check the balance before and after the first generation.
3. **Which model holds the room best.** Make one still and one clip first, then run `scripts/overlay_check.py`.
4. Some models are geo-restricted, and the seedream and seedance models may need access approval.
5. Whether the MCP server exposes these tools. The API works without it.

## First test (about 10 minutes)

1. One 16:9 still of the empty room from `assets/sketches/room_layout_sketch.jpg`, using the STYLE and ROOM lines in `docs/shotlist.md`.
2. Overlay check it. If the window, sill and rug sit on the sketch, it becomes the G1 base still.
3. One 4 s clip from it, camera locked, one small motion. Look at the room for drift. Note the credits spent.
4. Write the result in `docs/log.md`.
