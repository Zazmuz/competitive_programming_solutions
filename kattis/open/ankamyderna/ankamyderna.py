N, M = map(int, input().split())
ducksC = [int(x) for x in input().split()]
layers = [int(x) for x in input().split()]
l, h = 0, len(layers)
while l < h:
    m = (l + h + 1) // 2
    works = True
    ducks = ducksC[:]
    for i in range(m):
        color = layers[i] - 1
        if ducks[color] < (m-i)**2:
            works = False
            break
        ducks[color] -= (m-i)**2
    if works:
        l = m
    else:
        h = m - 1
print(l)