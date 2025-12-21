n, k = map(int, input().split())
word = input()
i = 0
for _ in range(n):
    print(word[i], end='')
    i += pow(2, k, n)
    i %= n