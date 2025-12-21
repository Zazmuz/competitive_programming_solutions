for case in range(int(input())):
    a = input()
    b = input()
    out = ''
    for i in range(len(a)):
        out += '.'if a[i] == b[i] else '*'
    print(a)
    print(b)
    print(out)
    print()