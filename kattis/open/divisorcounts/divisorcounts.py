import sys
input = sys.stdin.readline
o = sys.stdout.write

n = int(input())
divs = [0] * (n + 1)

for d in range(1, n + 1):
    for m in range(d, n + 1, d):
        divs[m] += 1
o('\n'.join(map(str, divs[1:])) + '\n')