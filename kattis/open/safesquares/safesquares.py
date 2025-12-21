g = [[1] * 8 for _ in range(8)]
for r in range(8):
    row = input()
    for c in range(8):
        if row[c] == 'R':
            for all_in_row in range(8):
                g[r][all_in_row] = 0
            for all_in_col in range(8):
                g[all_in_col][c] = 0
s = 0
for r in range(8):
    s += sum(g[r])
print(s)