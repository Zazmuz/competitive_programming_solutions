banned = set(list(input()))
sentence = input().split()
out = ""
for word in sentence:
    any_bad = False
    for letter in word:
        if letter in banned:
            any_bad = True
            break
    if not any_bad:
        out += word + " "
    else:
        out += "*"*len(word) + " "
print(out)