for _ in range(int(input())):
    n, m = map(int, input().split())
    items = [int(x) for x in input().split()]
    twopos = []
    s = []
    l = 0
    i = 0
    while i < n:

        if items[i] > m:
            l += items[i]
            i += 1
        elif items[i] < m:
            if l != 0:
                s.append(l)
            l = 0
            s.append(0)
            i += 1
        else:
            if l != 0:
                s.append(l)
            l = 0
            twopos.append(len(s))
            s.append(m)
            i += 1
    s.append(l)

    mmax = 0
    for pos in twopos:
        left, right = pos - 1, pos + 1
        sums = m
        if left >= 0:
            if s[left] != m:
                sums += s[left]
        if right < len(s):
            if s[right] != m:
                sums += s[right]
        mmax = max(mmax, sums)
    print(mmax)