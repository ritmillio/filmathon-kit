# 06 · Export and submit

## Final render

`rough_cut.py` already exports to the delivery spec: **H.264 + AAC, MP4, 24 fps, 1920×1080, faststart, -16 LUFS**. Set the output name in `film.json`:

```json
"output": "exports/teamname_filmtitle.mp4"
```

Use lowercase letters and digits, no spaces or accents: `csapatnev_filmcim.mp4`.

```bash
python3 scripts/rough_cut.py film.json
python3 scripts/check_delivery.py exports/teamname_filmtitle.mp4
```

All lines must say PASS, with `READY TO SUBMIT` at the end.

## Is upscaling to 4K worth it?

**No, not for this event.** The spec recommends 1920×1080, with 1280×720 as the minimum. Spend the time on story and sound. If a clip looks soft, a light film grain in the edit helps more than upscaling.

## Cinema checklist

- [ ] Runtime is 30–90 seconds, **including** title and credits
- [ ] Sound is in the file and clear. Voice is intelligible at low volume
- [ ] No black frames at the start or end
- [ ] No garbled on-screen text, no logos or real brands, no politics
- [ ] Everything was generated with the ElevenLabs Pro package (prize eligibility)
- [ ] `check_delivery.py` says `READY TO SUBMIT`
- [ ] You watched the **whole file** once, full screen, with sound, from the exported MP4 (not the project)
- [ ] Uploaded by **22:15**, not 22:29. There is no extension
- [ ] A backup copy is on a USB stick or cloud drive

## Tomorrow at the cinema

Doors open 08:45 at Cinema City Westend, screenings from 09:20. Bring the file on a USB stick as a backup.
