rooms = int(input())
collected = 0
for room in range(rooms):
    goombas, needed = [int(i) for i in input().split()]
    collected += goombas
    if collected < needed:
        print("impossible")
        exit()
print("possible")