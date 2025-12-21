lookup = {}
for i in range(int(input())):
    a, b = input().split()
    b = int(b)
    if a in lookup:
        lookup[a].append(b)
    else:
        lookup[a] = [b]

for key in lookup:
    lookup[key].sort()

for i in range(int(input())):
    a, b = input().split()
    print(lookup[a][int(b)-1])