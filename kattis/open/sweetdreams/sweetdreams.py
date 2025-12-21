bx, by = map(int, input().split())
for monster in range(int(input())):
    mx, my = map(int, input().split())
    if (bx - mx)**2 + (by - my)**2 <= 64:
        print("NO")
        break
else:
    print("YES")