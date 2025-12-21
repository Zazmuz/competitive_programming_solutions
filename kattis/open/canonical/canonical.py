n = int(input())
coins = list(map(int, input().split()))
coins.sort()
max_counter = coins[-1] + coins[-2]
INF = max_counter + 10
dp = [INF] * (max_counter + 1)
dp[0] = 0

for c in coins:
    for a in range(c, max_counter + 1):
        v = dp[a - c] + 1
        if v < dp[a]:
            dp[a] = v

greedy_rem = [0] * coins[-1]
idx = 0
m = len(coins)
for r in range(1, coins[-1]):
    while idx + 1 < m and coins[idx + 1] <= r:
        idx += 1
    greedy_rem[r] = greedy_rem[r - coins[idx]] + 1

for amnt in range(1, max_counter + 1):
    g = (amnt // coins[-1]) + greedy_rem[amnt % coins[-1]]
    if g != dp[amnt]:
        print('non-canonical')
        break
else:
    print('canonical')