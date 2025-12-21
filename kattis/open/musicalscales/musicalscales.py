c = {
    "A": 0,
    "A#": 1,
    "B": 2,
    "C": 3,
    "C#": 4,
    "D": 5,
    "D#": 6,
    "E": 7,
    "F": 8,
    "F#": 9,
    "G": 10,
    "G#": 11,
}

rc = {val: key for key, val in c.items()}

def major(pos):
    X = [0, 2, 4, 5, 7, 9, 11, 12]
    used = set()
    for x in X:
        used.add(rc[(pos + x)%12])
    return used
input()
song = set(input().split())
n = True
for note in c.keys():
    if not (song - major(c[note])):
        print(note, end=" ")
        n = False

if n:
    print("none")