g = []
for i in range(4):
    g.append(input())

alp = "ABCDEFGHIJKLMNO"
p = {a : (i // 4, i % 4) for i, a in enumerate(alp)}

s = 0
for x in range(4):
    for y in range(4):
        if g[x][y] != '.':
            px, py = p[g[x][y]]
            s += abs(px - x) + abs(py - y)
print(s)