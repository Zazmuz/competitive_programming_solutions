n, m = map(int, input().split())
ladder = [list(range(n)) for _ in range(m)]
for i in range(m):
    a = int(input())
    b = a + 1
    ladder[i][a-1], ladder[i][b-1] = ladder[i][b-1], ladder[i][a-1]
for i in range(n):
    k = i
    for j in range(m-1, -1, -1):
        k = ladder[j][k]
    print(k+1)