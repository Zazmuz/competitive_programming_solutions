primes = [False] * 542

# prime sieve

primes[0] = True
primes[1] = True
for i in range(2, 542):
    if not primes[i]:
        for j in range(i * i, 542, i):
            primes[j] = True

s = 0
for i in range(542):
    if not primes[i]:
        print(i)
        s += 1
        if s == 100:
            break