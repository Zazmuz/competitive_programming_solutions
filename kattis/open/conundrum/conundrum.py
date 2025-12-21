p = 'PER'
a = input()
s = 0
for i, l in enumerate(a):
    if l != p[i % 3]:
        s += 1
print(s)
