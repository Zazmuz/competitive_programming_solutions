n, a, b, c = map(int, input().split())
dp = {}
def B(l, L=-1):
    if (l, L) in dp:
        return dp[(l, L)]
    if l == 0:
        return 1
    r = 0
    if a > 0 and L != 0:
        for _ in range(a):
            r += B(l - 1, 0) % 1000000007
    if b > 0 and L != 1:
        for _ in range(b):
            r += B(l - 1, 1) % 1000000007
    if c > 0 and L != 2:
        for _ in range(c):
            r += B(l - 1, 2) % 1000000007
    dp[(l, L)] = r % 1000000007
    return r
print(B(n) % 1000000007)