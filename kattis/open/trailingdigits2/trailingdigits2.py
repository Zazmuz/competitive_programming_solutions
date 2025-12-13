n = int(input())
m = 10**10
tot = 0
for i in range(1,n + 1):
    tot += pow(i, i, m)
    tot %= m
print(tot)