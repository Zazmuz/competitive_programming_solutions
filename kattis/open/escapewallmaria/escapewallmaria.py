from collections import deque
q = deque()

t, row_amnt, col_amnt = map(int, input().split())

map = []
start_pos = None
for y in range(row_amnt):
    line = input()
    for x in range(col_amnt):
        if line[x] == 'S':
            start_pos = (x,y)
    map.append(line)

q.append((start_pos, 0))
visited = set()


while q:
    (x,y),steps = q.popleft()
    if steps > t:
        break

    if x == 0 or x == col_amnt - 1 or y == 0 or y == row_amnt - 1:  # Out of bounds
        print(steps)
        exit(0)

    for dx,dy,allowedDir in [(0,1,"U"),(0,-1,"D"),(1,0,"L"),(-1,0,"R")]:
        new_x = x + dx
        new_y = y + dy


        if (new_x,new_y) in visited:
            continue

        if map[new_y][new_x] == '0' or map[new_y][new_x] == allowedDir:
            visited.add((new_x,new_y))
            q.append(((new_x,new_y), steps + 1))

print("NOT POSSIBLE")