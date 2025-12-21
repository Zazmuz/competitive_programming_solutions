n, k, p = map(int, input().split())
p /= 100
r = n - k
continues = (r * 0.1 + 0.1) + p * (n * 0.1 + 0.1 + 0.3)
backspace = (0.1 + 0.1 + r * 0.1) + (1 - p) * (n * 0.1 + 0.1 + 0.3)
restart = 0.3 + n * 0.1 + 0.1
minn = min(continues, backspace, restart)
if minn == continues:
    print("continue")
elif minn == backspace:
    print("backspace")
else:
    print("restart")