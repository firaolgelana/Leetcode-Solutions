class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        originalNums = set(range(min(nums), max(nums) + 1))
        return sorted(originalNums ^ set(nums))