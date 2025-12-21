def dist(start, end):
    same = 0
    for i in range(min(len(start), len(end))):
        if start[i] == end[i]:
            same += 1
        else:
            break
    return len(end) - same + len(start) - same

for _ in range(int(input())):
    goal = input()
    current = input()
    suggestions = []
    for _ in range(3):
        suggestions.append(input())
    best = dist(current, goal)
    for s in suggestions:
        best = min(best, dist(s, goal)+1)
    print(best)