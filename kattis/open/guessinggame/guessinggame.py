import sys
low_guess, high_guess = 1, 10
lines = sys.stdin.readlines()
for two_lines in zip(lines[::2], lines[1::2]):
    guess, response = two_lines
    guess = int(guess)
    if response == "too high\n":
        high_guess = min(high_guess, guess-1)
    elif response == "too low\n":
        low_guess = max(low_guess, guess+1)
    else:
        if low_guess <= guess <= high_guess:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        low_guess, high_guess = 1, 10
#for line in sys.stdin.readlines():
