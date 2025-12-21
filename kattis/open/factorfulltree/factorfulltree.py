from collections import deque
nodes = int(input())
graph = [[] for i in range(nodes)]
for i in range(nodes-1):
    a, b = [int(i)-1 for i in input().split()]
    graph[a].append(b)
    graph[b].append(a)
leafs,v,q = [],set(),deque()
q.append((0, 0, [0]))
while q:
    currentnode, depth, path = q.popleft()
    if currentnode in v:continue
    v.add(currentnode)
    if len(graph[currentnode]) == 1:leafs.append((currentnode, depth, path))
    for neighbor in graph[currentnode]:q.append((neighbor, depth+1, path+[neighbor]))
primes = []
for i in range(2, 1000):
    isprime = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            isprime = False
            break
    if isprime:primes.append(i)
nextprime,factors = 0,[-1 for i in range(nodes)]
factors[0] = 1
for i in range(len(leafs)):
    worstcost = 0
    worstnode = None
    for leaf in leafs:
        leafnode, depth, path = leaf
        path = path[::-1]
        empty,cost = 0,1
        for currentnode in path:
            if factors[currentnode] == -1:
                empty += 1
            else:
                cost *= factors[currentnode]

            if currentnode == 0:
                cost *= primes[nextprime]**empty
                if cost > worstcost:worstcost,worstnode = cost,leaf
    worst_path = worstnode[2][::-1]
    leafs.remove(worstnode)
    for currentnode in worst_path:
        if factors[currentnode] == -1:factors[currentnode] = primes[nextprime]
    nextprime += 1
ans,v = [1 for i in range(nodes)], set()
q.append((0, 1))
while q:
    currentnode, cost = q.popleft()
    if currentnode in v:continue
    v.add(currentnode)
    ans[currentnode] = cost
    for neighbor in graph[currentnode]:q.append((neighbor, cost*factors[neighbor]))
print(*ans)