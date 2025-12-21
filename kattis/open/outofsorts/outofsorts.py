n, m, a, c, x0 = map(int, input().split())
current = x0
sequence = []
for _ in range(n):
    current = (a * current + c) % m
    sequence.append(current)

s = 0

for x in sequence:
    l = 0
    h = n - 1
    while l <= h:
        mid = (l + h) // 2
        mid_val = sequence[mid]
        if mid_val == x:
            s += 1
            break
        elif x < mid_val:
            h = mid - 1
        else:
            l = mid + 1

print(s)