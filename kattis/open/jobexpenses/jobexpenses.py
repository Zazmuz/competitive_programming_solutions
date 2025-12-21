input()
print(sum([abs(int(i)) if int(i) < 0 else 0 for i in input().split()]))