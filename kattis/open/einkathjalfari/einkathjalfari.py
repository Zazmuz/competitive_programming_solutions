from bisect import bisect_left, bisect_right, insort
import io, os
input_fast = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = lambda: input_fast().decode()

b = []

q = int(input())
out = []
for _ in range(q):
    line = input().split()
    c = line[0]
    
    if c == 'A':
        t = int(line[1])

        l = bisect_left(b, t)
        if l == len(b) or b[l] != t:
            insort(b, t)
    
    elif c == 'D':
        t = int(line[1])

        l = bisect_left(b, t)
        if l < len(b) and b[l] == t:
            b.pop(l)
    
    elif c == 'F':
        t1 = int(line[1])
        t2 = int(line[2])

        l = bisect_left(b, t1)
        r = bisect_right(b, t2)
        bc = r - l
        free = (t2 - t1 + 1) - bc
        out.append(str(free))
print('\n'.join(out))