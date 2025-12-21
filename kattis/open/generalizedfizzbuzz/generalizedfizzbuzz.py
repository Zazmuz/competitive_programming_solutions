fizz = 0
buzz = 0
fizzbuzz = 0

n, a, b = map(int, input().split())
for i in range(1, n+1):
    if i % a == 0 and i % b == 0:
        fizzbuzz += 1
    elif i % a == 0:
        fizz += 1
    elif i % b == 0:
        buzz += 1

print(fizz, buzz, fizzbuzz)