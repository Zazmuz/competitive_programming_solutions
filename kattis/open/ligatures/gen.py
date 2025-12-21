N = 1_000_000
Q = 100_000
k = 1
alphabet = "abcdefghijklmnopqrstuvwxyz"
from random import choice
with open("samp.txt", "w") as f:
    f.write(f"{N} {Q} {k}\n")
    f.write("".join([f"{choice(alphabet)}" for _ in range(N)]))
    f.write("\n")
    for _ in range(Q):
        for _ in range(k*2):
            f.write(f"{choice(alphabet)}")
        f.write("\n")