from collections import Counter
input()
p = [int(x) for x in input().split()]
c = Counter(p)
try:
    print(p.index(max(x for x in c if c[x] == 1)) + 1)
except ValueError:
    print("none")