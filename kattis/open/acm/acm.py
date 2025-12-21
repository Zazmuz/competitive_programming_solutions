from collections import defaultdict
r = []
d = defaultdict(int)
while True:
    line = input()
    if line == "-1":
        break

    m, p, b = line.split()
    m = int(m)
    if b == "wrong":
        d[p] += 20
        continue
    d[p] += m
    r.append(p)
s = 0
for p in r:
    s += d[p]
print(len(r), s)