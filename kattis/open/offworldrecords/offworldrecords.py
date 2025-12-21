n, curr, last = map(int, input().split())

s = 0
for _ in range(n):
    test = int(input())

    if test > curr + last:
        last = curr
        curr = test
        s += 1

print(s)