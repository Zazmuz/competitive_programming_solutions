q = []
for i in range(int(input())):
    q.append(input())

for _ in range(int(input())):
    e = input().split()
    if e[0] == "cut":
        cuts, cut = e[1], e[2]
        where = q.index(cut)
        q.insert(where, cuts)
    elif e[0] == "leave":
        leave = e[1]
        q.remove(leave)

for i in q:
    print(i)