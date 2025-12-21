g, r = map(int, input().split())
s = 0
if g > 0 and r > 0:
    rm = min(g, r)
    s += rm*10
    g -= rm
    r -= rm

while g > 0:
    if g >= 3:
        s += 10
        g -= 3
    elif g == 2:
        s += 3
        g -= 2
    else:
        s += 1
        g -= 1

print(s)