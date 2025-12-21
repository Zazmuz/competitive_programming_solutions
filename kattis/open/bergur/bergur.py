input()
l = [int(x) for x in input().split()]
l.reverse()
s = 0
lowest = float('inf')
for e in l:
    lowest = min(lowest, e)
    s += lowest
print(s)