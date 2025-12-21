k, s = map(int, input().split())
key = input()
cipher = input()

a = [''] * s

for i, c in enumerate(key):
    a[s - k + i] = ord(c) - ord('a')

for i in range(s - 1, k - 1, -1):
    a[i - k] = (ord(cipher[i]) - ord('a') - a[i]) % 26

for c in a:
    print(chr(c + ord('a')), end='')