from sys import stdin

data = stdin.read().splitlines()
itter = iter(data)
words = set()
while True:
    try:
        line = next(itter)

        for add in line.split():
            words.add(add)
    except StopIteration:
        break
words_list = list(words)
compound_words = set()
for i in range(len(words)):
    for j in range(len(words)):
        if i != j:
            compound = words_list[i] + words_list[j]

            compound_words.add(compound)

for compound_word in sorted(compound_words):
    print(compound_word)