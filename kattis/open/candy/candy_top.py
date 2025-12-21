from sys import setrecursionlimit
setrecursionlimit(10**6)
dp = {}

def max_sum(i, selected_amnt, min_swaps):
    if i == 0:
        return 0 if selected_amnt == 0 and min_swaps == 0 else -99999999999999999999999

    if (i, selected_amnt, min_swaps) in dp:
        return dp[(i, selected_amnt, min_swaps)]

    dp[(i, selected_amnt, min_swaps)] = max_sum(i - 1, selected_amnt, min_swaps)

    if min_swaps - i + selected_amnt >= 0:
        dp[(i, selected_amnt, min_swaps)] = max(
            dp[(i, selected_amnt, min_swaps)],
            max_sum(i - 1, selected_amnt - 1, min_swaps - i + selected_amnt) + numbers[i - 1]
        )

    return dp[(i, selected_amnt, min_swaps)]


n, f, T = map(int, input().split())
numbers = [*map(int, input().split())]

for c in range(n * f + 1):
    if max_sum(n, f, c) >= T:
        print(c)
        break
else:
    print("NO")
