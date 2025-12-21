c = 1
while True:
    n = int(input())
    if n == 0:
        break
    names_start = []
    names_end = []
    for i in range(n):
        name = input()
        if i % 2 == 0:
            names_start.append(name)
        else:
            names_end.append(name)
    new_names = []
    new_names.extend(names_start)
    names_end = names_end[::-1]
    new_names.extend(names_end)
    print(f"SET {c}")
    print(*new_names, sep="\n")
    c += 1