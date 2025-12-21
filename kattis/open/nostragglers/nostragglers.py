s = 0
for i in range(int(input())):
    _, a, b = input().split()
    b = int(b)

    s+=b if a == 'IN' else -b

print("NO STRAGGLERS" if s == 0 else s)