from collections import deque, defaultdict

def c(cc):
    x = ord(cc[0]) - ord('a')
    y = int(cc[1]) - 1
    return x, y

def rc(x, y):
    return chr(x + ord('a')) + str(y + 1)

def hash(a):
    xx, yy = c(a)
    return yy * 8 - xx


for case in range(int(input())):
    q = deque()
    s = c(input())
    s = (s[0], s[1])
    q.append((s, 0))
    visited = {s}
    dirs = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    best = defaultdict(list)
    m = 0
    while q:
        (x, y), dist = q.popleft()
        if dist >= m:
            m = dist
            best[m].append(rc(x, y))
        pos = (x, y)

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                new_pos = (nx, ny)
                if new_pos not in visited:
                    q.append((new_pos, dist + 1))
                    visited.add(new_pos)

    print(m, *sorted(best[m], key=hash, reverse=True))