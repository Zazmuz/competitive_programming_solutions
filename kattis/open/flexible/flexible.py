W, p = map(int, input().split())
spots = [int(x) for x in input().split()]
spots.append(0)
spots.append(W)
spots = sorted(spots)
possible = [False] * (W + 1)
def check_validity(t):
    for spot1 in spots:
        for spot2 in spots:
            if abs(spot1 - spot2) == t:
                return True
    return False
for test in range(1, W + 1):
    if check_validity(test):
        possible[test] = True
for i in range(W + 1):
    if possible[i]:
        print(i, end=' ')