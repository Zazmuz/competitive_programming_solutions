t=0
l={i:0 for i in range(13)}
for i in range(1,7):
    for j in range(1,7):
        t += 1
        l[i+j] += 1
input()
print(sum([l[i] / t for i in [int(i) for i in input().split()]]))
