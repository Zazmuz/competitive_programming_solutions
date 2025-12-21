input()
l = [int(x) for x in input().split()]
l.sort()
s = 0
last = -1
for c in l:
    if c <= last:
        s += 1
    last = c
print(s)