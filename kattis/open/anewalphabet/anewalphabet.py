a = """a @
b 8
c (
d |)
e 3
f #
g 6
h [-]
i |
j _|
k |<
l 1
m []\/[]
n []\[]
o 0
p |D
q (,)
r |Z
s $
t ']['
u |_|
v \/
w \/\/
x }{
y `/
z 2"""
b = {}
for i in a.split('\n'):
    froms, to = i.split()
    b[froms] = to
c = input()
for i in c:
    if i.lower() in b:
        print(b[i.lower()], end='')
    else:
        print(i, end='')