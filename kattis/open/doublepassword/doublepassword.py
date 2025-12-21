pass1 = input()
pass2 = input()
s = 0
for ia in range(0,10):
    for ib in range(0, 10):
        for ic in range(0, 10):
            for id in range(0, 10):
                pass3 = str(ia) + str(ib) + str(ic) + str(id)
                c = 0
                for i in range(4):
                    if pass3[i] == pass1[i] or pass3[i] == pass2[i]:
                        c += 1
                if c == 4:
                    s += 1
print(s)