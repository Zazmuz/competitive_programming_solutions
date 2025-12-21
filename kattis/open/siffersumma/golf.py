N=list(map(int,input()));n=len(N)-1;r=range;t=0
def ö(a,b,c):
 e=''
 for j in r(b+1):d=max(0,a-9*(b-j));e+=str(d);a-=d
 print(*c,e,sep='')
for i in r(n,-1,-1):
 a=t-1;t+=N[i]
 if N[i]==9 or not 0<=a<=9*(n-i):continue
 N[i]+=1;ö(a,n-i-1,N[:i+1]);exit()
ö(t-1,n,'1')