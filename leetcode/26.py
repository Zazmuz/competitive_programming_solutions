class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = nums[0]
        i = 1
        k = 1
        while i < len(nums):
            x = nums[i]
            if x == last:
                nums.pop(i)
            else:
                i += 1
                last = x
                k += 1
        return k