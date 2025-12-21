xs, ys = map(int, input().split())
xt, yt = map(int, input().split())
xp, yp = map(int, input().split())
pos = [xs, ys]
bigg = 1000000
def change_y(new_y):
    print(pos[0], new_y)
    pos[1] = new_y
def change_x(new_x):
    print(new_x, pos[1])
    pos[0] = new_x

print(4)
if yp < ys:
    change_y(bigg)
else:
    change_y(-bigg)

if xp > xt:
    change_x(-bigg)
else:
    change_x(bigg)

change_y(yt)
change_x(xt)