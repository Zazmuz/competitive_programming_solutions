wind = int(input())
for i in range(int(input())):
    x, y = input().split()
    y = int(y)
    if wind <= y:
        print(x, "opin")
    else:
        print(x, "lokud")