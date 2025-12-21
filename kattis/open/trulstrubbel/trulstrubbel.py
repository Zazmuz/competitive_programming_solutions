games = input()
t = 0
h = 0
for game in games:
    if game == 'T':
        t += 1
        if t >= 11 and t - h >= 2:
            t = 0
            h = 0
    elif game == 'H':
        h += 1
        if h >= 11 and h - t >= 2:
            t = 0
            h = 0

print(f"{t}-{h}")