alp = set(list('abcdefghijklmnopqrstuvwxyz'))
s = set()
for c in input():
    s.add(c)
d = alp - s
print(''.join(sorted(d)) if d else 'Good job!')