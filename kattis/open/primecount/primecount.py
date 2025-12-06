def solve():
    n = int(input())

    if n < 2:
        print(0)
        exit()

    s = int(n ** 0.5)
    vals = []
    i = 1

    while i <= n:
        v = n // i
        i = n // v + 1
        vals.append(v)

    m = len(vals)
    id1 = [0] * (s + 1)
    id2 = [0] * (s + 1)

    for i, v in enumerate(vals):
        if v <= s:
            id1[v] = i
        else:
            id2[n // v] = i

    g = [v - 1 for v in vals]

    for p in range(2, s + 1):
        if g[id1[p]] == g[id1[p - 1]]:
            continue

        sp = g[id1[p - 1]]
        p2 = p * p

        for i in range(m):
            v = vals[i]
            if v < p2:break

            div = v // p
            idx = id1[div] if div <= s else id2[n // div]
            g[i] -= g[idx] - sp

    print(g[0])
solve()