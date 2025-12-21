from collections import deque
for _ in range(int(input())):
    n, e, k = map(int, input().split())
    n += 1
    edges = [[] for _ in range(n)]
    for _ in range(e):
        a, b = map(int, input().split())
        edges[a].append(b)

    visited = [False] * n
    q = deque([])
    for _ in range(k):
        q.append(int(input()))

    while q:
        domino = q.popleft()
        if visited[domino]:
            continue
        visited[domino] = True
        for neigh in edges[domino]:
            q.append(neigh)

    print(sum(visited))