from math import ceil
while True:
    city_amn, box_amn = [int(i) for i in input().split()]
    if city_amn == -1 and box_amn == -1:
        exit()
    cities_pop = [int(input()) for i in range(city_amn)]
    input()
    lower = 1
    upper = max(cities_pop)

    while lower < upper:
        guess = (lower+upper)//2
        check = box_amn
        for i in cities_pop:
            check -= ceil(i/guess)

        if check < 0:
            lower = guess+1
        else:
            upper = guess
    print(lower)