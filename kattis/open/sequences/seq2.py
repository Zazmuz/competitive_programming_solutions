t, a, d = 0, 0, 1

row = input()

for c in reversed(row):
    if c == "0":
        a += d
        a %= 1000000007
    elif c == "1":
        t += a
        t %= 1000000007
    else:
        t *= 2
        t += a
        t %= 1000000007
        a *= 2
        a += d
        a %= 1000000007
        d *= 2
        d %= 1000000007

print(t)