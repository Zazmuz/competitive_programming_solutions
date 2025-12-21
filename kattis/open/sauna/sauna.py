lows, highs = [] , []
for i in range(int(input())):
    a,b = map(int, input().split())
    lows.append(a)
    highs.append(b)

low, high = max(lows), min(highs)
if low <= high:
    print(high+1-low, low)
else:
    print("bad news")