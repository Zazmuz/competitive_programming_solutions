n = int(input())
l = [int(x) for x in input().split()]
l.sort()
nl = []
nl.extend(l[n//3:(n//3)*2])
nl.extend(l[0:n//3])
nl.extend(l[(n//3)*2:n])
print(*nl)