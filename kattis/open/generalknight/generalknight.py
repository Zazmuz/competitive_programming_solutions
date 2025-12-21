a, b = map(int, input().split())
start = input()

def coords(chess_pos):
    col = ord(chess_pos[0]) - ord('a')
    row = int(chess_pos[1]) - 1
    return row, col

def coords_r(row, col):
    return chr(col + ord('a')) + str(row + 1)

def inside_board(r, c):
    return 0 <= r < 8 and 0 <= c < 8

y, x = coords(start)

moves = {(a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)}

seen = set()
for dx, dy in moves:
    ny, nx = y + dy, x + dx
    if inside_board(ny, nx):
        seen.add((ny, nx))

print(len(seen))
print(*[coords_r(y, x) for y, x in sorted(seen, key=lambda yx: (yx[1], yx[0]))])