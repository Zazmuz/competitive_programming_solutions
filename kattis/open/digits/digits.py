while True:
    s = input()

    if s == "END":
        break
    i = 0
    while True:
        i += 1
        l = len(str(s))

        if l < 8 and int(s) == 1:
            break
        s = str(l)
    print(i)