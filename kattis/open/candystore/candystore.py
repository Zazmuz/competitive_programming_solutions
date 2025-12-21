names, initials = [int(x) for x in input().split()]
initials_lookup = {}
for i in range(names):
    a, b = input().split()
    names_tog = a + " " + b
    inits = a[0]+b[0]
    if inits in initials_lookup:
        initials_lookup[inits].append(names_tog)
    else:
        initials_lookup[inits] = [names_tog]
for i in range(initials):
    init = input()
    name_list = initials_lookup.get(init, [])
    if len(name_list) == 0:
        print("nobody")
    elif len(name_list) == 1:
        print(name_list[0])
    else:
        print("ambiguous")