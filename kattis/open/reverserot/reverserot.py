a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
d = {a[i]: i for i in range(len(a))}
rd = {i: a[i] for i in range(len(a))}
while True:
    line = input()
    if line == '0':
        break
    r, m = line.split()
    r = int(r)
    encrypted = ''
    m = m[::-1]
    for c in m:
        encrypted += rd[(d[c] + r) % 28]
    print(encrypted)