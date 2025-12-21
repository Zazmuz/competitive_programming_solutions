nums = [int(input()) for i in range(int(input()))]
print(max(min(nums) - max(nums) // 2, 0))