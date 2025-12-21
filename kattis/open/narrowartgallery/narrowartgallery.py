from sys import setrecursionlimit
setrecursionlimit(1000000)
grid = []
dpt = {}
def dp(row, prev, left_block, path=''):
    if (row, prev, left_block) in dpt:
        return dpt[(row, prev, left_block)]
    if left_block < 0:
        return 999999999999
    if row == -1:
        if left_block == 0:
            return 0
        else:
            return 99999999999

    r = 9999999999
    if prev == '00':
        r = min(r, dp(row-1, '00', left_block, path+"\n00"))
        r = min(r, dp(row-1, '10', left_block-1, path+"\n10")+ grid[row][0])
        r = min(r, dp(row-1, '01', left_block-1, path+"\n01")+ grid[row][1])
    elif prev == '10':
        r = min(r, dp(row-1, '00', left_block, path+"\n00"))
        r = min(r, dp(row-1, '10', left_block-1, path+"\n10")+ grid[row][0])
    elif prev == '01':
        r = min(r, dp(row-1, '00', left_block, path+"\n00"))
        r = min(r, dp(row-1, '01', left_block-1, path+"\n01")+ grid[row][1])

    dpt[(row, prev, left_block)] = r

    return r

while True:
    rows, close = map(int, input().split())
    if rows == 0:
        break
    grid = []
    for i in range(rows):
        a, b = map(int, input().split())
        grid.append((a, b))

    t = sum(sum(row) for row in grid)
    print(t - dp(rows-1, '00', close, "++"))