import sys

input = sys.stdin.read
data = input().splitlines()

index = 0
while True:
    nodes, edges, queries = map(int, data[index].split())
    index += 1
    if nodes == 0:
        break

    graph = [[9999999999999999] * nodes for _ in range(nodes)]
    for i in range(nodes):
        graph[i][i] = 0

    for _ in range(edges):
        a, b, w = map(int, data[index].split())
        index += 1
        graph[a][b] = min(graph[a][b], w)

    dist = [row[:] for row in graph]

    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                if dist[i][k] < 9999999999999999 and dist[k][j] < 9999999999999999:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for k in range(nodes):
        if dist[k][k] < 0:
            for i in range(nodes):
                for j in range(nodes):
                    if dist[i][k] < 9999999999999999 and dist[k][j] < 9999999999999999:
                        dist[i][j] = -9999999999999999

    for _ in range(queries):
        a, b = map(int, data[index].split())
        index += 1
        if dist[a][b] == 9999999999999999:
            print("Impossible")
        elif dist[a][b] == -9999999999999999:
            print("-Infinity")
        else:
            print(dist[a][b])

    print("")