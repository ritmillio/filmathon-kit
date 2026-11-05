#!/usr/bin/env python3
"""ElevenLabs music from audio/music_plan.json. usage: el_music.py OUT.mp3 [seed]. Key from .env.local, never printed."""
import json, sys, urllib.request
key=[l.split('=',1)[1].strip() for l in open('.env.local') if l.startswith('ELEVENLABS_API_KEY=')][0]
body={'composition_plan':json.load(open('audio/music_plan.json')),'model_id':'music_v2_5'}
if len(sys.argv)>2: body['seed']=int(sys.argv[2])
r=urllib.request.Request('https://api.elevenlabs.io/v1/music?output_format=mp3_44100_192',data=json.dumps(body).encode(),headers={'xi-api-key':key,'Content-Type':'application/json'})
try: open(sys.argv[1],'wb').write(urllib.request.urlopen(r,timeout=300).read()); print('saved',sys.argv[1])
except urllib.error.HTTPError as e: print('HTTP',e.code,e.read().decode()[:600])
