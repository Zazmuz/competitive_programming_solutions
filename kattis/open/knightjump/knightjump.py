x = int(input())

grid = [list(input()) for _ in range(x)]

start = (-1, -1)
end = (0, 0)

for i in range(x):
    for j in range(x):
        if grid[i][j] == "K":
            start = (i, j)


from collections import deque

q = deque([(start, 0)])
visited = {start}

offsets = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
def is_inside_and_valid(pos):
    if 0 <= pos[0] < x and 0 <= pos[1] < x:
        return grid[pos[0]][pos[1]] != "#"
    return False

while q:
    cur, moves = q.popleft()
    if cur == end:
        print(moves)
        break
    for move in offsets:
        new_pos = (cur[0] + move[0], cur[1] + move[1])
        if is_inside_and_valid(new_pos) and new_pos not in visited:
            visited.add(new_pos)
            q.append((new_pos, moves + 1))
else:
    print("-1")