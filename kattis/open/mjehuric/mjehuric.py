nums = [int(x) for x in input().split()]

while nums != sorted(nums):
    if nums[0] > nums[1]:
        nums[0], nums[1] = nums[1], nums[0]
        print(*nums)

    if nums[1] > nums[2]:
        nums[1], nums[2] = nums[2], nums[1]
        print(*nums)

    if nums[2] > nums[3]:
        nums[2], nums[3] = nums[3], nums[2]
        print(*nums)

    if nums[3] > nums[4]:
        nums[3], nums[4] = nums[4], nums[3]
        print(*nums)