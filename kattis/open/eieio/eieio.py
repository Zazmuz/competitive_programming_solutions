sheep = int(input())
legs = int(input())
for x in range(sheep+1):
    y = sheep - x
    if 4*x + 2*y == legs:
        print(x)
        exit()
print("Rong talning")