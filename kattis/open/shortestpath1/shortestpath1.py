from heapq import heappop, heappush
from math import inf
def dijkstra(graph, root, n):
    dist = [inf for _ in range(n)]
    dist[root] = 0
    visited = [False for _ in range(n)]
    pq = [(0, root)]

    while pq:
        _, u = heappop(pq)
        if visited[u]:
            continue
        visited[u] = True

        for v, l in graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
                heappush(pq, (dist[v], v))
    return dist

while True:
    nodes, edges, queries, start = map(int, input().split())
    if not any([edges, nodes, queries, start]):
        break
    neighbors = [[] for node in range(nodes)]
    for edge in range(edges):
        a,b,c = map(int, input().split())
        neighbors[a].append((b,c))
        #neighbors[b].append((a, c))
    #print(neighbors)
    dists = dijkstra(neighbors, start, nodes)
    for query in range(queries):
        end = int(input())
        dd = dists[end]
        if dd == inf:
            print("Impossible")
        else:
            print(dd)
        #print(start, end)
