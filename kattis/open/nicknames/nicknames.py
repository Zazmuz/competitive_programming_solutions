import collections
p,t,r=input,int,range
m=collections.defaultdict(t)
for _ in r(t(p())):
  n=p()
  for i in r(len(n)):m[n[:i+1]]+=1
for _ in r(t(p())):
  print(m[p()])