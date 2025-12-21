from math import comb
def catlan_number(n):
    return comb(2*n, n) // (n+1)
for i in range(int(input())):
    print(catlan_number(int(input())))