input()
a = sum(int(i) for i in input().split())
b = sum(int(i) for i in input().split())

if a < b:
    print("Button 2")
elif a > b:
    print("Button 1")
else:
    print("Oh no")