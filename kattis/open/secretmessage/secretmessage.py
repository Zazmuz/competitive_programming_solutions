for _ in range(int(input())):
    m = input()
    s = 1
    while s**2 < len(m):
        s += 1
    grid = [[''] * s for _ in range(s)]
    for i, c in enumerate(m):
        y = i // s
        x = i % s
        grid[y][x] = c

    for x in range(s):
        for y in range(s - 1, -1, -1):
            if grid[y][x]:
                print(grid[y][x], end='')
    print()