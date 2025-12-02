f, s = map(int, input().split())
one = [int(x) for x in input().split()]
two = [int(x) for x in input().split()]

polynomial_product = [0] * (f + s - 1)
for i in range(f):
    for j in range(s):
        polynomial_product[i + j] += one[i] * two[j]

print(polynomial_product[0], end=' ')
for a in polynomial_product[1:]:
    if a != 0:
        print(a, end=' ')