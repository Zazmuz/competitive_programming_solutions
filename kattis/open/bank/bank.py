people, time_till_close = [int(x) for x in input().split()]

from heapq import heappush, heappop
from collections import defaultdict

leave_times = defaultdict(list)
for _ in range(people):
    money, leave = [int(x) for x in input().split()]
    leave_times[leave].append(money)

max_money = 0
heap = []
for i in range(time_till_close, -1, -1):
    for money in leave_times[i]:
        heappush(heap, -money)
    if heap:
        max_money -= heappop(heap)

print(max_money)