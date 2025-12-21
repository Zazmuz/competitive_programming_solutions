n = int(input())
cit = []
for _ in range(n):
    cit.append(int(input()))
if sum(cit) == 0:
    print(0)
    exit()
cit.sort()
l = 1
d = True
a = 1
while True:
    if d:
        t = l*2
    else:
        t = l + a
    c = 0

    L, H = 0, n-1

    while L <= H:
        mid = (L + H) // 2
        if cit[mid] >= t:
            c = n - mid
            H = mid - 1
        else:
            L = mid + 1

    if c >= t:
        l = t
    else:
        if d:
            d = False
        else:
            break
print(l)