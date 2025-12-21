node_amnt, edge_amnt = map(int, input().split())
edges = [set() for _ in range(node_amnt)]


def bronkerbosch(curr, mby, used, graph):
    cliqs = []
    if not mby and not used:
        cliqs.append(curr)
        return cliqs

    while mby:
        curr_node = mby.pop()
        curr_cliq = curr.union({curr_node})
        mby_cliq = mby.intersection(graph[curr_node])
        used_cliq = used.intersection(graph[curr_node])
        cliqs.extend(bronkerbosch(curr_cliq, mby_cliq, used_cliq, graph))
        used.add(curr_node)
    return cliqs


for edge in range(edge_amnt):
    a, b = map(int, input().split())
    edges[a].add(b)
    edges[b].add(a)

cliques = bronkerbosch(set(), set(range(node_amnt)), set(), edges)
print(max(len(clique) for clique in cliques))