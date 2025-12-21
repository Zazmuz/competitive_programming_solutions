from math import sqrt
for case in range(int(input())):
    message = input()
    grid_size = int(sqrt(len(message)))
    grid = []
    for i in range(grid_size):
        part = []
        for j in range(grid_size):
            part.append(message[grid_size*i + j])
        grid.append(part)
    for col in range(grid_size):
        for row in range(grid_size):
            cur = grid[row][grid_size-1-col]
            print(cur,end='')
    print()