for _ in range(int(input())):
    g = [int(x) for x in input().split()][1:]
    for k in range(len(g)):
        if g[k+1] != g[k]+1:
            print(k+2)
            break