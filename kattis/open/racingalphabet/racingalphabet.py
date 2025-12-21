alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
from math import pi
d = 60 * pi / 28
for _ in range(int(input())):
    word = input()
    t = 0
    i = alp.index(word[0])
    for c in word:
        j = alp.index(c)
        t += (min((i - j) % 28, (j - i) % 28)) * d / 15
        i = j
        t += 1
    print(t)