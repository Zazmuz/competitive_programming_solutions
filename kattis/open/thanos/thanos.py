for _ in range(int(input())):
    p, r, f = map(int, input().split())
    s = 0
    while p <= f:
        s += 1
        p *= r
    print(s)