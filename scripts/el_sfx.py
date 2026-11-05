#!/usr/bin/env python3
"""Generate the SOUND.md effects with ElevenLabs SFX v3 into audio/. usage: el_sfx.py [name ...] (default: all missing)"""
import json, os, re, sys, urllib.request, concurrent.futures as cf
key=[l.split('=',1)[1].strip() for l in open('.env.local') if l.startswith('ELEVENLABS_API_KEY=')][0]
rows=re.findall(r'^\| `([a-z_]+\.wav)` \| (.+?) \|$',open('SOUND.md').read(),re.M)
want=set(sys.argv[1:])
def gen(item):
    name,prompt=item
    if os.path.exists('audio/'+name) and not want: return name,'exists'
    b={'text':prompt,'model_id':'eleven_text_to_sound_v3','prompt_influence':0.5}
    if 'seamless loop' in prompt: b['loop']=True
    m=re.search(r'(\d+) seconds?',prompt)
    if m: b['duration_seconds']=min(30,max(0.5,float(m.group(1))))
    r=urllib.request.Request('https://api.elevenlabs.io/v1/sound-generation?output_format=wav_44100',data=json.dumps(b).encode(),headers={'xi-api-key':key,'Content-Type':'application/json'})
    try: open('audio/'+name,'wb').write(urllib.request.urlopen(r,timeout=180).read()); return name,'ok'
    except urllib.error.HTTPError as e: return name,'HTTP %s %s'%(e.code,e.read().decode()[:200])
todo=[r for r in rows if not want or r[0] in want]
with cf.ThreadPoolExecutor(5) as ex:
    for n,s in ex.map(gen,todo): print(n,s,flush=True)
