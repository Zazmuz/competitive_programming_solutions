org = input()
end = input()

if len(org) > len(end):
    print("Nej")
else:
    in_org = 0
    in_end = 0
    while in_end < len(end):
        if org[in_org] == end[in_end]:
            in_org += 1
            if in_org == len(org):
                print("Ja")
                exit()
        in_end += 1
    print("Nej")