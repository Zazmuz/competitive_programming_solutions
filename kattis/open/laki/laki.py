periodic_table = {
        "H": 1,
        "He": 2,
        "Li": 3,
        "Be": 4,
        "B": 5,
        "C": 6,
        "N": 7,
        "O": 8,
        "F": 9,
        "Ne": 10,
        "Na": 11,
        "Mg": 12,
        "Al": 13,
        "Si": 14,
        "P": 15,
        "S": 16,
        "Cl": 17,
        "Ar": 18,
        "K": 19,
        "Ca": 20,
        "Sc": 21,
        "Ti": 22,
        "V": 23,
        "Cr": 24,
        "Mn": 25,
        "Fe": 26,
        "Co": 27,
        "Ni": 28,
        "Cu": 29,
        "Zn": 30,
        "Ga": 31,
        "Ge": 32,
        "As": 33,
        "Se": 34,
        "Br": 35,
        "Kr": 36,
        "Rb": 37,
        "Sr": 38,
        "Y": 39,
        "Zr": 40,
        "Nb": 41,
        "Mo": 42,
        "Tc": 43,
        "Ru": 44,
        "Rh": 45,
        "Pd": 46,
        "Ag": 47,
        "Cd": 48,
        "In": 49,
        "Sn": 50,
        "Sb": 51,
        "Te": 52,
        "I": 53,
        "Xe": 54,
        "Cs": 55,
        "Ba": 56,
        "La": 57,
        "Ce": 58,
        "Pr": 59,
        "Nd": 60,
        "Pm": 61,
        "Sm": 62,
        "Eu": 63,
        "Gd": 64,
        "Tb": 65,
        "Dy": 66,
        "Ho": 67,
        "Er": 68,
        "Tm": 69,
        "Yb": 70,
        "Lu": 71,
        "Hf": 72,
        "Ta": 73,
        "W": 74,
        "Re": 75,
        "Os": 76,
        "Ir": 77,
        "Pt": 78,
        "Au": 79,
        "Hg": 80,
        "Tl": 81,
        "Pb": 82,
        "Bi": 83,
        "Po": 84,
        "At": 85,
        "Rn": 86,
        "Fr": 87,
        "Ra": 88,
        "Ac": 89,
        "Th": 90,
        "Pa": 91,
        "U": 92,
        "Np": 93,
        "Pu": 94,
        "Am": 95,
        "Cm": 96,
        "Bk": 97,
        "Cf": 98,
        "Es": 99,
        "Fm": 100,
        "Md": 101,
        "No": 102,
        "Lr": 103,
        "Rf": 104,
        "Db": 105,
        "Sg": 106,
        "Bh": 107,
        "Hs": 108,
        "Mt": 109,
        "Ds": 110,
        "Rg": 111,
        "Cn": 112,
        "Nh": 113,
        "Fl": 114,
        "Mc": 115,
        "Lv": 116,
        "Ts": 117,
        "Og": 118
    }
reverse_periodic_table = {v: k for k, v in periodic_table.items()}
def one(a, b):
    print(int(a) + int(b))

def two(a, b):
    print(eval(a) + eval(b))

def three(a, b):
    print(hex(int(a, 16) + int(b, 16)))

def four(a, b):
    print(f"{int(a[0]) + int(b[0])} + {int(a[1][:-1]) + int(b[1][:-1])}i")

def five(a, b):
    print(f"log({int(a)*int(b)})")

def six(a, b):
    a = [int(x) for x in a if x]
    b = [int(x) for x in b if x]
    l = list(set(a + b))
    l.sort()
    l = [str(x) for x in l]
    print(f"{{{', '.join(l)}}}")

def seven(a, b):
    a = periodic_table.get(a, 0)
    b = periodic_table.get(b, 0)
    print(f"{reverse_periodic_table[a+b]}")

def eight(a, b):
    mayan_to_arabic = {
        "𝋠": "0",
        "𝋡": "1",
        "𝋢": "2",
        "𝋣": "3",
        "𝋤": "4",
        "𝋥": "5",
        "𝋦": "6",
        "𝋧": "7",
        "𝋨": "8",
        "𝋩": "9",
        "𝋪": "A",
        "𝋫": "B",
        "𝋬": "C",
        "𝋭": "D",
        "𝋮": "E",
        "𝋯": "F",
        "𝋰": "G",
        "𝋱": "H",
        "𝋲": "I",
        "𝋳": "J",
    }
    arabic_to_mayan = {'0': '𝋠', '1': '𝋡', '2': '𝋢', '3': '𝋣', '4': '𝋤', '5': '𝋥', '6': '𝋦', '7': '𝋧', '8': '𝋨', '9': '𝋩', '10': '𝋪', '11': '𝋫', '12': '𝋬', '13': '𝋭', '14': '𝋮', '15': '𝋯', '16': '𝋰', '17': '𝋱', '18': '𝋲', '19': '𝋳'}


    a = [mayan_to_arabic[x] for x in a]
    b = [mayan_to_arabic[x] for x in b]
    a = int("".join(a), 20)
    b = int("".join(b), 20)
    c = a + b
    if c == 0:
        print("𝋠")
        return
    result = []
    while c > 0:
        result.append(arabic_to_mayan[str(c % 20) ])
        c //= 20
    result.reverse()
    result = "".join(result)
    print(result)

def nine(a, b):
    a = a.split(" mod ")
    b = b.split(" mod ")
    a1 = int(a[0])
    a2 = int(a[1])
    b1 = int(b[0])
    b2 = int(b[1])
    m = a2 * b2
    m1 = m // a2
    m2 = m // b2
    m1_inv = pow(m1, -1, a2)
    m2_inv = pow(m2, -1, b2)
    x = (a1 * m1 * m1_inv + b1 * m2 * m2_inv) % m
    print(f"{x} mod {m}")
def tuple_sort(a, b):
    return tuple([a, b]) # sorted
def ten(a, b):
    combined = tuple_sort(a, b)
    look = {
        tuple_sort("tragedy", "time") : "comedy",
        tuple_sort("repetition", "repetition") : "learning",
        tuple_sort("fire", "water") : "steam",
        tuple_sort("red", "blue") : "purple",
        tuple_sort("icelander", "deadline") : "procrastination",
        tuple_sort("throat", "potato") : "danish",
        tuple_sort("kattis", "program") : "verdict",
        tuple_sort("problem", "solution"): "AC",
        tuple_sort("contest", "geometry"): "WA",
        tuple_sort("nonsense", "annoyance"): "this problem",
    }
    print(look.get(combined, "unknown"))

adds = input().split(" + ")
nums = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
if len(adds) == 2:
    a, b = adds
    if all(x in nums for x in a) and all(x in nums for x in b):
        one(a, b)
    elif a.startswith('"') and b.startswith('"') and a.endswith('"') and b.endswith('"'):
        two(a, b)
    elif a.startswith("0x") and b.startswith("0x"):
        three(a, b)
    elif a.startswith("log") and b.startswith("log"):
        a = a[4:-1]
        b = b[4:-1]
        five(a, b)
    elif a.startswith("{") and b.startswith("{") and a.endswith("}") and b.endswith("}"):
        a = a[1:-1].split(",")
        b = b[1:-1].split(",")
        six(a, b)
    elif a in periodic_table and b in periodic_table:
        seven(a, b)
    elif a.isnumeric() and b.isnumeric():
        eight(a, b)
    elif "mod" in a and "mod" in b:
        nine(a, b)
    else:
        ten(a, b)
elif len(adds) == 4:
    a = (adds[0], adds[1])
    b = (adds[2], adds[3])
    four(a, b)