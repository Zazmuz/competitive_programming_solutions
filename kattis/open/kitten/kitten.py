kitten = int(input())
tree = {}
start = None
a = [int(_) for _ in input().split()]
while a != [-1]:
    if start is None:
        start = a[0]
    tree[a[0]] = a[1:]

    a = [int(_) for _ in input().split()]

def dfs(node, path):
    if node == kitten:
        print(node, " ".join(str(_) for _ in path[::-1]))
        return
    if node not in tree:
        return
    for child in tree[node]:
        dfs(child, path + [node])

dfs(start, [])