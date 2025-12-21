from sys import stdin, stdout
from array import array
lines = data = list(map(int, stdin.buffer.read().split()))
it = iter(data)
out = []
while True:
    c = next(it, None)
    if c is None:
        break
    n = next(it)

    values = [0] * n
    weights = [0] * n
    for i in range(n):
        values[i] = next(it)
        weights[i] = next(it)

    dp = [array('I', [0]) * (c + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        value = values[i - 1]
        weight = weights[i - 1]
        dp_prev = dp[i - 1]
        dp_curr = dp[i]
        if weight > c:
            dp_curr[:] = dp_prev
            continue

        if weight:
            dp_curr[:weight] = dp_prev[:weight]
        for w in range(weight, c + 1):
            a = dp_prev[w]
            b = dp_prev[w - weight] + value
            dp_curr[w] = b if b > a else a

    taken = []
    w = c
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            taken.append(i - 1)
            w -= weights[i - 1]
            if w == 0:
                break
    out.append(str(len(taken)))
    out.append(" ".join(map(str, taken[::-1])))
stdout.write("\n".join(out))