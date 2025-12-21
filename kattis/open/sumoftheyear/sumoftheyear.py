def sumsquare(n):
    return sum(range(1, n + 1)) ** 2
def sumcube(n):
    return sum(i ** 3 for i in range(1, n + 1))
print(sum(sumsquare(k) == sumcube(k) for k in range(1, 1 + int(input()))))