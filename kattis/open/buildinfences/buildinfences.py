n = int(input()) - 1
x_min, y_min = map(int, input().split())
x_max, y_max = x_min, y_min
for _ in range(n):
    x, y = map(int, input().split())
    x_min = min(x_min, x)
    y_min = min(y_min, y)
    x_max = max(x_max, x)
    y_max = max(y_max, y)
x_min -= 1
y_min -= 1
x_max += 1
y_max += 1

print(2*abs(x_max - x_min) + 2*abs(y_max - y_min))