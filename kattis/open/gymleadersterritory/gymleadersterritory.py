o,h=input,range
n,k,m=[int(_) for _ in o().split()]
l,q=[[] for _ in h(n+1)],[]
for _ in h(m):
    a, b = [int(_) for _ in o().split()]
    l[a]+=b,
    l[b]+=a,
for i in h(n+1):
    if len(l[i])==1:q+=i,
while q:
    N=q.pop(0)
    for A in l[N]:
        l[A].remove(N)
        if len(l[A])==1:q+=A,
    l[N]=[]
print("YES"if []==l[k]else"NO")