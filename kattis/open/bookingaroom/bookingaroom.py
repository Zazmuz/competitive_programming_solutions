rooms, taken = map(int, input().split())
if taken < rooms:
    rooms = set(range(1,rooms+1))
    for i in range(taken):
        rooms.remove(int(input()))
    print(rooms.pop())
else:
    print("too late")