v1x, v1y = map(int, input().split())
v2x, v2y = map(int, input().split())
v3x, v3y = map(int, input().split())
A = abs(v1x * (v2y - v3y) + v2x * (v3y - v1y) + v3x * (v1y - v2y)) / 2
print(A)
s = 0
for tree in range(int(input())):
    tx, ty = map(int, input().split())
    a1 = abs(tx * (v2y - v3y) + v2x * (v3y - ty) + v3x * (ty - v2y))
    a2 = abs(v1x * (ty - v3y) + tx * (v3y - v1y) + v3x * (v1y - ty))
    a3 = abs(v1x * (v2y - ty) + v2x * (ty - v1y) + tx * (v1y - v2y))

    if a1 + a2 + a3 == 2 * A:
        s += 1
print(s)