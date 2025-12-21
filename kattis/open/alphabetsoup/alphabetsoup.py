ALP = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
alp = set(list(input()))
print("Alphabet Soup!" if ALP == alp else "".join(sorted(list(ALP - alp))))