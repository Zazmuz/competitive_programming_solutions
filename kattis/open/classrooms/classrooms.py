import bisect

activities, max_overlap = [int(x) for x in input().split()]

intervals = []
for _ in range(activities):
    start, end = [int(x) for x in input().split()]
    intervals.append((end, start))
intervals.sort()

classrooms = []

score = 0

for i in range(activities):
    start_time = intervals[i][1]
    end_time = intervals[i][0]

    idx = bisect.bisect_left(classrooms, start_time)

    if idx == 0:
        if len(classrooms) < max_overlap:
            bisect.insort(classrooms, end_time)
            score += 1
    else:
        score += 1
        classrooms.pop(idx - 1)
        bisect.insort(classrooms, end_time)
print(score)
