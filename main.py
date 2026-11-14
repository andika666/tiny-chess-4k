import json as j,os,urllib.request as u
U=os.getenv("MAKEFUN_ENV_URL")
def P(p,b):return j.load(u.urlopen(U+p,j.dumps(b).encode()))
V=0,100,320,330,500,900,0
N=-33,-31,-18,-14,14,18,31,33
X=-17,-15,15,17
Y=-16,-1,1,16
G=X+Y
M=1e5
T={};A={}
C=[0]
I=[0]*40
def W():
 C[0]+=1;C[0]>15e4 and 1/0
def E(b,w,v):
 t=0
 for i,p in enumerate(b):
  if p:
   a=abs(p);f=i&7;r=i>>4;x=V[a]+(12-abs(2*f-7)-abs(2*r-7))*(0,2,5,5,2,1,0)[a];d=i-(v,w)[p<0]
   if a==1:x+=(r^7*(p<0))*8
   t+=x*p//a
 return t
def K(b,q,w):
 for d in-15,-17:
  t=q+d*w
  if not t&136 and b[t]==w:return 1
 for s,v,l in(N,2,0),(G,6,0),(X,3,1),(Y,4,1):
  for d in s:
   t=q+d
   while not t&136:
    p=b[t]
    if p:
     if p==v*w or p==5*w and(l or v>5):return 1
     break
    if not l:break
    t+=d
 return 0
def L(S,s):return K(S[0],S[2-(s>0)],-s)
def H(u):return ord(u[0])+16*ord(u[1])-881
def g(b,s,a,e,c=0):
 m=[];n=m.append
 for f,p in enumerate(b):
  if p*s<=0:continue
  z=abs(p)
  if z==1:
   d=16*s;P7=7*(s>0);r0=1+5*(s<0);t=f+d
   if not t&136 and not b[t]:
    if t>>4==P7:n((f,t,5))
    elif not c:
     n((f,t,0))
     if f>>4==r0:
      y=f+2*d
      if not b[y]:n((f,y,0))
   for o in d-1,d+1:
    t=f+o
    if t&136:continue
    q=b[t]
    if q*s<0:
     if t>>4==P7:n((f,t,5))
     else:n((f,t,0))
    elif t==e:n((f,t,0))
  else:
   for d in(N,X,Y,G,G)[z-2]:
    t=f+d
    while not t&136:
     q=b[t]
     if q*s<0 or not q and not c:n((f,t,0))
     if q:break
     if z%4==2:break
     t+=d
   if z==6 and not c:
    for k,r,j,x in((4,7,6,1),(4,0,2,2))if s>0 else((116,119,118,4),(116,112,114,8)):
     if a&x and all(not b[h] for h in range(min(k,r)+1,max(k,r))) and all(not K(b,h,-s) for h in(k,(k+j)//2,j)):n((k,j,0))
 return m
def D(S,m):
 b,w,v,a,e=S;f,t,r=m;n=b[:];p=n[f]
 if p*p==1 and t==e and not n[t]:n[f&112|t&7]=0
 n[t]=r*(p>0 or-1)or p;n[f]=0
 if p*p==36 and abs(t-f)==2:
  q,o=(f+3,f+1)if t>f else(f-4,f-1);n[o]=n[q];n[q]=0
 c=a
 if p*p==36:c&=(-4,-13)[p<0];w,v=(t,v)if p>0 else(w,t)
 for q,z in(0,2),(7,1),(112,8),(119,4):
  if q in(f,t):c&=~z
 return(n,w,v,c,(f+t)//2 if p*p==1 and abs(t-f)==32 else-1)
def Q(S,s,a,e):
 o,w,v,c,p=S;W()
 k=L(S,s)
 if not k:
  a=max(a,E(o,w,v)*s)
  if a>=e:return e
 j=0
 for x in sorted(g(o,s,c,p,1-k),key=lambda z:-abs(o[z[1]])):
  if not k and 0<abs(o[x[1]])<abs(o[x[0]])and K(o,x[1],-s):continue
  S2=D(S,x)
  if L(S2,s):continue
  j+=1
  z=-Q(S2,-s,-e,-a)
  if z>a:a=z
  if a>=e:break
 return-M if k and not j else a
def R(S,s,d,a,e):
 o,w,v,c,p=S;W()
 k=(*o,s,c,p)
 x=T.get(k);t=x and x[3]
 if x and x[0]>=d:return x[1]
 if d<=0:return Q(S,s,a,e)
 y=L(S,s)
 if d>2 and not y:
  z=-R((o,w,v,c,-1),-s,d-3,-e,-a)
  if z>=e:return e
 m=g(o,s,c,p)
 m.sort(key=lambda z:(z!=t,z!=I[d],-abs(o[z[1]])))
 l=a;u=-M;n=None;j=0
 for z in m:
  S2=D(S,z)
  if L(S2,s):continue
  j+=1;v=-R(S2,-s,d-1,-a-1,-a)if j>1 else-R(S2,-s,d-1,-e,-a)
  if j>1 and a<v<e:v=-R(S2,-s,d-1,-e,-a)
  if v>u:u=v;n=z
  if u>a:a=u
  if a>=e:
   if not o[z[1]]:I[d]=z
   break
 if not j:return-M if y else 0
 if l<u<e:T[k]=(d,u,0,n)
 return u
def F(f):
 q=f.split();b=[0]*128;w=v=4;P="PNBRQK";i=112
 for ch in q[0]:
  if ch=="/":i-=24
  elif ch.isdigit():i+=int(ch)
  else:
   u=P.find(ch.upper())+1;b[i]=u*(ch<'a'or-1)
   if u==6:w,v=(i,v)if ch.isupper()else(w,i)
   i+=1
 s=1-2*(q[1]<"w");c=sum(1<<"KQkq".find(ch)for ch in q[2]if ch>"-")
 e=H(q[3])if q[3]>"-"else-1
 return b,w,v,s,c,e
def Z(f,l,h):
 b,w,v,s,c,e=F(f);S=(b,w,v,c,e);T.clear();q=E(b,w,v)*s;k=(h,*b,s,c,e)
 m=[(H(u),H(u[2:]),u[4:]and"nbrq".find(u[4])+2 or 0) for u in l];C[0]=0;B=None
 for d in range(40):
  try:
   y=-M;n=None
   for x in m:
    S2=D(S,x)
    if L(S2,s):continue
    z=-R(S2,-s,d,-M,M)
    if A.get(k)==x:z=25*((q<0)-(q>0))
    if z>y:y=z;n=x
   B=n
  except Exception:break
 if not B:return l[0]
 f,t,r=B;A[k]=B;u="%c%d%c%d"%(97+(f&7),f//16+1,97+(t&7),t//16+1)
 return u+"nbrq"[r-2]if r else u
while 1:
 J=P("/game",{});s=J["status"]
 if s=="done":break
 if s=="your_move":J=P("/move",{"game":J["game"],"move":Z(J["fen"],J["legal_moves"],J["game"])})
