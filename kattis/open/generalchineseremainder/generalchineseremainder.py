from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


for _ in range(int(input())):
    a, n, b, m = map(int, input().split())
    K = lcm(n, m)
    g = gcd(n, m)

    if (a - b) % g != 0:
        print("no solution")
        continue

    _, x, _ = extended_gcd(n // g, m // g)
    x = (a + n * ((b - a) // g) * x) % K

    print(x, K)
