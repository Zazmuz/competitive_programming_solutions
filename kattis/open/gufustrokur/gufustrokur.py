a = int(input())
b = int(input())
print(min(abs(a - b), abs(b + 360 - a), abs(a + 360 - b)))