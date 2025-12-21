r, g, b = map(int, input().split())

if r > g and r > b:
    print("raudur")
elif g > r and g > b:
    print("graenn")
elif b > r and b > g:
    print("blar")
elif r == g and r > b:
    print("gulur")
elif r == b and r > g:
    print("fjolubleikur")
elif g == b and g > r:
    print("blagraenn")
elif g == b and g == r and g == 0:
    print("svartur")
elif g == b and g == r and g == 255:
    print("hvitur")
elif g == b and g == r:
    print("grar")
else:
    print("othekkt")