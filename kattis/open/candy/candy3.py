n, max_elements, target_sum = map(int, input().split())
numbers = [*map(int, input().split())]

max_swaps = (n * (n + 1) // 2) + 1

dp = [[-99999999999999999999999] * max_swaps for _ in range(max_elements + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    current_number = numbers[i - 1]
    max_swaps_so_far = i * (i + 1) // 2
    for swaps in range(max_swaps_so_far, i - 1, -1):
        for elements_selected in range(max_elements, 0, -1):
            dp[elements_selected][swaps] = max(
                dp[elements_selected][swaps],
                dp[elements_selected - 1][swaps - i] + current_number
            )
max_swaps_for_selected = max_elements * (max_elements + 1) // 2
for swaps in range(max_swaps):
    if target_sum <= dp[max_elements][swaps]:
        min_swaps_required = max(0, swaps - max_swaps_for_selected)
        print(min_swaps_required)
        break
else:
    print("NO")