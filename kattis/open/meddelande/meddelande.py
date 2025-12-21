rowN, colN = map(int, input().split())
pos = [0, 0]
word = ""

grid = [input()+"." for _ in range(rowN)]
grid.append("."*(colN+1))

for y in range(rowN):
    for x in range(colN):
        if grid[y][x] != ".":
            word += grid[y][x]

print(word)