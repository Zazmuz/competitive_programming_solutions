from collections import defaultdict, Counter
data = [input() for _ in range(int(input()))]
names = [line.split()[0] for line in data]
last_names = [" ".join(line.split()[1:]) for line in data]
bag = Counter(names)
nc = defaultdict(int)

for i, name in enumerate(names):
    if bag[name] == 1:
        print(name, last_names[i])
    else:
        nc[name] += 1
        if last_names[i]:
            print(f"{name.split()[0]} {nc[name]}. {last_names[i]}")
        else:
            print(f"{name} {nc[name]}.")