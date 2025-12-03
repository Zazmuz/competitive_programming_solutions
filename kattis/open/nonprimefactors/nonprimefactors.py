import subprocess
from collections import Counter
import sys

iterator = iter(sys.stdin.read().split())
num_test_cases = int(next(iterator))

snd = []
for _ in range(num_test_cases):
    snd.append(next(iterator))


proc = subprocess.Popen(
    ['factor'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
out, _ = proc.communicate('\n'.join(snd))

r = out.strip().split('\n')
o = []
for facs in r:
    factors = facs.split()[1:]
    factors = Counter(factors).values()

    nonPrime = 1
    for f in factors:
        nonPrime *= int(f) + 1
    o.append(str(nonPrime - len(factors)))
print('\n'.join(o))