quadkey = input()
big_cord = 2**len(quadkey)
x_min, x_max = 0, big_cord
y_min, y_max = 0, big_cord
for c in quadkey:
    if c == '0':
        x_max = (x_min + x_max) // 2
        y_max = (y_min + y_max) // 2
    elif c == '1':
        x_min = (x_min + x_max) // 2
        y_max = (y_min + y_max) // 2
    elif c == '2':
        x_max = (x_min + x_max) // 2
        y_min = (y_min + y_max) // 2
    elif c == '3':
        x_min = (x_min + x_max) // 2
        y_min = (y_min + y_max) // 2
print(len(quadkey), x_min, y_min)