n, m = map(int, input().split())

from collections import deque

graph = [[] for i in range(n)]
indeg = [0 for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    indeg[b] += 1

q = deque()
for i in range(n):
    if indeg[i] == 0:
        q.append(i)

order = []
while q:
    current = q.popleft()
    order.append(current)
    for neighbor in graph[current]:
        indeg[neighbor] -= 1
        if indeg[neighbor] == 0:
            q.append(neighbor)

if len(order) != n:
    print("IMPOSSIBLE")
else:
    for i in order:
        print(i + 1)
