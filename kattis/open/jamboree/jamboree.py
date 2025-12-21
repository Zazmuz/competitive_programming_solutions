item_amnt, scout_amnt = map(int, input().split())
items = [int(x) for x in input().split()]

items.sort(reverse=True)
scounts = [0] * scout_amnt

for i in range(item_amnt):
    if i < scout_amnt:
        scounts[i] = items[i]
    else:
        scounts[scout_amnt - 1 - (i % scout_amnt)] += items[i]

print(max(scounts))