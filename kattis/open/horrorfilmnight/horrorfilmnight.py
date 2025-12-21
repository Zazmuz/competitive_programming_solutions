a = [*map(int, input().split())][1:]
b = [*map(int, input().split())][1:]

c = ["" for _ in range(1000000)]
for i in a:
    c[i] += "a"
for i in b:
    c[i] += "b"

s = 0
on = "ab"
for i in c:
    if i == "":
        continue

    if on == "ab":
        if i == "a":
            on = "a"
        elif i == "b":
            on = "b"
        s += 1
    elif on == "a":
        if i == "b":
            on = "b"
            s += 1
        if i == "ab":
            on = "ab"
            s += 1
    elif on == "b":
        if i == "a":
            on = "a"
            s += 1
        if i == "ab":
            on = "ab"
            s += 1

print(s)