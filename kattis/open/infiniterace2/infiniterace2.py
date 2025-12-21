n = int(input())
q = int(input())
ahead_of = set()
laps = 0
for query in range(q):
    happened = int(input())
    if happened > 0:
        if happened in ahead_of:
            laps += 1
            ahead_of.clear()
            ahead_of.add(happened)
        else:
            ahead_of.add(happened)
    else:
        ahead_of.discard(-happened)
print(laps)