bag = []
try:
    for e in input():
        match e:
            case 'p':
                bag.append('m')
            case 'P':
                while not bag.pop() == 'm':
                    pass
            case 'g':
                bag.append('g')
            case 'G':
                while not bag.pop() == 'g':
                    pass
            case 'o':
                bag.append('j')
            case 'O':
                while not bag.pop() == 'j':
                    pass
    print(bag.count('m'))
    print(bag.count('g'))
    print(bag.count('j'))
except IndexError:
    print("Neibb")