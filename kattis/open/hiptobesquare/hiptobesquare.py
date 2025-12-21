scores = []
for i in range(3, 50_000, 2):
    scores.append(i**2 - 1)


for _ in range(int(input())):
    find = int(input())
    l = 0
    h = len(scores)
    while l < h:
        m = (l + h) // 2
        if scores[m] <= find:
            l = m + 1
        else:
            h = m

    print(l)