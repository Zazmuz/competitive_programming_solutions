r, f = map(int, input().split())
d = (180 * f / r) % 360
flips = d // 180
flips += (d-flips*180) > 90
if flips % 2 == 0:
    print("up")
else:
    print("down")