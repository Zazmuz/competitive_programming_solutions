l1, l2, l3 = map(int, input().split())
r1, r2, r3 = map(int, input().split())

u1, u2, u3 = l1/r1, l2/r2, l3/r3
m = min(u1, u2, u3)
print(l1-m*r1, l2-m*r2, l3-m*r3)