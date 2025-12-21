mode, word = input().split()
if mode == 'E':
    o = ''
    s = 0
    l = word[0]
    for c in word:
        if c == l:
            s += 1
        else:
            o += l + str(s)
            l = c
            s = 1
    o += l + str(s)
    print(o)
else:
    o = ''
    for c, t in zip(word[::2], word[1::2]):
        o += c * int(t)
    print(o)