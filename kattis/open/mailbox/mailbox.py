N = int(input())
K_MAX = 10
M_MAX = 100
inf = 999999999999999999999999
dp = [[[0] * (M_MAX+1) for _ in range(M_MAX+1)] for __ in range(K_MAX + 1)]

for k in range(1, K_MAX + 1):
    for a in range(M_MAX + 1, -1, -1):
        for b in range(a, M_MAX + 1):
            if a > b:
                dp[k][a][b] = 0
            elif k == 1:
                dp[k][a][b] = ((b + 1) * b) // 2 - ((a - 1) * a) // 2 # sum from a to b
            else:
                min_val = inf
                for x in range(a, b + 1):
                    if x - 1 < a:
                        left = 0
                    else:
                        left = dp[k - 1][a][x - 1]

                    if x + 1 > b:
                        right = 0
                    else:
                        right = dp[k][x + 1][b]

                    current = x + max(left, right)

                    if current < min_val:
                        min_val = current
                dp[k][a][b] = min_val

for _ in range(N):
    k, m = map(int, input().split())
    print(dp[k][0][m])

