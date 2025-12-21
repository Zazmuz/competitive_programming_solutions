ct = list(input())
sw = list(input())

for i in range(len(ct)):
    s = ord(sw[i]) - ord('A')
    c = ord(ct[i]) - ord('A')
    d = c - s
    d %= 26
    d = chr(d + ord('A'))
    sw.append(d)
    print(d, end='')