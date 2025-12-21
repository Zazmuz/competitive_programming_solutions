from collections import defaultdict
while True:
    n = int(input())
    if n == 0:
        break

    food = defaultdict(set)
    for _ in range(n):
        person, *items = input().split()
        for foo in items:
            food[foo].add(person)
    for foo in sorted(food):
        print(foo, *sorted(food[foo]))