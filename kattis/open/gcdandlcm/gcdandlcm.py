from collections import Counter

x, y = map(int, input().split())

m = y // x

if m == 1:
    divisors = [1]

else:
    import subprocess

    res = subprocess.check_output(f"factor {m}", shell=True).split()[1:]
    factors = Counter([x.decode() for x in res])

    prime_powers = []
    for p, exp in factors.items():
        p = int(p)
        prime_powers.append(p ** exp)

    divisors = [1]
    for pp in prime_powers:
        divisors = divisors + [d * pp for d in divisors]

    divisors = sorted(divisors)

pairs = []
for d in divisors:
    p, q = d, m // d
    a, b = x * p, x * q
    pairs.append((a, b))

pairs.sort()

for a, b in pairs:
    print(a, b)