from collections import deque
floors, start, goal, up, down = map(int, input().split())

if start == goal:
    print(0)
    exit()

q = deque()

q.append((start, 0))

visited = [False] * (floors + 1)
visited[start] = True

while q:
    pos, steps = q.popleft()
    if pos == goal:
        print(steps)
        exit()
    tryDown = pos - down
    tryUp = pos + up

    if tryDown >= 1:
        if not visited[tryDown]:
            visited[tryDown] = True
            q.append((tryDown, steps+1))

    if tryUp <= floors:
        if not visited[tryUp]:
            visited[tryUp] = True
            q.append((tryUp, steps+1))

print("use the stairs")