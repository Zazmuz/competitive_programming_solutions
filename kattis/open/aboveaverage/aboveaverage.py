i=input
for case in range(int(i())):
  p,*g=[int(_) for _ in i().split()]
  print(f"{len([_ for _ in g if _>sum(g)/p])/p*100:.3f}%")