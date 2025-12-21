d = {
    1: 1,
    2: 2
}
n = int(input())
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[n] % 1000000)