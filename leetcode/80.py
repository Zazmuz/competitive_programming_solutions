class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:return 1
        lastlast = nums[0]
        last = nums[1]
        i = 2
        while i < len(nums):
            x = nums[i]
            if x == last == lastlast:
                nums.pop(i)
            else:
                i += 1

                lastlast = last
                last = x
        return len(nums)