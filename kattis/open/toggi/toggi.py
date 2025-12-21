from math import log10
def guess(n):
    return n * log10(n) / 10**6


n = int(input())
l = 0
h = int(10**18)
while l < h:
    m = (l + h) // 2
    if guess(m) < n:
        l = m + 1
    else:
        h = m

l -= 1
print(l)