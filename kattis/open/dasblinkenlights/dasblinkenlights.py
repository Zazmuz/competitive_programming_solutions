a, b, t = map(int, input().split())
from math import lcm
print('yes' if lcm(a, b) <= t else 'no')