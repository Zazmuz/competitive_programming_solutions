import sys

lines = sys.stdin.read().split()
for line in lines:
    n = int(line)
    if n == 0:
        break
    
    res = n
    p = 2
    nt = n
    
    while p *p <= nt:
        if nt % p == 0:
            while nt % p == 0:
                nt //= p
            res-= res // p
        p += 1
        
    if nt > 1:
        res -= res // nt
        
    print(res)