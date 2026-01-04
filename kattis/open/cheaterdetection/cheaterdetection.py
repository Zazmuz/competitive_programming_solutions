for _ in range(int(input())):
    s = int(input().replace(".", ""))%3==2

    if s:
        print("IMPOSSIBLE")
    else:
        print("VALID")