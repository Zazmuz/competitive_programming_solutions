term = input()
input()
search_area = input().split()

s = 0

for area in search_area:
    if len(area) < len(term):
        continue
    for i in range(len(area) - len(term) + 1):
        if term == area[i:i+len(term)]:
            s += 1

print(s)