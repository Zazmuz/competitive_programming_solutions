s = 0
for i in range(int(input())):
    num = input()
    if "+39" in num and len(num.split("+39")[1]) in {9,10}:
        s += 1
print(s)