d = {}
for k in range(2, 1001):
    a, b = 1 % k, 2 % k
    n = 2
    seen = {b: n}
    while True:
        a, b = b, (a + b) % k
        n += 1
        if b in seen:
            d[k] = seen[b]
            break
        seen[b] = n

q = int(input())
for _ in range(q):
    n = int(input())
    print(d[n])