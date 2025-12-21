n = int(input())
s = input()

i, aa, hh = 0, 0, 0

while i < len(s) and aa < n and hh < n:
    a, h, played = 0, 0, 0

    for _ in range(5):
        if i >= len(s):
            break

        current = s[i]
        i += 1
        played += 1

        if current == 'A':
            a += 1
        else:
            h += 1

        remaining = 5 - played

        if a > h + remaining:
            aa += 1
            break

        if h > a + remaining:
            hh += 1
            break
    else:

        if a > h:
            aa += 1
        else:
            hh += 1

print("Hannes" if aa >= n else "Arnar")