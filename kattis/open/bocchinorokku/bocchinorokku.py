from bisect import bisect_left
n = int(input())
nums = [int(x) for x in input().split()]
nums_s = sorted(nums)
for n in nums:
    print(bisect_left(nums_s, n), end=" ")