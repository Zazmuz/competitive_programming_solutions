graph = {}
for i in range(int(input())):
    costs = [int(j) for j in input().split()]
    for j, cost in enumerate(costs):
        if cost != -1:
            graph[(i+1, j+1)] = cost

print(len(graph.keys()))
for key in graph.keys():
    print(*key, graph[key])