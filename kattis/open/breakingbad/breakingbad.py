item_amount = int(input())
items = []
for _ in range(item_amount):
    items.append(input())

bad_pair_amounts = int(input())
edges = {}
for _ in range(bad_pair_amounts):
    a, b = input().split()
    if a not in edges:
        edges[a] = []
    if b not in edges:
        edges[b] = []
    edges[a].append((b, _))
    edges[b].append((a, _))



walt = set()
seen = set()
jesse = set()
from collections import deque
for item in items:
    if item in seen:
        continue
    if item in edges:
        color = {}
        color[item] = 0
        q = deque([item])
        while q:
            current = q.popleft()
            if current in seen:
                continue
            seen.add(current)
            for neighbor, edge in edges[current]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[current]
                    q.append(neighbor)
                elif color[neighbor] == color[current]:
                    print("impossible")
                    exit()
        for k, v in color.items():
            if v == 0:
                walt.add(k)
            else:
                jesse.add(k)
    else:
        walt.add(item)
print(*walt)
print(*jesse)