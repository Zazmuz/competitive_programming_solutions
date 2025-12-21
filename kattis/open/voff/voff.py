from collections import deque
amount_of_heard, min_between = map(int, input().split())
heard = [int(_) for _ in input().split()]

dogs_in_recovery = deque([heard[0]])

for _ in range(1, amount_of_heard):
    next_bark = heard[_]
    lowest = dogs_in_recovery[0]
    if lowest + min_between <= next_bark:
        dogs_in_recovery.popleft()
    dogs_in_recovery.append(next_bark)

print(len(dogs_in_recovery))