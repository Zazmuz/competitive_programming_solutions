n=int(input()) //5
u= n//3
u2 = u*u

if n%3==0:
    o = 3*u
elif n%3==1:
    o = 7*u + 2
else:
    o = 11*u + 5

print(1 + 24*u2+ 4*o)