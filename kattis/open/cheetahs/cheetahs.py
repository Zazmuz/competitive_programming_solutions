from sys import setrecursionlimit
setrecursionlimit(100000)
n = int(input())
func = []
start = -1
for i in range(n):
    ins = [int(_) for _ in input().split()]
    start = max(start, ins[0])
    func.append((ins[1], ins[1]*ins[0]))

def dist(x):
    mins = 9999999999999999999999999999
    maxs = -999999999999999999999999999
    for fun in func:
        mins = min(mins, fun[0]*x - fun[1])
        maxs = max(maxs, fun[0]*x - fun[1])
    return maxs - mins

def ternary(l, r):
    for loopc in range(120):
        m1 = (2*l + r) / 3
        m2 = (2*r + l) / 3
        if dist(m1) < dist(m2):
            l, r = l, m2
        else:
            l,r = m1, r
    return dist(l)
print(ternary(start, 1e9))