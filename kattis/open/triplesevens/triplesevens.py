input()
print('777' if all(any([int(x) == 7 for x in input().split()]) for _ in range(3)) else '0')