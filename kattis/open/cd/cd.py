while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    mix = 0
    s = 0
    jill = []
    for i in range(n):
        asd = int(input())
        mix = max(asd, mix)
        jill.append(asd)

    index = 0
    for i in range(m):

        dsa = int(input())
        if dsa > mix:
            for sad in range(m-i-1):
                input()
            break
        while dsa > jill[index]:
            index += 1
        if jill[index] == dsa:
            s += 1

    print(s)
    #[jill.add(int(input())) for i in range(n)]
    #[jill.add(int(input())) for j in range(n)]
    #print(n+m - len(jill))