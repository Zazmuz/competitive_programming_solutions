cases = int(input())
for case in range(cases):
    a, m1, b, m2 = map(int, input().split())
    m = m1 * m2

    inv = pow(m1, -1, m2)
    k = (((b - a) % m2) * inv) % m2
    print(m1*k + a, m)