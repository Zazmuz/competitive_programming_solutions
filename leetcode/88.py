class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:] = []

        i = 0
        while len(nums2) > 0:
            if i >= len(nums1):
                nums1.append(nums2.pop(0))
                continue

            a, b = nums2[0], nums1[i]
            if a <= b:
                nums1.insert(i, nums2.pop(0))
            else:
                i += 1