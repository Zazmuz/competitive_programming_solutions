T, K = [int(x) for x in input().split()]

j = 0
for n in range(1, T+ 1):
    j += K
    j %= n

print(j)