N = 100
from random import randint
F = randint(1, N)
T = randint(1, 10**11)
print(N, F, T)
print(*[randint(1, 10**6) for _ in range(N)])