R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
offset = {"E":(1,0), "W":(-1,0), "S":(0,1), "N":(0,-1)}

def inside(xt, yt):
    return 0<=xt<C and 0<=yt<R


pos = (0,0)
visited = set()
moves = 0
while True:
    if not inside(*pos):
        print("Out")
        exit()
    g=grid[pos[1]][pos[0]]
    if g == "T":
        print(moves)
        exit()
    if pos in visited:
        print("Lost")
        exit()

    visited.add(pos)
    pos = (pos[0]+offset[g][0], pos[1]+offset[g][1])
    moves += 1