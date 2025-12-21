n = input()
m = len(input())

n = n.zfill(m)

n = n[:-m+1] + '.' + n[-m+1:].rstrip('0')

if n[-1] == '.':
    n = n[:-1]
elif n[0] == '.':
    n = '0' + n

print(n)