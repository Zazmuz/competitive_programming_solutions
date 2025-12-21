n,k=map(int,input().split())
M=10**9+7
p=k+2
a=0
v=[a:=(a+pow(i+1,k,M))%M for i in range(p)]
n%=M
f=[1]*(p+1)
for i in range(1,p+1):
 f[i]=f[i-1]*i%M
F = [1] * (p + 1)
F[p]=pow(f[p],M-2,M)
for i in range(p,0,-1):
 F[i-1]=F[i]*i%M
P=[1]*(p+2)
for i in range(1,p+1):
 P[i]=P[i-1]*(n-i)%M
S=[1]*(p+3)
for i in range(p,0,-1):
 S[i]=S[i+1]*(n-i)%M
s=0
for i in range(1,p+1):
 n=P[i-1]*S[i+1]%M
 d=(f[i-1]*f[p-i])%M
 t=v[i-1]*n%M
 t=t*pow(d,M-2,M)%M
 if(p-i)%2==1:
  t=(M-t)%M
 s=(s+t)%M
print(s)