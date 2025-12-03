import sys
import subprocess
from collections import Counter

input = sys.stdin.readline
o = sys.stdout.write

n = int(input())
res = subprocess.check_output(f"factor {n}", shell=True).split()[1:]
primes = [int(x) for x in res]
c = Counter(primes)

divs = [1]
for p, e in c.items():
    new_divs = []
    for d in divs:
        pk = 1
        for _ in range(e + 1):
            new_divs.append(d * pk)
            pk *= p
    divs = new_divs

divs.sort()
o('\n'.join(map(str, divs)))
