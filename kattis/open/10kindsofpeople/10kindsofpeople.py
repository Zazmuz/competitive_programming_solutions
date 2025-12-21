from collections import deque
r_len, c_len = map(int, input().split())
maps = []
for i in range(r_len):
    maps.append(list(input()))

n = int(input())

points_of_interest = []
for i in range(n):
    r1, c1, r2, c2 = map(int, input().split())
    points_of_interest.append((r1-1, c1-1, r2-1, c2-1))

done_points = [False for _ in range(n)]

for index, (r1, c1, r2, c2) in enumerate(points_of_interest):
    if done_points[index]:
        print(done_points[index])
        continue
    q = deque([(r1, c1, "0"), (r1, c1, "1")])
    visited_bin = set()
    visited_dec = set()
    if maps[r1][c1] == "0":
        visited_bin.add((r1, c1))
    else:
        visited_dec.add((r1, c1))

    bin_yes = False
    dec_yes = False
    while q:
        r, c, bin_or_dec = q.popleft()
        if maps[r][c] != bin_or_dec:
            continue
        if r == r2 and c == c2:
            if bin_or_dec == "0": bin_yes = True
            else: dec_yes = True
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= r+dr < r_len and 0 <= c+dc < c_len:
                if bin_or_dec == "0":
                    if (r+dr, c+dc) not in visited_bin and maps[r+dr][c+dc] == bin_or_dec:
                        visited_bin.add((r+dr, c+dc))
                        q.append((r+dr, c+dc, bin_or_dec))
                else:
                    if (r+dr, c+dc) not in visited_dec and maps[r+dr][c+dc] == bin_or_dec:
                        visited_dec.add((r+dr, c+dc))
                        q.append((r+dr, c+dc, bin_or_dec))

    if bin_yes:
        if dec_yes:
            print("both")
        else:
            print("binary")
    elif dec_yes:
        print("decimal")
    else:
        print("neither")

    for index_2 in range(index, n):
        r1_2, c1_2, r2_2, c2_2 = points_of_interest[index_2]
        if (r1_2, c1_2) in visited_bin and (r2_2, c2_2) in visited_bin:
            done_points[index_2] = "binary"
        elif (r1_2, c1_2) in visited_dec and (r2_2, c2_2) in visited_dec:
            done_points[index_2] = "decimal"