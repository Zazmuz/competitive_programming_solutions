while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:break
    
    e = []
    g = [[] for _ in range(a)]
    for _ in range(b):
        u, v, w = map(int, input().split())
        e.append((u, v, w))
        g[u].append(v)

    dist = [9999999999999] * a
    dist[d] = 0

    for _ in range(a - 1):
        for u, v, w in e:
            if dist[u] != 9999999999999 and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    nphard = [False] * a
    for _ in range(a):
        for u, v, w in e:
            if dist[u] != 9999999999999 and dist[u] + w < dist[v]:
                nphard[v] = True
            if nphard[u]:
                nphard[v] = True

    for _ in range(c):
        t = int(input())
        if nphard[t]:
            print("-Infinity")
        elif dist[t] == 9999999999999:
            print("Impossible")
        else:
            print(dist[t])
    print()
