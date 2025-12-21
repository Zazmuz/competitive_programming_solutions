from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bag = Counter(nums)
        return bag.most_common(1)[0][0]