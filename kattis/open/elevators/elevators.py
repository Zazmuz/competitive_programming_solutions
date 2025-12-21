d = {
    'residential': {},
    'commercial': {},
    'industrial': {}
}
for p in d.keys():
    d[p][1] = 0
for p in range(2,6):
    d['residential'][p] = 1
for p in range(6,11):
    d['residential'][p] = 2
for p in range(11,16):
    d['residential'][p] = 3
for p in range(16,21):
    d['residential'][p] = 4

for p in range(2,8):
    d['commercial'][p] = 1
for p in range(8,15):
    d['commercial'][p] = 2
for p in range(15,21):
    d['commercial'][p] = 3

for p in range(2,5):
    d['industrial'][p] = 1
for p in range(5,9):
    d['industrial'][p] = 2
for p in range(9,13):
    d['industrial'][p] = 3
for p in range(13,17):
    d['industrial'][p] = 4
for p in range(17,21):
    d['industrial'][p] = 5

a, b = input().split()
b = int(b)
print(d[a][b])