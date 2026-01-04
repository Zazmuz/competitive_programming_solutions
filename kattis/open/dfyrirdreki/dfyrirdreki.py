a = int(input())
b = int(input())
c = int(input())
delta = b * b - 4 * a * c
if delta < 0:
    print(0)
elif delta == 0:
    print(1)
else:
    print(2)