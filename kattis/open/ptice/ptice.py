input()
ans = input()
a = 'ABC' * 100
b = 'BABC' * 100
g = 'CCAABB' * 100

sa = 0
sb = 0
sg = 0

i = 0
while i < len(ans):
    if ans[i] == a[i]:
        sa += 1
    if ans[i] == b[i]:
        sb += 1
    if ans[i] == g[i]:
        sg += 1
    i += 1

print(max(sa, sb, sg))
if sa == max(sa, sb, sg):
    print('Adrian')
if sb == max(sa, sb, sg):
    print('Bruno')
if sg == max(sa, sb, sg):
    print('Goran')