row, col = map(int, input().split())
grid = [[False]*col for _ in range(row)]
for _ in range(int(input())):
    r, c = map(int, input().split())
    grid[r-1][c-1] = True

def count_neighbors(x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < col and 0 <= y + j < row:
                count += grid[y + j][x + i]
    return count

around = [0]*9
for i in range(col):
    for j in range(row):
        if grid[j][i]:
            around[count_neighbors(i, j)] += 1

print(" ".join(map(str, around)))