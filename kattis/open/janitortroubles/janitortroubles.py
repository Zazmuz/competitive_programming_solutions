from math import sqrt
a = [int(_) for _ in input().split()]
s = sum(a)/2
print(sqrt((s-a[0])*(s-a[1])*(s-a[2])*(s-a[3]))) # Brahmagupta's formula (blä)
