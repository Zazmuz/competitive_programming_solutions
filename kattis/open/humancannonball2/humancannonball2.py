from math import sin, cos
for case in range(int(input())):
    v0, theta, x1, h1, h2 = map(float, input().split())
    theta = theta * 3.141592653589793 / 180
    h1, h2 = h1 + 1, h2 - 1
    g = 9.81
    t = x1 / (v0 * cos(theta))
    y = v0 * t * sin(theta) - 0.5 * g * t * t
    if h1 < y < h2:
        print("Safe")
    else:
        print("Not Safe")