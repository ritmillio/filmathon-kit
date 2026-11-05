#!/usr/bin/env python3
"""Recolour the lamp's two black tear drops in the stage 3 clip to a soft muted blue.
Only very dark pixels inside two narrow boxes beside the lamp pole, in frames 95-140, are changed. Editing step, not generation."""
import subprocess, numpy as np, sys
src,dst=sys.argv[1],sys.argv[2]
W,H=1920,1080; fb=W*H*3
rd=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
wr=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','24','-i','-','-c:v','libx264','-crf','14','-pix_fmt','yuv420p',dst],stdin=subprocess.PIPE)
BLUE=np.array([118,160,214],dtype=np.float32)   # soft muted blue
boxes=[(292,380,342,720),(406,380,466,720)]     # x0,y0,x1,y1 (left drop, right drop), pole outline at x~345-395 excluded
n=0
while True:
    buf=rd.stdout.read(fb)
    if len(buf)<fb: break
    f=np.frombuffer(buf,np.uint8).reshape(H,W,3).copy()
    bx=list(boxes)
    if n>=130: bx+=[(332,785,352,832),(428,785,472,832)]   # tiny splash spots on the floor
    if 95<=n<=143:
        for x0,y0,x1,y1 in bx:
            reg=f[y0:y1,x0:x1].astype(np.float32)
            lum=reg.mean(axis=2)
            a=np.clip((30-lum)/12.0,0,1)[...,None]       # only near-black pixels -> opacity
            reg=reg*(1-a)+BLUE*a
            f[y0:y1,x0:x1]=reg.astype(np.uint8)
    wr.stdin.write(f.tobytes()); n+=1
wr.stdin.close(); wr.wait(); print('frames',n)
