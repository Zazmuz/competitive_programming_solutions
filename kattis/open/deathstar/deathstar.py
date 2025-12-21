N = int(input())
grid = []
for _ in range(N):
    grid.append([int(x) for x in input().split()])

arr = [0] * N
for i in range(N):
    for j in range(N):
        arr[i] |= grid[i][j]
print(*arr)