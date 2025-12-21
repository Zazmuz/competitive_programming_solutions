n = int(input())
last = input()
s = 0
for i in range(n-1):
    new = input()
    if last == new:
        s += 1
    last = new
print(s)