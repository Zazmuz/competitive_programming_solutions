from collections import defaultdict
cnt = defaultdict(int)
for _ in range(int(input())):
    courses = tuple(sorted([int(x) for x in input().split()]))
    cnt[courses] += 1

cnts = cnt.values()
maxx = max(cnts)
tot = sum(c for c in cnts if c == maxx)
print(tot)