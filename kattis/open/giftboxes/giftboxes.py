n, m = [int(x) for x in input().split()]
if m <= n:
    print(-1)
    exit()

w = [int(x) for x in input().split()]

end = -1
last_seen = {}

for i, x in enumerate(w):
    if x in last_seen:
        end = max(end, last_seen[x])
    last_seen[x] = i

s = -end
l, r = 0, end
for i, x in enumerate(w):
    if x not in last_seen: break

    end = max(i + 1, end, last_seen[x])
    if i - end >= s:
        s = i - end
        l, r = i + 1, end

    last_seen.pop(x)

print(l, r)