from sys import stdin
for line in stdin.readlines():
    line = line.split()
    name = []
    vals = []
    for thing in line:
        if thing.isalpha():
            name.append(thing)
        else:
            vals.append(float(thing))
    print(sum(vals) / len(vals), " ".join(name))