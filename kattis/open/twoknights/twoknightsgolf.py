k,t,f=[["qwertyuiop","asdfghjkl;","zxcvbnm,./","^^      ^^"],["QWERTYUIOP","ASDFGHJKL:","ZXCVBNM<>?","^^      ^^"]],-1,-2
b=lambda c:0<=c[0]<10and 0<=c[1]<4
s=lambda c,w:k[w][c[1]][c[0]]=='^'
def j(c,m,o,l,y):
 p=c[0]+m[0],c[1]+m[1]
 if not b(p)or o==p:return c,l
 if s(p,y):q.append((p,o,l));return p,l
 e=k[s(o,1-y)][p[1]][p[0]]
 if e==w[l]:q.append((p,o,l+1));return p,l+1
 return c,l
while 1:
 w,v=input(),set()
 if w=='*':break
 q=[((0,3),(9,3),0)]
 while q:
  g,h,l=q.pop()
  if l==len(w):print('1');break
  if(l,g,h)in v:continue
  v.add((l,g,h))
  for m in zip([1,2,t,f]*2,2*[2,1]+2*[f,t]):j(g,m,h,l,0);j(h,m,g,l,1)
 else:print('0')