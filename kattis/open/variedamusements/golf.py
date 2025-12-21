n,a,b,c=map(int,input().split())
M=1000000007
dp={}
def B(l, L=-1):
 if(l,L)in dp:return dp[(l,L)]
 if l==0:return 1
 r=0
 if a>0and L!=0:
  for _ in range(a):
   r+=B(l-1,0)
 if b>0and L!=1:
  for _ in range(b):
   r+=B(l-1,1)
 if c>0and L!=2:
  for _ in range(c):
   r+=B(l-1,2)
 dp[(l,L)]=r%M
 return r
print(B(n)%M)