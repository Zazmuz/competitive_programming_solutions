l, w, n, r = map(int, input().split())
r = r ** 2
cranes = [[int(i) for i in input().split()] for time in range(n)]
walls = [(-l / 2, 0), (l / 2, 0), (0, -w / 2), (0, w / 2)]
can_reach = []
for crane in cranes:
    reaches = 0
    for ij, wall in enumerate(walls):
        if abs(crane[0] - wall[0]) ** 2 + abs(crane[1] - wall[1]) ** 2 <= r:
            reaches |= 1 << ij
    if reaches:
        can_reach.append(reaches)

mem = {}


def recc(index, added, sums):
    if (index, sums) in mem:
        return mem[(index, sums)] + added
    if sums == 15:
        return added
    if index >= len(can_reach):
        return 9999999

    ret = min(recc(index + 1, added + 1, sums | can_reach[index]), recc(index + 1, added, sums))
    mem[(index, sums)] = ret - added
    return ret


ccc = recc(0, 0, 0)
if ccc > 9999:
    print('Impossible')
else:
    print(ccc)
