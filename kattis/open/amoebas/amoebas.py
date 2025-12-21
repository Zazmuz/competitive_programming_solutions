r, c = map(int, input().split())
g = [input() for _ in range(r)]
v = [[False] * c for _ in range(r)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
a = 0
from collections import deque
q = deque()

for i in range(r):
    for j in range(c):
        if g[i][j] == '#' and not v[i][j]:
            a += 1
            q.append((i, j))
            v[i][j] = True
            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c and g[nx][ny] == '#' and not v[nx][ny]:
                        v[nx][ny] = True
                        q.append((nx, ny))
print(a)