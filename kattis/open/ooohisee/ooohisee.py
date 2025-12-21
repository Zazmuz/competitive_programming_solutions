r, c = map(int, input().split())
grid = [input() for _ in range(r)]

poss = set()

for i in range(r):
    for j in range(c):
        if grid[i][j] == "0":
            poss.add((i, j))

def inside(x, y):
    return 0 <= x < r and 0 <= y < c


goods = 0
gg = set()
from itertools import product
for pos in poss:
    x, y = pos
    asd = 0
    for i, j in product(range(-1, 2), repeat=2):
        if i == 0 and j == 0:
            continue
        if inside(x + i, y + j):
            if grid[x + i][y + j] == "O":
                asd += 1

    if asd == 8:
        goods += 1
        gg.add((x+1, y+1))

if goods == 1:
    print(*list(gg)[0])
else:
    print("Oh no!" + ("" if goods == 0 else f" {goods} locations"))