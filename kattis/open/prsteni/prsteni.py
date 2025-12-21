from math import gcd
def simp(a, b):
    return a // gcd(a, b), b // gcd(a, b)

input()
spins = [int(x) for x in input().split()]
rel = spins[0]

for spin in spins[1:]:
    a, b = simp(rel, spin)
    print(f"{a}/{b}")