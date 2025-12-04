def divCnt(n):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1
            if i * i != n:
                cnt += 1
    return cnt


line = input()
x = int(line)

if x == 1:
    print(1)
    exit()

for y in range(60, 1, -1):
    r = int(x ** (1.0 / y))

    n = -1
    if (r + 1) ** y == x:
        n = r + 1
    elif r ** y == x:
        n = r

    if n != -1:
        if divCnt(n) == y:
            print(n)
            exit()
print(-1)