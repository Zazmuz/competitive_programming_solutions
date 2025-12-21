import heapq
N, K = [int(x) for x in input().split()]
pcc={}
for i in input().split():
    pcc[i]=pcc.get(i,0)-1
occ=list(pcc.values())
heapq.heapify(occ)
for i in range(K):
    x=heapq.heappop(occ)
    heapq.heappush(occ,x+1)
val = heapq.heappop(occ)
if val < 0:
    print(val*-1)
else:
    print(0)