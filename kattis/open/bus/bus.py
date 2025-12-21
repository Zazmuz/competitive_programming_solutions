for _ in range(int(input())):
    k = int(input())
    p = 0
    for _ in range(k):
        p += 0.5
        p *= 2
    print(int(p))