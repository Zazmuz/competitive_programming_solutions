n = int(input())
if n <= 0:
    n = -n
    print(-n * (n + 1) // 2 + 1)
else:
    print(n * (n + 1) // 2)