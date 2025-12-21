line = input().split(';')
s = 0
for l in line:
    if '-' in l:
        l = [int(i) for i in l.split("-")]
        s += len(range(l[0],l[1]+1))
    else:
        s += 1
print(s)