import random
n = int(input())
while True:
    a = random.randint(-900, 900)
    b = n - a
    if a != 0 and b != 0 and -990 < b < 990:
        break
print(a, b)