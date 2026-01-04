n = int(input())

lim = n
prime = [1] * lim
prime[0] = 0
prime[1] = 0

for i in range(2, int(lim**0.5) + 1):
    if prime[i]:
        prime[i*i:lim:i] = [0] * len(prime[i*i:lim:i])
        
primm = [i for i, p in enumerate(prime) if p]

preS = [0] * (len(primm) + 1)
for i in range(len(primm)):
    preS[i+1] = preS[i] + primm[i]
        
maxx = 0
for l in range(1, len(primm) + 1):
    if preS[l] >= n:
        maxx = l
        break
else:
    maxx = len(primm)

for l in range(maxx, 0, -1):
    for i in range(len(primm) - l + 1):
        s = preS[i+l] - preS[i]
        if s >= n:
            break
        
        if prime[s]:
            print(s)
            exit()