n = int(input())
a = [[" " for _ in range(3 + 2*n)] for _ in range(3 + 2*n)]

m = len(a) // 2
a[m][len(a)-1] = "x"
x, y = m, len(a)-1
x -= 1
y -= 1
while 0 < x < len(a)-1 and 0 < y < len(a)-1:
    a[x][y] = "\\"
    a[x][y] = "\\"
    x -= 1
    y -= 1

a[m][0] = "x"
x, y = m, 0
x += 1
y += 1
while 0 < x < len(a)-1 and 0 < y < len(a)-1:
    a[x][y] = "\\"
    x += 1
    y += 1

a[0][m] = "x"
x, y = 0, m
x += 1
y -= 1
while 0 < x < len(a)-1 and 0 < y < len(a)-1:
    a[x][y] = "/"
    x += 1
    y -= 1

a[len(a)-1][m] = "x"

x, y = len(a)-1, m
x -= 1
y += 1
while 0 < x < len(a)-1 and 0 < y < len(a)-1:
    a[x][y] = "/"
    x -= 1
    y += 1
for row in a:
    print("".join(row).rstrip())