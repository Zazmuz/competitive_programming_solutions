from heapq import heappush, heappop
row_amnt, col_amnt, facilities_amnt, S, G = map(int, input().split())
cells_by_facility = [[] for _ in range(facilities_amnt)]
for fi in range(facilities_amnt):
    _, *ks = input().split()
    ks = [int(x) for x in ks]
    kc = [(ks[i]-1, ks[i+1]-1) for i in range(0, len(ks), 2)]
    for pair in kc:
        r, c = pair
        cells_by_facility[fi].append((r, c))

cells_by_facility = [sorted(c) for c in cells_by_facility]

students = []
students_by_facility = [[] for _ in range(facilities_amnt)]
for s in range(S):
    r, c, ID, f = map(int, input().split())
    students_by_facility[f-1].append((ID, r-1, c-1))
    students.append(((r-1, c-1), ID))

students_by_facility = [sorted(c) for c in students_by_facility]

fac_steps = [[] for _ in range(facilities_amnt)]
for f in range(facilities_amnt):
    for i, inf in enumerate(students_by_facility[f]):
        ID, r, c = inf
        er, ec = cells_by_facility[f][i]
        heappush(fac_steps[f], (abs(r - er) + abs(c - ec)))
gs = [(int(x),i) for i,x in enumerate(input().split())]
gs.sort()

steps_for_fac = [9999999999]*facilities_amnt
for g, fi in gs:
    steps = 0
    while g > 0:
        steps += heappop(fac_steps[fi])
        g -= 1
    steps_for_fac[fi] = steps
steps_for_fac.sort()
print(sum(steps_for_fac[:G]))