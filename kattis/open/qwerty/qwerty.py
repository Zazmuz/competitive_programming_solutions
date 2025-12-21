a = "qwertyuiopasdfghjklzxcvbnm"
b = "abcdefghijklmnopqrstuvwxyz"
conv = {
    b[i]: a[i] for i in range(len(a))
}
input()
word = list(input())
for i in range(len(word)):
    if word[i] in conv:
        word[i] = conv[word[i]]
print("".join(word))