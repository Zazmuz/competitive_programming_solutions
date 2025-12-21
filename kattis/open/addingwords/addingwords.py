import sys
dictionary = {}
for line in sys.stdin.readlines():
    inp = line.split()
    if inp[0] == 'def':
        dictionary[inp[1]] = int(inp[2])

    elif inp[0] == 'calc':
        try:
            result = dictionary[inp[1]]
            for i in range(2, len(inp) - 1, 2):
                if inp[i] == '+':
                    result += dictionary[inp[i + 1]]
                else:
                    result -= dictionary[inp[i + 1]]
            reversed_dictionary = {v: k for k, v in dictionary.items()}
            print(f"{line[5:-1]} {reversed_dictionary[result]}")
        except:
            print(line[5:-1] + ' unknown')
    else:
        dictionary = {}