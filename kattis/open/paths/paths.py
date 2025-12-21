import sys
sys.setrecursionlimit(99999999)
nodeA, edgeA, colorA = [int(i) for i in input().split()]
nodeColor = [int(i) for i in input().split()]
nodeColor = [None] + nodeColor
connections = [[] for i in range(nodeA+1)]
memo = {}
for i in range(edgeA):
    fromN, toN = [int(i) for i in input().split()]
    connections[fromN].append(toN)
    connections[toN].append(fromN)



def walk(node, seen):
    check = (node, seen)
    if check in memo:
        return memo[check]

    ret = 1
    myColor = 1 << nodeColor[node]
    seen |= myColor
    for newNode in connections[node]:
        if ((1<<nodeColor[newNode])&seen>0):
            continue
        ret += walk(newNode, seen)

    memo[check] = ret
    return ret

s = 0
for dos in range(1,nodeA+1):
    s += walk(dos,0)

print(s-nodeA)