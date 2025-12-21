from decimal import Decimal
times = []
sugar = []
n=int(input())
for i in range(n):
    t, g = map(Decimal, input().split())
    sugar.append(g)
    times.append(t)

s = 0
k=Decimal(1000)
for i in range(1,n):
    s += ((times[i] - times[i-1]) * (sugar[i] + sugar[i-1]) / 2) / k

print(s)