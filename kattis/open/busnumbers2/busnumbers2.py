from collections import defaultdict
bus_numbers = defaultdict(int)
seen = set()
for i in range(1, int(400_000**(1/3))):
    for j in range(1, int(400_000**(1/3))):
        a = [i, j]
        a.sort()
        if tuple(a) in seen:
            continue
        seen.add(tuple(a))
        bus_numbers[i**3 + j**3] += 1
bus_numbers = {k for k, v in bus_numbers.items() if v > 1}
bus_numbers = sorted(list(bus_numbers))

n = int(input())
found = -1
for num in bus_numbers:
    if num < n:
        found = num
    else:
        break

print("none" if found == -1 else found)