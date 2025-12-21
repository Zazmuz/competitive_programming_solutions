n = int(input())
seen = set()
s = 12
for _ in range(n):
    uni, name = input().split()
    if uni not in seen:
        seen.add(uni)
        print(uni, name)
        s -= 1
    if s == 0:
        break