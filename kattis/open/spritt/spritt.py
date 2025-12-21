classrooms, available = [int(i) for i in input().split()]
s = 0
for i in range(classrooms):
    s += int(input())
print("Jebb" if s <= available else "Neibb")