a = input()
b = input()
o = ''
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for c in range(len(b)):
    s = alp.index(b[c])
    if c % 2 == 1:
        o += alp[(alp.index(a[c]) + s) % 26]
    else:
        o += alp[(alp.index(a[c]) - s) % 26]
print(o)