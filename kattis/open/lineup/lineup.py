n = []
for _ in range(int(input())):
    n.append(input())

if n == sorted(n):
    print("INCREASING")
elif n == sorted(n, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")