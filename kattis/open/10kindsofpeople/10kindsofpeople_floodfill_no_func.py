from collections import deque
r_len, c_len = map(int, input().split())
maps = []
for i in range(r_len):
    maps.append(list(input()))

flood_map = [[-1 for _ in range(c_len)] for _ in range(r_len)]
flood_count = 0


n = int(input())

q = deque()
offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(n):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

    if flood_map[r1][c1] == -1:
        tile_allowed = maps[r1][c1]
        q.append((r1, c1))
        flood_map[r1][c1] = flood_count
        while q:
            r, c = q.popleft()
            for dr, dc in offsets:
                new_r = r+dr
                new_c = c+dc
                if 0 <= new_r < r_len and 0 <= new_c < c_len:
                    if flood_map[new_r][new_c] == -1 and maps[new_r][new_c] == tile_allowed:
                        flood_map[new_r][new_c] = flood_count
                        q.append((new_r, new_c))
        flood_count += 1

    if flood_map[r2][c2] == -1:
        tile_allowed = maps[r2][c2]
        q.append((r2, c2))
        flood_map[r2][c2] = flood_count

        while q:
            r, c = q.popleft()
            for dr, dc in offsets:
                new_r = r+dr
                new_c = c+dc
                if 0 <= new_r < r_len and 0 <= new_c < c_len:
                    if flood_map[new_r][new_c] == -1 and maps[new_r][new_c] == tile_allowed:
                        flood_map[new_r][new_c] = flood_count
                        q.append((new_r, new_c))
        flood_count += 1

    if flood_map[r1][c1] == flood_map[r2][c2]:
        print("binary" if maps[r1][c1] == "0" else "decimal")
    else:
        print("neither")