s = input()
a = 0
b = 0
for i in range(len(s)):
    if s[i] == 'A':
        a += int(s[i+1])
    if s[i] == 'B':
        b += int(s[i+1])
print('A' if a > b else 'B')