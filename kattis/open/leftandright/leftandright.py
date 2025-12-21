n = int(input()) - 1
direction = list(input())

out = []

s = []

for i in range(n):
    if direction[i] == 'R':
        out.append(i+1)
        while s:
            out.append(s.pop())
    else:
        s.append(i+1)
s.append(n+1)
while s:
    out.append(s.pop())

print("\n".join(map(str, out)))