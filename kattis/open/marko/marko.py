w = [input() for _ in range(int(input()))]
allowed = [int(x) for x in list(input())]
needed = {}
s = 2
i = 3
j = 0
alp = "abcdefghijklmnopqrtuvwxy"
while j < len(alp):
    needed[alp[j]] = s
    i -= 1
    if i == 0:
        s += 1
        i = 3
    j += 1
needed['s'] = 7
needed['z'] = 9

s = 0
for word in w:
    for c_i in range(len(word)):
        if needed[word[c_i]] != allowed[c_i]:
            break
    else:
        s += 1
print(s)