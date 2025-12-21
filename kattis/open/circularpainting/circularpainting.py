a = 0
for _ in range(int(input())):
    d, r1, r2 = map(int, input().split())
    d /= 360
    a += 3.141592653589793 * (r2**2 - r1**2) * d
print(a)