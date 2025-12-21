class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        a = nums[-k:] + nums[:-k]
        nums[:] = a[:]
        return nums