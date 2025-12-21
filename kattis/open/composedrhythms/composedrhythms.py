a = int(input())
out = []
if a % 2 == 1:
    out.append('3')
    a -= 3

for i in range(a // 2):
    out.append('2')

print(len(out))
print(' '.join(out))