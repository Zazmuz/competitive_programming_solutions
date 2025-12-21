n,m=map(int,input().split())
s=[[0,0] for _ in range(n+1)]
b=set()
for _ in range(m):
    t,p=map(int,input().split())
    s[t][0]+=1
    s[t][1]-=p
    if s[t]>s[1]:b.add(t)
    if t==1:b=set(i for i in b if s[i]>s[1])
    print(len(b)+1)