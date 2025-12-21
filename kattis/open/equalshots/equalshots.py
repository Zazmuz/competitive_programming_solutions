a, b = map(int, input().split())
ass = 0
bss = 0
for i in range(a):
    c, d = map(int, input().split())
    ass += c * d

for i in range(b):
    c, d = map(int, input().split())
    bss += c * d

if ass == bss:
    print("same")
else:
    print("different")