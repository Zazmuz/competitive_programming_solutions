input()
from heapq import heapify, heappop
f = [int(x) for x in input().split()]
heapify(f)
print(heappop(f) + heappop(f))