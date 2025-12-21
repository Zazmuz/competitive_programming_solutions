from collections import deque
n, m = map(int, input().split())
start = input()
end = input()

allowed = set()
for _ in range(m):
    allowed.add(input())

allowed.add(end)
q = deque()
q.append((start, 0, (start,)))

while q:
    curr, dist, path = q.popleft()
    if curr == end:
        print(dist)
        for p in path:
            print(p)
        break

    for digit_pos in range(len(curr)):
        digit = int(curr[digit_pos])
        for change in [-1, 1]:
            new_digit = (digit + change) % 10
            new_comb = curr[:digit_pos] + str(new_digit) + curr[digit_pos+1:]
            if new_comb in allowed:
                q.append((new_comb, dist + 1, path + (new_comb,)))
                allowed.remove(new_comb)
else:
    print("Neibb")