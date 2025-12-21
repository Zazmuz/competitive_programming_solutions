t = int(input())

b = 0
w = 0
for _ in range(t):
    w += 1
    if w > 6*60 and b < 30:
        b += 1
        w -= 1
    elif w > 9*60 and b < 45:
        b += 1
        w -= 1

    elif w > 10*60:
        b += 1
        w -= 1

print(b)