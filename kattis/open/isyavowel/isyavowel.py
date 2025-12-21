vowels = {"a", "e", "i", "o", "u"}

line = input()
c = 0
for letter in line:
    if letter in vowels:
        c += 1

print(c, c+line.count("y"))