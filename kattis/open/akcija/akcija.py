bA = int(input())
b = [int(input()) for _ in range(bA)]
b.sort(reverse=True)
s = 0
d = 0
for bo in b:
    if d == 2:
        d = 0
        continue
    s += bo
    d += 1
print(s)