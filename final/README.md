# Final delivery

`teamname_alifetimeinonelittleroom.mp4` is the final film "a lifetime in one little room": 60.5 s, 1920x1080, 24 fps, H.264 + AAC, silent animation plus the team's music and a black chalk title card at the end. **Rename `teamname` to the real team name before uploading to the Filmathon.**

- `music_film_v2_teen_smooth1.m4a`: the audio track taken (without re-encoding) from the team's `film_v2_teen_smooth1.mp4`. **To confirm by the team: it was generated in ElevenLabs** (the rules count only ElevenLabs audio).
- `title_card_a_lifetime_in_one_little_room.jpg`: the end card (generated with `gpt-image-2.5-sunburst` inside ElevenLabs; prompt `docs/prompts/title_card_a.txt`; background set to pure black by a levels edit).
- All pictures and video were generated with ElevenLabs (Veo 3.1, GPT image 2.5 via ElevenLabs); prompts and specs are in `docs/`, the log of every decision is `docs/log.md`, and the scripts that built the film are in `scripts/` (`el_do.py`, `make_film.py`, `blue_tears.py`).
- Intermediate media (about 5 GB of clips, stills, sound effects) stays on the team's computer and is not in git.
