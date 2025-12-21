stations, connections = map(int, input().split())
graph = [[] for _ in range(stations)]
for _ in range(connections):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
me, tinder_date = map(int, input().split())
me, tinder_date = me-1, tinder_date-1

seen_me = [False] * stations
seen_date = [False] * stations
from collections import deque
q = deque([me])
seen_me[me] = True
while q:
    node = q.popleft()
    for neigh in graph[node]:
        if not seen_me[neigh]:
            seen_me[neigh] = True
            q.append(neigh)
q = deque([tinder_date])
seen_date[tinder_date] = True
while q:
    node = q.popleft()
    if seen_me[node]:
        print("yes")
        print(node + 1)
        exit(0)
    for neigh in graph[node]:
        if not seen_date[neigh]:
            seen_date[neigh] = True
            q.append(neigh)
print("no")