left, right, first, second = [int(_) for _ in input().split(" ")]

from math import lcm
combined = lcm(first, second)
min_mult = (left + combined - 1) // combined
max_mult = right//combined

print(max_mult - (min_mult-1))