r,g,b,k = map(int,input().split())
o = g + b
if o > 0:
    print(r + k)
else:
    print(max(r, r - 2 + k))