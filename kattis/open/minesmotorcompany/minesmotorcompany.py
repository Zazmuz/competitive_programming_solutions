conv = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
s = 0
x, y = -1, -1
for _ in range(int(input())):
    if x == -1:
        x, y = input()
        x, y = conv[x], conv[y]
        continue
    a, b = input()
    a, b = conv[a], conv[b]
    xd = abs(x - a)
    yd = abs(y - b)
    x, y = a, b

    s += xd + yd
print(s)