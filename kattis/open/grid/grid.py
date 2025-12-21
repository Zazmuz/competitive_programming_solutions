r, c = map(int, input().split())
from collections import deque

visited = [[False] * c for _ in range(r)]
grid = [[int(_) for _ in list(input())] for _ in range(r)]
start = (0, 0)
q = deque()
q.append((start, 0))


def is_within(x1, y1):
    if 0 <= x1 < c and 0 <= y1 < r:
        return True
    else:
        return False


cardinals = ((-1, 0), (1, 0), (0, -1), (0, 1))

while q:
    node, taken = q.popleft()
    x, y = node
    if x == c-1 and y==r-1:
        print(taken)
        exit()
    steps = grid[y][x]
    for card in cardinals:
        diff_x, diff_y = card[0] * steps, card[1] * steps
        new_x, new_y = x+diff_x, y+diff_y
        if is_within(new_x, new_y) and not visited[new_y][new_x]:
            q.append(((new_x, new_y), taken+1))
            visited[new_y][new_x] = True

print(-1)