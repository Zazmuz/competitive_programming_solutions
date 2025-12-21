from time import time
start = time()
from sys import setrecursionlimit
setrecursionlimit(10**6)
r_len, c_len = map(int, input().split())
maps = []
for i in range(r_len):
    maps.append(list(input()))

flood_map = [[-1 for _ in range(c_len)] for _ in range(r_len)]
flood_count = 0


def flood_fill(r, c, count):
    if flood_map[r][c] != -1:
        return
    flood_map[r][c] = count
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_r = r+dr
        new_c = c+dc
        if 0 <= new_r < r_len and 0 <= new_c < c_len:
            if maps[new_r][new_c] == maps[r][c] and flood_map[new_r][new_c] == -1:
                flood_fill(new_r, new_c, count)
n = int(input())

for i in range(n):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

    if flood_map[r1][c1] == -1:
        flood_fill(r1, c1, flood_count)
        flood_count += 1
    if flood_map[r2][c2] == -1:
        flood_fill(r2, c2, flood_count)
        flood_count += 1

    if flood_map[r1][c1] == flood_map[r2][c2]:
        print("binary" if maps[r1][c1] == "0" else "decimal")
    else:
        print("neither")

print(time()-start)