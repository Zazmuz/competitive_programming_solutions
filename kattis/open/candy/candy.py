n, f, t = map(int, input().split())
numbers = [*map(int, input().split())]
dp = [[[-1] * (n * f + 1) for _ in range(f + 1)] for _ in range(n + 1)]


def max_sum(i, k, c):
    if i == 0:
        return 0 if k == 0 and c == 0 else -99999999999999999999999
    if k < 0 or c < 0:
        return -99999999999999999999999
    if dp[i][k][c] == -1:
        dp[i][k][c] = max_sum(i - 1, k, c)
        if c - i + k >= 0:
            dp[i][k][c] = max(dp[i][k][c], max_sum(i - 1, k - 1, c - i + k) + numbers[i - 1])
    return dp[i][k][c]

# what are the dimensions of dp?
print(len(dp), len(dp[0]), len(dp[0][0]))
print(len(dp[0][0]) * len(dp[0]) * len(dp))

for c in range(n * f + 1):
    if max_sum(n, f, c) >= t:
        print(c)
        break
else:
    print("NO")
