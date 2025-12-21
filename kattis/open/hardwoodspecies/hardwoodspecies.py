from sys import stdin
from collections import Counter
lines = stdin.read().splitlines()
bag = Counter(lines)
import sys
print(sys.executable)
trees = len(lines)
for tree in sorted(bag):
    print(tree, bag[tree] / trees * 100)