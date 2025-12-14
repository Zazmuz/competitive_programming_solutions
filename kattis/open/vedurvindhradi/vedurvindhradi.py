def check(speed):
    if 0 <= speed <= 0.2:
        return "Logn"
    elif 0.3 <= speed <= 1.5:
        return "Andvari"
    elif 1.6 <= speed <= 3.3:
        return "Kul"
    elif 3.4 <= speed <= 5.4:
        return "Gola"
    elif 5.5 <= speed <= 7.9:
        return "Stinningsgola"
    elif 8.0 <= speed <= 10.7:
        return "Kaldi"
    elif 10.8 <= speed <= 13.8:
        return "Stinningskaldi"
    elif 13.9 <= speed <= 17.1:
        return "Allhvass vindur"
    elif 17.2 <= speed <= 20.7:
        return "Hvassvidri"
    elif 20.8 <= speed <= 24.4:
        return "Stormur"
    elif 24.5 <= speed <= 28.4:
        return "Rok"
    elif 28.5 <= speed <= 32.6:
        return "Ofsavedur"
    elif speed >= 32.7:
        return "Farvidri"
    else:
        raise ValueError("Invalid input")

s = float(input())
print(check(s))