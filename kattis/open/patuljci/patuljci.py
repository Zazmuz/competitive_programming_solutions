from itertools import combinations

dwarfs = [int(input()) for _ in range(9)]
total = sum(dwarfs) - 100
for imp1, imp2 in combinations(dwarfs, 2):
    if imp1 + imp2 == total:
        dwarfs.remove(imp1)
        dwarfs.remove(imp2)
        break
print(*dwarfs, sep="\n")