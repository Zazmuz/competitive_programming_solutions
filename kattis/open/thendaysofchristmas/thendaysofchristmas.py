gifts = 0
prev = 0
for i in range(1, int(input())+1):
    gifts += prev + i
    prev += i
print(prev)
print(gifts)