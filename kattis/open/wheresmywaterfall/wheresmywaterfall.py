y, x, w = map(int, input().split())
wx = [int(x) for x in input().split()]
grid = [list(input()) for _ in range(y)]
from collections import deque
q = deque()
for wi in wx:
    q.append((wi, 0))

while q:
    cx, cy = q.popleft()

    if cx < 0 or cx >= x or cy == y:
        continue

    if grid[cy][cx] == 'O':
        grid[cy][cx] = '~'
    else:
        continue

    if cy == y-1:
        continue

    down = grid[cy+1][cx]
    if down in '#?':
        q.append((cx-1, cy))
        q.append((cx+1, cy))
    else:
        q.append((cx, cy+1))

for row in grid:
    print(''.join(row))