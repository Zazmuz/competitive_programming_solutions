from random import choice
c,r = 1000,1000
q = 1000
case_name = "case1.txt"
types = "allBinary"


with open(case_name, "w") as f:
    f.write(f"{r} {c}\n")
    for _ in range(r):
        if types == "fullRandom":
            f.write("".join(choice("01") for _ in range(c)) + "\n")
        elif types == "allBinary":
            f.write("0"*c + "\n")
        elif types == "allDecimal":
            f.write("1"*c + "\n")
    f.write(f"{q}\n")
    for _ in range(q):
        f.write(f"{choice(range(1, r+1))} {choice(range(1, c+1))} {choice(range(1, r+1))} {choice(range(1, c+1))}\n")