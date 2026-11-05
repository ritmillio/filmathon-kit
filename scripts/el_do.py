#!/usr/bin/env python3
"""One-call ElevenLabs generation for stages. Key from .env.local, never printed.
  el_do.py still NAME --prompt-file F --ref R [--ref R2 ...] [--model sunburst|flare] [--res 1K|2K]
      -> stills/NAME.png and stills/NAME.jpg (1920x1080)
  el_do.py clip NAME --prompt-file F --start S.jpg --end E.jpg [--model fast|std] [--secs 6]
      -> shots/NAME.mp4 (raw) and exports/NAME_silent.mp4 (no audio, held on twos, 1080p 24 fps)
Retries on HTTP 429/5xx. Exit code 2 on a failed generation (not charged)."""
import argparse, base64, json, os, subprocess, sys, time, urllib.request, urllib.error
key=[l.split('=',1)[1].strip() for l in open('.env.local') if l.startswith('ELEVENLABS_API_KEY=')][0]
def req(method,url,body=None):
    for i in range(5):
        r=urllib.request.Request(url,method=method,data=json.dumps(body).encode() if body else None,headers={'xi-api-key':key,'Content-Type':'application/json'})
        try: return json.load(urllib.request.urlopen(r,timeout=180))
        except urllib.error.HTTPError as e:
            msg=e.read().decode()[:400]
            if e.code in (429,500,502,503) and i<4: time.sleep(20*(i+1)); continue
            print('HTTP',e.code,msg); sys.exit(2)
def ref(p):
    m={'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg'}[os.path.splitext(p)[1].lower()]
    return {'type':'inline_base64','content_base64':base64.b64encode(open(p,'rb').read()).decode(),'mime_type':m}
a=argparse.ArgumentParser(); a.add_argument('kind'); a.add_argument('name'); a.add_argument('--prompt-file',required=True)
a.add_argument('--ref',action='append',default=[]); a.add_argument('--start'); a.add_argument('--end')
a.add_argument('--model'); a.add_argument('--res'); a.add_argument('--secs',type=int,default=6); a=a.parse_args()
prompt=open(a.prompt_file).read().strip()
if a.kind=='still':
    mid='gpt-image-2.5-'+(a.model or 'sunburst')
    b={'model_id':mid,'prompt':prompt,'aspect_ratio':'16:9','resolution':a.res or '1K'}
    if a.ref: b['images']=[ref(p) for p in a.ref]
    base='https://api.elevenlabs.io/v1/flows/image'; wait=4
else:
    mid='veo-3.1-generate-001' if a.model=='std' else 'veo-3.1-fast-generate-001'
    b={'model_id':mid,'prompt':prompt,'aspect_ratio':'16:9','resolution':'1080p','duration_secs':a.secs,'generate_audio':False,
       'negative_prompt':'people, text, camera movement, zoom, objects appearing or disappearing'}
    if a.start: b['start_frame']=ref(a.start)
    if a.end: b['end_frame']=ref(a.end)
    base='https://api.elevenlabs.io/v1/flows/video'; wait=10
gid=req('POST',base,b)['id']; print('started',gid,flush=True)
for _ in range(120):
    time.sleep(wait); r=req('GET',f'{base}/{gid}')
    if r.get('status') not in ('pending','generating','processing','running','queued'): break
if r.get('status')!='completed': print('FAILED',json.dumps(r)[:400]); sys.exit(2)
if a.kind=='still':
    urllib.request.urlretrieve(r['content_url'],f'stills/{a.name}.png')
    from PIL import Image
    Image.open(f'stills/{a.name}.png').convert('RGB').resize((1920,1080)).save(f'stills/{a.name}.jpg',quality=95)
    print('saved stills/%s.png and .jpg'%a.name)
else:
    urllib.request.urlretrieve(r['content_url'],f'shots/{a.name}.mp4')
    subprocess.run(['ffmpeg','-v','error','-y','-i',f'shots/{a.name}.mp4','-an','-vf','fps=12,fps=24,format=yuv420p','-c:v','libx264','-crf','14','-t',str(a.secs),f'exports/{a.name}_silent.mp4'],check=True)
    print('saved shots/%s.mp4 and exports/%s_silent.mp4'%(a.name,a.name))
