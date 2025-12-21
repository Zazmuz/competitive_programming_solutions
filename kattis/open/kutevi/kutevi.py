from collections import deque

n, k = map(int, input().split())
angles = list(map(int, input().split()))
qq = list(map(int, input().split()))

possible = set(angles)
q = deque(angles)

while q:
    a = q.popleft()
    for b in list(possible):
        for new_angle in [(a + b) % 360, abs(a - b) % 360]:
            if new_angle not in possible:
                possible.add(new_angle)
                q.append(new_angle)

for angle in qq:
    print("YES" if angle in possible else "NO")