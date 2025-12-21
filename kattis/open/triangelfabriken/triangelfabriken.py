angels = [int(input()) for _ in range(3)]
maxx = max(angels)
ninety = angels.count(90) == 1
if ninety:
    print("Ratvinklig Triangel")
else:
    if maxx < 90:
        print("Spetsig Triangel")
    else:
        print("Trubbig Triangel")