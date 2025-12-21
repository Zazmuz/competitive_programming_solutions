s = 0
for _ in range(int(input())):
    mode, fallmelt = [int(x) for x in input().split()]
    if mode == 0:
        s += fallmelt
    elif mode == 1:
        s = max(0, s - fallmelt)
print(s)