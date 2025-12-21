p, d = map(int, input().split())
v = {}
for i in range(p):
    D, a, b = map(int, input().split())
    if D not in v:
        v[D] = [0, 0]
    v[D][0] += a
    v[D][1] += b
aw = 0
bw = 0
V = 0
for i in range(1, d+1):
    a, b = v[i]
    V += a + b
    used_for_win = (a + b) // 2 + 1
    if a > b:

        print('A', a - used_for_win, b)
        aw += a - used_for_win
        bw += b
    elif b > a:
        print('B', a, b - used_for_win)
        aw += a
        bw += b - used_for_win
print(abs(aw - bw) / V)