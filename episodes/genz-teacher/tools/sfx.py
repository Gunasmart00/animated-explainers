import numpy as np, wave
SR=48000
def save(name,x):
    x=np.clip(x,-1,1); w=wave.open(name,'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((x*32767).astype(np.int16).tobytes()); w.close()
rng=np.random.default_rng(1)
def bandnoise(n, f0, f1, q=6):
    # sweep a resonant bandpass across noise (simple 2-pole)
    x=rng.standard_normal(n); y=np.zeros(n); y1=y2=0
    for i in range(n):
        f=f0*(f1/f0)**(i/n); w0=2*np.pi*f/SR; r=np.exp(-w0/(2*q))
        a1=-2*r*np.cos(w0); a2=r*r
        yi=(1-r)*x[i]-a1*y1-a2*y2; y2=y1; y1=yi; y[i]=yi
    return y/np.max(np.abs(y))
n=int(0.45*SR); t=np.arange(n)/SR
env=np.sin(np.pi*np.clip(t/0.45,0,1))**2
save('whoosh.wav', 0.8*bandnoise(n,300,3000,3)*env)
n=int(1.4*SR); t=np.arange(n)/SR
f=30+40*np.exp(-t*6); ph=2*np.pi*np.cumsum(f)/SR
imp=np.sin(ph)*np.exp(-t*2.6); imp[:int(0.01*SR)]+=rng.standard_normal(int(0.01*SR))*np.linspace(1,0,int(0.01*SR))*0.6
save('impact.wav', 0.95*imp)
n=int(0.42*SR); t=np.arange(n)/SR
# scratch: noise filtered with zig-zag centre freq
x=rng.standard_normal(n); out=np.zeros(n); y1=y2=0
for i in range(n):
    ph=(t[i]/0.21)%1; fc=600+2600*(ph if int(t[i]/0.21)%2==0 else 1-ph)
    w0=2*np.pi*fc/SR; r=np.exp(-w0/8); a1=-2*r*np.cos(w0); a2=r*r
    yi=(1-r)*x[i]-a1*y1-a2*y2; y2=y1; y1=yi; out[i]=yi
out/=np.max(np.abs(out)); env=np.minimum(1,t/0.01)*np.exp(-t*2)
save('scratch.wav', 0.85*out*env)
n=int(0.12*SR); t=np.arange(n)/SR
save('pop.wav', 0.7*np.sin(2*np.pi*(700+900*t/0.12)*t)*np.exp(-t*30))
print('ok')
