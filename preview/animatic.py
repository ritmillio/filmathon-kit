#!/usr/bin/env python3
"""Free 60 s animatic: shot cards from docs/shotlist.md over the base room, placeholder sound from the cue sheet.
TIMING ONLY. Never used in the final film. Costs no credits."""
import csv, os, re, subprocess, zlib
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
os.makedirs('preview/cards', exist_ok=True); os.makedirs('preview/ph', exist_ok=True)
F=lambda s: ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', s)
bg=ImageEnhance.Brightness(Image.open('stills/g1_base_room.jpg').convert('RGB').resize((1920,1080))).enhance(0.45)
shots=[]
for l in open('docs/shotlist.md'):
    c=[x.strip() for x in l.strip().strip('|').split('|')]
    if len(c)>=7 and c[0].isdigit(): shots.append((int(c[0]),c[2],int(c[3]),c[4],c[5],c[6]))
def wrap(d,t,f,w):
    out,line=[],''
    for wd in t.split():
        if d.textlength((line+' '+wd).strip(),font=f)>w: out.append(line); line=wd
        else: line=(line+' '+wd).strip()
    return out+[line]
lst=open('preview/cards/list.txt','w'); t0=0
for n,tm,sec,state,motion,snd in shots:
    im=bg.copy(); d=ImageDraw.Draw(im); y=70
    d.text((70,y),f'SHOT {n}   {tm} s',font=F(64),fill='#f3c98b'); y+=100
    for lab,txt,col in (('STATE',state,'#dce8f8'),('MOTION',motion,'#e0a42b'),('SOUND',snd,'#a9c1e6')):
        d.text((70,y),lab,font=F(30),fill=col); y+=44
        for ln in wrap(d,txt,F(40),1750): d.text((70,y),ln,font=F(40),fill='#ffffff'); y+=54
        y+=26
    d.text((70,1010),'ANIMATIC - timing only, not for the final film',font=F(28),fill='#a9c1e6')
    im.save(f'preview/cards/c{n:02d}.png'); lst.write(f"file 'c{n:02d}.png'\nduration {sec}\n")
lst.write(f"file 'c{shots[-1][0]:02d}.png'\n"); lst.close()
loops=('room_tone','rain','clock','lamp_hum','wind','heart','breath','music','guitar')
for r in csv.DictReader(open('audio/sound_cues.csv')):
    f=r['file']; p='preview/ph/'+f
    if os.path.exists(p): continue
    h=zlib.crc32(f.encode()); fr=180+h%700; base=f.split('.')[0]
    if base=='music': src=f'sine=f=262:d=60,tremolo=f=1:d=0.6'
    elif any(base.startswith(k) for k in loops):
        src=f'anoisesrc=d=12:c=brown:a=0.3' if not base.startswith('heart') else f'sine=f=55:d=12,tremolo=f={1 if "slow" in base else 2}:d=1'
    else: src=f'sine=f={fr}:d=0.6,afade=t=out:st=0.05:d=0.5'
    subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i',src,'-ar','44100','-ac','1',p],check=True)
subprocess.run(['python3','audio/mix_audio.py','--cues','audio/sound_cues.csv','--audio-dir','preview/ph','--out','preview/mix_placeholder.wav'],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','preview/cards/list.txt','-i','preview/mix_placeholder.wav','-vf','fps=24,format=yuv420p','-c:v','libx264','-crf','20','-c:a','aac','-t','60','exports/animatic_60s_placeholder.mp4'],check=True)
print('ok')
