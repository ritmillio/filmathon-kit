#!/usr/bin/env python3
"""Minimal ElevenLabs Flows client (image/video). Key from .env.local, never printed.
usage: el_gen.py image|video OUT --model M --prompt-file F [--ref FILE ...] [--start FILE] [--secs N] [--res R]"""
import argparse, base64, json, os, sys, time, urllib.request
def key():
    for l in open('.env.local'):
        if l.startswith('ELEVENLABS_API_KEY='): return l.split('=',1)[1].strip()
def ref(p):
    m={'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg'}[os.path.splitext(p)[1].lower()]
    return {'type':'inline_base64','content_base64':base64.b64encode(open(p,'rb').read()).decode(),'mime_type':m}
def call(method,url,body=None):
    r=urllib.request.Request(url,method=method,data=json.dumps(body).encode() if body else None,
        headers={'xi-api-key':key(),'Content-Type':'application/json'})
    try: return json.load(urllib.request.urlopen(r,timeout=120))
    except urllib.error.HTTPError as e: print('HTTP',e.code,e.read().decode()[:800]); sys.exit(1)
a=argparse.ArgumentParser()
a.add_argument('kind'); a.add_argument('out'); a.add_argument('--model',required=True)
a.add_argument('--prompt-file',required=True); a.add_argument('--ref',action='append',default=[])
a.add_argument('--start'); a.add_argument('--secs',type=int,default=5); a.add_argument('--res')
a=a.parse_args()
b={'model_id':a.model,'prompt':open(a.prompt_file).read().strip(),'aspect_ratio':'16:9'}
if a.kind=='image':
    if a.ref: b['images']=[ref(p) for p in a.ref]
    if a.res: b['resolution']=a.res
else:
    b['duration_secs']=a.secs; b['resolution']=a.res or '1080p'; b['generate_audio']=False
    if a.start: b['start_frame']=ref(a.start)
    if a.model.startswith('veo'):
        b['negative_prompt']='people, hands, faces, text, camera movement, zoom, pan, new objects, 3D render, photoreal'
base='https://api.elevenlabs.io/v1/flows/'+a.kind
g=call('POST',base,b); gid=g['id']; print('started',gid,flush=True)
for _ in range(90):
    time.sleep(3 if a.kind=='image' else 10)
    r=call('GET',f'{base}/{gid}')
    if r.get('status') not in ('pending','processing','running','queued','generating'):
        break
print(json.dumps({k:(v if k!='output' else '...') for k,v in r.items()})[:600])
open(a.out+'.json','w').write(json.dumps(r)[:20000])
