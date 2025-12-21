p = []
for _ in range(int(input())):
    p.append(int(input()))
p.sort()
pp = [0]
for i in range(len(p)):
    pp.append(pp[-1] + p[i])

m = 999999999999999999
for i in range(len(p)):
    m = min(m, i * p[i] - pp[i] + (p[-1] * (len(p) - i - 1) - (pp[-1] - pp[i + 1])))
print(m)