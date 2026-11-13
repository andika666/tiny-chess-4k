import json,os,urllib.request as u
U=os.environ["MAKEFUN_ENV_URL"]
def P(p,b):
 q=u.Request(U+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 with u.urlopen(q) as r:return json.load(r)
V=(0,100,320,330,500,900,0)
N=(-33,-31,-18,-14,14,18,31,33)
X=(-17,-15,15,17)
Y=(-16,-1,1,16)
G=X+Y
M=1e5
T={}
C=[0]
class A(Exception):pass
def E(b):
 t=0
 for i,p in enumerate(b):
  if p:
   a=p if p>0 else -p;f=i&7;r=i>>4;x=V[a]+(12-abs(2*f-7)-abs(2*r-7))*int("0255210"[a])
   if a==1:x+=(r if p>0 else 7-r)*8
   t+=x if p>0 else -x
 return t
def K(b,q,w):
 for d in (-15,-17) if w>0 else (15,17):
  t=q+d
  if not t&136 and b[t]==w:return 1
 for s,v,l in ((N,2,0),(G,6,0),(X,3,1),(Y,4,1)):
  for d in s:
   t=q+d
   while not t&136:
    p=b[t]
    if p:
     if p==v*w or p==5*w and (l or v==6):return 1
     break
    if not l:break
    t+=d
 return 0
def L(S,s):return K(S[0],S[1] if s>0 else S[2],-s)
def H(u):return(ord(u[0])-97)+(int(u[1])-1)*16
def g(b,s,a,e,c=0):
 m=[]
 for f,p in enumerate(b):
  if p*s<=0:continue
  z=p if p>0 else -p
  if z==1:
   d=16*s;P7,r0=(7,1) if s>0 else (0,6);t=f+d
   if not t&136 and not b[t]:
    if (t>>4)==P7:m.append((f,t,5))
    elif not c:
     m.append((f,t,0))
     if (f>>4)==r0:
      y=f+2*d
      if not b[y]:m.append((f,y,0))
   for o in (d-1,d+1):
    t=f+o
    if t&136:continue
    q=b[t]
    if q and q*s<0:
     if (t>>4)==P7:m.append((f,t,5))
     else:m.append((f,t,0))
    elif t==e:m.append((f,t,0))
  else:
   for d in (N if z==2 else G if z==6 else X if z==3 else Y if z==4 else X+Y):
    t=f+d
    while not t&136:
     q=b[t]
     if q:
      if q*s<0:m.append((f,t,0))
      break
     if not c:m.append((f,t,0))
     if z==2 or z==6:break
     t+=d
   if z==6 and not c:
    for k,r,j,x in (((4,7,6,1),(4,0,2,2)) if s>0 else ((116,119,118,4),(116,112,114,8))):
     if a&x and all(not b[h] for h in range(min(k,r)+1,max(k,r))) and all(not K(b,h,-s) for h in (k,k+(1 if j>k else -1),j)):m.append((k,j,0))
 return m
def D(S,m):
 b,w,v,a,e=S;f,t,r=m;n=b[:];p=n[f]
 if abs(p)==1 and t==e and not n[t]:n[(f>>4)*16+(t&7)]=0
 n[t]=r*(1 if p>0 else -1) if r else p;n[f]=0
 if abs(p)==6 and abs(t-f)==2:
  q,o=(f+3,f+1) if t>f else (f-4,f-1);n[o]=n[q];n[q]=0
 c=a
 if abs(p)==6:c&=~(1|2) if p>0 else ~(4|8);w,v=(t,v) if p>0 else (w,t)
 for q,z in ((0,2),(7,1),(112,8),(119,4)):
  if f==q or t==q:c&=~z
 return (n,w,v,c,(f+t)//2 if abs(p)==1 and abs(t-f)==32 else -1)
def Q(S,s,a,e):
 o,w,v,c,p=S;C[0]+=1
 if C[0]>1e5:raise A
 if not L(S,s):
  t=E(o)*(1 if s>0 else -1)
  if t>=e:return e
  if t>a:a=t
 for x in g(o,s,c,p,1):
  S2=D(S,x)
  if L(S2,s):continue
  z=-Q(S2,-s,-e,-a)
  if z>a:a=z
  if a>=e:break
 return a
def R(S,s,d,a,e):
 o,w,v,c,p=S;C[0]+=1
 if C[0]>1e5:raise A
 k=(tuple(o),s,c,p)
 x=T.get(k);t=None
 if x:
  t=x[3]
  if x[0]>=d:return x[1]
 if d<=0:return Q(S,s,a,e)
 m=g(o,s,c,p)
 m.sort(key=lambda z:-(z==t)*M*10-abs(o[z[1]]))
 l=a;u=-M;n=None;j=0
 for z in m:
  S2=D(S,z)
  if L(S2,s):continue
  j+=1;v=-R(S2,-s,d-1,-e,-a)
  if v>u:u=v;n=z
  if u>a:a=u
  if a>=e:break
 if not j:return -M if L(S,s) else 0
 if l<u<e:T[k]=(d,u,0,n)
 return u
def F(f):
 q=f.split();b=[0]*128;w=v=4;P="PNBRQK";i=112
 for ch in q[0]:
  if ch=="/":i-=24
  elif ch.isdigit():i+=int(ch)
  else:
   u=P.index(ch.upper())+1;b[i]=u if ch.isupper() else -u
   if u==6:w,v=(i,v) if ch.isupper() else (w,i)
   i+=1
 s=1-2*(q[1]=="b");c=sum(1<<"KQkq".index(ch) for ch in q[2] if ch in"KQkq")
 e=H(q[3]) if q[3]!="-" else -1
 return b,w,v,s,c,e
def Z(f,l):
 b,w,v,s,c,e=F(f);S=(b,w,v,c,e);T.clear()
 m=[(H(u),H(u[2:]),"nbrq".index(u[4])+2 if len(u)==5 else 0) for u in l];C[0]=0;B=None
 for d in range(40):
  try:
   y=-M;n=None
   for x in m:
    S2=D(S,x)
    if L(S2,s):continue
    z=-R(S2,-s,d,-M,M)
    if z>y:y=z;n=x
   B=n
  except A:break
 if not B:return l[0]
 f,t,r=B;u=chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)
 return u+("nbrq"[r-2] if r else "")
while 1:
 J=P("/game",{})
 if J["status"]=="done":break
 while J["status"]=="your_move":J=P("/move",{"game":J["game"],"move":Z(J["fen"],J["legal_moves"])})
