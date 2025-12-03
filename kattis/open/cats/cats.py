import io, os, sys
input_fast = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = lambda: input_fast().decode()

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

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])

    dsu = DSU(n)
    mst_weight = 0
    edges_count = 0

    for u, v, weight in edges:
        if dsu.union(u, v):
            mst_weight += weight
            edges_count += 1

    if edges_count != n - 1:
        return -1

    return mst_weight


for case in range(int(input())):
    milk, cat_amnt = map(int, input().split())
    edge_amnt = (cat_amnt * (cat_amnt - 1)) // 2
    edges = []
    for edge in range(edge_amnt):
        a, b, d = map(int, input().split())
        edges.append((a, b, d))

    milk_spillage = kruskal(cat_amnt, edges)
    milk_needed = milk_spillage + cat_amnt
    if milk_needed > milk:
        print("no")
    else:
        print("yes")