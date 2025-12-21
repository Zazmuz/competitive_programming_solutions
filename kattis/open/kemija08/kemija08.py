vowels = {'a', 'e', 'i', 'o', 'u'}
d = ''
w = input()
i = 0
while i < len(w):
    d += w[i]
    if w[i] in vowels:
        i += 2
    i += 1
print(d)