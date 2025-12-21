def count_inversions(l, n):
    return sum(l[i] > l[j] for i in range(n) for j in range(i + 1, n))

for _ in range(int(input())):
    c, *ll = map(int, input().split())
    print(c, count_inversions(ll, len(ll)))