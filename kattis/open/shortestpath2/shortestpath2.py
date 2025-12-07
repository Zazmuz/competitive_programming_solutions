import heapq
while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:break
    g = [[] for _ in range(a)]
    for _ in range(b):
        u, v, t_start, P, dst = map(int, input().split())
        g[u].append((v, t_start, P, dst))

    dist = [9999999999999] * a
    dist[d] = 0
    pq = [(0, d)]
    while pq:
        curr, u = heapq.heappop(pq)
        if curr > dist[u]:
            continue
        for v, t_start, P, dst in g[u]:
            if P == 0:
                if curr <= t_start:
                    arr = t_start + dst
                    if arr < dist[v]:
                        dist[v] = arr
                        heapq.heappush(pq, (arr, v))
            else:
                if curr <= t_start:
                    dep = t_start
                else:
                    k = (curr - t_start + P - 1) // P
                    dep = t_start + k * P
                arr = dep + dst
                if arr < dist[v]:
                    dist[v] = arr
                    heapq.heappush(pq, (arr, v))

    for _ in range(c):
        t = int(input())
        if dist[t] == 9999999999999:
            print("Impossible")
        else:
            print(dist[t])
    print()
