TAD = [0,0,1]

row = list(input())

for CHR in reversed(row):
    if CHR == "1":
        TAD[0] += TAD[1]
    elif CHR == "0":
        TAD[1] += TAD[2]
    elif CHR == "?":
        TAD[0] *= 2
        TAD[0] += TAD[1]
        TAD[1] *= 2
        TAD[1] += TAD[2]
        TAD[2] *= 2

print(TAD[0])