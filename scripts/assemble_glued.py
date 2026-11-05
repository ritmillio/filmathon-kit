#!/usr/bin/env python3
"""Join section clips into one 52 s track with glue. usage: assemble_glued.py DIR TAKE PAD.mp3 OUT.wav
Glue: equal-power crossfades centred on each cut, a reverb tail from each outgoing clip that rings into the next section, one quiet continuous pad underneath."""
import subprocess, sys, numpy as np, wave
D,T,PAD,OUT=sys.argv[1:5]; SR=44100; rng=np.random.default_rng(7)
B=[0,6,14,20,28,34,40,46,52]
TARGET=[-26,-19,-19,-27,-15,-22,-26,-21]
X=1.0; PADDB=-31; TAILDB=-7; RT=2.2
def load(p):
    r=subprocess.run(['ffmpeg','-v','error','-i',p,'-f','f32le','-ac','2','-ar',str(SR),'-'],capture_output=True,check=True).stdout
    return np.frombuffer(r,dtype=np.float32).reshape(-1,2)
def rms(c): return 20*np.log10(np.sqrt((c**2).mean())+1e-9)
# reverb impulse: decaying noise, darkened
n=int(RT*SR); t=np.arange(n)/SR
ir=np.stack([rng.standard_normal(n)*np.exp(-t*6.9/RT) for _ in range(2)],1)
for ch in range(2):
    k=np.ones(8)/8; ir[:,ch]=np.convolve(ir[:,ch],k,'same')
ir/=np.abs(ir).sum(0).max()
def reverb(x):
    L=len(x)+len(ir); N=1<<(L-1).bit_length()
    return np.stack([np.fft.irfft(np.fft.rfft(x[:,c],N)*np.fft.rfft(ir[:,c],N),N)[:L] for c in range(2)],1).astype(np.float32)
out=np.zeros((int((52+RT)*SR),2),dtype=np.float32)
for i in range(8):
    c=load(f'{D}/s{i+1}_{T}.mp3')
    a=B[i]-(X/2 if i>0 else 0); b=B[i+1]+(X/2 if i<7 else 0)
    c=c[:int((b-a)*SR)]; c=c*10**((TARGET[i]-rms(c))/20)
    k=int(X*SR); env=np.ones(len(c),dtype=np.float32)
    if i>0: env[:k]=np.sin(np.linspace(0,np.pi/2,k))
    if i<7: env[-k:]=np.minimum(env[-k:],np.cos(np.linspace(0,np.pi/2,k)))
    s=int(a*SR); out[s:s+len(c)]+=c*env[:,None]
    if i<7:  # reverb tail of the outgoing clip's last 1.2 s rings on into the next section
        seg=c[-int(1.2*SR):]*np.cos(np.linspace(0,np.pi/2,int(1.2*SR)))[:,None]
        tail=reverb(seg); tail*=10**((rms(seg)+TAILDB-rms(tail))/20)
        tail*=np.concatenate([np.ones(int(.2*SR)),np.cos(np.linspace(0,np.pi/2,len(tail)-int(.2*SR)))])[:,None]**2
        e=s+len(c)-int(1.2*SR); out[e:e+len(tail)]+=tail[:len(out)-e]
pad=load(PAD)[:int(52*SR)]; pad=pad*10**((PADDB-rms(pad))/20)
fi=int(2*SR); pad[:fi]*=np.linspace(0,1,fi)[:,None]
out[:len(pad)]+=pad
out=out[:int(52*SR)]
out/=max(1,np.abs(out).max()/0.95)
w=wave.open(OUT,'wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype('<i2').tobytes());w.close()
print('wrote',OUT,len(out)/SR,'s')
