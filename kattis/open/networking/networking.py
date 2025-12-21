from collections import defaultdict

n, k = map(int, input().split())
lecturers = defaultdict(list)

for _ in range(n):
    d, s = input().split()
    lecturers[s].append(int(d))

dp = [-1] * (k + 1)
dp[0] = 0
for group in list(lecturers.values()):
    temp_dp = dp.copy()
    for credit in group:
        for j in range(k, credit - 1, -1):
            if temp_dp[j - credit] != -1:
                dp[j] = max(dp[j], temp_dp[j - credit] + credit)

max_credits = max(filter(lambda x: x <= k, dp))
print(max_credits)

