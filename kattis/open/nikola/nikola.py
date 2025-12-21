import heapq

INF = 9999999999999999
n = int(input())

price = [-1] + [int(input()) for _ in range(n)]
dp = [[INF] * (n + 2) for _ in range(n + 2)] # [pos][jump_length] = min cost

initial_cost = price[2]
dp[2][1] = initial_cost
heap = [(initial_cost, 2, 1)]

heapq.heapify(heap)

while heap:
    cost, pos, jump = heapq.heappop(heap)
    if cost > dp[pos][jump]: continue

    # back
    new_jump = jump
    new_pos = pos - new_jump
    if new_pos >= 1:
        new_cost = cost + price[new_pos]
        if new_cost < dp[new_pos][new_jump]:
            dp[new_pos][new_jump] = new_cost
            heapq.heappush(heap, (new_cost, new_pos, new_jump))

    # forward
    new_jump = jump + 1
    new_pos = pos + new_jump
    if new_pos <= n:
        new_cost = cost + price[new_pos]
        if new_cost < dp[new_pos][new_jump]:
            dp[new_pos][new_jump] = new_cost
            heapq.heappush(heap, (new_cost, new_pos, new_jump))

min_cost = INF
for jump_len in range(n + 1):
    if dp[n][jump_len] < min_cost:
        min_cost = dp[n][jump_len]

print(min_cost)
