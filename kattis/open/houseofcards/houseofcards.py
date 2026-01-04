n = int(input())
hh = 3*n*(n+1) // 2
while not (hh - n) % 4 == 0:
    n += 1
    hh += 3*n
print(n)