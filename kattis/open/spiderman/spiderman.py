INF = 9999999999
for _ in range(int(input())):
    n = int(input())
    heights = [int(x) for x in input().split()]
    dp = [[INF] * (n + 1) for _ in range(1001)]
    parent_dir = [[''] * (n + 1) for _ in range(1001)]
    dp[0][0] = 0

    for x in range(n):
        for y in range(1001):
            if dp[y][x] != INF:
                new_h_UP = y + heights[x]
                new_h_DOWN = y - heights[x]

                if new_h_UP >= 0:
                    highest = max(new_h_UP, dp[y][x])
                    if highest < dp[new_h_UP][x+1]:
                        dp[new_h_UP][x+1] = highest
                        parent_dir[new_h_UP][x+1] = 'U'


                if new_h_DOWN >= 0:
                    highest = max(new_h_DOWN, dp[y][x])
                    if highest < dp[new_h_DOWN][x+1]:
                        dp[new_h_DOWN][x+1] = highest
                        parent_dir[new_h_DOWN][x+1] = 'D'
    if dp[0][-1] == INF:
        print('IMPOSSIBLE')
    else:
        o = ''
        h = 0
        for xi in range(n, -1, -1):
            d = parent_dir[h][xi]
            o += d
            if d == 'U':
                h -= heights[xi-1]
            else:
                h += heights[xi-1]
        print(o[::-1])