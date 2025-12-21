_, q, k = [int(_) for _ in input().split()]

to_match = input()
#to_match = [to_match[i:i+2] for i in range(0, len(to_match))]
from collections import defaultdict
memo = defaultdict(int)


alp = "abcdefghijklmnopqrstuvwxyz"



i = 0
while i < len(to_match) - 1:
    memo[to_match[i:i+2]] += 1
    i += 1

for let1 in alp:
    lig = let1*2
    i = 0
    s = 0
    while i < len(to_match):
        if to_match[i:i + 2] == lig:
            s += 1
            i += 2
        else:
            i += 1
    memo[lig] = s

for qi in range(q):
    print(memo[input()])
