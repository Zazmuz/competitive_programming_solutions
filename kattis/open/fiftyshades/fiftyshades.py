s = 0
for i in range(int(input())):
    a = input().lower()
    if "rose" in a or "pink" in a:
        s += 1
print("I must watch Star Wars with my daughter" if s == 0 else s)