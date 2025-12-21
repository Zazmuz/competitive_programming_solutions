
n = int(input())
grid = []
r=[]#[0 for i in range(n)]
c=[0 for j in range(n)]
for line in range(n):
    i = input()
    count = 0
    for char in range(n):
        if i[char] == '1':
            count += 1
            c[char] += 1

    r.append(count)
rr = sum(r)
cr = sum(c)
guess = set()
for row in r:
    if (rr-row)+(n-row) <= n:
        guess.add('-')
        break
for col in c:
    if (cr-col)+(n-col) <= n:
        guess.add('|')

if len(guess) == 2:
    print('+')
else:
    print(*guess)