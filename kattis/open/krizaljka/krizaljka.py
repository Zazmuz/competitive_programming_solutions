word1, word2 = input().split()

for c in word1:
    if c in word2:
        ind1 = word1.index(c)
        ind2 = word2.index(c)
        break

for ROW in range(len(word2)):
    if ROW == ind2:
        print(word1,end="")
    else:
        for COL in range(len(word1)):
            if COL == ind1:
                print(word2[ROW],end="")
            else:
                print(".",end="")
    print()