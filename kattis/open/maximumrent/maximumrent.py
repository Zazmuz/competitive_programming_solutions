price_per_size, price_per_bulb = map(int, input().split())
size_max, outlet_min = map(int, input().split())

x, y = 1, 1

l, r = 1, size_max
while l <= r:
    mid = (l + r) // 2
    if 2*mid + size_max-mid >= outlet_min:
        r = mid - 1
    else:
        l = mid + 1

x_min = l
x_max = size_max - y

for _ in range(10000):
    mid1 = (2 * x_min + x_max) / 3
    mid2 = (x_min + 2 * x_max) / 3

    y1 = max(1, size_max - mid1)
    y2 = max(1, size_max - mid2)

    f1 = mid1 * price_per_size + y1 * price_per_bulb
    f2 = mid2 * price_per_size + y2 * price_per_bulb

    if f1 < f2:
        x_min = mid1
    else:
        x_max = mid2
x = round(x_min)
y = max(1, size_max - x)

print(x * price_per_size + y * price_per_bulb)