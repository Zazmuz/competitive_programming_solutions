b, _ = map(int, input().split())
cutoff = (b+1) // 2 + 1
for trip in [int(x) for x in input().split()]:
    if trip >= cutoff:
        print(b, end=' ')
    else:
        print(1, end=' ')