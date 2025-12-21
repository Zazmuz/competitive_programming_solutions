points_x = []
points_y = []
for i in range(3):
    x, y = [int(x) for x in input().split()]
    points_x.append(x)
    points_y.append(y)

uniq_x = None
uniq_y = None

for i in points_x:
    if points_x.count(i) == 1:
        uniq_x = i

for i in points_y:
    if points_y.count(i) == 1:
        uniq_y = i

print(uniq_x, uniq_y)