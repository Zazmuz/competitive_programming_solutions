from heapq import heappop, heappush
acorn_amount, totoro_size = map(int, input().split())
acorns = [int(_) for _ in input().split()]
mod = {}
for acorn in acorns:
    amod = acorn % 4
    if amod not in mod:
        mod[amod] = []
    heappush(mod[amod],-acorn)
while totoro_size % 4 in mod and mod[totoro_size % 4]:
    eaten = heappop(mod[totoro_size % 4])
    totoro_size -= eaten
print(totoro_size)