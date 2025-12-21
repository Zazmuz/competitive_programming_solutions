from math import pi
while True:
    r, t, p = map(lambda x: float(x) if '.' in x else int(x), input().split())
    if r == 0 and t == 0 and p == 0:
        break
    ac = r*r*pi
    sc = p / t
    ag = sc * (r*2*r*2)
    print(ac, ag)