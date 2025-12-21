m1, m2, f = map(int, input().split())
g = 0.25 * m1 + 0.25 * m2 + 0.5 * f
if g >= 90:
    print("A")
elif g >= 80:
    print("B")
elif g >= 70:
    print("C")
elif g >= 60:
    print("D")
else:
    print("F")