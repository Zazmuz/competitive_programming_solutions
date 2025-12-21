from collections import deque

def dfs(i):
    global time, bridges
    time += 1
    low[i] = disc[i] = time
    for j in people[i]:
        if disc[j] == 0:
            parent[j] = i
            dfs(j)
            low[i] = min(low[i], low[j])
            if low[j] > disc[i]:
                bridges += 1
        elif j != parent[i]:
            low[i] = min(low[i], disc[j])

while True:
    p, c = map(int, input().split())
    if p == c == 0:
        break

    people = [[] for _ in range(p)]
    for _ in range(c):
        i, j = map(int, input().split())
        people[j].append(i)
        people[i].append(j)

    visited = [False] * p
    visited[0] = True
    q = deque([0])
    while q:
        i = q.popleft()
        for j in people[i]:
            if not visited[j]:
                visited[j] = True
                q.append(j)

    if not all(visited):
        print("Yes")
        continue

    bridges = 0
    low = [0] * p
    disc = [0] * p
    parent = [0] * p
    time = 0
    for i in range(p):
        if not visited[i]:
            continue

        if disc[i] == 0:
            dfs(i)

    print("Yes" if bridges != 0 else "No")