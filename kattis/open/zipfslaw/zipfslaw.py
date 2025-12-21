import re
from sys import stdin
from collections import Counter
lines = iter(stdin.read().splitlines())
while lines:
    try:
        n = int(next(lines))
    except:
        break


    to_process = ""
    a = next(lines)

    while a != "EndOfText":
        to_process += " " + a.lower()
        a = next(lines)
    b = re.split('[^a-z]', to_process)
    b = list(filter(None, b))

    bag = Counter(b)
    to_out = sorted(i for i in bag if bag[i]==n)
    if len(to_out) == 0:
        print("There is no such word.")
    else:
        print("\n".join(to_out))
    print()