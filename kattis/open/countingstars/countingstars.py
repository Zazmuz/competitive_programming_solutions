import sys
from collections import deque
lines_left_of_case = 0
first = True
offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
case = 1

def floodFill(x, y, grid, places):
    q = deque([(x, y)])
    while q:
        current = q.popleft()
        x, y = current
        for dx,dy in offsets:
            newX = x + dx
            newY = y + dy

            if 0 <= newX < cols and 0 <= newY < rows:
                if grid[newY][newX] == '-':
                    grid[newY][newX] = str(places)
                    q.append((newX, newY))
for line in sys.stdin.readlines():
    if first:
        rows, cols = map(int, line.split())
        lines_left_of_case = rows
        first = False
        grid = []


    elif lines_left_of_case > 0:
        grid.append(list(line.strip()))
        lines_left_of_case -= 1
        if lines_left_of_case == 0:
            first = True




    if first:
        places = 0
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == '-':
                    places += 1
                    grid[y][x] = str(places)
                    floodFill(x, y, grid, places)
        print(f"Case {case}: {places}")
        case += 1