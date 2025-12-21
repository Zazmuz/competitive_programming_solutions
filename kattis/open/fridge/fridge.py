cnt = [0]*10
for c in input():
    cnt[ord(c) - 48] += 1

for i in range(1, 1001):
    if i > 1:
        if cnt[0] < i-1:
            print('1'+'0'*(i-1))
            exit(0)

    for j in range(1, 10):
        if cnt[j] < i:
            print(i*str(j))
            exit(0)