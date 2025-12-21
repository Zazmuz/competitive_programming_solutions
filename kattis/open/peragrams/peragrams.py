from collections import Counter
ms = Counter(list(input()))
a=[0,0]
for k in ms.keys():
    a[ms[k]%2] += 1
print(max(0, a[1]-1))