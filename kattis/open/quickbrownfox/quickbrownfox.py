needed = set(list("abcdefghijklmnopqrstuvwxyz"))
for i in range(int(input())):
    occ = set(list(input().lower()))
    left = needed-occ
    if len(left) == 0:
        print("pangram")
    else:
        print("missing", "".join(sorted(left)))