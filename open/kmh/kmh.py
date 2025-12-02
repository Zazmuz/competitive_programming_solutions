from math import ceil
n = int(input())
h = 0
for _ in range(n):
    s = input()
    if s != "/":
        h = max(int(s), h)
        print(s)
    else:
        print(10 * ceil((h+1)/10))