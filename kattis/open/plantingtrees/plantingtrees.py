input()
l = [int(x) for x in input().split()]
l.sort(reverse=True)
d = 0
s = 0
for p in range(len(l)):
    d += 1
    s = max(s, l[p] + 1 + d)
print(s)