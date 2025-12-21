from collections import Counter
bag = Counter()
while True:
    a = input()
    if a == "***":
        break
    bag[a] += 1
bag[".................."] = 0
bag = sorted(bag.items(), key=lambda x: x[1], reverse=True)
if bag[0][1] == bag[1][1]:
    print("Runoff!")
else:
    print(bag[0][0])