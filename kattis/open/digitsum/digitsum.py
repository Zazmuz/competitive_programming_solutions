cases = int(input())
dp = {}

ss = lambda x: sum(int(i) for i in str(x))

def rec(n):
    if n in dp:
        return dp[n]
    if n <= 0:
        return 0
    ret = 0
    if n % 10 == 0:
        ret += 10 * rec(n // 10)
        ret += 45 * (n // 10)
    else:
        ret += rec(n - 1)
        ret += ss(n - 1)
    dp[n] = ret
    return ret


for case in range(cases):
    f, t = map(int, input().split())
    t += 1
    f, t = map(rec, (f, t))
    print(t - f)