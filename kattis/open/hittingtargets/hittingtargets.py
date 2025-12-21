obn = int(input())
targets = []
for i in range(obn):
    ins = input().split()
    typ, rest = ins[0], ins[1:]
    if typ == "rectangle":
        targets.append(("r", int(rest[0]), int(rest[1]), int(rest[2]), int(rest[3])))
    else:
        targets.append(("c", int(rest[0]), int(rest[1]), int(rest[2])))

shots = int(input())



for i in range(shots):
    hits = 0
    x, y = map(int, input().split())
    for target in targets:
        if target[0] == "r":
            if target[1] <= x <= target[3] and target[2] <= y <= target[4]:
                hits += 1
        else:
            if (x - target[1])**2 + (y - target[2])**2 <= target[3]**2:
                hits += 1

    print(hits)