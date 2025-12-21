input()
words = input()[::-1].split()
words.sort(reverse=True)
for word in words:
    print(word, end=' ')