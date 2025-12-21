r,g,b,k=map(int,input().split())
print(r+k if g+b else max(r,r-2+k))