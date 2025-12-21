s = 0
for i in range(int(input())):
    a, b = input().split()
    if b == "nej":
        s = max(s, int(a))
print(s)