def conv(product):
    fat, protein, sugar, starch, alcohol = product.split()

    if "g" in fat:
        fat = int(fat[:-1]) * 9
    elif "C" in fat:
        fat = int(fat[:-1])

    if "g" in protein:
        protein = int(protein[:-1]) * 4
    elif "C" in protein:
        protein = int(protein[:-1])

    if "g" in sugar:
        sugar = int(sugar[:-1]) * 4
    elif "C" in sugar:
        sugar = int(sugar[:-1])

    if "g" in starch:
        starch = int(starch[:-1]) * 4
    elif "C" in starch:
        starch = int(starch[:-1])

    if "g" in alcohol:
        alcohol = int(alcohol[:-1]) * 7
    elif "C" in alcohol:
        alcohol = int(alcohol[:-1])

    calories = sum(i for i in [fat, protein, sugar, starch, alcohol] if type(i) is int)
    percent = sum(int(i[:-1]) for i in [fat, protein, sugar, starch, alcohol] if type(i) is str)

    other_percent_worth = 100-percent
    total_calories = calories / (other_percent_worth / 100)
    percent_worth = total_calories / 100
    if type(fat) is str:
        fat = percent_worth*int(fat[:-1])
    return total_calories, fat

while True:
    food = input()
    if food == "-":
        break
    cals, fats = 0, 0
    while food != "-":
        food_cal, food_fat = conv(food)
        cals += food_cal
        fats += food_fat
        food = input()
    print(str(round(fats / cals * 100))+"%")