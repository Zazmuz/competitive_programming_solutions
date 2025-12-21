while True:
    n = int(input())
    if n == 0:
        break
    a = [int(input()) for _ in range(n)]
    b = [int(input()) for _ in range(n)]
    aS = sorted(a)
    bS = sorted(b)

    adict = {v: i for i, v in enumerate(aS)}
    bdict = {v: i for i, v in enumerate(bS)}
    bdictR = {i: v for i, v in enumerate(bS)}

    a = [adict[v] for v in a]
    for i in range(n):
        print(bdictR[a[i]])
    print()