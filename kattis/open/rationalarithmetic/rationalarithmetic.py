from fractions import Fraction
for case in range(int(input())):
    x1, y1, op, x2, y2 = input().split()
    a = Fraction(int(x1), int(y1))
    b = Fraction(int(x2), int(y2))
    c = eval(f"a {op} b")
    print(f"{c.numerator} / {c.denominator}")