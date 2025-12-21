n, m = map(int, input().split())
from collections import Counter
c = Counter([int(input()) for _ in range(n)])
if max(c.values()) + m >= n:
    print('Ja')
else:
    print('Nej')