import sys, math

sys.setrecursionlimit(200000)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i

            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.num_sets -= 1
            return True
        return False

def kruskal(n, edges, allowed_comp):
    edges.sort(key=lambda x: x[2])

    dsu = DSU(n)
    mst_weight = 0
    edges_count = 0

    for u, v, weight in edges:
        if dsu.union(u, v):
            if dsu.num_sets <= allowed_comp:
                return weight
            mst_weight += weight
            edges_count += 1

    if edges_count != n - 1:
        return -1

    return mst_weight

for case in range(int(input())):
    sat, n = map(int, input().split())

    nodes = []
    for node in range(n):
        a, b = map(int, input().split())
        nodes.append((a,b))

    edges = []
    taken = set()

    for i, s in enumerate(nodes):
        for j, e in enumerate(nodes):
            if i != j:
                x_diff = abs(s[0] - e[0])
                y_diff = abs(s[1] - e[1])
                dist = math.sqrt(x_diff**2 + y_diff**2)

                edges.append((i, j, dist))

    cost = kruskal(n, edges, sat)
    print(f"{cost:.2f}")