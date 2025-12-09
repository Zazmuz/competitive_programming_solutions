import heapq


for _ in range(int(input())):
    input()
    v = int(input())
    g = [[] for _ in range(v)]
    for u in range(v):
        line = [*map(int, input().split())]
        # clean zippp?????
        for d, s in zip(line[1::2], line[2::2]):
            g[u].append((d, s))
    
    q = int(input())

    for _ in range(q):
        s, t, k = map(int, input().split())
        dist = [[9999999999999] * (k + 1) for _ in range(v)]
        dist[s][1] = 0
        pq = [(0, s, 1)]
        
        while pq:
            d, u, steps = heapq.heappop(pq)
            if d > dist[u][steps]:continue
            if u == t:break

            if steps < k:
                for nv, s in g[u]:
                    nd = d + s
                    if nd < dist[nv][steps + 1]:
                        dist[nv][steps + 1] = nd
                        heapq.heappush(pq, (nd, nv, steps + 1))
        
        ans = min(dist[t])
        print(-1 if ans == 9999999999999 else ans)
    print()