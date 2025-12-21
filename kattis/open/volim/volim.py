p = int(input())
t = 3 * 60 + 30
for q in range(int(input())):
    tt, v = input().split()
    tt = int(tt)
    t -= tt
    if t < 0:
        print(p)
        break
    if v == 'T':
        p += 1
        p %= 9
        if p == 0:
            p = 1