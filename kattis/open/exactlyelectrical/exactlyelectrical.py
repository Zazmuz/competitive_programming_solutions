sx, sy = map(int, input().split())
dx, dy = map(int, input().split())
e = int(input())
dist = abs(sx-dx) + abs(sy-dy)
if dist <= e and (e-dist) % 2 == 0:
    print('Y')
else:
    print('N')