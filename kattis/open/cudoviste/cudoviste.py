grid = []
r, c = map(int, input().split())
for i in range(r):
    grid.append(input())
wacks = [0, 0, 0, 0, 0]
for row in range(r):
    for col in range(c):
        a = ''
        if row+1 < r and col+1 < c:
            a += grid[row][col]
            a += grid[row][col+1]
            a += grid[row+1][col]
            a += grid[row+1][col+1]
            if a.count('#') == 0:
                wacks[a.count('X')] += 1
for thing in wacks:
    print(thing)