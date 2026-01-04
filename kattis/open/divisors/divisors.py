def sieve(n):
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

def exponent_in_factorial(n, p):
    exp = 0
    power = p
    while power <= n:
        exp += n // power
        power *= p
    return exp

def count_divisors(n, k, primes):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    k = min(k, n - k)
    
    divisor_count = 1
    for p in primes:
        if p > n:
            break
        exp = exponent_in_factorial(n, p) - exponent_in_factorial(k, p) - exponent_in_factorial(n - k, p)
        if exp > 0:
            divisor_count *= (exp + 1)
    
    return divisor_count

primes = sieve(431)

import sys
lines = sys.stdin.read().strip().split('\n')
for line in lines:
    n, k = map(int, line.split())
    print(count_divisors(n, k, primes))