
n = int(input())

dp = {1: 0}

def s(x):
    path = []
    curr = x
    while curr not in dp:
        path.append(curr)
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = 3 * curr + 1
    
    bb = dp[curr]
    for i, val in enumerate(reversed(path)):
        dp[val] = bb + i + 1
    
    return dp[x]

mmax = -1
best = 1

for x in range(1, n):
    steps = s(x)
    if steps > mmax:
        mmax = steps
        best = x
print(best)