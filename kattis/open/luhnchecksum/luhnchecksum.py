for _ in range(int(input())):
    num = input()[::-1]
    s = 0
    for i, d in enumerate(num):
        if i%2 == 1:
            d = int(d) * 2
            s += sum(int(x) for x in str(d))
        else:
            s += int(d)
    if s % 10 == 0:
        print("PASS")
    else:
        print("FAIL")