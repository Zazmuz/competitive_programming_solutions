word = input()
b,k = 0,0
for letter in word:
    if letter == "b":
        b += 1
    if letter == "k":
        k += 1

if b > k:
    print("boba")
elif k > b:
    print("kiki")
elif b+k == 0:
    print("none")
elif b == k:
    print("boki")
else:
    raise ValueError("This should never happen")