input()
c,e,s=input(),0,0
for l in c:
    if l=="1"or e>0:e,s=2if l=="1"else e-1,s+1
print(s)