t = float('inf')
for _ in range(int(input())):
    tt, oo = map(int, input().split())
    if oo == 0:
        t = min(t, tt)
print(t if t != float('inf') else -1)