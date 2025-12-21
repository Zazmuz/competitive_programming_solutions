input()
print("yes" if sum([int(i) for i in input().split()]) % 3 == 0 else "no")