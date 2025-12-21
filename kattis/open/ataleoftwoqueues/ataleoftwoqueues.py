input()
a = sum(int(i) for i in input().split())
b = sum(int(i) for i in input().split())

if a < b:
    print("left")
elif a > b:
    print("right")
else:
    print("either")