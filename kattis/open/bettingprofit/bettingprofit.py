for bet in range(int(input())):
    m, o, f = input().split()
    m, o = int(m), int(o)

    if f == "+":
        print(m / 100 * o)
    else:
        print(m / o * 100)