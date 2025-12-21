from sys import stdin
lines = stdin.read().splitlines()
for line in lines:
    line = [int(_) for _ in line.split()]
    n = line[0]
    line = {abs(line[i+1] - line[i+2]) for i in range(n-1)}
    alls = {i for i in range(1,n)}
    print("Jolly" if len(alls - line) == 0 else "Not jolly")