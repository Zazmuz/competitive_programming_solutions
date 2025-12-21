conv = ["2",
        "22",
        "222",
        "3",
        "33",
        "333",
        "4",
        "44",
        "444",
        "5",
        "55",
        "555",
        "6",
        "66",
        "666",
        "7",
        "77",
        "777",
        "7777",
        "8",
        "88",
        "888",
        "9",
        "99",
        "999",
        "9999"]

for i in range(int(input())):
    sentence = input()
    res = ""
    last = "-"
    to_add = ""
    for char in sentence:
        index = ord(char) - ord("a")
        if 0 <= index <= 25:
            to_add += conv[index]
        elif char == " ":
            to_add += "0"

        if last[-1] == to_add[0]:
            res += " "
        last = to_add
        res += to_add
        to_add = ""
    print(f"Case #{i+1}: {res}")