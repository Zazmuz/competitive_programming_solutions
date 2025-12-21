n = int(input())
Ii = [int(x) for x in input().split()]
m = int(input())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, d = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((b, d))
    edges[b].append((a, d))

import heapq
pq = []
start = 0
end = n-1
heapq.heappush(pq, (0, -Ii[start], start))
dist = [(99999999999, 0)]*n
dist[start] = (0, -Ii[start])
while pq:
    dst, items, node  = heapq.heappop(pq)
    if dist[node][0] < dst:
        continue
    for nnode, ndst in edges[node]:
        ndst += dst
        nitem = items - Ii[nnode]
        if dist[nnode][0] > ndst or (dist[nnode][0] == ndst and dist[nnode][1] > nitem):
            dist[nnode] = (ndst, nitem)
            heapq.heappush(pq, (ndst, nitem, nnode))
if dist[end][0] == 99999999999:
    print("impossible")
else:
    print(dist[end][0], -dist[end][1])