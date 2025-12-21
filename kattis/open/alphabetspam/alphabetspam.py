word = input()
lenword = len(word)
print(word.count("_") / lenword)

lower = 0
for i in "abcdefghijklmnopqrstuvwxyz":
    lower += word.count(i)

print(lower / lenword)

higher = 0

for i in "abcdefghijklmnopqrstuvwxyz".upper():
    higher += word.count(i)

print(higher / lenword)

print((lenword - word.count("_") - lower - higher) / lenword)