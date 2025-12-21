import itertools
_, t = map(int, input().split())
e = [int(x) for x in input().split()]
ps = list(itertools.accumulate(e))
d = 0
for e in ps:
    if e <= t:
        d += 1
print(d)