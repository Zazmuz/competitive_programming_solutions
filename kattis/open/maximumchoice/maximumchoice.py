import math
a,b = map(int,input().split())
print(int(1 + (math.log(a,b + 1))//1))