from collections import deque
input()

def interact_query(x):
    print("?", x)
    return int(input())

l = -int(10**9)
h = int(2*10**9)

H = interact_query(h)
L = interact_query(l)

ducks = {H, L}

q = deque()
q.append((L, H))

while q:
    l, h = q.popleft()

    m = (l + h + 1) // 2
    duck_pos = interact_query(m)

    if duck_pos == l or duck_pos == h:
        continue

    if duck_pos not in ducks:
        ducks.add(duck_pos)
        q.append((l, duck_pos))
        q.append((duck_pos, h))

print("!", len(ducks))
print(*sorted(ducks))