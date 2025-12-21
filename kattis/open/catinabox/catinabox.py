h, w, l, CAT = map(int, input().split())
v = h * w * l
if v == CAT:
    print('COZY')
elif v < CAT:
    print('TOO TIGHT')
else:
    print('SO MUCH SPACE')