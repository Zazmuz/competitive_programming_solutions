from collections import deque
row_amnt, col_amnt = map(int, input().split())
grid = []
for _ in range(row_amnt):
    for num in input().split():
        grid.append(int(num))

l, h = 0, 10**9
directions = [1, -1, col_amnt, -col_amnt]
while l < h:
    m = (l + h) // 2
    visited = [False] * (row_amnt * col_amnt)
    visited[0] = True
    q = deque()
    q.append(0)
    works = False
    while q:
        p = q.popleft()
        if p == len(grid) - 1:
            works = True
            break

        for d in directions:
            if col_amnt != 1:
                if p % col_amnt == 0 and d == -1: continue
                if p % col_amnt == col_amnt-1 and d == 1: continue
            np = p + d
            if np < 0 or np >= len(grid): continue
            if visited[np]: continue
            if grid[np] - grid[p] <= m:
                visited[np] = True
                q.append(np)
        else:
            continue
    if works:
        h = m
    else:
        l = m+1
print(l)