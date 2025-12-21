grid = [[int(i) for i in input().split()] for j in range(4)]
move = int(input())
can_merge = [[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True]]
if move == 0:
    new = [[0]*4 for ii in range(4)]
    for row in range(4):
        for moving in range(4):
            number_moving = grid[row][moving]
            #print(grid)
            #print("og", moving, row, number_moving)
            while moving-1 >= 0 and new[row][moving-1] == 0:
                moving -= 1
                #print(moving)
            if moving-1 >= 0 and new[row][moving-1] == number_moving  and can_merge[row][moving-1]:
                new[row][moving-1] = number_moving*2
                can_merge[row][moving-1] = False
            else:
                new[row][moving] = number_moving

if move == 2:
    new = [[0]*4 for ii in range(4)]
    for row in range(4):
        for moving in range(3, -1, -1):
            number_moving = grid[row][moving]
            #print(grid)
            #print("og", moving, row, number_moving)
            while moving+1 < 4 and new[row][moving+1] == 0:
                moving += 1
                #print(moving)
            if moving+1 < 4 and new[row][moving+1] == number_moving and can_merge[row][moving+1]:
                new[row][moving+1] = number_moving*2
                can_merge[row][moving+1] = False
            else:
                new[row][moving] = number_moving

if move == 1:
    new = [[0]*4 for ii in range(4)]
    for col in range(4):
        for moving in range(4):
            number_moving = grid[moving][col]
            #print(grid)
            #print("og", moving, col, number_moving)
            while moving-1 >= 0 and new[moving-1][col] == 0:
                moving -= 1
                #print(moving)
            if moving-1 >= 0 and new[moving-1][col] == number_moving and can_merge[moving-1][col]:
                new[moving-1][col] = number_moving*2
                can_merge[moving-1][col] = False
            else:
                new[moving][col] = number_moving

if move == 3:
    new = [[0]*4 for ii in range(4)]
    for col in range(4):
        for moving in range(3, -1, -1):
            number_moving = grid[moving][col]
            #print(grid)
            #print("og", moving, col, number_moving)
            while moving+1 < 4 and new[moving+1][col] == 0:
                moving += 1
                #print(moving)
            if moving+1 < 4 and new[moving+1][col] == number_moving and can_merge[moving+1][col]:
                new[moving+1][col] = number_moving*2
                can_merge[moving+1][col] = False
            else:
                new[moving][col] = number_moving



for line in new:
    print(' '.join([str(num) for num in line]))

"""
1 1 1 0
1 2 3 0
0 3 0 0
2 0 3 3
1"""