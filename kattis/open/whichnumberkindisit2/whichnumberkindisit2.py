from math import sqrt

def is_odd(n):
    return n % 2 == 1

def is_square(n):
    return n == int(sqrt(n)) ** 2

for i in range(int(input())):
    n = int(input())
    p=False
    if is_odd(n):
        print("O", end="")
        p=True
    if is_square(n):
        print("S", end="")
        p=True

    if not p:
        print("EMPTY", end="")
    print()