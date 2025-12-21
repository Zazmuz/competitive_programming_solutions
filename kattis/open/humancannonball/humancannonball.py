import math
import heapq

xs, ys = map(float, input().split())
xe, ye = map(float, input().split())
cannon_amnt = int(input())
cannons = [tuple(map(float, input().split())) for _ in range(cannon_amnt)]

r = 5.0

nodes = [(xs, ys)] + cannons + [(xe, ye)]
m = len(nodes)

def dist(i, j):
    (x1, y1), (x2, y2) = nodes[i], nodes[j]
    return math.hypot(x1 - x2, y1 - y2)

INF = 999999999999999
dists = [INF] * m
dists[0] = 0.0
q = [(0, 0)]

while q:
    cur, u = heapq.heappop(q)
    if cur > dists[u]:continue
    if u == m - 1:break
    for v in range(m):
        if v == u:continue
        dv = dist(u, v)
        if u == 0:
            w = dv / r
        else:
            w = min(dv / r, 2.0 + abs(dv - 50.0) / r)
        nd = cur + w
        if nd < dists[v]:
            dists[v] = nd
            heapq.heappush(q, (nd, v))

print(dists[-1])
