# Using the ElevenLabs web app's other video models (Kling, MiniMax, Seedance, Gemini Omni)

**Why the app:** the team's screenshots of the ElevenLabs "Image & Video" model picker show Kling 4.0, MiniMax H3 and H3 Max, FLUX 3, Gemini Omni Flash and Seedance 2.0/2.5. They are part of the ElevenLabs package, so they are allowed. **They are app-only**: the live API spec and the docs snapshot (`.claude/skills/elevenlabs/references/image-video-flows.md`) list only Veo 3.1 and the Seedance family, and Seedance returns `model_access_denied` for our API key. The assistant cannot call the app models; a person generates them in the app and drops the files into the repo.

**Prices shown in the app (default settings, credits per generation):** Gemini Omni Flash 1.2 = 439, MiniMax H3 / H3 Max = 1,515, Kling 4.0 = 2,854, Seedance 2.0 = 3,258, Seedance 2.5 = 4,979. Compared with the API: Veo 3.1 Fast about 2,400, Veo 3.1 standard about 4,800-7,000.

## Comparison test: stage 1 (first 6 seconds), same inputs for every model
Files in `exports/for_app/`: `1_start_frame.jpg` (cold room, lamp asleep, door closed), `2_end_frame.jpg` (door open, lamp lit), `3_prompt.txt` (the creative acting script).
Settings in the app: **16:9, 6 seconds, highest resolution offered (1080p if possible), native audio OFF**, start frame attached (and the end frame too where the model has an end-frame slot). Paste the prompt. If a model has no end-frame slot, add to the prompt: "ends with the door open and the lamp glowing".
Save each result as `shots/first6_<model>.mp4`: `first6_kling40.mp4`, `first6_minimax_h3max.mp4`, `first6_seedance25.mp4`, `first6_omni_flash.mp4`. Tell the assistant and it will cut them on twos (silent), put them next to the Veo versions and compare.

## What to judge (the same checklist as before)
1. Nothing pops in, vanishes or teleports. 2. Cradle stays at the centre of the rug, bear on the sill, lamp at the left, door on the right and always visible. 3. The acting: anticipation, squash and stretch, personality (the lamp's wake-up and hop, the bear's reactions). 4. The hand-made look holds (crayon grain, marker lines). 5. No people, no text.

## Already done (Veo 3.1, API)
- `exports/cmp_veo_std_silent.mp4`: better acting (dust in the beam, a wink). Flaws: the shade briefly morphs into a walking creature; the bear tips over.
- `exports/cmp_veo_fast_silent.mp4`: a brown blob character pops in at the lamp's base. Rejected.
