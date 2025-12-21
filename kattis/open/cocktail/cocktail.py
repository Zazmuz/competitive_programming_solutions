n, t = [int(_) for _ in input().split()]
a = [int(input()) for _ in range(n)]
a.sort()
for i in range(n):
    if a[i] <= i*t:
        print("NO")
        exit()
print("YES")