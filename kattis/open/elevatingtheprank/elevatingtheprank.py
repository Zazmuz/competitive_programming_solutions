start, end = [int(x) for x in input().split()]
stop_at = set([int(input()) for x in range(int(input()))]) - {start, end}
time = 0
if start < end:
    for i in range(start, end):
        time += 4
        if i in stop_at:
            time += 10
elif start > end:
    for i in range(start, end, -1):
        time += 4
        if i in stop_at:
            time += 10
print(time)