#!/usr/bin/env python3
"""Join per-section music clips into one 52 s track. usage: assemble_sections.py DIR TAKE OUT.wav  (clips DIR/s1_TAKE.mp3..s8)"""
import subprocess, sys, numpy as np, wave
D,T,OUT=sys.argv[1:4]; SR=44100
B=[0,6,14,20,28,34,40,46,52]
TARGET=[-26,-19,-19,-27,-15,-22,-26,-21]   # RMS dB per section: story arc
X=1.0                                       # crossfade seconds, centred on each cut
def load(p):
    r=subprocess.run(['ffmpeg','-v','error','-i',p,'-f','f32le','-ac','2','-ar',str(SR),'-'],capture_output=True,check=True).stdout
    return np.frombuffer(r,dtype=np.float32).reshape(-1,2)
out=np.zeros((int(52*SR),2),dtype=np.float32)
for i in range(8):
    c=load(f'{D}/s{i+1}_{T}.mp3')
    a=B[i]-(X/2 if i>0 else 0); b=B[i+1]+(X/2 if i<7 else 0)
    n=int((b-a)*SR); c=c[:n]
    rms=20*np.log10(np.sqrt((c**2).mean())+1e-9); c=c*10**((TARGET[i]-rms)/20)
    env=np.ones(len(c),dtype=np.float32); k=int(X*SR)
    if i>0: env[:k]=np.linspace(0,1,k)
    if i<7: env[-k:]=np.minimum(env[-k:],np.linspace(1,0,k))
    s=int(a*SR); out[s:s+len(c)]+=c*env[:,None]
out/=max(1,np.abs(out).max()/0.95)
w=wave.open(OUT,'wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype('<i2').tobytes());w.close()
print('wrote',OUT,len(out)/SR,'s')
