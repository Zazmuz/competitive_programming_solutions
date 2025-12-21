for case in range(int(input())):
    n = int(input())
    x = [int(_) for _ in input().split()]
    y = [int(_) for _ in input().split()]
    x.sort()
    y.sort(reverse=True)

    print(f"Case #{case+1}:", sum(x[i] * y[i] for i in range(n)))