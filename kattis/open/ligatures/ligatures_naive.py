_, q, k = [int(_) for _ in input().split()]

to_match = input()
to_match = [to_match[i:i+2] for i in range(0, len(to_match), 1)]
for qi in range(q):
    ligs = input()
    ligs = {ligs[i:i+2] for i in range(0, len(ligs), 2)}

    i = 0
    s = 0
    while i < len(to_match):
        if to_match[i] in ligs:
            s += 1
            i += 2
        else:
            i += 1
    print(s)