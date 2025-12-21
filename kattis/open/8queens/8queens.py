valid = True
board = [list(input()) for i in range(8)]

def check_queen(x, y):
    board[y][x] = "."

    # leftright
    for yx_i in range(8):
        if board[y][yx_i] == "*":
            return False
        if board[yx_i][x] == "*":
            return False

    for xy_i in range(8):
        if not x-xy_i < 0:
            if not y-xy_i < 0:
                if board[y-xy_i][x-xy_i] == "*":
                    return False
            if not y+xy_i > 7:
                if board[y+xy_i][x-xy_i] == "*":
                    return False
        if not x+xy_i > 7:
            if not y-xy_i < 0:
                if board[y-xy_i][x+xy_i] == "*":
                    return False
            if not y+xy_i > 7:
                if board[y+xy_i][x+xy_i] == "*":
                    return False
    board[y][x] = "*"
    return True

cnt = 0
for row in range(8):
    for col in range(8):
        if board[col][row] == "*":
            cnt += 1
            valid &= check_queen(row, col)

if cnt != 8:
    valid = False
print("valid" if valid else "invalid")