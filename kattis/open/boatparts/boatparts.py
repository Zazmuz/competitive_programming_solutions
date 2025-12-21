parts, days = map(int, input().split())
s = set()
for i in range(days):
    s.add(input())
    if len(s) == parts:
        print(i+1)
        exit()
print("paradox avoided")