fibs = [1, 1]
n = int(input())
while fibs[-1] <= n:
    fibs.append(fibs[-1] + fibs[-2])

used = []
for f in reversed(fibs):
    if f <= n:
        n -= f
        used.append(f)
print(*sorted(used))