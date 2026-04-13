class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_diff = float('inf')
        ans = 0
        for i in range(len(nums)):
            if nums[i] == target:
                if abs(i - start) < min_diff:
                    ans = abs(i - start)
                    min_diff = abs(i - start)
        return ans
        