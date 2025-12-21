nums = [int(x) for x in input().split()]
order = input()

nums.sort()

for i in order:
    if i == "A":
        print(nums[0], end=" ")
    elif i == "B":
        print(nums[1], end=" ")
    else:
        print(nums[2], end=" ")