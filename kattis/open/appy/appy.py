kids = []
for _ in range(int(input())):
    amnt, *apps = input().split()
    kids.append(apps)

used = set()
for kid in kids:
    for app in kid:
        if app not in used:
            print(app, end=" ")
            used.add(app)
            break