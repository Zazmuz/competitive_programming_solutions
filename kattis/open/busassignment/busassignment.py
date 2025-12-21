on = 0
needed = 0
for _ in range(int(input())):
    leave, enter = map(int, input().split())
    on += enter - leave
    needed = max(needed, on)

print(needed)