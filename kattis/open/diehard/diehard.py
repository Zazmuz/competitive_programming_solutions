die = [[int(x) for x in input().split()] for _ in range(3)]

wins_losses = [[] for _ in range(3)]
for two_active in ["120", "102", "210", "012", "201", "021"]:
    first = two_active.index("1")
    second = two_active.index("2")
    for rollA in range(6):
        for rollB in range(6):
            if die[first][rollA] > die[second][rollB]:
                wins_losses[first].append("W")
            elif die[first][rollA] < die[second][rollB]:
                wins_losses[first].append("L")
            else:
                wins_losses[first].append("T")
best = "No dice"
for i in range(2, -1, -1):
    a, b = wins_losses[i][:len(wins_losses[i])//2], wins_losses[i][len(wins_losses[i])//2:]
    a = [x for x in a if x != "T"]
    b = [x for x in b if x != "T"]
    if a:
        a = a.count("W") / len(a)
    else:
        a = 0
    if b:
        b = b.count("W") / len(b)
    else:
        b = 0
    worse = min(a, b)
    if worse >= 0.5:
        best = i+1
print(best)