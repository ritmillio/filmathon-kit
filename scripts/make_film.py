#!/usr/bin/env python3
"""Join the scene clips into one silent film with 0.5 s dissolves between scenes (ending clips joined hard).
usage: make_film.py OUT.mp4   (falls back to the v3 clip for any v4 clip that does not exist yet)"""
import os, subprocess, sys
D=0.5
scenes=[ (['exports/s01_v4_silent.mp4'],['exports/s01_v3_silent.mp4']),
         (['exports/s02_v4_silent.mp4'],['exports/s02_v3_silent.mp4']),
         (['exports/s03_v4_silent.mp4'],['exports/s03_v3_blue_silent.mp4']),
         (['exports/s04_v4_silent.mp4'],['exports/s04_v2_silent.mp4']),
         (['exports/s05_v2_silent.mp4'],['exports/s05_v2_silent.mp4']),
         (['exports/s06_v5_silent.mp4'],['exports/s06_v4_silent.mp4']),
         (['exports/s7_v4_a_silent.mp4','exports/s7_v4_b_silent.mp4'],['exports/s78_v3_a_silent.mp4','exports/s78_v3_b_silent.mp4'])]
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
chosen=[]
for new,old in scenes:
    use=new if all(os.path.exists(f) for f in new) else old
    print(('NEW ' if use is new else 'fallback ')+', '.join(use)); chosen.append(use)
cmd=['ffmpeg','-v','error','-y']; inputs=[]; seg=[]   # seg: (input indices, duration)
for use in chosen:
    idx=[]
    for f in use: cmd+=['-i',f]; idx.append(len(inputs)); inputs.append(f)
    seg.append((idx,sum(dur(f) for f in use)))
filt=''; labels=[]
for si,(idx,_) in enumerate(seg):
    for k in idx: filt+=f'[{k}:v]scale=1920:1080,setsar=1,fps=24,format=yuv420p[n{k}];'
    filt+=''.join(f'[n{k}]' for k in idx)+f'concat=n={len(idx)}:v=1:a=0[s{si}];'
cur='s0'; t=seg[0][1]
for si in range(1,len(seg)):
    off=t-D; filt+=f'[{cur}][s{si}]xfade=transition=fade:duration={D}:offset={off:.3f}[x{si}];'; cur=f'x{si}'; t=off+D+seg[si][1]-D if False else t+seg[si][1]-D
filt=filt.rstrip(';')
cmd+=['-filter_complex',filt,'-map',f'[{cur}]','-c:v','libx264','-crf','16','-pix_fmt','yuv420p',sys.argv[1]]
subprocess.run(cmd,check=True); print('total about %.1f s'%t)
