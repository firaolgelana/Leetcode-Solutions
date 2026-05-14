class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        nums2 = list(range(1, len(nums)))
        nums2.append(len(nums) - 1)
        return nums == nums2
        