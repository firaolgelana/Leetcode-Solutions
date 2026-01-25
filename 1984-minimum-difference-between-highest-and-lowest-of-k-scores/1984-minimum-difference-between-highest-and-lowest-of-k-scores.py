class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDiff = float('inf')
        for i in range(k - 1, len(nums)):
            minDiff = min(minDiff, nums[i] - nums[i - k + 1])

        return minDiff
        