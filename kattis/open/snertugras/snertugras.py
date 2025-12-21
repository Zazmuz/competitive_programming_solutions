h, w = map(int, input().split())
grid = []
for row in range(h):
    grid.append(list(input()))

start = None
for row in range(h):
    for col in range(w):
        if grid[row][col] == 'S':
            start = (row, col)
            break
    if start:break

from collections import deque
q = deque([(start, 0)])
while q:
    pos, d = q.popleft()
    r, c = pos

    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < h and 0 <= nc < w:
            if grid[nr][nc] == 'G':
                print(d+1)
                exit()
            elif grid[nr][nc] == '.':
                grid[nr][nc] = '#'
                q.append(((nr, nc), d+1))
print("thralatlega nettengdur")