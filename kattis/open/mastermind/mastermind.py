from collections import Counter
l, code, guess = input().split()
l = int(l)

non_matching_code = Counter()
non_matching_guess = Counter()
r = 0
for i in range(l):
    if code[i] != guess[i]:
        non_matching_code[code[i]] += 1
        non_matching_guess[guess[i]] += 1
    else:
        r += 1
s = 0
for k in non_matching_guess.keys():
    s += min(non_matching_guess[k], non_matching_code[k])
print(r,s)