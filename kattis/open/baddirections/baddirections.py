for _ in range(int(input())):
    a, b = input().split()
    a = int(a)
    for c in b:
        c = int(c)
        print((c+a)%10, end="")
    print()