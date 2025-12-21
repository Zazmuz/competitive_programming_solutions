n = int(input())
a = [True] * n

s = n
i = 0
love_me = True
while s > 0:
    if a[i]:
        if not love_me:
            if s == 1:
                print(i + 1)
                exit()
            a[i] = False
            love_me = not love_me
            s -= 1
        else:
            love_me = not love_me

    i += 1
    i %= n