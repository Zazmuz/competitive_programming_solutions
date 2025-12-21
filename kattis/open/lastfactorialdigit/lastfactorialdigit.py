from math import factorial
for case in range(int(input())):
    a = int(input())
    b = str(factorial(a))
    print(b[-1])