from sys import stdin
from math import acos, pi
for line in stdin.readlines():
    r, x, y = map(float, line.split())
    d2 = (x**2 + y**2)
    r2 = r**2
    if d2 > r2 or r <= 0:
        print("miss")
        continue

    d = d2**0.5
    crack_area = r2 * acos(d / r) - d * max(0.0, r2 - d2)**0.5
    all_area = pi * r2
    other = all_area - crack_area
    minn = min(crack_area, other)
    maxx = max(crack_area, other)
    print(maxx, minn)