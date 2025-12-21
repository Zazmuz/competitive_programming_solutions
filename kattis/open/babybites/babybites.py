input()
said = input().split()
c=1
for el in said:
    if el.isnumeric() and int(el) != c:
        print("something is fishy")
        exit()
    c += 1
print("makes sense")