from heapq import heappop, heappush
input()
p = [-int(x) for x in input().split()]
q = []
for i in p:
    heappush(q, i)

a = 0
b = 0
t = 0
while q:
    if t % 2 == 0:
        a -= heappop(q)
    else:
        b -= heappop(q)
    t += 1
print(a, b)