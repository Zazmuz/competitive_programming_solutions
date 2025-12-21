from collections import Counter
s = 1
while True:
    n = int(input())
    if n == 0:
        break
    animals = []
    for _ in range(n):
        *t, a = input().split()
        animals.append(a.lower())
    c = Counter(animals)

    print(f"List {s}:")
    for k in sorted(c):
        print(f"{k} | {c[k]}")
    s += 1