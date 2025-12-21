def printpath(u, v):
    for i in range(files):
        if dist[u][i] == 1 and (dist[i][v] == dist[u][v] - 1 or dist[u][v] == 1):
            print(names[u], end=" ")
            if dist[u][v] > 1:
                printpath(i, v)
            break

files = int(input())
names = input().split()
name_to_index = {name: indx for indx, name in enumerate(names)}

dist = [[9999999999999999] * files for _ in range(files)]
next_node = [[-1] * files for _ in range(files)]

for _ in range(files):
    filename, rows = input().split()
    rows = int(rows)

    imports = []
    for _ in range(rows):
        imports += input()[7:].split(", ")

    filename = name_to_index[filename]
    for imp in imports:
        imp = name_to_index[imp]
        dist[filename][imp] = 1
        next_node[filename][imp] = imp


for k in range(files):
    for i in range(files):
        for j in range(files):
            if dist[i][k] < 9999999999999999 and dist[k][j] < 9999999999999999:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                next_node[i][j] = next_node[i][k]


small_index = None
smallest = 9999999999999999
for i in range(files):
    if dist[i][i] < smallest:
        smallest = dist[i][i]
        small_index = i
if smallest < 9999999999999999:
    printpath(small_index, small_index)
else:
    print("SHIP IT")