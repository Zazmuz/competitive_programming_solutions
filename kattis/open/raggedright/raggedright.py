import sys
t=[len(x)for x in sys.stdin]
print(sum((max(t)-x)**2for x in t[:-1]))