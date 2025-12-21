while True:
    a, b = map(int, input().split())
    if a == b:
        break
    if a > b:
        print("More")
    else:
        print("Less")