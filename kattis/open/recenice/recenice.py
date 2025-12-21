def number_to_words(num):
    if num < 20:
        return ones[num]
    elif num < 100:
        t = num // 10
        r = num % 10
        return tens[t] + (ones[r] if r else "")
    else:
        h = num // 100
        r = num % 100
        part = ones[h] + "hundred"
        if r == 0:
            return part
        elif r < 20:
            return part + ones[r]
        else:
            t = r // 10
            s = r % 10
            return part + tens[t] + (ones[s] if s else "")


N = int(input())
words = [input() for _ in range(N)]

ones = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]
tens = [
    "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
]

placeholder_index = None
for i, w in enumerate(words):
    if w == '$':
        placeholder_index = i
        break

for candidate in range(1, 1000):
    spelled = number_to_words(candidate)

    words[placeholder_index] = spelled

    total_letters = sum(len(w) for w in words)

    if total_letters == candidate:
        print(" ".join(words))
        break