for _ in range(int(input())):
    n = input()
    s = sum(int(x) for x in list(n)) - 1
    n = int(n)
    while sum(int(x) for x in list(str(n))) != s:
        n -= 1
    print(n)