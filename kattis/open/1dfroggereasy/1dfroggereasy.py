n, s, m = [int(i) for i in input().split()]
board = [int(i) for i in input().split()]

hops = 0
pos = s-1
seen = set()
seen.add(pos)


while True:
    if board[pos] == m:
        print("magic")
        print(hops)
        exit()

    hops += 1
    pos += board[pos]
    if pos in seen:
        print("cycle")
        print(hops)
        exit()
    seen.add(pos)
    if pos < 0:
        print("left")
        print(hops)
        exit()
    elif pos >= n:
        print("right")
        print(hops)
        exit()

